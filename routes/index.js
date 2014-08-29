var express = require('express');
var router = express.Router();
var fs = require('fs');
var path = require('path');

/* GET home page. */
router.get('/', function(req, res) {
	var about1 = 'public/text/about1.txt';
	var about2 = 'public/text/about2.txt';
	var about3 = 'public/text/about3.txt';
	var info = 'public/text/info.txt';
	var a1;
	var a2; 
	var a3;
	var i1;

	fs.readFile(about1, {encoding: 'utf-8'}, function(err, data) {
			a1 = data;
			fs.readFile(about2, {encoding: 'utf-8'}, function(err, data2) {
				a2 = data2;
				fs.readFile(about3, {encoding: 'utf-8'}, function(err, data3) {
					a3= data3;
					fs.readFile(info, {encoding: 'utf-8'}, function(err, data4) {
						i1= data4;
						res.render('index', { title: 'timelaps', about1: a1, about2: a2, about3: a3, info: i1});
					});
				});
			});
	});
	
	
});

module.exports = router;
