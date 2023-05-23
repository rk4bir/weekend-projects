import 'package:flutter/material.dart';
import 'counter.dart';


class PandemicDataRow extends StatelessWidget {
  /*
  * takes infected, recovered, deaths
  * returns two row of data infected counter, recovered counter, death counter object
  */
  final infected;
  final recovered;
  final deaths;

  PandemicDataRow({Key key, this.infected, this.recovered, this.deaths}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.only(left: 20, right: 20, top: 15, bottom: 15),
      margin: EdgeInsets.only(left:10, right: 10),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20),
        color: Colors.grey[100],
        boxShadow: [
          BoxShadow(
            offset: Offset(0, .5),
            blurRadius: .3,
            color: Colors.grey,
          ),
        ],
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: <Widget>[
          // infected counter
          Counter(
            color: Colors.pink[800],
            number: infected,
            title: "Total Infected",
          ),
          // recovered counter
          Counter(
            color: Colors.green[800],
            number: recovered,
            title: "Total Recovered",
          ),
          // deaths counter
          Counter(
            color: Colors.red[800],
            number: deaths,
            title: "Total Deaths",
          ),
        ],
      ),
    );
  }
}
