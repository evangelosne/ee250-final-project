import React from 'react'
import { useState, useEffect } from 'react'
// import axios from "axios";
import Spinner from './Spinner'

const Data = () => {

  // const [data, setData] = useState(null)
  const [list, setList] = useState([])
  // function getData() {
  //   axios({
  //     method: "GET",
  //     url:"http://localhost:5000/youtuberData",
  //   })
  //   .then((response) => {
  //     const res = response.data
  //     setData(({
  //       yt_name: res.name,
  //       yt_email: res.email}))
  //   }).catch((error) => {
  //     if (error.response) {
  //       console.log(error.response)
  //       console.log(error.response.status)
  //       console.log(error.response.headers)
  //       }
  //   })}

  useEffect(() => {
    fetch('http://127.0.0.1:5000/youtuberData')
      .then(response => response.json())
      .then(list => setList(list));
  }, []);

  return (
    <div className="h-screen overflow-y-hidden text-center">
      <div className="flex flex-col text-[#5A5859] text-3xl justify-center" style={{width: "100vw", height: "75vh"}}>
      <div>Top Trending Youtube Channels in Category</div>
      {list.length > 0 ? (
        <ul>
          {list.map((item, index) => (
            <li key={index}>{index+1}. {item}</li>
          ))}
        </ul>
      ) : (
        <div className="flex flex-col text-align text-xl justify-center" style={{width: "100vw", height: "75vh"}}><Spinner /></div>
      )}
      </div>
    </div>
  )
}
export default Data
