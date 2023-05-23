const express = require('express');
const app = express();
const port = 3000;
const { exec } = require("child_process");
const path = require('path');
const fs = require('fs');

let isOpen = null;
let openingTime = null;
let closingTime = null;

fs.readFile('isOpen.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  isOpen = data;
  console.log(isOpen);
});

fs.readFile('openingTime.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  openingTime = data;
  console.log(openingTime);
});

fs.readFile('closingTime.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  closingTime = data;
  console.log(closingTime);
});

app.use(express.static("client"));

app.use(express.urlencoded({ extended: true })); // Parse URL-encoded bodies

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'client/index.html'));
});

app.post('/setTimes', (req, res) => {
  openingTime = req.body.openingTime;
  closingTime = req.body.closingTime;
  console.log(`Opening Time: ${openingTime}`);
  console.log(`Closing Time: ${closingTime}`);
  fs.writeFile('openingTime.txt', openingTime, (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('Opening time written to openingTime.txt');
  });
  fs.writeFile('closingTime.txt', closingTime, (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('Closing time written to closingTime.txt');
  });
  res.redirect('/');
});

function checkTime() {
  const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  console.log(`Current Time: ${currentTime}`);

  if (currentTime === openingTime) {
    if (isOpen == 0) {
      app.get('/openDoor', (req, res) => {
        console.log(isOpen);
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
          fs.writeFile('isOpen.txt', isOpen.toString(), (err) => {
            if (err) {
              console.error(err);
              return;
            }
            res.redirect('/openDoor');
          });
        } else {
          res.redirect('/');
        }
      });
    }
  }

  if (currentTime === closingTime) {
    if (isOpen == 1) {
      app.get('/closeDoor', (req, res) => {
        console.log(isOpen);
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
          fs.writeFile('isOpen.txt', isOpen.toString(), (err) => {
            if (err) {
              console.error(err);
              return;
            }
            res.redirect('/closeDoor');
          });
        } else {
          res.redirect('/');
        }
      });
    }
  }
}

setInterval(checkTime, 1000); // Check time every second

app.get('/openDoor', (req, res) => {
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
      fs.writeFile('isOpen.txt', isOpen.toString(), (err) => {
        if (err) {
          console.error(err);
          return;
        }
        res.redirect('/openDoor');
      });
    } else {
      res.redirect('/');
    }
});

app.get('/closeDoor', (req, res) => {
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
      fs.writeFile('isOpen.txt', isOpen.toString(), (err) => {
        if (err) {
          console.error(err);
          return;
        }
        res.redirect('/closeDoor');
      });
    } else {
      res.redirect('/');
    }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
