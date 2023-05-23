import React from 'react';
import Rating from '@material-ui/lab/Rating';
import { withStyles, makeStyles } from '@material-ui/core/styles';
import StarBorderIcon from '@material-ui/icons/StarBorder';
import Box from '@material-ui/core/Box';


const StyledRating = withStyles({
  iconFilled: {
    color: '#04b39b',
  },
  iconHover: {
    color: '#04b39b',
  },
})(Rating);

const useStyles = makeStyles({
  root: {
    display: 'flex',
    alignItems: 'center',
  },
  box: {
    marginLeft: '7px'
  }
});

/* rating component (along with review number)*/
export default function CustomRating(props) {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <StyledRating
        name="customized-color"
        size='small'
        defaultValue={props.value}
        precision={1}
        getLabelText={(value) => `${value} Heart${value !== 1 ? 's' : ''}`}
        icon={<StarBorderIcon fontSize="inherit" />}
      />
      <Box className={classes.box}>{props.review}</Box>
    </div>
  );
}
