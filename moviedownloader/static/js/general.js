
$(document).ready(function(){	

	//Initiates Search of Movie
	$("#searchButton").click(function(){
		var query = $("#searchQuery").val();
		var siteText = $("#siteOptions").text();
		
		//Checks if all conditions have been met for searching
		if(siteText.replace(/[^A-Z0-9]/ig, "") === "SelectSitetoSearch" && query === ""){
			$("#siteOptions").css('border-color', 'red');
			$("#searchQuery").css('border-color', 'red');
			$("#textboxAlert").show();
			$("#dropdownAlert").show();
		}else if(siteText.replace(/[^A-Z0-9]/ig, "") === "SelectSitetoSearch"){
			$("#siteOptions").css('border-color', 'red');
			$("#dropdownAlert").show();
		}else if (query === ""){
			$("#searchQuery").css('border-color', 'red');
			$("#textboxAlert").show();
		}else{
			window.location.href = "../search" + siteText + "/" + query + "/1";
		}
	});	
	
	//Replaces the current site  with the selected one from the dropdown
	$(".dropdown-menu li a").click(function(){
		var selText = $(this).text();
		$("#siteOptions").html(selText + '<span class="caret"></span>');
		
		//Disables Warning Message
		$('#siteOptions').css('border-color', '');
		$("#dropdownAlert").hide();
	});
	
	//Disables Warning Message
	$('#searchQuery').on('input',function(e){	
		$('#searchQuery').css('border-color', '');
		$("#textboxAlert").hide();
    });
	
	//Handles both "Previous" and "Next" Button of the Pagination
	$(".paginationButtons").click(function(){
		var path = window.location.pathname;
		var page = path.substr(path.length - 2);
		var keyWord = $(this).getAttribute("aria-label");
		
		if(keyWord == "next"){
			page = parseInt(page.substr(0,1)) + 1;
			window.location.href = "../" + page.toString();
		}else if (page != 1){
			page = parseInt(page.substr(0,1)) - 1;
			window.location.href = "../" + page.toString();
		}
	});

});