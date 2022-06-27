const pythonServerConfig = require('../controllers/pythonServerConfig')
const httpServer = require('../controllers/httpServer')
const exchangeStorage = require("../history/exchange-storage")
const exchange = async (req, res, next) => {
    
    if (!req.body.amount || !req.body.toCurrency || !req.body.fromCurrency ){
        res.statusCode = 404;
        res.setHeader('Content-Type', 'application/json');
        return res.json({"error":"Request As Not Expected!"});
    }
    const data = JSON.stringify({
        amount : req.body.amount,
        toCurrency : req.body.toCurrency,
        fromCurrency : req.body.fromCurrency,
        date : req.body.date,
    });
    const options = pythonServerConfig.pythonServerConfig(path = req.path, method = req.method);
    options.headers = {
        'Content-Type': 'application/json',
        'Content-Length': data.length
        };
    
    httpServer.sendHttpRequest(res, options, data, function(body,data){
        exchangeStorage.add_exchange_history(JSON.parse(data), body);
        return res.json(body);
    });
   /* const statusCode = statusCodeMessage[0];
    const response = statusCodeMessage[1];*/
    

      
};
module.exports = {
   exchange
};