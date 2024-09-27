import React, { useState } from 'react';
import { fetchData } from '../services/api';

const FetchData = ({ setResults }) => {
 const [url, setUrl] = useState('');

 const handleSubmit = async (e) => {
  e.preventDefault();
  try {
   const response = await fetchData(url);
   setResults(response.data);
  } catch (error) {
   console.error(error);
  }
 };

 return (
  <form onSubmit={handleSubmit}>
   <input
    type="text"
    placeholder="Enter subreddit URL"
    value={url}
    onChange={(e) => setUrl(e.target.value)}
   />
   <button type="submit">Fetch Data</button>
  </form>
 );
};

export default FetchData;
