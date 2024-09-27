import React, { useState } from 'react';
import Login from '.components/Login';
import FetchData from './components/FetchData';
import DisplayResults from './components/DisplayResults';

function App() {
  const [results, setResults] = useState(null);

  return (
    <div className="App">
      <Login />
      <FetchData setResults={setResults} />
      {results && <DisplayResults results={results} />}
    </div>
  );
}

export default App;
