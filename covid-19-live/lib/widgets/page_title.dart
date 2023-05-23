import 'package:flutter/material.dart';


class PageTitle extends StatelessWidget {
  // returns a title and subtitle widget for given values
  final String title;
  final String subTitle;
  PageTitle({Key key, this.title, this.subTitle}) : super(key: key);

  @override  
  Widget build(BuildContext context){
    return Center(
      child: Container(
        color: Colors.transparent,
        padding: EdgeInsets.only(top: 10, bottom: 10, left: 20, right: 20),
        margin: EdgeInsets.only(top: 40),
        child: Text.rich(
          TextSpan(
            text: "$title",
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 36,
              fontFamily: 'Georgia',
              color: Colors.green[800],
            ),
            children: <TextSpan>[
              TextSpan(
                text: '\n$subTitle', 
                style: TextStyle(
                  fontWeight: FontWeight.normal,
                  fontSize: 10,
                  color: Colors.green[600],
                ),
              ),
            ]
          ),
        ),
      )
    );
  }
}
