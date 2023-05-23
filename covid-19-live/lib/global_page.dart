import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

// installed
import 'package:charts_flutter/flutter.dart' as charts;
	
import 'data/global.dart';
import 'data/global_daily.dart';

import 'charts/pie.dart';
import 'charts/bar.dart';

import 'widgets/active_data.dart';
import 'widgets/page_title.dart';
import 'helpers/text_formats.dart';
import 'widgets/pandemic_data_row.dart';
import 'widgets/loader.dart';


class GlobalPage extends StatefulWidget {
	// global page widget
 	@override
  	_GlobalPageState createState() => _GlobalPageState();
}


class _GlobalPageState extends State<GlobalPage> with TickerProviderStateMixin {
	// declaration of API data variables
	Future<CovidData> futureCovidData;
	Future<List> futureCovidDataDaily;

	@override
	void initState() {
		// initialize the state variables
		super.initState();
		futureCovidData = fetchCovidData();
		futureCovidDataDaily = fetchCovidDataDaily();
	}

	@override
	Widget build(BuildContext context) {
		// main widget
		return Container(
	        color: Colors.grey[50],
			child: Scaffold(
				backgroundColor: Colors.transparent,
		      	body: Column(
			        children: <Widget>[
			          	Expanded(
			            	child: _builGlobalDataPresentation(context),
			        	),
			        ],
		      	),
		    ),
	    );
	}

	Widget _builGlobalDataPresentation(BuildContext context){
		// build every child widgets
		return FutureBuilder<CovidData>(
            future: futureCovidData,
            builder: (context, snapshot) {
				if (snapshot.hasData) {
					// real time data
					int cases = snapshot.data.confirmed;
					int recovered = snapshot.data.recovered;
					int deaths = snapshot.data.deaths;
					int active = cases - (recovered + deaths);

					// data in percentage
					double active_percentage = double.parse(((active * 100)/cases).toStringAsFixed(2));
					double recovered_percentage = double.parse(((recovered * 100)/cases).toStringAsFixed(2));
					double deaths_percentage = double.parse(((deaths * 100)/cases).toStringAsFixed(2));

					// percentage data for pie
					var piedata = [
						new Task('Active Cases', active_percentage, Colors.pink),
						new Task('Recovered', recovered_percentage, Colors.green),
						new Task('Deaths', deaths_percentage, Colors.red),
					];

					var series = [
						charts.Series(
							domainFn: (Task task, _) => task.task,
							measureFn: (Task task, _) => task.taskvalue,
							colorFn: (Task task, _) =>
							charts.ColorUtil.fromDartColor(task.colorval),
							id: 'Pandemic data',
							data: piedata,
							labelAccessorFn: (Task row, _) => '${row.taskvalue}%',
						),
					];
					
					// return the pie chart and data containers
					return ListView(
	              		children: <Widget>[
	              			// Title
				            PageTitle(
				            	title: "Global Outbreak", 
				            	subTitle: "Last updated: " + lastUpdatedDateFormatter(snapshot.data.lastUpdate)
				            ),
	              			PieChart(seriesData: series),
	              			PandemicDataRow(
	              				infected: cases,
	              				recovered: recovered,
	              				deaths: deaths,
	              			),
			              	ActiveDataContainer(number: active, title: "ACTIVE CASES", bg: Colors.indigo[900]),
			              	Container(
			              		decoration: BoxDecoration(
							    	border: Border.all(color: Colors.grey[300])
							  	),
			              	),

			              	// daily bar chart report
			              	_buildGlobalDailyBarChart(context),
	              		],
	            	);
					
				} else if (snapshot.hasError) {
					return Center(
						child: Container(
							child: Text(
								"Make sure your internet is working.",
								style: TextStyle(
									fontSize: 20,
									color: Colors.pink,
								),
							),
						),
					);
				}
				// By default, show a loading spinner.
				return LoadingSpinner();
            },
        );
	}

