import './styles/App.css';
import NavBar from './components/Navbar';
import Footer from './components/Footer';
import AboutMeScreen from './screens/AboutMeScreen';

function App() {
  return (
    <div>
        <NavBar/>
        
        <AboutMeScreen/>

        <Footer/>
    </div>
  );
}

export default App;
