import React from 'react';

const DisplayResults = ({ results }) => {
 return (
  <div>
   {/* Display the results as desired */}
   <h2>{results.title}</h2>
   <p>{results.description}</p>
   {/* Add more details */}
  </div>
 );
};

export default DisplayResults;
