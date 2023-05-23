import 'package:flutter/material.dart';
import 'package:charts_flutter/flutter.dart' as charts;


class BarChart extends StatelessWidget {
  /*
  * Bar chart based on date string and corresponding number
  * it takes series data of charts.Series object and hideLegend (true or false) 
  * that controls showing of chart label
  */
  final seriesData;
  final hideLegend;
  BarChart({Key key, this.seriesData, this.hideLegend}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // main widget 
    return Padding(
      padding: EdgeInsets.all(10),
      child: Container(
        height: 500,  // must needed property
        padding: EdgeInsets.only(top: 40,),
        margin: EdgeInsets.only(bottom: 30),
        child: Center(
          child: Column(
            children: <Widget>[
              // chart
              Expanded(
                child: charts.BarChart(
                  seriesData,
                  animate: true,
                  animationDuration: Duration(seconds: 1),
                  domainAxis: new charts.OrdinalAxisSpec(),
                  barRendererDecorator: new charts.BarLabelDecorator(
                    insideLabelStyleSpec: new charts.TextStyleSpec(
                      color: charts.MaterialPalette.white,
                      fontFamily: 'Georgia',
                      fontWeight: 'bold',
                      fontSize: 10,
                    ),
                    outsideLabelStyleSpec: new charts.TextStyleSpec(
                      color: charts.MaterialPalette.black,
                      fontFamily: 'Georgia',
                      fontWeight: 'bold',
                      fontSize: 10,
                    ),
                  ),
                  behaviors: [
                    // shows legend if hideLegend is not provided or passed false value
                    if( hideLegend == null || hideLegend == false ) new charts.DatumLegend(
                        outsideJustification: charts.OutsideJustification.endDrawArea,
                        horizontalFirst: true,
                        desiredMaxRows: 2,
                        cellPadding: new EdgeInsets.only(right: 10.0, bottom: 4.0, top:20.0),
                        position: charts.BehaviorPosition.bottom,
                        entryTextStyle: charts.TextStyleSpec(
                          color: charts.MaterialPalette.black,
                          fontFamily: 'Georgia',
                          fontSize: 12,
                        ),
                      ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
