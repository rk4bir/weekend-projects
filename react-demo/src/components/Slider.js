import React, { useState } from 'react';
import ItemsCarousel from 'react-items-carousel';
import Grid from '@material-ui/core/Grid';
import ImgMediaCard from './includes/Card.js';
import ChevronRight from '@material-ui/icons/ChevronRight';
import ChevronLeft from '@material-ui/icons/ChevronLeft';
import IconButton from '@material-ui/core/IconButton';

// images
import img1 from './images/slide-items/h1.jpg';
import img2 from "./images/slide-items/h2.jpg";
import img3 from "./images/slide-items/h3.jpg";
import img4 from './images/slide-items/h4.jpg';
import img5 from "./images/slide-items/h5.jpg";
import img6 from "./images/slide-items/h6.jpg";


const homeItems = [
  {
    'src': img1,
    'imageTitle': 'NIGHTLIFE - NEW YORK',
      'longTitle': "Unique Cob Cottage",
      'amount': 128,
      'rating': 5,
      'review': '284 - superhost',
  },
  {
    'src': img2,
    'imageTitle': 'ENTERTAINMENT - VANCOUVER',
      'longTitle': "The Joshua Tree House",
      'amount': 250,
      'rating': 5,
      'review': '284 - superhost',
  },
  {
    'src': img3,
    'imageTitle': 'PHOTO CLASS - LOS ANGELES',
      'longTitle': "A Pirate's Life For Me!",
      'amount': 209,
      'rating': 5,
      'review': '179 - superhost',
  },
  {
    'src': img4,
    'imageTitle': 'NIGHTLIFE - NEW YORK',
      'longTitle': "Unique Cob Cottage",
      'amount': 128,
      'rating': 5,
      'review': '284 - superhost',
  },
  {
    'src': img5,
    'imageTitle': 'ENTERTAINMENT - VANCOUVER',
      'longTitle': "The Joshua Tree House",
      'amount': 250,
      'rating': 5,
      'review': '284 - superhost',
  },
  {
    'src': img6,
    'imageTitle': 'PHOTO CLASS - LOS ANGELES',
      'longTitle': "A Pirate's Life For Me!",
      'amount': 209,
      'rating': 5,
      'review': '179 - superhost',
  },
]

export default function ItemCarouselSlider( ) {
  const [activeItemIndex, setActiveItemIndex] = useState(0);
  const chevronWidth = 40;
  return (
    <Grid item spacing={1}>
      <ItemsCarousel
        requestToChangeActive={setActiveItemIndex}
        activeItemIndex={activeItemIndex}
        numberOfCards={3}
        gutter={20}
        leftChevron={<IconButton color="primary" aria-label="upload picture" component="span">
          <ChevronLeft />
        </IconButton>}
        rightChevron={<IconButton color="primary" aria-label="upload picture" component="span">
          <ChevronRight />
        </IconButton>}
        outsideChevron
        chevronWidth={chevronWidth}
      >
        {homeItems.map((homeItem) => (
          <Grid item md={12} xs={12}>
              <ImgMediaCard 
                src={homeItem.src} 
                imageTitle={homeItem.imageTitle}
                longTitle={homeItem.longTitle}
                amount={homeItem.amount}
                rating={homeItem.rating}
                review={homeItem.review}
              />
          </Grid>
        ))}
      </ItemsCarousel>
    </Grid>
  );
}