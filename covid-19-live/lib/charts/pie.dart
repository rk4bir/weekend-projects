import 'package:flutter/material.dart';
import 'package:charts_flutter/flutter.dart' as charts;


class PieChart extends StatelessWidget {
	// Generates a percentage Pie chart: takes series data as argument
	final seriesData;
	PieChart({Key key, this.seriesData}) : super(key: key);

	@override
	Widget build(BuildContext context) {
		// main widget here...
		return Padding(
			padding: EdgeInsets.all(10),
			child: Container(
				height: 400,	// must needed property
				padding: EdgeInsets.only(top: 30),
				margin: EdgeInsets.only(bottom: 30),
				child: Center(
					child: Column(
						children: <Widget>[
							// chart
							Expanded(
								child: charts.PieChart(
									seriesData,
									animate: true,
									animationDuration: Duration(seconds: 2),
									behaviors: [
										new charts.DatumLegend(
											outsideJustification: charts.OutsideJustification.endDrawArea,
											horizontalFirst: true,
											desiredMaxRows: 2,
											cellPadding: new EdgeInsets.only(right: 10.0, bottom: 4.0, top:4.0),
											position: charts.BehaviorPosition.top,
											entryTextStyle: charts.TextStyleSpec(
												color: charts.MaterialPalette.black,
												fontFamily: 'Georgia',
												fontSize: 10,
												fontWeight: 'bold',
											),
										),
									],
									defaultRenderer: new charts.ArcRendererConfig(
										arcWidth: 80,
										arcRendererDecorators: [
								        	new charts.ArcLabelDecorator(
								        		showLeaderLines: true,
								            	labelPosition: charts.ArcLabelPosition.inside,
												insideLabelStyleSpec: charts.TextStyleSpec(
													color: charts.MaterialPalette.white,
													fontSize: 12,
													fontWeight: 'bold',
												),
								            )
								        ],
									),
								),
							),
						],
					),
				),
			),
		);
  	}
}
