import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import Paper from '@material-ui/core/Paper';


/* Google Map API Component */
const MapMarker = ({ label }) => (
  <Paper 
    style={{
      backgroundColor: '#ffffff',
      zIndex: 9999,
      height: '20px',
      maxWidth: '50px',
      minWidth: '40px',
      fontSize: '12px',
      width: '40px',
      borderRadius: '10px',
      fontWeight: 'bold',
      textAlign: 'center',
      paddingTop: '7px',
      shadowOffset: {
        width: 1,
        height: 1
      }
    }}
  >
    {label}
  </Paper>
);
 
class SimpleGMap extends Component {
  static defaultProps = {
    center: {
     lat: 23.8103,
     lng: 90.4125
    },
    zoom: 14
  };
 
  render() {
    return (
      // Important! Always set the container height explicitly
      <div style={{ height: '100vh', width: '100%' }}>
        <GoogleMapReact
          bootstrapURLKeys={{ key: "API GOES HERE..." }}
          defaultCenter={this.props.center}
          defaultZoom={this.props.zoom}
        >
          <MapMarker
            lat={23.8103}
            lng={90.4125}
            label="$25"
          />

          <MapMarker
            lat={23.8103}
            lng={90.4211}
            label="$30"
          />

          <MapMarker
            lat={23.8103}
            lng={90.4299}
            label="$35"
          />

          <MapMarker
            lat={23.8103}
            lng={90.4025}
            label="$45"
          />
        </GoogleMapReact>
      </div>
    );
  }
}
 
export default SimpleGMap;
