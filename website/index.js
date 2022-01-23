const express = require('express')
const app = express()
const port = 3000
const { exec } = require("child_process");


app.use(express.static("client"));
const path = require('path');
const fs = require('fs')

var isOpen = null;

fs.readFile('isOpen.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }
  isOpen = data
  console.log(isOpen)
})


app.get('/openDoor', (req, res) => {

	console.log(isOpen)
	if (isOpen == 0) {

    		exec("python3 pythonScripts/openDoor.py", (error, stdout, stderr) => {
    			if (error) {
        			console.log(`error: ${error.message}`);
        			return;
    			}
    			if (stderr) {
        			console.log(`stderr: ${stderr}`);
        			return;
    			}
    			console.log(`stdout: ${stdout}`);
    		});
		isOpen = 1;
		fs.writeFile('isOpen.txt', isOpen.toString(), err => {
  			if (err) {
    				console.error(err)
    				return
  			}
			res.sendFile(path.join(__dirname, 'client/open.html'))
  		//file written successfully
		})
   	}

});

app.get('/closeDoor', (req, res) => {

	console.log(isOpen)
	if (isOpen == 1) {
		exec("python3 pythonScripts/closeDoor.py", (error, stdout, stderr) => {
    			if (error) {
        			console.log(`error: ${error.message}`);
        			return;
    			}
    			if (stderr) {
        			console.log(`stderr: ${stderr}`);
        			return;
    			}
    			console.log(`stdout: ${stdout}`);
		});
		isOpen = 0;
		fs.writeFile('isOpen.txt', isOpen.toString(), err => {
  			if (err) {
    				console.error(err)
    				return
  			}
			res.sendFile(path.join(__dirname, 'client/close.html'))
			
  		//file written successfully
		})
	}
	
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
