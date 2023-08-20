// markdown =  document.getElementById("RoadMapMD").innerHTML;
// const data = markmap.transform(markdown);
//
// markmap.Markmap.create("#RoadMap", null, data);
//

var markmap_list = document.querySelectorAll(".mark-map")
for (let index = 0; index < markmap_list.length; index++) {
    var markdown = markmap_list[index].getElementsByTagName('pre')[0].innerHTML
    var data =  markmap.transform(markdown)
    var reference = markmap_list[index].getElementsByTagName('svg')[0].id
    markmap.Markmap.create('#'+reference, null, data)
}