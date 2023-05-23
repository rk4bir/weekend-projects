import 'package:flutter/material.dart';
import '../helpers/text_formats.dart';
import '../animations/drop.dart';
import 'drop.dart';

class Counter extends StatelessWidget {
  /*
  * takes number, color, title as arguments
  * returns a counter with a static rain drop on top of the number 
  * and title in the bottom of the number
  */
  final int number;
  final Color color;
  final String title;
  const Counter({
    Key key,
    this.number,
    this.color,
    this.title,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        
        // rain drop
        RainDrop(color: color),
        
        // padding
        SizedBox(height: 10),

        // number
        Text(
          '${makeCommaSeperatedNumber(number)}',
          style: TextStyle(
            fontSize: 24, 
            fontWeight: FontWeight.bold,
            fontFamily: "Georgia",
            color: color,
            shadows: [
              Shadow(
                  blurRadius: 2.0,
                  color: Colors.grey,
                  offset: Offset(1.0, 1.0),
              ),
            ],
          ),
        ),

        // title`
        Text(
          title, 
          style: TextStyle(
            fontSize: 12, 
            fontFamily: "Georgia",
            color: color,
            shadows: [
              Shadow(
                blurRadius: 2.0,
                color: Colors.grey,
                offset: Offset(0.5, 0.5),
              ),
            ],
          ),
        ),
      ],
    );
  }
}
