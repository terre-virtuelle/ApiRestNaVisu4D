const express = require('express');
const WebSocket = require('ws');
var net = require('net');
const https = require("https");
const fs = require('fs');
const {exec} = require("child_process");
const {process} = require("./scenario2Pdf");
var cors = require('cors');
let gpxParser = require('./GPXParser.js');

//var HOST_NAME = 'localhost';

var HOST_NAME = '93.90.200.21';
var PORT_EXT = 3003;
var PORT_INT = 9898;
var PORT_INT_SIGNALK = 10110;

var tcpClient;
var first = true;


var clientsNaVisu = [];
var app = express();

//WebSocket part one NaVisu client is connecting
const wss = new WebSocket.Server({port: PORT_INT});
// one NaVisu's client is connecting
wss.on('connection', ws => {
    ws.on('message', message => {
    });
    ws.send('connected');
    clientsNaVisu.push(ws);
});

//Connection at SignalK
if (first === true) {
    tcpClient = new net.Socket();
    tcpClient.connect(PORT_INT_SIGNALK, HOST_NAME, function () {
        console.log('SignalK connected on ' + HOST_NAME + ':' + PORT_INT_SIGNALK);
        //  tcpClient.write('$GPRMC,120014.41,A,4823.52,N,00425.71,W,12.55,125.51,150422,0.00,W*55\r\n');
    });
    first = false;
}


//API REST part
var CONTROL = '/control';
var DISPLAY = '/display';
var INFO = '/info';
var FILTER = '/filter';
var READ_FILE = '/read';
var EXPORT_FILE = '/export';
var IMAGE = '/image';
var VIDEO = '/video';
var WRITE_FILE = '/write';
var TRACK_NMEA = '/nmea';
var TEST = '/test';


var router = express.Router();
var bodyParser = require("body-parser");
var execSync = require('child_process').execSync, child;

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

const corsOptions = {origin: "*",
    methods: "GET,HEAD,PUT,PATCH,POST,DELETE",
    allowedHeaders: "Access-Control-Allow-Headers,Access-Control-Allow-Origin,"
            + "Access-Control-Request-Method,Access-Control-Request-Headers,"
            + "Origin,Cache-Control,Content-Type,X-Token,X-Refresh-Token",
    credentials: true,
    preflightContinue: false,
    optionsSuccessStatus: 204};

app.use(cors(corsOptions));



app.use(router);

app.get('/', function (req, res) {
    console.log(req.socket.remoteAddress);
});

app.listen(PORT_EXT, HOST_NAME, function () {
    console.log("Server listen  http://" + HOST_NAME + ":" + PORT_EXT);
});

router.route(CONTROL)
        .get(function (req, res) {
            var mes = {
                cmd: req.query.cmd,
                origin: req.query.origin,
                ext: req.query.ext,
                target: req.query.target
            };
            if (mes.cmd === 'scenario' && mes.ext === 'json') {
                try {
                    fs.readFile('data/scenarios/' + mes.target + '/' + mes.target + '.json', {encoding: 'utf-8'}, function (err, data) {
                        res.writeHead(200, {'Content-Type': 'application/json'});
                        res.write(data);
                        res.end();
                    });
                } catch (er) {
                    console.log(er);
                }
            }
            if (mes.cmd === 'scenario' && mes.ext === 'pdf') {
                fs.readFile('data/scenarios/' + mes.target + '/pdf/' + mes.target + '.pdf', function (err, data) {
                    if (!err) {
                        res.writeHead(200, {'Content-Type': 'application/pdf'});
                        res.write(data);
                        res.end();
                    } else {
                        console.log(err);
                    }
                });
            }

        })
        .post(function (req, res) {
            res.json({message: "",
                nom: req.body.nom,
                methode: req.method});
        })
        .put(function (req, res) {
            var mes = {
                cmd: req.query.cmd,
                origin: req.query.origin,
                target: req.query.target,
                latitude: req.query.latitude,
                longitude: req.query.longitude,
                altitude: req.query.altitude,
                heading: req.query.heading,
                pitch: req.query.pitch,
                roll: req.query.roll,
                timestamp: req.query.timestamp
            };
            console.log(mes);
            clientsNaVisu.forEach(element => element.send(JSON.stringify(mes)));
            res.json(mes);
        });
router.route(DISPLAY)
        .put(function (req, res) {
            var mes = {
                cmd: req.query.cmd,
                parameter: req.query.parameter,
                origin: req.query.origin,
                target: req.query.target,
                latitude: req.query.latitude,
                longitude: req.query.longitude,
                altitude: req.query.altitude,
                timestamp: req.query.timestamp
            };
            clientsNaVisu.forEach(element => element.send(JSON.stringify(mes)));
            res.json(mes);
        });
