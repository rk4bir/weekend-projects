// dependencies
import 'package:http/http.dart' as http;

// default
import 'package:flutter/material.dart';
import 'dart:async';
import 'dart:convert';


Future<CovidData> fetchCovidData() async {
    /*
    * fetch world data from mathdroi API and 
    * returs a single CovidData object 
    */
    final response = await http.get('https://covid19.mathdro.id/api');
    if (response.statusCode == 200) 
        return CovidData.fromJson(json.decode(response.body));
    throw Exception("Couldn't connect to API");
}


class CovidData {
    /*
    * Converts json object to CovidData object creating 
    * confirmed, recovered, deaths, lastUpdate data as property of this
    * object. 
    */
    final int confirmed;
    final int recovered;
    final int deaths;
    final String lastUpdate;

    CovidData({this.confirmed, this.recovered, this.deaths, this.lastUpdate});

    factory CovidData.fromJson(Map<String, dynamic> json) {
        return CovidData(
            confirmed: json['confirmed']['value'],
            recovered: json['recovered']['value'],
            deaths: json['deaths']['value'],
            lastUpdate: json['lastUpdate'].toString()
        );
    }
}
