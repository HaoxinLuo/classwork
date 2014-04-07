console.log("Hello Min");

var mtnrange = [20,30,55,80,30,42,20,80,45,60];

var difflists = _.map(mtnrange,function(item,i,list){
    return [].concat(list[i],list[i+1]);
});

var diffs = _.map(difflists,function(x){
    return Math.abs(x[1]-x[2]);
});

var bigmtns = _.filter(diffs,function(x){
    return x>30;
});

//****************************************************************************

//using cull.js
//map(fn,list) not map(list,fn)

var zipc = _.curry(function(a,b){return  _.zip(a,b);});
var takec= _.curry(function(a){return _.take(a,a.length-1);}); // a.length-1?
