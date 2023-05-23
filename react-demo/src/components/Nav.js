import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Button from '@material-ui/core/Button';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
// import Link from '@material-ui/core/Link';
import Container from '@material-ui/core/Container';
import { makeStyles } from '@material-ui/core/styles';
import { Link } from "react-router-dom";


const useStyles = makeStyles((theme) => ({
  '@global': {
    ul: {
      margin: 0,
      padding: 0,
      listStyle: 'none',
    },
  },
  appBar: {
    borderBottom: `1px solid ${theme.palette.divider}`,
  },
  toolbar: {
    flexWrap: 'wrap',
    paddin: 0,
    margin: 0,
  },
  toolbarTitle: {
    flexGrow: 1,
  },
  link: {
    margin: theme.spacing(1, 2),
    fontWeight: 'bold',
    fontSize: 14,
    color: '#000000',
    textDecoration: 'none'
  },
}));


// navigation 
export default function Nav() {
  const classes = useStyles();

  return (
    <AppBar position="static" color="transparent" elevation={0} className={classes.appBar}>
      <Container maxWidth='lg' style={{padding: '0px', margin: '0 auto'}}>
        <Toolbar className={classes.toolbar}>
          {/* brand name */}
          <Typography 
            variant="h4" 
            color='primary' 
            noWrap 
            className={classes.toolbarTitle}
            style={{
              color: "#8bc34a",
              fontWeight: "bold",
              textTransform: "none",
            }}
          >
            Aircnc
          </Typography>{/* brand name */}

          {/* nav links */}
          <nav>
            <Link to="/react-demo" className={classes.link}>Home</Link>
            <Link to='#' className={classes.link}>Host your name</Link>
            <Link to='#' className={classes.link}>Host your enterprise</Link>
            <Link to="/react-demo/map-page" className={classes.link}>Map Page</Link>
            <Link to="#" className={classes.link}>Log In</Link>
          </nav>{/* nav links */}

          {/*sign up button */}
          <Button 
            style={{
              color: "#ffffff",
              backgroundColor: "#8bc34a",
              borderRadius: "30px",
              fontWeight: "600",
              textTransform: "none",
            }}
            href="#" 
            variant="contained" 
            disableElevation className={classes.link}
          >
            Sign Up
          </Button>{/*sign up button */}
        </Toolbar>
      </Container>
    </AppBar>
  );
}
