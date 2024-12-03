import React from 'react'
import './Home.css'

const Home = () => {
  return (
    <div className="h-screen overflow-y-hidden flex flex-col items-center justify-center mx-auto">
        <h1 className="mx-auto max-w-[686px] text-title text-center">Welcome to Sifa and Evangelos' EE250 Project</h1>
        <p className="mt-[30px] mb-[30px] w-[500px] text-center">This website finds the top YouTubers of whichever category you choose and gives you their email addresses for contact</p>
        <form action={`${"http://localhost:3000"}/youtuberData`} method="GET">
            <button type="submit">Click here</button>
        </form>
    </div>
  )
}


export default Home
