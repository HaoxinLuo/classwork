/*
[x*x for x in [1,2,3,4,5]] -> [1,4,9,16,25]
this takes everything in the given list and runs the function on each element
hence this resembles map()

[x for x in [1,2,3,4,5,6] if x %2=< 0] -> [2,4,6] 
this only does the above if the element is even
this is called filter

*/

var square = function(x){ return x*x;}
var even = function(x){return x%2==0;}

//write map(). take a list and apply a given function to each element
//e.g. map([1,2,3,4],square); -> [1,4,9,16]
var map=function(l,f){
    var ans = []
    for (var i = 0;i<l.length;i++){
	ans.push(f(l[i]));
    }
    return ans;
}

//write filter(). apply filter to a list. 
//e.g. filter([1,2,3,4],even); -> [2,4]
var filter=function(l,f){
    var ans = [];
    for (var i = 0;i<l.length;i++){
	if (f(l[i])){
	    ans.push(l[i]);
	}
    }
    return ans;
}

var l = [30,35,65,50,60,30,20];

var mountain=function(l){
    





}

var zip = function(a,b){
    var ans = [];
    var d = a.length;
    var c = b.length;
    for(var i = 0;i<min(d,c);i++){
	ans.push([a[i],b[i]]);	
    }
    return ans;
}