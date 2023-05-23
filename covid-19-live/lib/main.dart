import 'package:flutter/material.dart';

// pages
import 'global_page.dart';
import 'country_page.dart';
import 'info_page.dart';
import 'animations/title_icon.dart';


void main() {
	runApp(
  	MaterialApp(
      title: "Pandemic Live",
      home: HomePage(),
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
  	),
  );
}


class HomePage extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: DefaultTabController(
        length: 3,
        child: Scaffold(
          appBar: PreferredSize(
            preferredSize: Size.fromHeight(70.0), // here the desired height
            child: AppBar(
              centerTitle: true, // centers the title of app bar
              backgroundColor: Colors.green[800], // app bar background
              title: Row(
                children: <Widget>[
                  Text.rich(
                    TextSpan(
                      text: 'Pandemic Live',
                      style: TextStyle(
                        fontSize: 32, 
                        //fontWeight: FontWeight.bold,
                        color: Colors.grey[100],
                        shadows: [
                          Shadow(
                              blurRadius: 2.0,
                              color: Colors.grey[800],
                              offset: Offset(1.5, 1.5),
                          ),
                        ],
                      ),
                    ),
                  ),
                  //AnimatedRainDrop(size: 35, color: Colors.blue),
                  TitleBarIconTransition(),
                ],
              ),
            ),
          ),
          body: SafeArea(
            child: TabBarView(
              children: [
                GlobalPage(),
                CountryPage(),
                InfoPage(),
              ],
            ),
          ),

          bottomNavigationBar: Container(
            color: Colors.white,
            child: TabBar(
              indicatorColor: Colors.white, // selected tab bottom border
              labelColor: Colors.green[900], // selected lable color
              unselectedLabelColor: Colors.grey,  // unselected lable color
              tabs: [
                Tab(
                  icon: Icon(Icons.public, size: 28),
                  //text: 'Global',
                ),
                Tab(
                  icon: Icon(Icons.flag, size: 28),
                  //text: 'Country',
                ),
                Tab(
                  icon: Icon(Icons.info, size: 28),
                  //text: 'info',
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
