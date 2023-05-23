import Button from '@material-ui/core/Button';
import React from 'react';
	

/* filter button for map page */
export default function FilterButton(props){
	return (
		<Button 
      style={{
        color: "#000000",
        fontWeight: "normal",
        textTransform: "none",
        paddingBottom: '5px',
        paddingTop: '5px',
        marginBottom: '30px',
        borderRadius: '20px',
        fontSize: '11px',
        marginRight: '5px',
      }}
      href="#" 
      variant="outlined" 
    >
      {props.title}
    </Button>
	);
}