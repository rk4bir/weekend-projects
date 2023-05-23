// dependencies
import 'package:http/http.dart' as http;

// default
import 'package:flutter/material.dart';
import 'dart:async';
import 'dart:convert';


/*===================Country name from IP===========================*/

Future<List> fetchCountryName() async {
    // returns iso2 code and country name as a list
    
    // NB: this code will be updated in some future version
    // hints: no point to return obj[0]['name'] instead it could be [name, iso2]
    final response = await http.get('https://ipapi.co/json/');

    if (response.statusCode == 200) {
        return [
            {
                'name': json.decode(response.body)['country_name'],
                'iso2': json.decode(response.body)['country_code']
            }
        ];
    } else {
        throw Exception("Couldn't connect to API");
    }
}


/*===================== country data in brief from mathdroid api ==============================*/

Future<CovidData> fetchCovidData(String country) async {
    // takes country as argument and fetch data from mathdroid api
    // returns a CovidData object
    final response = await http.get('https://covid19.mathdro.id/api/countries/$country');
    
    if (response.statusCode == 200) {
        return CovidData.fromJson(json.decode(response.body));
    } else {
        throw Exception("Couldn't connect to API");
    }
}


class CovidData {
    // converts country total summary from json to this CovidData type object as 
    // future 
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


/*========================= Country summary data from covid19api =======================*/

Future<List> fetchCovidCountryDailyAffectedData(String country) async {
    /*
    * takes country as argument which is required
    * fetches country's confirmed cases list (day wise)
    * returns a list of the data summary e.g. [{...}, {...}...]
    */
    final response = await http.get('https://api.covid19api.com/total/dayone/country/$country/status/confirmed');

    if (response.statusCode == 200) {
        return json.decode(response.body);
    } else {
        throw Exception("Couldn't connect to API");
    }
}


Future<List> fetchCovidCountryDailyDeathsData(String country) async {
    /*
    * takes country as argument which is required
    * fetches country's deaths data list (day wise)
    * returns a list of the data summary e.g. [{...}, {...}...]
    */
    final response = await http.get('https://api.covid19api.com/total/dayone/country/$country/status/deaths');

    if (response.statusCode == 200) {
        return json.decode(response.body);
    } else {
        throw Exception("Couldn't connect to API");
    }
}


Future<List> fetchCovidCountryDailyRecoveredData(String country) async {
    /*
    * takes country as argument which is required
    * fetches country's recovered data list (day wise)
    * returns a list of the data summary e.g. [{...}, {...}...]
    */
    final response = await http.get('https://api.covid19api.com/total/dayone/country/$country/status/recovered');

    if (response.statusCode == 200) {
        return json.decode(response.body);
    } else {
        throw Exception("Couldn't connect to API");
    }
}


Future<List> fetchCovidCountryDailyAllData(String country) async {
    /*
    * takes country as argument which is required
    * fetches country's all (deaths, affected, recovered) list (day wise)
    * returns a list of the data summary e.g. [{...}, {...}...]
    */
    final response = await http.get('https://api.covid19api.com/total/dayone/country/$country');

    if (response.statusCode == 200) {
        return json.decode(response.body);
    } else {
        throw Exception("Couldn't connect to API");
    }
}


Future<List<Country>> fetchAPICountryList() async {
    /*
    * fetch countries list from covid19api.com
    * returns a list of Country object e.g. [countryObject1, countryObject2, ...] 
    */
    final response = await http.get("https://api.covid19api.com/countries");

    if (response.statusCode == 200) {
        final parsed = json.decode(response.body).cast<Map<String, dynamic>>();
        return parsed.map<Country>((json) => Country.fromJson(json)).toList();
    } else {
        throw Exception("Couldn't connect to API");
    }
}


class Country {
    /* 
    * converts country data to a Country type object with 
    * name, slug, iso2 as properties
    * 
    * NB: iso2 is important because all country name can't make a success api
    *     response because some of them contains <space> and other characters.
    *     so, iso2 is handy to deal with the problem.
    *     
    *     Also, this app uses two APIs and they both use iso2 to be able to 
    *     fetch country data easily.
    */
    final String name;
    final String slug;
    final String iso2;

    Country({this.name, this.slug, this.iso2});

    factory Country.fromJson(Map<String, dynamic> json) {
        return Country(
            name: json['Country'],
            slug: json['Slug'],
            iso2: json['ISO2'],
        );
    }
}
