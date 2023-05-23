import React from 'react';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import FlexCard from './includes/FlexCard.js';
import Typography from '@material-ui/core/Typography';
import FilterButton from './includes/FilterButton.js';
import SimpleGMap from './includes/Map.js';

// images 
import img1 from './images/slide-items/h2.jpg';
import img2 from "./images/slide-items/h3.jpg";
import img3 from "./images/slide-items/h5.jpg";


// card items
const cardItems = [
  {
    'src': img1,
    'longTitle': "Discover the city's party scene",
    'amount': 35,
    'rating': 4.5,
    'review': 64,
    'description': "4 guests 2 bedrooms 2 bed 2 baths",
    'facility': "Wifi Air Conditioning Kitchen",
    'other': "Cancellation flexibility available",
  },
  {
    'src': img2,
    'longTitle': "Discover the city's party scene",
    'amount': 45,
    'rating': 5,
    'review': 164,
    'description': "4 guests 2 bedrooms 2 bed 2 baths",
    'facility': "Wifi Air Conditioning Kitchen",
    'other': "Cancellation flexibility available",
  },
  {
    'src': img3,
    'longTitle': "Discover the city's party scene",
    'amount': 45,
    'rating': 5,
    'review': 164,
    'description': "4 guests 2 bedrooms 2 bed 2 baths",
    'facility': "Wifi Air Conditioning Kitchen",
    'other': "Cancellation flexibility available",
  }
]


export default function MapPage (props) {
  return (
    <Grid container spacing={0}>
       
      {/* left contents grid */} 
      <Grid item md={5} xs={12}>
        <Paper style={{padding: '20px'}}>
            <Typography  color="textSecondary" component="p" style={{fontSize: '12px'}}>
              122 stays, Apr 13-20 3 guests
            </Typography>
            <Typography component="p" style={{fontSize: '18px', fontWeight: 'bold', paddingBottom: '20px'}}>
              Stay In Dhaka Division
            </Typography>

            <FilterButton title="Cancellation flexibility" />
            <FilterButton title="Price" />
            <FilterButton title="Type of place" />
            <FilterButton title="Instant book" />
            
            {cardItems.map((cardItem) => (
              <FlexCard 
                src={cardItem.src}
                longTitle={cardItem.longTitle} 
                amount={cardItem.amount}
                review={cardItem.review}
                description={cardItem.description}
                facility={cardItem.facility}
                other={cardItem.other}
                rating={cardItem.rating}
              />
            ))}
        </Paper>
      </Grid>

      {/* Google map content grid */}
      <Grid item md={7} xs={12}>        
        <SimpleGMap />
      </Grid>
    </Grid>
  );
}
