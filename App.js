import React, { useEffect, useState } from "react";

function App() {
  const [tweets, setTweets] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/tweets")
      .then((response) => response.json())
      .then((data) => setTweets(data))
      .catch((error) => console.error("Error fetching tweets:", error));
  }, []);

  return (
    <div>
      <h1>Real-Time Disaster Tweets</h1>
      {tweets.length === 0 ? (
        <p>Loading...</p>
      ) : (
        <ul>
          {tweets.map((tweet, index) => (
            <li key={index}>{tweet.text}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
