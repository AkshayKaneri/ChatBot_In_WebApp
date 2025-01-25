const express = require("express");
const cors = require("cors");
const bodyParser = require('body-parser');
const path = require("path");
const { spawn } = require("child_process");

const app = express();
//midddleware
app.use(cors());
app.use(bodyParser.json());

// Routes
app.post('/chat', (req, res) => {
    const userInput = req.body.prompt;
    if (!userInput) {
        return res.status(400), json({ error: 'No Prompt Provided' })
    }
    // spawn the python process
    const py3EnvPath = path.join(__dirname, "..", 'python-env/transformers-env/bin/python3');
    const modelPath = path.join(__dirname, "..", 'python-env/test_model.py')
    const pythonProcess = spawn(
        py3EnvPath,
        [modelPath, userInput]);
    let responseText = '';

    //collect data from python script
    pythonProcess.stdout.on('data', (data) => {
        responseText += data.toString();
    })

    //handle script completion
    pythonProcess.on('close', (code) => {
        if (code !== 0) {
            return res.status(500).json({ error: 'Python script failed' });
        }
        res.json({ response: responseText.trim() });
        pythonProcess.kill();
    })

    //error
    pythonProcess.on('error', (err) => {
        console.log("Failed to start Python Process", err);
        res.status(500).json({ error: 'Model processing failed. Please try again.' })
    })
})

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on ${PORT} port`)
})