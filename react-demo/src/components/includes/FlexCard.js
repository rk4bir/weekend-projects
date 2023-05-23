import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import 'typeface-roboto';
import Star from '@material-ui/icons/Star';
import Box from '@material-ui/core/Box';
import ListItemText from '@material-ui/core/ListItemText';
import ListItem from '@material-ui/core/ListItem';


const useStyles = makeStyles({
  root: {
    backgroundColor: 'transparent',
    marginBottom: '5px',
    padding: '2px'
  },
  longTitle: {
    fontSize: '14px',
    fontWeight: 'bold',
    marginTop: '-15px'
  },
  description: {
    paddingTop: '10px', 
    fontSize: '12px',
    color: 'textSecondary'
  },
  facility: {
    paddingTop: '5px', 
    fontSize: '13px',
  },
  other: {
    marginTop: '20px', 
    fontSize: '13px',
  },

  
  amount: {
    fontSize: '10px',
  },
  rating: {
    display: 'flex',
    paddingTop: '20px',
    fontSize: '12px',
  },
});

/* flex card for map page */
export default function ImgMediaCard(props) {
  const classes = useStyles();
  
  return (
    <Card className={classes.root} elevation={0}>

      {/*grid container */}
      <Grid container spacing={1}>

        {/* Image grid */}
        <Grid item md={6} >
          <CardMedia
            component="img"
            alt={props.imageTitle}
            height="200"
            image={props.src}
            style={{borderRadius: '20px'}}
          />
        </Grid>

        {/* content grid */}
        <Grid item md={6} >
          <CardContent className={classes.title}>

            {/* title */}
            <Typography variant="body1" component="p" className={classes.longTitle}>
              {props.longTitle}
            </Typography>
            
            {/* description */}
            <Typography  color="textSecondary" component="p" className={classes.description}>
                {props.description}
            </Typography>
            
            {/* facilities in brief */}
            <Typography  color="textSecondary" component="p" className={classes.facility}>
              {props.facility}
            </Typography>

            {/* other info */}
            <Typography  color="textSecondary" component="p" className={classes.other}>
              {props.other}
            </Typography>
            
            {/* rating, pricing, review info */}
            <ListItem style={{padding: '0px'}}>
              <Box className={classes.rating}>
                <Star fontSize='small' style={{marginTop: '-4px', marginRight: '4px', color: '#8bc34a'}} /> {props.rating} ({props.review})
              </Box>
              <ListItemText style={{marginLeft: '50px', fontSize: '12px'}} 
                primary={
                  <Typography component="p" style={{fontSize: '12px', fontWeight: 'bold', marginTop: '20px'}}>
                  ${props.amount}/ night
                  </Typography>
                }
                secondary={
                  <Typography color='textSecondary' component="p" style={{fontSize: '10px', fontWeight: 'normal'}}>
                  ${3*props.amount} total
                  </Typography>
                }
              />
            </ListItem>
          </CardContent>
        </Grid> {/* content grid item */}
      </Grid>
    </Card>
  );
}
