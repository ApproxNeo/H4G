import './styles/App.css';
import NavBar from './components/Navbar';
import Footer from './components/Footer';
import AboutMeScreen from './screens/AboutMeScreen';
import ProblemScreen from './screens/ProblemScreen';
import ProjectScreen from './screens/ProjectScreen';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div>
        <NavBar/>
        <Routes>
          <Route path="/" element={<AboutMeScreen/>}/>
          <Route path="/problems" element={<ProblemScreen/>}/>
          <Route path="/projects" element={<ProjectScreen/>}/>
        </Routes>
        <Footer/>
    </div>
  );
}

export default App;
