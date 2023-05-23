import 'package:flutter/material.dart';
import '../helpers/text_formats.dart';


class PandemicDataTable extends StatelessWidget {
  /* 
  * takes data list as argument, each list element expected to 
  * contain: affected, recovered, deaths, reportDate
  * returns a colorful table 
  */
  final data;
  const PandemicDataTable({Key key, this.data}) : super(key: key);

  String formatDate(String date){
    return date.split('T')[0];
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        padding: EdgeInsets.only(left: 10, right: 10, top: 40, bottom: 40),
        child: Table(
          border: TableBorder.all(),
          children: [
            // title row
            TableRow( children: [
                TableCell(
                  child: Container(
                    alignment: Alignment.center,
                    height: 80,
                    padding: EdgeInsets.all(10),
                    color: Colors.orange,
                    child: Text('Affected', style: TextStyle(fontWeight: FontWeight.bold)),
                  ),
                ),
                TableCell(
                  child: Container(
                    height: 80,
                    alignment: Alignment.center,
                    padding: EdgeInsets.all(10),
                    color: Colors.green,
                    child: Text('Recovered', style: TextStyle(fontWeight: FontWeight.bold,)),
                  ),
                ),
                TableCell(
                  child: Container(
                    height: 80,
                    alignment: Alignment.center,
                    padding: EdgeInsets.all(10),
                    color: Colors.red,
                    child: Text('Deaths', style: TextStyle(fontWeight: FontWeight.bold)),
                  ),
                ),
                TableCell(
                  child: Container(
                    height: 80,
                    alignment: Alignment.center,
                    padding: EdgeInsets.all(10),
                    color: Colors.blue,
                    child: Text('Date', style: TextStyle(fontWeight: FontWeight.bold)),
                  ),
                ),
            ]),
            // data row
            for (int i=0; i < data.length; i++ )
              TableRow( children: [
                TableCell(
                  child: Container(
                    alignment: Alignment.center,
                    padding: EdgeInsets.all(10),
                    color: Colors.orange[200],
                    child: Text(
                      makeCommaSeperatedNumber(data[i]['Confirmed']), 
                      textAlign: TextAlign.center,
                    ),
                  ),
                ),
                TableCell(
                  child: Container(
                    alignment: Alignment.center,
                    padding: EdgeInsets.all(10),
                    color: Colors.green[200],
                    child: Text(makeCommaSeperatedNumber(data[i]['Recovered']), textAlign: TextAlign.center),
                  ),
                ),
                TableCell(
                  child: Container(
                    alignment: Alignment.center,
                    padding: EdgeInsets.all(10),
                    color: Colors.red[200],
                    child: Text(makeCommaSeperatedNumber(data[i]['Deaths']), textAlign: TextAlign.center),
                  ),
                ),
                TableCell(
                  child: Container(
                    alignment: Alignment.center,
                    padding: EdgeInsets.all(10),
                    color: Colors.blue[200],
                    child: Text(formatDate(data[i]['Date'].toString()), textAlign: TextAlign.center),
                  ),
                ),
              ]),
          ],
        ),
      ),
    );
  }
}
