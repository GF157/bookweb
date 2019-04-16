var bigBox = document.getElementById("bigBox");//获取bigBox节点对象
var lis = document.querySelectorAll(".controls li");//获取所有的li节点对象
var viewHeight = document.body.clientHeight;//获取当前页面高度
var flag = true;//设置开关
var index = 0;//设置索引

//封装事件,兼容浏览器
function on(obj,eventType,fn){
    if(obj.addEventListener){
        obj.addEventListener(eventType, fn);
    }else{
        obj.attachEvent("on" + eventType, fn);
    }
}
//鼠标滚动事件处理函数
function handler(e){
    var _e = window.event || e;
    if(flag){
        flag = false;
        if(_e.wheelDelta==120 || _e.detail==-3){//如果鼠标滚轮向上滚动，detail为火狐判断条件
            index--;
            if(index<0){
                index = 0;
            }
        }else{//向下滚动
            index++;
            if(index>lis.length-1){//如果索引大于页面数，就是滚到最后一张页面时，再滚动鼠标页面不再滚动
                index = lis.length-1;
            }
        }
        bigBox.style.top = -index*viewHeight + "px";//bigBox整体上移index个页面
        for(var i=0; i<lis.length; i++){
            lis[i].className = "";//重置全部li的类
        }
        lis[index].className = "active";//设置当前li的类名
        setTimeout(function(){//页面滚动间隔一秒，防止滚动太快
            flag = true;//重新开启开关
        },1000);
    }
}
on(document,"mousewheel",handler);//滚轮滚动事件
on(document,"DOMMouseScroll",handler);//滚轮滚动事件，适配火狐浏览器
//数字标签点击处理
for(var i=0; i<lis.length; i++){
    lis[i].tag = i;
    lis[i].onclick = function(){
        for(var j=0; j<lis.length; j++){
            lis[j].className = "";
        }
        lis[this.tag].className = "active";
        bigBox.style.top = -this.tag*viewHeight + "px";
    }
}

//jQuery is required to run this code
$( document ).ready(function() {

    scaleAnimationContainer();

    initBannerAnimationSize('.animation-container .animation img');
    initBannerAnimationSize('.animation-container .mask');
    initBannerAnimationSize('.animation-container video');

    $(window).on('resize', function() {
        scaleAnimationContainer();
        scaleBannerAnimationSize('.animation-container .animation img');
        scaleBannerAnimationSize('.animation-container .mask');
        scaleBannerAnimationSize('.animation-container video');
    });

});

function scaleAnimationContainer() {

    var height = $(window).height() + 5;
    var unitHeight = parseInt(height) + 'px';
    $('.homepage-banner').css('height',unitHeight);

}

function initBannerAnimationSize(element){

    $(element).each(function(){
        $(this).data('height', $(this).height());
        $(this).data('width', $(this).width());
    });

    scaleBannerAnimationSize(element);

}

function scaleBannerAnimationSize(element){

    var windowWidth = $(window).width(),
    windowHeight = $(window).height() + 5,
    animationWidth,
    animationHeight;

    console.log(windowHeight);

    $(element).each(function(){
        var animationAspectRatio = $(this).data('height')/$(this).data('width');

        $(this).width(windowWidth);

        if(windowWidth < 1000){
            animationHeight = windowHeight;
            animationWidth = animationHeight / animationAspectRatio;
            $(this).css({'margin-top' : 0, 'margin-left' : -(animationWidth - windowWidth) / 2 + 'px'});

            $(this).width(animationWidth).height(animationHeight);
        }

        $('.homepage-banner .animation-container video').addClass('fadeIn animated');

    });
}