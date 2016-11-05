const fs = require('fs');
const argv = require('minimist')(process.argv.slice(2));
const http = require('http');
const url = require('url');
//const XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;

var filename = process.argv[2];
if(!filename){
  console.log("ERR: Please enter a file name");
}

var fileoutput = argv.o;
var apioutput = argv.i;
var dataIn;
var dataOut = [];

dataIn = JSON.parse(fs.readFileSync(filename));

for (ev of dataIn) {
  var tmp = {
    "@id":ev.id.toString(),
    "@type":"m:"+ev.type.replace('Obsel',''),
    "begin":ev.start,
    "end":ev.start
  }
  if(ev.x)
    tmp["m:x"] = ev.x;
  if(ev.y)
    tmp["m:y"] = ev.y;
  if(ev.z)
    tmp["m:z"] = ev.z;
  if(ev.playerName)
    tmp["m:playerName"] = ev.playerName;
  if(ev.data)
    tmp["m:data"] = ev.data;
  if(ev.blockName)
    tmp["m:blockName"] = ev.blockName;
  if(ev.itemName)
    tmp["m:itemName"] = ev.itemName;
  if(ev.amount)
    tmp["m:amount"] = ev.amount;
  if(ev.damage)
    tmp["m:damage"] = ev.damage;
  if(ev.cause)
    tmp["m:cause"] = ev.cause;
  if(ev.resultBCraft)
    tmp["m:resultBCraft"] = ev.resultBCraft;
  if(ev.numberOfCrafts)
    tmp["m:numberOfCrafts"] = ev.numberOfCrafts;
  if(ev.resultData)
    tmp["m:resultData"] = ev.resultData;
  if(ev.resultType)
    tmp["m:resultType"] = ev.resultType;

  dataOut.push(tmp);
}


if(!fileoutput && !apioutput)
  fileoutput = 'output.json';
if(fileoutput)
  fs.writeFileSync(fileoutput, JSON.stringify(dataOut));

if(apioutput){

  var targetURL = url.parse(apioutput);

  var postOptions = {
    hostname: targetURL.hostname,
    port: targetURL.port,
    path: targetURL.path,
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(dataOut)
    }
  }

  var req = http.request(postOptions, (res) => {
    console.log(`STATUS: ${res.statusCode}`);
    console.log(`HEADERS: ${JSON.stringify(res.headers)}`);
    res.setEncoding('utf8');
    res.on('data', (chunk) => {
      console.log(`BODY: ${chunk}`);
    });
    res.on('end', () => {
      console.log('No more data in response.');
    });
  });
  req.on('error', (e) => {
    console.log(`problem with request: ${e.message}`);
  });

  // write data to request body
  req.write(JSON.stringify(dataOut));
  req.end();
}
