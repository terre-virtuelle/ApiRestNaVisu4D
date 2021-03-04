const express = require('express');
const WebSocket = require('ws');

var HOSTNAME = 'localhost';
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
var router = express.Router();
var bodyParser = require("body-parser");


app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.use(router);

app.listen(PORT_EXT, HOSTNAME, function () {
    console.log("Server listen  http://" + HOSTNAME + ":" + PORT_EXT);
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
                roll: req.query.roll
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

//exemple curl PUT
//curl -X PUT "http://localhost:3000/control?cmd=position&origin=SMAUG&target=camera&latitude=48.00&longitude=-4.50&altitude=30000&heading=90.0&pitch=0.0&roll=0.0"
