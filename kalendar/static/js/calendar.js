function Calendar(day,month,year,d){

d = parseInt(day)

if (day == '08' ){
	d = 8}
if (day == '09'){
	d= 9
}

m = parseInt(month)
y = parseInt(year)




$.get( "http://oldbeliverscalendar.pythonanywhere.com/kalendar/",{uday : d, umonth: m,uyear: y,udate:d}, function( data ) {

obj = document.getElementById("VICalendar");

	if (obj!=null){

		obj.innerHTML  = data;
	}

	if (obj== null){

	document.body.innerHTML += '<div id ="VICalendar">'+data+'</div>';
	}

$( "#datepicker" ).datepicker({ dateFormat: 'yy/mm/dd' });


});


}



function copy_clip(meintext)
{
 if (window.clipboardData)
   {
   //  IE
   window.clipboardData.setData("Text", meintext);
   }
   else if (window.netscape)
   {
 try {
 if (netscape.security.PrivilegeManager.enablePrivilege)
    netscape.security.PrivilegeManager.enablePrivilege('UniversalXPConnect');
    // netscape.security.PrivilegeManager.enablePrivilege('UniversalBrowserRead');
    // netscape.security.PrivilegeManager.enablePrivilege("UniversalBrowserWrite")
 } catch (e) { return;}

    var clip = Components.classes['@mozilla.org/widget/clipboard;1']
                  .createInstance(Components.interfaces.nsIClipboard);
    //alert(clip);
    if (!clip) return;

    var trans = Components.classes['@mozilla.org/widget/transferable;1']
                   .createInstance(Components.interfaces.nsITransferable);
    if (!trans) return;

    trans.addDataFlavor('text/unicode');

    var str = new Object();
    var len = new Object();

    var str = Components.classes["@mozilla.org/supports-string;1"]
                 .createInstance(Components.interfaces.nsISupportsString);

    var copytext=meintext;

    str.data=copytext;

    trans.setTransferData("text/unicode",str,copytext.length*2);

    var clipid=Components.interfaces.nsIClipboard;

    if (!clip) return false;

    clip.setData(trans,null,clipid.kGlobalClipboard);

   }

   return false;
}

$(document).ready(function(){

	var d = new Date(); Calendar(d.getDate(), d.getMonth() + 1,d.getFullYear(),d);
});


