import 'package:flutter/material.dart';


class LoadingSpinner extends StatefulWidget {
  const LoadingSpinner ({ Key key}): super(key: key);
  _LoadingSpinnerState createState() => _LoadingSpinnerState();
}


class _LoadingSpinnerState extends State<LoadingSpinner> with TickerProviderStateMixin {
  	Widget build(BuildContext context) {
    	// main widget
    	return Center(
			child: Container(
				padding: EdgeInsets.all(30),
				child: CircularProgressIndicator(
				  	//backgroundColor: Colors.green[800],
				  	valueColor: AlwaysStoppedAnimation<Color>(Colors.green[800]),
				)
			),
		);
  	}
}
