import 'package:flutter/material.dart';
import 'widgets/page_title.dart';


class InfoPage extends StatefulWidget {
  @override
  _InfoPageState createState() => _InfoPageState();
}


class _InfoPageState extends State<InfoPage> {

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.indigo[50],
      ),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        body: Container(
          padding: EdgeInsets.only(left: 30, right: 30),
          child: ListView(
            children: <Widget>[
              SizedBox(height: 100),
              Text.rich(
                TextSpan(
                  text: 'Pandemic Live',
                  style: TextStyle(
                    fontSize: 30, 
                    fontWeight: FontWeight.normal,
                    color: Colors.green,
                    shadows: [
                      Shadow(
                          blurRadius: 2.0,
                          color: Colors.blue,
                          offset: Offset(1.5, 1.5),
                      ),
                    ],
                  ),
                ),
              ),

              SizedBox(height: 5),
              Text.rich(
                TextSpan(
                  text: 'Version: v1.0.1',
                  style: TextStyle(
                    fontSize: 16, 
                    color: Colors.black,
                    shadows: [
                      Shadow(
                          blurRadius: 1.0,
                          color: Colors.blue,
                          offset: Offset(0.5, 0.5),
                      ),
                    ],
                  ),
                ),
              ),

              SizedBox(height: 5),
              Text.rich(
                TextSpan(
                  text: 'Author: Raihan Kabir',
                  style: TextStyle(
                    fontSize: 16, 
                    color: Colors.black,
                    shadows: [
                      Shadow(
                          blurRadius: 1.0,
                          color: Colors.blue,
                          offset: Offset(0.5, 0.5),
                      ),
                    ],
                  ),
                ),
              ),

              SizedBox(height: 5),
              Text.rich(
                TextSpan(
                  text: 'Email: r.kabir01@pm.me',
                  style: TextStyle(
                    fontSize: 16, 
                    color: Colors.black,
                    shadows: [
                      Shadow(
                          blurRadius: 1.0,
                          color: Colors.blue,
                          offset: Offset(0.5, 0.5),
                      ),
                    ],
                  ),
                ),
              ),

              SizedBox(height: 5),
              Text.rich(
                TextSpan(
                  text: "\nIt's a free app, aimed to provide current pandemic update. " + 
                        "It shows global and country pandemic update along with analytical chart/graph and " + 
                        "data table in real time. This app fetch JSON data from John Hopkins University CSSE via API.",
                  style: TextStyle(
                    fontSize: 14, 
                    color: Colors.black,
                    shadows: [
                      Shadow(
                          blurRadius: 1.0,
                          color: Colors.blue,
                          offset: Offset(0.5, 0.5),
                      ),
                    ],
                  ),
                ),
              ),

              SizedBox(height: 200),
              Text.rich(
                TextSpan(
                  text: 'NB: ',
                  style: TextStyle(
                    fontSize: 14, 
                    fontWeight: FontWeight.bold,
                    color: Colors.black,
                    shadows: [
                      Shadow(
                          blurRadius: 1.0,
                          color: Colors.blue,
                          offset: Offset(0.5, 0.5),
                      ),
                    ],
                  ),
                  children: <TextSpan>[
                    TextSpan(
                      text: "If you face any problem with the app, please report to the author's e-mail.",
                      style: TextStyle(
                        fontWeight: FontWeight.normal,
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

