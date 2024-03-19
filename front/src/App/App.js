import './App.css';
import './SideBar/SideBar'
import SideBar from './SideBar/SideBar';
import Main from './Main/Main';

function App() {
  return (
    <div className="App">
      <div className="App-SideBar">
        <SideBar />
      </div>
      <div className="App-Main">
        <Main />
      </div>
    </div>
  );
}

export default App;
