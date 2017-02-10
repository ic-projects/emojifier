meme is love meme is life

using a combination of word embeddings and neural networks the program predicts which emoji is useful based on sentence context

we collected data from reddit and twitter and using tensorflow we trained the different models such as character level lstm, word level lstm and fixed input neural network and also using googles word2vector for word embeddings

tying the front end to the back end was very hard we started out with ruby on rails to start a background python process which was used for the emoji prediction but we could not find a way to append the standard input stream for the process so instead we used nodejs to run in parallel with a python server which listened for post requests from the nodejs client and then using twmoji to beautifully render the final emojis

describing emojis as a single word problems with training data on tensorflow

having a finished product in our first hackathon

learning six different programming languages more about machine learning and using real world data

turning text into raw memes we already have some extra features built and ready to go theyre just waiting for front end implementations 

there are clearly some bugs we dont know why it choose the virgin islands flag and the moon emojis so often

we also hope to make some optimisations to improve loading speed
