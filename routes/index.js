var express = require('express');
var router = express.Router();
var fs = require('fs');
var path = require('path');

/* GET home page. */
router.get('/', function(req, res) {
	var filePath = 'public/text/about.txt';
	fs.readFile(filePath, {encoding: 'utf-8'}, function(err, data) {
		if (err) {
			console.log(err);
		} else {
			console.log('data' + data);
			res.render('index', { title: 'timelaps', about: data });
		}
	})
});

module.exports = router;
