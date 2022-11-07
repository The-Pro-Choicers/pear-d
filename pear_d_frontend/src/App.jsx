import {Login, Home} from './pages';
import {Routes, Route} from 'react-router-dom';
import './App.css';


function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<Login/>}/>
        <Route path='/home' element={<Home/>}/>
      </Routes>
      
    </div>
  );
}

export default App;
