let time = null 
let X = []
let T = []
let initX, i=0
let stop = true
function down(e){
    stop = false
    initX = e.screenX
    i = 0
}

function over(e){
    if(stop) return
    throttle(function(){    
        i+=20
        X.push(e.screenX)
        T.push(i) 
    }, 20)()
}
function up(){
    stop=true
    console.log(X)
    console.log(T)
}

function throttle(fn, wait) {
    var previous = 0
    var timer = null
    return function () {
        var context = this
        var args = arguments
        if (!previous) {
            previous = Date.now()
            fn.apply(context, args)
        } else if (previous + wait >= Date.now()) {
            if (timer) {
                // console.log(timer)
                clearTimeout(timer)
                timer = null
            }
            // console.log(timer)
            timer = setTimeout(function () {
                // console.log(timer)
                previous = Date.now()
                fn.apply(context, args)
            }, wait)
        } else {
            previous = Date.now()
            fn.apply(context, args)
        }
    }
}
