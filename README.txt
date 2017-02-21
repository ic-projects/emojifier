Meme is love, meme is life.

Using a combination of word embeddings and neural networks, the program predicts which emoji is useful based on sentence context.

We collected data from Reddit and Twitter and using TensorFlow we trained the different models such as character level LSTM, word level LSTM and fixed input neural network and also using Google's word2vector for word embeddings.

Tying the front end to the back end was very hard. We started out with Ruby on Rails to start a background Python process which was used for the emoji prediction but we could not find a way to append the standard input stream for the process, so instead we used Node.js to run in parallel with a Python server which listened for POST requests from the Node.js client and then using Twmoji to beautifully render the final emojis.

Describing emojis as a single word, problems with training data on TensorFlow.

Having a finished product in our first hackathon!

Learning six different programming languages, more about machine learning, and using real world data.

Turning text into raw memes: we already have some extra features built and ready to go theyre just waiting for front end implementations.
