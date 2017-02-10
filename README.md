# EMOJIFIER
Available at [emojifier.co.uk](http://www.emojifier.co.uk).

## Inspiration
Meme 🐸 is 🐸 love, ❤💘💌 meme 🐸❤ is 🐸 life.

## What it does
Using a combination of word embeddings and neural networks the program predicts which emoji 🖱 is useful 🔧 based on sentence context.

## How we built it
We 🇻🇮 collected data 💁 from Reddit and Twitter and using TensorFlow we 🇻🇮 trained the different models such as character level 🎛 LSTMs 🎛 word level 🎛 LSTMs 🎛 and fixed input neural networks and also using Google's Word2Vector for ⏺🎙 word 🎙 embeddings.

Tying the front 🚅 end 🔙💆 to 🔙 the back 🔜◀↩ end 🔙🔜 was 🔙 very hard. We 🇻🇮 started out ✌🔜🆙 with ✌ ruby 💎 on rails 🚈 to start 🔙 a background python 🐊🐆🐍 process which was used for ⏺🎙 the ⏺ emoji 🖱 prediction but we 🇻🇮 could not ‼ find 🛅 a way 🌌 to 🌌 append the standard input stream for ⏺🎙 the ⏺ process, so 🙄 instead we 🇻🇮 used nodejs to run 🎽 in parallel with a python 🐊🐆🐍 server 💻🖨 which listened 👂 for ⏺🎙 post 🏣🏤🚩 requests 🏣 from the nodejs client and then 🔜 using twmoji to beautifully render the final 🌛 emojis.

## Challenges we ran into
Describing emojis as a single 🔂 word, 🔂 problems with training data 💁 on TensorFlow.

## Accomplishments that we're proud of
Having a finished 🏁 product in our 🇻🇮 first 🌛🌓 hackathon 🌛.

## What we learned
Learning six 6⃣7⃣5⃣ different 6⃣4⃣5⃣ programming languages, more about machine 🎰 learning 🎰 and using real ‼ world 🏔🌐🌏 data 🏔.

## What's next for EM😜JI🔥
Turning text 📜 into 🔜 raw memes 🐸! We 🇻🇮 already have some 💑 extra features built 🏗 and ready to go, they're 🆗 just 🙄 waiting 🚏🔄 for ⏺🎙 front 🚅 end 🔙💆 implementations 🔙. There ‼ are clearly some 💑 bug 🐛🐞 too - we 🇻🇮 dont 🇲🇶🇵🇷🆗 know 🙄👀 why 🤒 it 🤒 chooses ⚒ the virgin islands 🏞🗾🗿 flag 🚩🏴⚜ and 🚩 the moon 🌔🌕🌝 emojis 🌔🌕 so 🙄 often! We 🇻🇮 also hope 🙏 to 🙏 make some 💑 optimisations to improve loading 🔄 speed 🐎.
