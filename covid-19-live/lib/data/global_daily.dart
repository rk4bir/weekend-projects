// dependencies
import 'package:http/http.dart' as http;

// default
import 'package:flutter/material.dart';
import 'dart:async';
import 'dart:convert';


Future<List> fetchCovidDataDaily() async {
	/*
    * fetch world's daily data from mathdroi API and 
    * returs a list of data (day wise)
    */
    final response = await http.get('https://covid19.mathdro.id/api/daily');
    if (response.statusCode == 200) {
        return json.decode(response.body);
    } else {
        throw Exception("Couldn't connect to API");
    }
}
