import {Landing, Login, Home, SignUp, Activate, Restaurants, ResetPassword, ResetPasswordConfirm} from './pages';
import {Routes, Route} from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './store';
import './App.css';


function App() {
  return (
  <Provider store={store}>
    <div className="App">
      
        <Routes>
          <Route path='/' element={<Landing/>}/>
          <Route path='/login' element={<Login/>}/>
          <Route path='/home' element={<Home/>}/>
          <Route path='/signup' element={<SignUp/>}/>
          <Route path='/passreset' element={<ResetPassword/>}/>
          <Route path='/password/reset/confirm/:uid/:token' element={<ResetPasswordConfirm/>}/>
          <Route path='/activate/:uid/:token' element={<Activate/>} />
        </Routes>
    </div>
  </Provider>
      
      
    
  );
}

export default App;