router.route(INFO)
        .put(function (req, res) {

        })
        .post(function (req, res) {
            res.json({message: "",
                nom: req.body.nom,
                methode: req.method});
        })
        .get(function (req, res, next) {
            var mes = {
                cmd: req.query.cmd,
                origin: req.query.origin,
                target: req.query.target
            };
            //  clientsNaVisu.forEach(element => element.send(JSON.stringify(mes)));
            //Envoi message au client  depuis le premier client NaVisu
            try {
                clientsNaVisu[0].send(JSON.stringify(mes));
                clientsNaVisu[0].on('message', mes => {
                    res.json(mes);
                });
            } catch (err) {
                console.error(err);
            }
        });
router.route(FILTER)
        .get(function (req, res) {
            //  console.log('req',req);
            var mes = {
                cmd: req.query.cmd,
                origin: req.query.origin,
                date: req.query.date,
                input: req.query.input,
                option: req.query.option,
                latBBox: req.query.latBBox,
                lonBBox: req.query.lonBBox,
                dateIndexes: req.query.dateIndexes
            };
            try {
                if (!fs.existsSync('./data/' + mes.input + mes.date + '.nc')) {
                    console.log('./data/' + mes.input + mes.date + '.nc');
                    const url = 'https://services.data.shom.fr/telechargement/oceano/'
                            + mes.input
                            + mes.date
                            + '.dl/file/'
                            + mes.input
                            + mes.date
                            + '.dl.zip';
                    const path = './'
                            + mes.input
                            + mes.date
                            + '.dl.zip';
                    console.log('url', url);
                    const request = https.get(url, function (response) {
                        var file;
                        if (response.statusCode === 200) {
                            file = fs.createWriteStream(path);
                            response.pipe(file);
                        }
                        file.on('finish', () => {
                            console.log('unzip ./' + mes.input + mes.date + '.dl.zip');
                            const zip = execSync('unzip ./' + mes.input + mes.date + '.dl.zip').toString();
                            console.log('gunzip ./' + mes.input + mes.date + '.nc.gz');
                            const gunzip = execSync('gunzip ./' + mes.input + mes.date + '.nc.gz').toString();
                            console.log('mv ./' + mes.input + mes.date + '.nc data/');
                            const mv = execSync('mv ./' + mes.input + mes.date + '.nc data/').toString();
                            console.log('java -jar NetCDF.jar bbox ' + mes.origin + ' ' + mes.date + ' ' + mes.input + ' ' + mes.option + ' out ' + mes.lonBBox + ' ' + mes.latBBox + ' ' + mes.dateIndexes);
                            const bbox = execSync('java -jar NetCDF.jar bbox ' + mes.origin + ' ' + mes.date + ' ' + mes.input + ' ' + mes.option + ' out ' + mes.lonBBox + ' ' + mes.latBBox + ' ' + mes.dateIndexes).toString();
                            console.log('rm ./' + mes.input + mes.date + '.*');
                            const rmAll = execSync('rm ./' + mes.input + mes.date + '.*').toString();

                            console.log({
                                zip,
                                gunzip,
                                mv,
                                bbox,
                                rmAll
                            });
                            fs.readFile("data/out.json", "utf8", function (err, data) {
                                if (err) {
                                    console.log("err");
                                    throw err;
                                }
                                res.send(data);
                            });
                            console.log('rm ./' + mes.input + mes.date + '.*');
                            const rmOut = execSync('rm ./out').toString();
                            const rmOutJSON = execSync('rm data/out.json').toString();
                        });
                        request.setTimeout(60000, function () { // if after 60s file not downlaoded, we abort a request 
                            request.abort();
                        });
                    });
                }
                //file exists
                else {
                    console.log('./data/' + mes.input + mes.date + '.nc exist yet');
                    const bbox = execSync('java -jar NetCDF.jar bbox ' + mes.origin + ' ' + mes.date + ' ' + mes.input + ' ' + mes.option + ' out ' + mes.lonBBox + ' ' + mes.latBBox + ' ' + mes.dateIndexes).toString();
                    console.log(
                            'java -jar NetCDF.jar bbox ' + mes.origin + ' ' + mes.date + ' ' + mes.input + ' ' + mes.option + ' out ' + mes.lonBBox + ' ' + mes.latBBox + ' ' + mes.dateIndexes
                            );

                    fs.readFile("data/out.json", "utf8", function (err, data) {
                        if (err) {
                            console.log("No data in the bbox");
                            //throw err;
                            data = '';
                        }
                        //var resultArray = //do operation on data that generates say resultArray;
                        //  console.log('src', data);
                        res.send(data);
                        if (data !== '') {
                            const rmOut = execSync('rm ./out').toString();
                            const rmOutJSON = execSync('rm data/out.json').toString();
                        }
                    });

                }
            } catch (err) {
                console.error(err);
            }
        });
