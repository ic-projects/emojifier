# EMOJIFIER
Now available for you to try at [emojifier.co.uk](http://www.emojifier.co.uk)!

## Inspiration
Meme 🐸 is love, ❤💘💌 meme 🐸 is life.

## What it does
Using 🐸 a combination ❤💘💌 of 🐸 word 😛 embeddings and neural 🐁 networks, 📵 the 5⃣ program predicts which emoji ⌨ is useful 🔧 based on 🔙 sentence 🚟 context.

## How we built it
We 🇺🇸 collected ® data 💁 from 🔙 Reddit 🇨🇺 and Twitter 📺 and 🐁 using 📵 TensorFlow 5⃣ we 🇺🇸 trained 🚋 the 5⃣ different 3⃣ models 🎎 such 🔧 as 🔜 character 🤓 level 🎚 LSTM, word 😛 level 🎚 LSTM and fixed input neural 🐁 network 🛰 and also using Google's 👓 word2vector for ⏹⏺ word 😛 embeddings.

Tying 🇺🇸 the 5⃣ front 🚅 end 🔚 to 🇨🇺 the 5⃣ back 🔙◀↩ end 🔚 was 📵 very 🤔 hard. 😣 We 🇺🇸 started 🔙 out ✌🔙 with 🆙 Ruby 💎 on 🔙 Rails 🚋 to 🎚 start 🔚 a 😛 background 🎚 Python 🐊🐆 process which was used 🐁 for ⏹⏺ the 5⃣ emoji ⌨ prediction but 🔙 we 🇺🇸 could 🔜 not 🤔 find 👀 a way 🌌 to append 📁 the 5⃣ standard input stream for ⏹⏺ the 5⃣ process, so 🤔 instead 🍶 we 🇺🇸 used Node.js to run 🎽 in 🔙 parallel with 🆙 a Python 🐊🐆 server 💻 which listened 👂 for ⏹⏺ POST 🏣🏤 requests from 🔙 the 5⃣ Node.js client and then 🔙 using Twmoji to beautifully 😔 render the 5⃣ final ▶ emojis.

## Challenges we ran into
Describing 🇺🇸 emojis 5⃣ as 🔜 a 🔚 single 🔂 word, 😛 problems 🔙◀↩ with 🆙 training 🚋 data 💁 on 🔙 TensorFlow. 🇺🇸

## Accomplishments that we're proud of
Having 🇺🇸 a 5⃣ finished 🏁 product 🏷 in 🔙 our 🇺🇸 first 9⃣ hackathon! 🆙

## What we learned
Learning 🏫 six 6⃣7⃣5⃣ different 3⃣ programming 📺 languages, 🇪🇨 more 🇺🇸 about 9⃣ machine 🎰 learning, 🏫 and using real world 🗺🌐🌏 data. 💁

## What's next for EM😜JI🔥
Turning ⤵ text 📜 into 🔙 raw 🆕 memes: 🐸 we 🇺🇸 already 🔜 have 🎰 some 💑 extra features built 🏛 and 🗺🌐🌏 ready 🔜 to go 🇹🇬 they're 🆗 just 🤔 waiting 🚏 for ⏹⏺ front 🚅 end 🔚 implementations.
