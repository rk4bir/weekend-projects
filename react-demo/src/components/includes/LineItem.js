import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import Add from '@material-ui/icons/Add';
import Remove from '@material-ui/icons/Remove';


export default function LineItem (props){
  const [amount, setAmount] = React.useState(0);

  const onPlusClick = () => {
    var newAmount = amount + 1;
    setAmount(newAmount);
  };
  const onMinusClick = () => {
    var newAmount = amount - 1;
    if ( newAmount < 0 ) newAmount = 0;
    setAmount(newAmount);
  };

  return (
    <Grid container style={{paddingLeft: '20px', paddingRight: '20px', paddingTop: '20px'}}>
      
      {/* title and subtitle grid item */}
      <Grid item md={9} style={{textAlign: 'left'}}>
        <Typography gutterBottom variant="p" component="p" style={{color: '#000000', fontSize: '15px', fontWeight: 'bold', background: 'transparent'}}>
          {props.title}
        </Typography>
        <Typography gutterBottom variant="p" component="p" style={{color: '#a3a29e', fontSize: '11px', background: 'transparent'}}>
          {props.subtitle}
        </Typography>
      </Grid>

      {/* amount and controllers grid item */}
      <Grid item  md={3} style={{textAlign: 'right', }}>
        <Box style={{display: 'flex'}}>
          <Remove onClick={onMinusClick} fontSize='small'/>
          <Typography gutterBottom variant="body" component="p" style={{color: '#000000', fontSize: '15px', marginLeft: '20px', marginRight: '20px'}}>{amount}</Typography>
          <Add onClick={onPlusClick} fontSize='small'/>
        </Box>
      </Grid>
    </Grid>
  );
}