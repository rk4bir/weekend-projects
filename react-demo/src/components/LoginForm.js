import React from 'react';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import { shadows } from '@material-ui/system';



const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },

  form: {
    marginTop: theme.spacing(1),
  },
  formControl: {
    marginTop: '10px',
    marginBottom: '5px',
  },
  select: {
    backgroundColor: '#ffffff',
    border: '1px solid #d4cfcf',
    borderBottom: 'none',
  },
  textfield: {
    borderColor: 'green'
  }
}));


/* login form */
export default function LoginForm() {
  const classes = useStyles();
  const [country, setCountry] = React.useState('');
  
  const handleChange = (event) => setCountry(event.target.value);

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Typography component="h1" variant="h5" style={{fontSize: '16px', fontWeight: 'bold' }}>
          Log In
        </Typography>
        <form className={classes.form} noValidate>

          <FormControl fullWidth variant="filled" className={classes.formControl}>
            <InputLabel id="select-filled-label">Country/Region</InputLabel>
            <Select
              labelId="select-filled-label"
              id="select-filled"
              value='3'
              className={classes.select}
              onChange={handleChange}
            >
              <MenuItem value={1}>China(+86)</MenuItem>
              <MenuItem value={2}>Japan(+81)</MenuItem>
              <MenuItem value={3}>Bangladesh(+88)</MenuItem>
            </Select>
          </FormControl>
 
          <TextField
            variant="outlined"
            margin="normal"
            fullWidth
            name="phone"
            label="Phone Number"
            type="text"
            id="phone"
          />
          <Typography component="body" variant="h5" style={{marginTop: '6px', padding: '4px', color: 'grey', fontSize: '13px' }}>
            We'll call or text you to confirm your number. Standard message and data rates apply.
          </Typography>
          
          {/*continue button */}
          <Button 
            style={{
              color: "#ffffff",
              backgroundColor: "#8bc34a",
              fontWeight: "normal",
              textTransform: "none",
              marginTop: '10px',
              marginBottom: '10px',
              paddingTop: '10px',
              paddingBottom: '10px',
              borderRadius: '10px',
            }}
            fullWidth='true'
            href="#" 
            variant="contained" 
            disableElevation className={classes.link}
          >
            Continue
          </Button>{/*sign up button */}

          <Grid container>
            <Grid item>
              <Typography component="body" variant="h5" style={{marginTop: '6px', padding: '4px', color: 'grey', fontSize: '12px', textAlign: 'center' }}>          
                Don't have an account?
                <Link style={{fontWeight: 'bold', color: '#000000', marginLeft: '5px'}} href="#" variant="body" underline='none'>
                  {"Sign Up"}
                </Link>
              </Typography>
            </Grid>
          </Grid>
        </form>
      </div>
    </Container>
  );
}
