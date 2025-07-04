var selectedRow = null;
function onFormSubmit() {
var formData = readFormData();
if(isValid()){
    if (selectedRow == null) {
    insertNewRecord(formData);
    alert("Your details are saved Sucessfully........");
  }
 else{
  updateRecord(formData);
 }
  resetForm();
}
}

function readFormData() {
  var formData = {};
  formData["stuName"] = document.getElementById("stuName").value;
  formData["stuCourse"] = document.getElementById("stuCourse").value;
  formData["clgName"] = document.getElementById("clgName").value;
  return formData;
}

function resetForm() {
  document.getElementById("stuName").value = "";
  document.getElementById("stuCourse").value = "";
  document.getElementById("clgName").value = ""
  selectedRow = null;
}

function insertNewRecord(data) {
  var table = document
    .getElementById("stulist")
    .getElementsByTagName("tbody")[0];
  var newRow = table.insertRow(table.length);
  cell1 = newRow.insertCell(0);
  cell1.innerHTML = data.stuName;
  cell2 = newRow.insertCell(1);
  cell2.innerHTML = data.stuCourse;
  cell3 = newRow.insertCell(2);
  cell3.innerHTML = data.clgName;
  cell6 = newRow.insertCell(3);
  cell6.innerHTML = `<button><a onClick="onEdit(this)">Update</a></button><button><a onClick="onDelete(this)">Delete</a></button>`;
  console.log("Record Inserted Successfully!");
}
function onEdit(td)
{if(confirm("Are you sure to update your details")){
selectedRow=td.parentElement.parentElement;  
document.getElementById("stuName").value=selectedRow.cells[0].innerHTML;
document.getElementById("stuCourse").value=selectedRow.cells[1].innerHTML;
document.getElementById("clgName").value=selectedRow.cells[2].innerHTML;
}
}
function updateRecord(formData)
{
  alert("Your form updated sucessfully.......")
selectedRow.cells[0].innerHTML=formData.stuName;
selectedRow.cells[1].innerHTML=formData.stuCourse;
selectedRow.cells[2].innerHTML=formData.clgName;
}
function onDelete(td)
{
if(confirm("are you want to delete this record")){
  row=td.parentElement.parentElement;
  document.getElementById("stulist").deleteRow(row.rowIndex);
  resetForm();
}
}

function isValid(){
var a=document.getElementById("stuName").value;
// var  b = document.getElementById("facDep").value;
// var c= document.getElementById("facSub").value;
// var d= document.getElementById("facAge").value;
//  var e= document.getElementById("facPlace").value;
if(a==""|| a==null ){return false;}
else
{return true;}

}