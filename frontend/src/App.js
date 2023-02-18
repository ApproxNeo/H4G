import NavBar from './components/Navbar';
import Footer from './components/Footer';
import AboutMeScreen from './screens/AboutMeScreen';
import ProblemScreen from './screens/ProblemScreen';
import ProjectScreen from './screens/ProjectScreen';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div style={{display: 'flex', flexDirection: 'column', minHeight: '100vh'}}>
        <NavBar/>
          <div style={{flex: 1, flexGrow: 1, height: '100%'}}>
            <Routes>
              <Route path="/" element={<AboutMeScreen/>}/>
              <Route path="/problems" element={<ProblemScreen/>}/>
              <Route path="/projects" element={<ProjectScreen/>}/>
            </Routes>
          </div>
        <Footer/>
    </div>
  );
}

export default App;
