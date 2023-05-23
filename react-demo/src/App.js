import React from 'react';
import Container from '@material-ui/core/Container';
// import logo from './logo.svg';
import './App.css';
import Nav from './components/Nav.js';
// import LoginForm from './components/LoginForm.js';
import LandingPage from './components/LandingPage.js';
import MapPage from './components/MapPage.js';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

function App() {
  return (
  	<Router>
	    <div className="App"> 	
	      	<Nav />
	      	<Container className='PageContainer' maxWidth="lg">
	      		<Switch>
	      			<Route exact path="/react-demo">
	      				<LandingPage />
	      			</Route>
	      			<Route exact path="/react-demo/map-page">
	      				<MapPage />
	      			</Route>
	      		</Switch>
	      	</Container>
	    </div>
    </Router>
  );
}

export default App;
