/* 
  Acronyms

  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 

  Do it with .split first if you need to, then try to do it without
*/

const str1 = "object oriented programming";
const expected1 = "OOP";

function acronymize(str){
  var arr = str.split(" ")
  var result = ""
  // console.log(arr);
  // console.log(arr);
  for(var i=0;i<arr.length;i++){
    // console.log(arr[i][0].toUpperCase());
    result += arr[i][0].toUpperCase()
  }
  return result
}
console.log(acronymize(str1))



// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expected2 = "APIE";

function acronymize(str){
  var arr = str.split(" ")
  var result = ""
  for(var i=0;i<arr.length;i++){
    result += arr[i][0].toUpperCase()
  }
  return result
}
console.log(acronymize(str2))




const str3 = "software development life cycle";
const expected3 = "SDLC";

function acronymize(str){
  var arr = str.split(" ")
  var result = ""
  for(var i=0;i<arr.length;i++){
    result += arr[i][0].toUpperCase()
  }
  return result
}
console.log(acronymize(str3))




// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expected4 = "GIT";

// Bonus
function acronymize(str) {
  var arr = str.split(" ")
  var result = ""
  console.log(arr);
   for(var i=0;i< arr.length;i++){
     if(arr[i] != "") {
      result += arr[i][0].toUpperCase()
     }
   }
   return result
 }
 console.log(acronymize(str4));
