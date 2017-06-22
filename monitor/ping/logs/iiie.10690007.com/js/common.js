$(function () {
$("[data-search-btn]").click(function() {
	var params={};
	$("[data-search-input]").each(function() {
		params[$(this).attr('name')] = $.trim($(this).val());
	});
	$("table[data-toggle='table']").bootstrapTable('refresh', {
		query : params
	});
});

$('.Wdate').click(function(){
	WdatePicker({el:this,isShowWeek:false,highLineWeekDay:false,firstDayOfWeek:1,dateFmt:'yyyy-MM-dd HH:mm:ss',doubleCalendar:false})
});

$("[data-dialog]").click(function(){
	var url=$(this).attr("data-dialog");
	var width=$(this).attr("data-dialog-width");
	if(width==undefined)
		width=600;
	var height=$(this).attr("data-dialog-height");
	if(height==undefined)
		height=400;
	var title=$(this).attr("data-dialog-title");
	var id=$(this).attr("data-dialog-id")
	if(id==undefined)
		id="dialog"
	
	dialog(true,url,id,width,height,title);
});
});
var tableSet={
	fn:{
		showTime:function(time,fmt){
			if(fmt==undefined)
				fmt='yyyy-MM-dd hh:mm:ss';
			if(time==undefined)
				return;
			var d=new Date(time);
		    var o = {
		        "M+": d.getMonth() + 1,
		        "d+": d.getDate(),
		        "h+": d.getHours(),
		        "m+": d.getMinutes(),
		        "s+": d.getSeconds(),
		        "q+": Math.floor((d.getMonth() + 3) / 3),
		        "S": d.getMilliseconds()
		    };
		    if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (d.getFullYear() + "").substr(4 - RegExp.$1.length));
		    for (var k in o)
		    	if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
		    		return fmt;
		},
		ratio:function(number){
			return Math.round(number*10000)/100+'%';
		}
	}
}