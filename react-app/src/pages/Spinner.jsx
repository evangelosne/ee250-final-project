import React from 'react';
import './Spinner.css';  

const Spinner = () => {
  return (
    <>
      <div className="spinner mx-auto mt-[50px]"></div>
      <p className="text-small-body text-[#5A5859] mx-auto mt-5">Loading...</p>
    </>
  );
};

export default Spinner;
