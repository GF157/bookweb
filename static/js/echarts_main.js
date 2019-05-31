
<script type="text/javascript">
    var dom = document.getElementById("p2_x1");
    var myChart = echarts.init(dom, 'walden');
    var app = {};
    option = null;
    app.title = '坐标轴刻度与标签对齐';

    option = {
        color: ['#3398DB'],
        title:{
            text:'热门出版社出版数目与平均评分人数',
            x: 'center'
        },
        tooltip : {
            trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
    {
        type : 'category',
        data : [
        {% for i in Press_top %}    
        '{{ i.tags }}',
        {% endfor %}],
        axisTick: {
            alignWithLabel: true
        }
    }
    ],
    yAxis : [
    {
        type : 'value'
    }
    ],
    series : [
    {
        name:'出版书籍数',
        type:'bar',
        barWidth: '60%',
        data:[
        {% for i in Press_top %}    
        {{ i.num_of_tag }},
        {% endfor %}
        ]
    },
    {
        name:'评分人数',
        type:'line',
        barWidth: '60%',
        data:[
        {% for i in Press_top %}    
        {{ i.number }},
        {% endfor %}
        ]
    },

    ]
};
;
if (option && typeof option === "object") {
    myChart.setOption(option, true);
}
</script>