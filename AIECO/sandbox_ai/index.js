const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')

const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
  organization: "org-oQ7PsCLvXKZqJ9EPBbdC3Uzx",
  // apiKey: process.env.OPENAI_API_KEY,
  apiKey: "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",
});
const openai = new OpenAIApi(configuration);

// create a simple express api that calls the function above
// add body parser and cors to express
const app = express()
app.use(bodyParser.json())
app.use(cors())

const port = 3080

app.post('/', async (req, res) => {
  const { message } = req.body;
  console.log('message: ', message)

  const response = await openai.createCompletion({
    model: "text-davinci-003",
    // model: "gpt-3.5-turbo",
    prompt: `${message}`,
    max_tokens: 2000,
    temperature: 0.5,
  });

  // console.log('response: ', response)
  console.log(response.data.choices[0].text)

  res.json({
    message: response.data.choices[0].text
  })
});

// app.get('/models', async (req, res) => {
//   const response = await openai.listEngines();
//   console.log('response: ', response)
//   res.json({
//     models: response.data
//   })
// });

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
});

// run the server
// node index.js