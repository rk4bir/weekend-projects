import 'date-fns';
import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Link from '@material-ui/core/Link';
import Box from '@material-ui/core/Box';
import FormControl from '@material-ui/core/FormControl';
import InputBase from '@material-ui/core/InputBase';
import ChevronRight from '@material-ui/icons/ChevronRight';
import Search from '@material-ui/icons/Search';
import DateFnsUtils from '@date-io/date-fns';
import {
  MuiPickersUtilsProvider,
  KeyboardDatePicker,
} from '@material-ui/pickers';
import ListItemText from '@material-ui/core/ListItemText';
import ListItem from '@material-ui/core/ListItem';
import ExpandLess from '@material-ui/icons/ExpandLess';
import ExpandMore from '@material-ui/icons/ExpandMore';
import List from '@material-ui/core/List';
import Collapse from '@material-ui/core/Collapse';
import Button from '@material-ui/core/Button';

import ImgMediaCard from './includes/Card.js';
import ItemCarouselSlider from './Slider.js';
import LineItem from './includes/LineItem.js';

// images
import img1 from './images/cards/night-life.jpg';
import img2 from './images/cards/entertainment.jpg';
import img3 from './images/cards/photo-class.jpg';
import img4 from './images/cards/photography.jpg';


// styles
const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    display: 'flex',
    marginTop: '50px'
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
    marginBottom: '15px'
  },
  header: {
  	fontSize: '20px',
  	fontWeight: 'bold',
  },
  link: {
  	textAlign: 'right',
  	fontSize: '12px',
  	fontWeight: 'normal',
  },
  linkBox: {
  	textAlign: 'right',
  	marginBottom: '10px'
  }
}));


// card items
const experiencItems = [
	{
		'src': img1,
		'imageTitle': 'NIGHTLIFE - NEW YORK',
  		'longTitle': "Discover the city's party scene",
  		'amount': 35,
  		'rating': 5,
  		'review': 64,
	},
	{
		'src': img2,
		'imageTitle': 'ENTERTAINMENT - VANCOUVER',
  		'longTitle': "Tour with an Enthusiastic local!",
  		'amount': 3,
  		'rating': 5,
  		'review': 1,
	},
	{
    'src': img3,
		'imageTitle': 'PHOTO CLASS - LOS ANGELES',
  		'longTitle': "Must Have L.A. Pictures!",
  		'amount': 39,
  		'rating': 5,
  		'review': 179,
	},
	{
    'src': img4,
		'imageTitle': 'PHOTOGRAPHY - NEW YORK',
  		'longTitle': "Retro photoshot in NYC",
  		'amount': 49,
  		'rating': 5,
  		'review': 72,
	},
]