	Widget _buildGlobalDailyBarChart(BuildContext context) {
		// builds global daily chart		
		String formatDateString(String dateString){
			String day = dateString.split('-')[1];
			String month = dateString.split('-')[2];
			return "$day/$month";
		}

		String makeShortNumber(double number){
			if (number.toString().length > 5) {
				String str = "";
				String str_num = number.toString();
				for ( int i=0; i < str_num.length - 5; i++ ) {
					str += str_num[i];
				}
				return str + "K";
			}

			return "$number";
		}

		return FutureBuilder<List>(
	        future: futureCovidDataDaily,
	        builder: (context, snapshot) {
				if (snapshot.hasData) {
					int len = snapshot.data.length - 1;
					var barChartData1 = [
						new Task(formatDateString(snapshot.data[len-6]['reportDate']), double.parse(snapshot.data[len-6]['confirmed']['total'].toStringAsFixed(1)), Colors.orange),
						new Task(formatDateString(snapshot.data[len-5]['reportDate']), double.parse(snapshot.data[len-5]['confirmed']['total'].toStringAsFixed(1)), Colors.orange),
						new Task(formatDateString(snapshot.data[len-4]['reportDate']), double.parse(snapshot.data[len-4]['confirmed']['total'].toStringAsFixed(1)), Colors.orange),
						new Task(formatDateString(snapshot.data[len-3]['reportDate']), double.parse(snapshot.data[len-3]['confirmed']['total'].toStringAsFixed(1)), Colors.orange),
						new Task(formatDateString(snapshot.data[len-2]['reportDate']), double.parse(snapshot.data[len-2]['confirmed']['total'].toStringAsFixed(1)), Colors.orange),
						new Task(formatDateString(snapshot.data[len-1]['reportDate']), double.parse(snapshot.data[len-1]['confirmed']['total'].toStringAsFixed(1)), Colors.orange),
						new Task(formatDateString(snapshot.data[len]['reportDate']), double.parse(snapshot.data[len]['confirmed']['total'].toStringAsFixed(1)), Colors.orange)
					];

                    var series1 = [
                      charts.Series(
                        domainFn: (Task task, _) => task.task,
                        measureFn: (Task task, _) => task.taskvalue,
                        colorFn: (Task task, _) => charts.ColorUtil.fromDartColor(task.colorval),
                        id: 'Daily summery',
                        data: barChartData1,
                        labelAccessorFn: (Task row, _) => '${makeShortNumber(row.taskvalue)}',
                      ),
                    ];

                    var barChartData3 = [
						new Task(formatDateString(snapshot.data[len-6]['reportDate']), double.parse(snapshot.data[len-6]['deaths']['total'].toStringAsFixed(1)), Colors.red),
						new Task(formatDateString(snapshot.data[len-5]['reportDate']), double.parse(snapshot.data[len-5]['deaths']['total'].toStringAsFixed(1)), Colors.red),
						new Task(formatDateString(snapshot.data[len-4]['reportDate']), double.parse(snapshot.data[len-4]['deaths']['total'].toStringAsFixed(1)), Colors.red),
						new Task(formatDateString(snapshot.data[len-3]['reportDate']), double.parse(snapshot.data[len-3]['deaths']['total'].toStringAsFixed(1)), Colors.red),
						new Task(formatDateString(snapshot.data[len-2]['reportDate']), double.parse(snapshot.data[len-2]['deaths']['total'].toStringAsFixed(1)), Colors.red),
						new Task(formatDateString(snapshot.data[len-1]['reportDate']), double.parse(snapshot.data[len-1]['deaths']['total'].toStringAsFixed(1)), Colors.red),
						new Task(formatDateString(snapshot.data[len]['reportDate']), double.parse(snapshot.data[len]['deaths']['total'].toStringAsFixed(1)), Colors.red)
					];

                    var series3 = [
                      charts.Series(
                        domainFn: (Task task, _) => task.task,
                        measureFn: (Task task, _) => task.taskvalue,
                        colorFn: (Task task, _) => charts.ColorUtil.fromDartColor(task.colorval),
                        id: 'Daily summery',
                        data: barChartData3,
                        labelAccessorFn: (Task row, _) => '${makeShortNumber(row.taskvalue)}',
                      ),
                    ];
                    // bar chart for last 6 days affected number
                    return Column(
                    	children: <Widget>[
                    		SizedBox(height: 100),
                    		Center(
			              		child: Text.rich(
				              		TextSpan(
				              			text: "Daily Cases",
					              		style: TextStyle(
					              			color: Colors.black,
					              			fontSize: 26,
					              			fontFamily: "Georgia",
					              			fontWeight: FontWeight.bold,
					              		),
					              		children: <TextSpan>[
					              			TextSpan(
						              			text: "\nLast 7 days data",
							              		style: TextStyle(
							              			color: Colors.grey,
							              			fontSize: 12,
							              			fontFamily: "Georgia",
							              			fontWeight: FontWeight.normal,
							              		),
					              			),
					              		],
				              		),
				              	),
			              	),
			              	BarChart(seriesData: series1, hideLegend: true),

			              	Container(
			              		decoration: BoxDecoration(
							    	border: Border.all(color: Colors.grey[300])
							  	),
			              	),
			              	
			              	SizedBox(height: 100),
                    		Center(
			              		child: Text.rich(
				              		TextSpan(
				              			text: "Daily Deaths",
					              		style: TextStyle(
					              			color: Colors.black,
					              			fontSize: 26,
					              			fontFamily: "Georgia",
					              			fontWeight: FontWeight.bold,
					              		),
					              		children: <TextSpan>[
					              			TextSpan(
						              			text: "\nLast 7 days data",
							              		style: TextStyle(
							              			color: Colors.grey,
							              			fontSize: 12,
							              			fontFamily: "Georgia",
							              			fontWeight: FontWeight.normal,
							              		),
					              			),
					              		],
				              		),
				              	),
			              	),
			              	BarChart(seriesData: series3, hideLegend: true),
                    	],
                    );
				} else if (snapshot.hasError) {
					return Center(
						child: Container(
							child: Text(
								"Could not fetch data from API!",
								style: TextStyle(
									fontSize: 20,
									color: Colors.pink,
								),
							),
						),
					);
				}

				// By default, show a loading spinner.
				return LoadingSpinner();
	        },
	    );
	}
}


class Task {
    String task;
    double taskvalue;
    Color colorval;

    Task(this.task, this.taskvalue, this.colorval);
}
