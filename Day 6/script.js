var departmentobject={
  'B.tech' : ['CSE','Mech','Civil','CSE-AI & DS','EEE','ECE'],
  'Degree' : ['B.A','B.Com','B.Sc']
}

window.onload = function(){
  var departmentselect = document.getElementById('department');
  var subjectselect = document.getElementById('subject');
  for (var x in departmentobject){
    departmentselect.options[departmentselect.options.length] = new Option(x);
  }
  departmentselect.onchange = function(){
    subjectselect.length = 1;
    var subject = departmentobject[this.value];
    for (var i=0;i<subject.length;i++){
      subjectselect.options[subjectselect.options.length] = new Option(subject[i]);
    }
  }
}

var selectedRow = null;
function onFormSubmit() {
var formData = readFormData();
if(isValid()){
    if (selectedRow == null) {
    insertNewRecord(formData);
    alert("Your details are saved Sucessfully........");
    console.log(insertNewRecord(formData));
  }
 else{
  updateRecord(formData);
 }
  resetForm();
}
}

function readFormData() {
  var formData = {};
  formData["facName"] = document.getElementById("facName").value;
  formData["department"] = document.getElementById("department").value;
  formData["subject"] = document.getElementById("subject").value;
  formData["facAge"] = document.getElementById("facAge").value;
  formData["facPlace"] = document.getElementById("facPlace").value;
  return formData;
}
function resetForm() {
  document.getElementById("facName").value = "";
  document.getElementById("department").value = "";
  document.getElementById("subject").value = "";
  document.getElementById("facAge").value = "";
  document.getElementById("facPlace").value = "";
  selectedRow = null;
}
function insertNewRecord(data) {
  var table = document
    .getElementById("faclist")
    .getElementsByTagName("tbody")[0];
  var newRow = table.insertRow(table.length);
  cell1 = newRow.insertCell(0);
  cell1.innerHTML = data.facName;
  cell2 = newRow.insertCell(1);
  cell2.innerHTML = data.department;
  cell3 = newRow.insertCell(2);
  cell3.innerHTML = data.subject;
  cell4 = newRow.insertCell(3);
  cell4.innerHTML = data.facAge;
  cell5 = newRow.insertCell(4);
  cell5.innerHTML = data.facPlace;
  cell6 = newRow.insertCell(5);
  cell6.innerHTML = `<a onClick="onEdit(this)">Update</a><a onClick="onDelete(this)">Delete</a>`;
}
function onEdit(td)
{if(confirm("Are you upadate your details")){
selectedRow=td.parentElement.parentElement;  
document.getElementById("facName").value=selectedRow.cells[0].innerHTML;
document.getElementById("department").value=selectedRow.cells[1].innerHTML;
document.getElementById("subject").value=selectedRow.cells[2].innerHTML;
document.getElementById("facAge").value=selectedRow.cells[3].innerHTML;
document.getElementById("facPlace").value=selectedRow.cells[4].innerHTML;}
}
function updateRecord(formData)
{
  alert("Your form updated sucessfully.......")
selectedRow.cells[0].innerHTML=formData.facName;
selectedRow.cells[1].innerHTML=formData.department;
selectedRow.cells[2].innerHTML=formData.subject;
selectedRow.cells[3].innerHTML=formData.facAge;
selectedRow.cells[4].innerHTML=formData.facPlace;
}
function onDelete(td)
{
if(confirm("are you want to delete this record")){
  row=td.parentElement.parentElement;
  document.getElementById("faclist").deleteRow(row.rowIndex);
  resetForm();
}
}

function isValid(){
var a=document.getElementById("facName").value;
var  b = document.getElementById("department").value;
var c= document.getElementById("subject").value;
var d= document.getElementById("facAge").value;
 var e= document.getElementById("facPlace").value;
if(a==""|| a==null ){
  return false;
}else if(b==""|| b==null || isNaN(b)==false){
  alert("Please enter department name correctly!");
}else if(c==""|| c==null || isNaN(c)==false){
  alert("Please enter subject name correctly!");
}
else if(isNaN(d) || d<18 || d>65) {
  alert("Your age is not elgible");
}else if(e==""|| e==null || isNaN(e)==false){
   alert("Please enter your place name correctly!");
}
else
{return true;}

}