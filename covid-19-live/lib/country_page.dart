import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

// installed
import 'package:charts_flutter/flutter.dart' as charts;
import 'package:autocomplete_textfield/autocomplete_textfield.dart';

// utilities
import 'helpers/text_formats.dart';
import 'data/country.dart';
import 'widgets/active_data.dart';
import 'charts/bar.dart';
import 'widgets/page_title.dart';
import 'widgets/pandemic_data_row.dart';
import 'widgets/table.dart';
import 'widgets/loader.dart';


class CountryPage extends StatefulWidget {
  // country page widget
  @override
  _CountryPageState createState() => new _CountryPageState();
}


class _CountryPageState extends State<CountryPage> {

  // API data declaration
  Future<CovidData> futureCovidData;
  Future<List> futureCovidCountryDailyAffectedData;
  Future<List> futureCovidCountryDailyDeathsData;
  Future<List> futureCovidCountryDailyRecoveredData;
  Future<List> futureCovidCountryDailyAllData;
  Future<List<Country>> futureAPICountryList;
  Future<String> futureCountryName;

  // auto complete search field widget object
  AutoCompleteTextField searchTextField;

  // default country name and its iso2 code
  String country = 'bangladesh';
  String iso2 = 'BD';

  void _setStateVariables(String country_name, String iso2){
    /*
    * function that initializes state variables
    * if country_name and iso2 is provided they're used otherwise use default values
    */

    // NB: if iso2 and country_name not provided, this function assumed them to be null string
    if ( country_name == '' && iso2 == '' ){
      futureCountryName = fetchCountryName().then((c){
        this.setState((){
          country = c[0]['name'];
          iso2 = c[0]['iso2'];
          futureCovidData = fetchCovidData(iso2);   // country data
          futureCovidCountryDailyAffectedData = fetchCovidCountryDailyAffectedData(iso2);   // cases summary
          futureCovidCountryDailyDeathsData = fetchCovidCountryDailyDeathsData(iso2);       // deaths summary
          futureCovidCountryDailyRecoveredData = fetchCovidCountryDailyRecoveredData(iso2); // recovered summary
          futureCovidCountryDailyAllData = fetchCovidCountryDailyAllData(iso2);             // daily all data summery
        });
      });
    } else {
      this.setState((){
        country = country_name;
        iso2 = iso2;
        futureCovidData = fetchCovidData(iso2);   // country data
        futureCovidCountryDailyAffectedData = fetchCovidCountryDailyAffectedData(iso2);   // cases summary
        futureCovidCountryDailyDeathsData = fetchCovidCountryDailyDeathsData(iso2);       // deaths summary
        futureCovidCountryDailyRecoveredData = fetchCovidCountryDailyRecoveredData(iso2); // recovered summary
        futureCovidCountryDailyAllData = fetchCovidCountryDailyAllData(iso2);             // daily all data summery
      });
    }
  }

  @override
  void initState() {
    // initializes state variables
    super.initState();
    futureAPICountryList = fetchAPICountryList();
    _setStateVariables('', ''); 
  }

