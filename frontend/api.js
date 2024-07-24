import React, { useState } from 'react';
import axios from 'axios';

function redditFetcher() {
 const [url, setUrl] = useState('');
 const [data, setData] = useState(null);
 const [loading, setLoading] = useState(false);
}

const fetchData = async () => {
 setLoading(true);
 try {
  const response = await axios.post('http://localhost:5000/fetch', { url });
  setData(response.data);
 } catch (error) {
  console.error('Error fetching data', error);
 } finally {
  setLoading(false);
 }
};

return (
 <div>
  <input type="text" value={url} onChange={(e) => setUrl(e.target.value)} placeholder="Enter Reddit URL" />
  <button onClick={fetchData} disabled={loading}>Analyze</button>
  {loading && <p>Loading...</p>}
  {data && <div>
   <h3>Results:</h3>
   <p>Title: {data.title}</p>
   <p>Sentiments: {JSON.stringify(data.sentiments)}</p>
   <p>Emotions: {JSON.stringify(data.emotions)}</p>
  </div>}
 </div>
);
