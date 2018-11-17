var restify = require('restify');
var TimeController = require('./time_controller');
var server = restify.createServer();
server.use(restify.plugins.bodyParser());

server.on('restifyError', function(req, res, err, callback) {
    if(err.fields){
        err.toJSON = function () {
            return {
                name: err.name,
                message: err.message,
                fields: err.fields
            };
        };
    }
    return callback();
});

var timeController = new TimeController();
server.get({path: '/time'}, timeController.getTime);
server.put({path: '/time'}, timeController.setTime);

server.listen(8090, function() {
	console.log('%s listening at %s', server.name, server.url);
});