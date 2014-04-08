console.log("CURRY");

var add2 = funciton(a,b){ //standard multi para function
    return a=b;
}

// add2p(3)-> return function that takes b, then add 3 to it
//add2p(3,7) will not work. add2p(3)(7) -> 10
var add2p = function(a){ //'currying'? single para function
    return function(b){
	return a+b;
    }
}
/* example flexibility
   add5 = add2p(5) -> function that will take one parameter then add 5 to it
   add12 = add2p(12) -> " " " " " " " " 12 ""
   ^^ partial application
*/


var add3 = function(a,b,c){
    return a + b + c;
}

//var3P(3)(4)(5) -> 12
var add3p = function(a){
    return function(b){
	return function(c){
	    return a+b+c;
	}}}
/* could be useful to 'store' data. calculate one value, and save it in the function until the other parameters are calculated. 
*/

//lowdash(and other liibraries like it) has curry()
var add3c = _.curry(add3);
// _.curry supports all styles of paramenter 
// add3c(10)(20)(30) -> 60
// add3c(10,20,30) -> 60 
// add3c(10),add3c(20),add3c(30) -> 60 


var greetc = _.curry(function(a,b,c){
    return a+" "+b+" "+c;
});

var g2 = greetc("My Dear"); //g2("bond")-> 'My Dear Bond'
var g3 = greetc("Hey","Mrs");//g3('smith')-> 'Hey Mrs smith'
		  

//****************************************************************************
var curryMap = _.curry(cull.map);
var curryFil = _.curry(cull.filter);

var sqlist = curryMap(square);
var oddList = curryFil(odd);
var sqodd = _.compose(sqlist,oddList);