  @override
  Widget build(BuildContext context) {
    // country page's main widget
    return Container(
      decoration: BoxDecoration(
        color: Colors.grey[50],
      ),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        body: Column(
          children: <Widget>[
            // autocomplete country search box
            _buildSearchBox(context, futureAPICountryList),
            SizedBox(height: 10, ),

            // dynamic api data driven widgets
            _buildDynamicWidgets(context, futureCovidCountryDailyAffectedData),
          ],
        ),
      ),
    );
  }

  Widget _buildDynamicWidgets(BuildContext context, Future<List> futureCovidCountryData){
    /*
    * The entire api based widgets are vlaidated via futureCovidCountryDailyData.   
    * If futureCovidCountryDailyData has no data then it will show greeting message, as ther're no data
    * Otherwise it will disply charts
    */
    return FutureBuilder<List>(
      future: futureCovidCountryData,
      builder: (context, snapshot){
        if( snapshot.hasData ) {

          // if list not empty return all charts and table
          if ( snapshot.data.length > 0 ) {
            return Expanded(
              child: ListView(
                children: <Widget>[
                  
                  // page title && main bar chart
                  PageTitle(title: country.toUpperCase(), subTitle: 'pandemic update'),
                  _buildMainBarChart(context),

                  // pandemic data row: affected, recovered, deaths
                  _buildPandemicDataRow(context, futureCovidData),
                  // pandemic data row: active cases with animation
                  _buildPandemicActiveDataBox(context, futureCovidData),

                  // daily bar charts
                  _buildSeperatorLine(context),
                  _buildBarDailyBarChart(context, futureCovidCountryDailyAffectedData, Colors.orange, "Daily Affected"),
                  _buildSeperatorLine(context),
                  _buildBarDailyBarChart(context, futureCovidCountryDailyRecoveredData, Colors.green, "Daily Recovered"),
                  _buildSeperatorLine(context),
                  _buildBarDailyBarChart(context, futureCovidCountryDailyDeathsData, Colors.red, "Daily Deaths"),

                  // daily data summary
                  SizedBox(height: 30,),
                  Center(
                    child: Text.rich(
                      TextSpan(
                        text: "Daily Summary",
                        style: TextStyle(
                          color: Colors.black,
                          fontSize: 26,
                          fontFamily: "Georgia",
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  ),
                  _buildDailyDataTable(context),
                ],
              ),
            );
            // if data list is empty return error message
          } else {
            return Center(
              child: Container(
                padding: EdgeInsets.only(top: 200, left: 20, right: 20, bottom: 20),
                child: Text(
                  "Great! No data for ${country} yet.",
                  style: TextStyle(
                    fontSize: 20,
                    color: Colors.green,
                  ),
                ),
              ),
            );
          }
        } else if (snapshot.hasError){
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
      }// builder
    );
  }

  String formatDateString(String dateString){
    /*
    * takes dateString as argument expected format: yyyy-mm-ddThh:mm:ss.msZ
    * returns mm/dd formatted string
    */
    String date = dateString.split('T')[0];
    String day = date.split('-')[2];
    String month = date.split('-')[1];
    return "$month/$day";
  }

  String makeShortNumber(double number){
    // takes integer, double. converts to string and converts to thousands 1000 => 1K
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

  Widget _buildBarDailyBarChart(BuildContext context, Future<List> futureCovidCountryDailyData, Color color, String title) {
    // builds daily bar chart on a given API data: can be used for affected, recovery and deaths charts
    return FutureBuilder<List>(
      future: futureCovidCountryDailyData,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          // has data 
          try{
            var api_data = snapshot.data;
            int len = api_data.length - 1;
            var barChartData = [
              new Task(formatDateString(api_data[len-6]['Date']), double.parse(api_data[len-6]['Cases'].toStringAsFixed(1)), color),
              new Task(formatDateString(api_data[len-5]['Date']), double.parse(api_data[len-5]['Cases'].toStringAsFixed(1)), color),
              new Task(formatDateString(api_data[len-4]['Date']), double.parse(api_data[len-4]['Cases'].toStringAsFixed(1)), color),
              new Task(formatDateString(api_data[len-3]['Date']), double.parse(api_data[len-3]['Cases'].toStringAsFixed(1)), color),
              new Task(formatDateString(api_data[len-2]['Date']), double.parse(api_data[len-2]['Cases'].toStringAsFixed(1)), color),
              new Task(formatDateString(api_data[len-1]['Date']), double.parse(api_data[len-1]['Cases'].toStringAsFixed(1)), color),
              new Task(formatDateString(api_data[len]['Date']), double.parse(api_data[len]['Cases'].toStringAsFixed(1)), color),
            ];

            var series = [
              charts.Series(
                domainFn: (Task task, _) => task.task,
                measureFn: (Task task, _) => task.taskvalue,
                colorFn: (Task task, _) => charts.ColorUtil.fromDartColor(task.colorval),
                id: 'Daily summery',
                data: barChartData,
                labelAccessorFn: (Task row, _) => '${makeCommaSeperatedNumber(row.taskvalue)}',
              ),
            ];

            return Column(
              children: <Widget>[
                SizedBox(height: 100),
                Center(
                  child: Text.rich(
                    TextSpan(
                      text: title,
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
                            fontSize: 14,
                            fontFamily: "Georgia",
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
                BarChart(seriesData: series, hideLegend: true,),
              ],
            );
            // if does not has
          } catch (er) {
            return Center(
              child: Container(
                child: Text(
                  "No data to show!",
                  style: TextStyle(
                    fontSize: 20,
                    color: Colors.pink,
                  ),
                ),
              ),
            );
          }
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
      }
    );
  }

  Widget _buildDailyDataTable(BuildContext context) {
    // builds table data presentation for gived API data
    return FutureBuilder<List>(
      future: futureCovidCountryDailyAllData,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return PandemicDataTable(data: snapshot.data.reversed.toList());
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
      }
    );
  }

  Widget _buildSeperatorLine(BuildContext context){
    // returns a seperator widget
    return Container(
      decoration: BoxDecoration(
        border: Border.all(color: Colors.grey[300])
      ),
    );
  }

  Widget _buildSearchBox(BuildContext context, Future<List<Country>> countries){
    // autocomplete search box widget
    return FutureBuilder<List<Country>> (
      future: countries,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return searchTextField = AutoCompleteTextField<Country>(
            clearOnSubmit: true,
            suggestions: snapshot.data,
            decoration: InputDecoration(
              contentPadding: EdgeInsets.all(10),
              hintText: "Search country",
              hintStyle: TextStyle(color: Colors.green[800]),
              border: new UnderlineInputBorder(
              borderSide: new BorderSide(
                  color: Colors.red
                )
              ),
            ),
            itemFilter: (item, query){
              return item.slug.toString().startsWith(query.toLowerCase());
            },
            itemSorter: (a, b) {
              return a.name.compareTo(b.name);
            },
            itemBuilder: (context, item) {
              return Container(
                padding: EdgeInsets.only(left: 20, right: 20, top: 10, bottom: 10),
                decoration: BoxDecoration(
                  border: Border.all(color: Colors.grey[300])
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: <Widget>[
                    Text(item.name, style: TextStyle(fontSize: 16)),
                    SizedBox(width: 20.0,),
                    Text(item.iso2, style: TextStyle(fontSize: 16)),
                  ],
                ),
              );
            },
            itemSubmitted: (item) {
              // when a country is selected from search result, it resets the state variables
              // and hence data from API are fetched again so the respective widgets
              _setStateVariables(item.name, item.iso2);
            }
          );
        } else if (snapshot.hasError) {
          return Center(
            child: Container(
              padding: EdgeInsets.only(top: 30),
              child: Text(
                "Couldn't fetch data!",
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
      }
    );
  }

  Widget _buildMainBarChart(BuildContext context){
    // builds main bar chart widget for country
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
          var barChartData = [
            new Task('Total Cases', double.parse(cases.toStringAsFixed(1)), Colors.orange),
            new Task('Active Cases', double.parse(active.toStringAsFixed(1)), Colors.pink),
            new Task('Recovered', double.parse(recovered.toStringAsFixed(1)), Colors.green),
            new Task('Deaths', double.parse(deaths.toStringAsFixed(1)), Colors.red),
          ];

          var series = [
            charts.Series(
              domainFn: (Task task, _) => task.task,
              measureFn: (Task task, _) => task.taskvalue,
              colorFn: (Task task, _) =>
              charts.ColorUtil.fromDartColor(task.colorval),
              id: 'country data',
              data: barChartData,
              labelAccessorFn: (Task row, _) => '${makeCommaSeperatedNumber(row.taskvalue)}',
            ),
          ];
          
          return BarChart(seriesData: series, hideLegend: true);
          
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

  Widget _buildPandemicDataRow(BuildContext context, Future<CovidData> data){
    // builds pandemic data row widget
    return FutureBuilder<CovidData>(
      future: data,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          // real time data
          int cases = snapshot.data.confirmed;
          int recovered = snapshot.data.recovered;
          int deaths = snapshot.data.deaths;
          int active = cases - (recovered + deaths);
         
          return PandemicDataRow(
            infected: cases,
            recovered: recovered,
            deaths: deaths,
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

  Widget _buildPandemicActiveDataBox(BuildContext context, Future<CovidData> data){
    // builds pandemic active data widget with animated raindrop
    return FutureBuilder<CovidData>(
      future: data,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          // real time data
          int cases = snapshot.data.confirmed;
          int recovered = snapshot.data.recovered;
          int deaths = snapshot.data.deaths;
          int active = cases - (recovered + deaths);
         
          return ActiveDataContainer(number: active, title: "ACTIVE CASES", bg: Colors.indigo[900]);
          
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
