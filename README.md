# ChatBot-SongRecommender

### Tech stack
- Backend: Flask, cakechat(backend server for chatbot)
- Frontend: React.js

# Demo Video 
[![ChatBot-SongRecommender](http://img.youtube.com/vi/Oo1N9rIRP0g/0.jpg)](http://www.youtube.com/watch?v=Oo1N9rIRP0g)


### Features

- Chatbot: user can chat with chatbot.
- Song Recommendation: Based on the "mood" of the user while chatting with chatbot songs are recommended dynamically.
- Similar Songs: Based on the last song listened by the user from the list of the recommended songs, similar songs are made available to the user.

### Implementation Details

- Mood of the user is analysed with help of 'IBM tone analyser'
- Chatbot: cakechat backend server is used as chatbot.
- Song Recommendation is done with help of 'last.fm' API
- User writes a message. Based on the user's message, IBM tone analyser analyses the mood of the user. This mood along with message is used for cakechat server to get chat response. Mood is also used to get songs recommendation from last.fm API.

## References
https://www.crio.do/projects/python-chatbot-api/?utm_source=email&utm_medium=newsletter