router.route(READ_FILE)
        .put(function (req, res) {
            console.log('req', req);
            var mes = {
                cmd: req.query.cmd,
                origin: req.query.origin,
                path: req.query.path,
                target: req.query.target,
                timestamp: req.query.timestamp
            };
            console.log(mes);
            try {
                if (mes.cmd === 'scenario') {
                    fs.readFile('data/' + mes.path + '/' + mes.target, "utf8", function (err, data) {
                        clientsNaVisu.forEach(element => element.send(data));
                        res.send(data);
                    });
                }
            } catch (err) {
                console.error(err);
            }
        })
        .get(function (req, res, next) {
            var mes = {
                cmd: req.query.cmd,
                origin: req.query.origin,
                target: req.query.target
            };
                if (mes.cmd === 'gpxSimulation') {
                    const data = fs.readFileSync('./data/simulations/' + mes.target, {encoding:"utf8", flag:'r'}); 
                    var parser = new gpxParser();
                    parser.parse(data);
                    var wpts = {wpts: parser.routes[0].points, distances: parser.routes[0].distance};
                    var result = JSON.stringify(wpts);
                    clientsNaVisu.forEach(element => element.send(result));
                   res.send(result);
                }
        });
router.route(IMAGE)
        .get(function (req, res, next) {
            var mes = {
                cmd: req.query.cmd,
                origin: req.query.origin,
                path: req.query.path,
                target: req.query.target
            };
            if (mes.cmd === 'scenario') {
                try {
                    fs.readFile('data/' + mes.path + '/images/' + mes.target, function (err, data) {
                        res.writeHead(200, {'Content-Type': 'image/png'});
                        res.end(data); // Send the file data to the browser.
                        clientsNaVisu.forEach(element => element.send(data));
                    });
                } catch (er) {
                    console.log(er);
                }
            }
        });
router.route(VIDEO)
        .get(function (req, res, next) {
            var mes = {
                cmd: req.query.cmd,
                origin: req.query.origin,
                path: req.query.path,
                target: req.query.target
            };
            if (mes.cmd === 'scenario') {
                try {
                    fs.readFile('data/' + mes.path + '/videos/' + mes.target, function (err, data) {   
                        res.writeHead(200, {'Content-Type': 'video/mp4'});
                        res.end(data); // Send the file data to the browser.
                        clientsNaVisu.forEach(element => element.send(data));
                    });
                } catch (err) {
                    console.log(err);
                }
            }
        });
router.route(TEST)
        .get(function (req, res, next) {
            var mes = {
                cmd: req.query.cmd,
                origin: req.query.origin,
                target: req.query.target
            };
            if (mes.cmd === 'oceanovox') {
                try {
                    fs.readFile('data/tests/' + mes.target, "utf8", function (err, data) {
                        clientsNaVisu.forEach(element => element.send(data));
                        res.send(data);
                    });
                } catch (er) {
                    console.log(er);
                }
            }
        });
router.route(WRITE_FILE)
        .put(function (req, res) {
            var mes = {
                cmd: req.query.cmd,
                origin: req.query.origin,
                path: req.query.path,
                target: req.query.target
            };
            try {
                if (mes.cmd === 'log') {
                    writeFile('data/logs/' + mes.path + 'log', mes.target);
                    console.log('server log');
                }
                res.send('logged');
            } catch (err) {
                console.error(err);
            }
        });
router.route(TRACK_NMEA)
        .put(function (req, res) {
            var mes = {
                cmd: req.query.cmd,
                origin: req.query.origin,
                path: req.query.path,
                data: req.query.data
            };
            try {
                if (mes.cmd === 'display') {
                    tcpClient.write(mes.data + '\r\n');
                }
                res.send('nmea');
            } catch (err) {
                console.error(err);
            }
        });
router.route(EXPORT_FILE)
        .put(function (req, res) {
            var mes = {
                cmd: req.query.cmd,
                origin: req.query.origin,
                target: req.query.target
            };
            try {
                if (mes.cmd === 'scenario') {
                    process(mes.target);
                }
                res.send('printed');
            } catch (err) {
                console.error(err);
            }
        });

writeFile = async (target) => {
    console.log(clientsNaVisu[0].send('log'));
    // var response = await fs.writeFileSync(target, data);
}
;
