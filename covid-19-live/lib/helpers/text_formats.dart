String makeCommaSeperatedNumber(var number) {
	/*
	* Takes a number as argument
	* converts it to string and makes it comma seperated string e.g. 1000 => 1,000 
	* returns comma seperated number string
	*/
	return number.toStringAsFixed(0).replaceAllMapped(new RegExp(r'(\d{1,3})(?=(\d{3})+(?!\d))'), (Match m) => '${m[1]},');
}


String upperCase(var str) {
	// converts string to uppercase
	return str.toUpperCase();
}


String lowerCase(var str) {
	// converts string to lowercase
	return str.toLowerCase();
}


String lastUpdatedDateFormatter(String lastUpdatedDate) {
	/*
	* takes lastUpdatedDate as argument (from api): expected argument format is yyyy-mm-ddThh:mm:ss.msZ
	* returns formatted string e.g. yyyy-mm-dd hh:mm:ss GMT
	*/
    if (lastUpdatedDate != null) {
    	var dateTime = lastUpdatedDate.split('T');
		var date =  dateTime[0];
		var time = dateTime[1].split('.')[0];

		return "$date $time GMT";
    }
    return '';
}
