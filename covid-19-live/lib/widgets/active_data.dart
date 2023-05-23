import 'package:flutter/material.dart';
import '../helpers/text_formats.dart';
import '../animations/drop.dart';


class ActiveDataContainer extends StatelessWidget {
	/*
	* This widget takes number, title and bg (background color) as arguments
	* returns animated rain drop and number with the given backgroud color
	*/
	final int number;
	final String title;
	final bg;
	
	ActiveDataContainer({Key key, this.number, this.title, this.bg}) : super(key: key);

	@override
	Widget build(BuildContext context) {
	    return Container(
			margin: const EdgeInsets.only(left: 40, right: 40, top: 15, bottom: 40),
			padding: const EdgeInsets.only(top: 10, bottom: 10, left: 15, right: 15),
			alignment: Alignment.center,
			child: Column(
				children: <Widget>[
					// animated raindrop
					AnimatedRainDrop(color: Colors.indigo[700], size: 50.0),

					// number
					Text.rich(
						TextSpan(
							text: '${makeCommaSeperatedNumber(number)}',
							style: TextStyle(
								fontSize: 48, 
								fontWeight: FontWeight.bold,
								fontFamily: "Georgia",
								color: Colors.indigo[700],
								shadows: [
							        Shadow(
							          	blurRadius: 3.0,
							          	color: Colors.grey,
							          	offset: Offset(2.0, 2.0),
							        ),
							    ],
							),
							// title
							children: <TextSpan>[
						      	TextSpan(
						      		text: '\n$title ', 
						      		style: TextStyle(
						      			fontSize: 14, 
						      			fontWeight: FontWeight.normal,
						      			color: Colors.indigo[600],
						      			fontFamily: "Georgia",
						      			shadows: [
									        Shadow(
									          	blurRadius: 1.0,
									          	color: Colors.grey,
									          	offset: Offset(.5, .5),
									        ),
									    ],
						      		)
						      	),
						    ],
						),
					),
				],
			),
		);
	}
}
