import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Data from './pages/Data';


function App() {
  return (
    <div className="App">
    <Router basename="/">
      <Routes>
        {/* Route to Landing Page (root) */}
        <Route path="/" element={<Home/>} />

        {/* Route to EnterLinks Page */}
        <Route path="/youtuberData" element={<Data/>} />
      </Routes>
    </Router>
    </div>
  );
}

export default App;