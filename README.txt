const express = require('express');
const WebSocket = require('ws');

var HOST_NAME = 'localhost';
//var HOST_NAME = '93.90.200.21';
var PORT_EXT = 3003;
var PORT_INT = 9898;

var clientsNaVisu = [];
var app = express();

//WebSocket part
const wss = new WebSocket.Server({port: PORT_INT});

wss.on('connection', ws => {
    ws.on('message', message => {
        // console.log(`Received message => ${message}`);
    });
    ws.send('connected');
    clientsNaVisu.push(ws);
});

//API REST part
var CONTROL = '/control';
var INFO = '/info';
var FILTER = '/filter';

var router = express.Router();
var bodyParser = require("body-parser");
var exec = require('child_process').exec, child;

**********************************************************
  //le 30 juil 21
Fait le test :
const http = require("https");


http.get("https://services.data.shom.fr/telechargement/oceano/HYDRODYN-SURF_HYCOM3D-SURF_R1000_MANGASC_20210730.dl/file/HYDRODYN-SURF_HYCOM3D-SURF_R1000_MANGASC_20210730.dl.zip", res => {
  let data = "";
  res.on("data", d => {
   console.log(d);
  });
});
// OK, reçu le binaire, il faut le suvegarder
*************************************************************

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.use(router);

app.listen(PORT_EXT, HOST_NAME, function () {
    console.log("Server listen  http://" + HOST_NAME + ":" + PORT_EXT);
});


router.route(CONTROL)
        .get(function (req, res) {
            //TODO
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
            clientsNaVisu.forEach(element => element.send(JSON.stringify(mes)));
            res.json(mes);
        })
        .delete(function (req, res) {
            res.json({message: "Suppression ", methode: req.method});
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
            clientsNaVisu[0].send(JSON.stringify(mes));
            clientsNaVisu[0].on('message', mes => {
                res.json(mes);
            });
        });
router.route(FILTER)
        .get(function (req, res) {
            //TODO
        })
        .post(function (req, res) {
            //TODO
        })
        .put(function (req, res) {
            var mes = {
                cmd: req.query.cmd,
                origin: req.query.origin,
                date: req.query.date,
                input: req.query.input,
                output: req.query.output,
                latBBox: req.query.latBBox,
                lonBBox: req.query.lonBBox,
                dateIndexes: req.query.dateIndexes
            };
           // Lire input
           
           
           
           
            child = exec('java -jar NetCDF.jar ' + mes.cmd + ' ' + mes.date + ' ' + mes.input + '  ' + mes.output + ' ' + mes.lonBBox + ' ' + mes.latBBox + ' ' + mes.dateIndexes,
                    function (error, stdout, stderr) {
                        if (stdout !== null && stdout !== '') {
                            console.log('stdout: ' + stdout);
                        }
                        if (stderr !== null && stderr !== '') {
                            console.log('stderr: ' + stderr);
                        }
                        if (error !== null) {
                            console.log('exec error: ' + error);
                        }
                    });

        })
        .delete(function (req, res) {
            //TODO
        });
//java -jar NetCDF.jar ncks 20210703 HYDRODYN-SURF_HYCOM3D-SURF_R1000_MANGASC_ out -4.80,-4.70 48.30,48.25 0,23
//exemples curl PUT
//curl -X PUT "http://localhost:3000/control?cmd=position&origin=SMAUG&target=camera&latitude=48.00&longitude=-4.50&altitude=30000&heading=90.0&pitch=0.0&roll=0.0"
//curl -X PUT "http://localhost:3000/filter?cmd=ncks&origin=NAVISU&date=20210703&input=HYDRODYN-SURF_HYCOM3D-SURF_R1000_MANGASC_&output=out
//&latBBox=-4.80,-4.70&lonBBox=-4.80,-4.70&dateIndexes=0,23"


********************Le 31 juillet 2021***************
http://localhost:3003/filter?cmd=ncks&origin=NAVISU&date=20210730&input=HYDRODYN-SURF_HYCOM3D-SURF_R1000_MANGASC_&output=out1&latBBox=-4.80,-4.70&lonBBox=-4.80,-4.70&dateIndexes=0,23

// PB sur out.

serge@serge-XPS-15-9550:~/Data/developement_2020/ApiRestServerNaVisu4D$ node serverApiRest.js 
Server listen  http://localhost:3003
{
  zip: 'Archive:  ./HYDRODYN-SURF_HYCOM3D-SURF_R1000_MANGASC_20210730.dl.zip\n' +
    '  inflating: HYDRODYN-SURF_HYCOM3D-SURF_R1000_MANGASC_20210730.nc.gz  \n' +
    '  inflating: HYDRODYN-SURF_HYCOM3D-SURF_R1000_MANGASC_20210730.xml  \n' +
    '  inflating: HYDRODYN-SURF_HYCOM3D-SURF_R1000_MANGASC_20210730.gml  \n',
  gunzip: '',
  mv: '',
  nks: 'netCDF2Czml.compute  start\n' +
    'cmd : ncks -v lon,out -v lat,-4.80,-4.70 -d time,-4.80,-4.70 -v u,v /home/serge/Data/developement_2020/ApiRestServerNaVisu4D/data/HYDRODYN-SURF_HYCOM3D-SURF_R1000_MANGASC_20210730.nc -O /home/serge/Data/developement_2020/ApiRestServerNaVisu4D/data/-O.nc\n' +
    'netCDF2Czml.compute /home/serge/Data/developement_2020/ApiRestServerNaVisu4D/data/-O.nc over\n' +
    '\n',
  rmAll: '',
  rm: ''
}
*********************************
http://localhost:3003/filter?cmd=bbox&origin=NAVISU&date=20210808&input=HYDRODYN-SURF_HYCOM3D-SURF_R1000_MANGASC_&output=out1&latBBox=48.0,48.5&lonBBox=-4.5,-4.0&dateIndexes=0,23



20210812

/

// Dump de variables
ncdump -v var file1.nc   > valeurs_var