export default function LandingPage() {
  const classes = useStyles();

  // state management
  const [selectedDate, setSelectedDate] = React.useState(new Date('2021-05-08T21:11:59'));
  const [open, setOpen] = React.useState(true);

  const handleClick = () => {
    setOpen(!open);
  };

  const handleDateChange = (date) => {
    setSelectedDate(date);
  };

  return (
    <div className={classes.root}>
      {/* container grid */}
      <Grid container spacing={3}>
        {/* left content grid */}
        <Grid item lg={4} md={4} xs={12}>
          <Paper className={classes.paper} style={{textAlign: 'left'}}>
            <Typography gutterBottom variant="p" component="p" style={{fontSize: '14px', fontWeight: 'bold', background: 'transparent'}}>
              LOCATION
            </Typography>

            {/* location input */}
            <FormControl fullWidth variant="filled" style={{border: 'none'}}>
              <InputBase
                className={classes.input}
                placeholder="Add city, landmark or address"
                inputProps={{ 'aria-label': 'Add city, landmark or address' }}
                style={{fontSize: '12px'}}
              />
            </FormControl>
          </Paper>

          <Grid container spacing={1}>
              <MuiPickersUtilsProvider utils={DateFnsUtils}>
                <Grid item md={6} xs={6}>
                  <Paper className={classes.paper} style={{textAlign: 'left'}}>
                    <KeyboardDatePicker
                      disableToolbar
                      variant="inline"
                      format="MM/dd/yyyy"
                      margin="normal"
                      id="date-picker-inline"
                      label="Arival"
                      value={selectedDate}
                      onChange={handleDateChange}
                      KeyboardButtonProps={{
                        'aria-label': 'Arival Date',
                      }}
                    />
                  </Paper>
                </Grid>
                <Grid item md={6} xs={6}>
                  <Paper className={classes.paper} style={{textAlign: 'left'}}>
                    <KeyboardDatePicker
                      disableToolbar
                      variant="inline"
                      format="MM/dd/yyyy"
                      margin="normal"
                      id="date-picker-inline-2"
                      label="Departure"
                      value={selectedDate}
                      onChange={handleDateChange}
                      KeyboardButtonProps={{
                        'aria-label': 'Departure Date',
                      }}
                    />
                  </Paper>
                </Grid>
              </MuiPickersUtilsProvider>
          </Grid>

          <Paper className={classes.paper} style={{textAlign: 'left', marginBottom: '1px', padding: '0'}}>
            <ListItem button onClick={handleClick}>
              <Typography gutterBottom variant="p" component="p" style={{color: '#a3a29e', fontSize: '12px',  background: 'transparent'}}>
                Guests
              </Typography>
              <ListItemText primary="" />
              {open ? <ExpandLess /> : <ExpandMore />}
            </ListItem>
            <Collapse in={open} timeout="auto" unmountOnExit>
              <List component="div" disablePadding>
                <ListItem button className={classes.nested}>
                  <Typography gutterBottom variant="p" component="p" style={{color: '#000000', fontSize: '15px', fontWeight: 'bold', background: 'transparent'}}>
                    2 ADULTS, 1 CHILD
                  </Typography>
                </ListItem>
              </List>
            </Collapse>
          </Paper>

          <Paper className={classes.paper} style={{marginBottom: '0', padding: '0'}}>
            <LineItem title='ADULTS' subtitle='' />
            <LineItem title='CHILD' subtitle='Age: 2-12' />
            <LineItem title='BABIES' subtitle='Younger than 2' />
            <Grid item style={{padding: '10px', textAlign: 'right'}}>
              <Button 
                variant='outlined' 
                size='small'
                style={{
                color: "#8bc34a",
                borderColor: '#8bc34a'
              }}
              >
                Apply
              </Button>
            </Grid>
          </Paper>

          <Button 
            style={{
              marginTop: '15px', 
              textTransform: "none", 
              paddingTop: '10px', 
              paddingBottom: '10px',
              color: "#ffffff",
              backgroundColor: '#8bc34a'
            }}
            variant='contained'
            color='primary'
            elevation={0}
            fullWidth
          >
            <Search fontSize='small'/> Search
          </Button>
                    
        </Grid>

        {/* content card based grid: right */}
        <Grid item lg={8} md={8} xs={12}>
        
        	{/* title: experiences */}
        	<Typography gutterBottom variant="body" component="body" className={classes.header}>
		          Experiences
		      </Typography>

		      <Box className={classes.linkBox}>
		    	  <Link href="#" underline='none' color="inherit" className={classes.link}>
				      See all<ChevronRight fontSize='small' />
				    </Link>
			    </Box>
          <Grid container spacing={1}>
            	{experiencItems.map((experiencItem) => (
    	        <Grid item md={3} xs={6}>
    	          	<ImgMediaCard 
    	          		src={experiencItem.src} 
    	          		imageTitle={experiencItem.imageTitle}
    	          		longTitle={experiencItem.longTitle}
    	          		amount={experiencItem.amount}
    	          		rating={experiencItem.rating}
    	          		review={experiencItem.review}
    	          	/>
    	        </Grid>
            	))}
          </Grid>

          {/* title: home */}
          <Typography gutterBottom variant="body" component="body" className={classes.header}>
                Homes
          </Typography>

    	    <Box className={classes.linkBox}>
    	    	<Link href="#" underline='none' color="inherit" className={classes.link}>
    			    See all<ChevronRight fontSize='small' />
    			 </Link>
    			</Box>
          {/* card items carousel */}
	        <ItemCarouselSlider />
        </Grid>
      </Grid>
    </div>
  );
}
