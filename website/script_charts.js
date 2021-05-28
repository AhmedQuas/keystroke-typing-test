function hand_pie(right_hand, left_hand){
    let myChart1 = document.getElementById('myChart1').getContext('2d');

     let HandPieChart = new Chart(myChart1, {
   type:'pie',
   data:{
     labels:[
     'Praworęczni',
     'Leworęczni'
     ],

     datasets:[{
       label:'Hands',
       data:[
           right_hand,
           left_hand
       ],
       backgroundColor:[
         'rgba(255, 99, 132, 0.6)',
         'rgba(54, 162, 235, 0.6)',
       
       ],
       borderWidth:1,
       borderColor:'#777',
       hoverBorderWidth:3,
       hoverBorderColor:'#000'
     }]
   },
   options:{
     responsive: true,
     title:{
       display:true,
       text:'Preferencje wykorzystywania rąk przez użytkowników',
       fontSize:25
     },
     legend:{
       display:true,
       position:'right',
       labels:{
         fontColor:'#000'
       }
     },
     layout:{
       padding:{
         left:50,
         right:0,
         bottom:0,
         top:0
       }
     },
     tooltips:{
       enabled:true
     }
   }
 });
}
function sex_pie(men, women){
  let myChart2 = document.getElementById('myChart2').getContext('2d');

   let SexChart = new Chart(myChart2, {
 type:'pie',
 data:{
   labels:[
   'Mężczyźni',
   'Kobiety'
   ],

   datasets:[{
     label:'Płeć',
     data:[
         men,
         women
     ],
     backgroundColor:[
       'rgba(255, 255, 132, 0.6)',
       'rgba(54, 255, 235, 0.6)',
     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
   title:{
     display:true,
     text:'Płeć wśród użytkowników',
     fontSize:25
   },
   legend:{
     display:true,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function native_pie(men, women){
  let myChart3 = document.getElementById('myChart3').getContext('2d');

   let NativeChart = new Chart(myChart3, {
 type:'pie',
 data:{
   labels:[
   'Polski',
   'Inne'
   ],

   datasets:[{
     label:'Język ojczysty',
     data:[
         men,
         women
     ],
     backgroundColor:[
      'rgba(153, 102, 255, 0.6)',
      'rgba(55, 159, 64, 0.6)'
     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
   title:{
     display:true,
     text:'Język ojczysty wśród uczestników',
     fontSize:25
   },
   legend:{
     display:true,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function education_pie(primary, high, student, graduate, undergraduate){
  let myChart4 = document.getElementById('myChart4').getContext('2d');
   let NativeChart = new Chart(myChart4, {
 type:'pie', //doughnut
 data:{
   labels:[
   'Uczeń szkoły podstawowej',
   'Uczeń szkoły ponadpodstawowej',
   'Student',
   'Absolwent uczelni wyższej',
   'Nie ukończył studiów'
   ],

   datasets:[{
     label:'Wykształcenie',
     data:[
        primary, 
        high, 
        student, 
        graduate, 
        undergraduate
     ],
     backgroundColor:[
      'rgba(255, 209, 12, 0.6)',
      'rgba(3, 12, 215, 0.6)',
      'rgba(255, 99, 132, 0.6)',
      'rgba(54, 162, 35, 0.6)',
      'rgba(151, 412, 192, 0.6)'

     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
   title:{
     display:true,
     text:'Wykształcenie wśród uczestników',
     fontSize:25
   },
   legend:{
     display:true,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function employment_pie(unemployed, withcomputer, withoutcomputer){
  let myChart5 = document.getElementById('myChart5').getContext('2d');
   let NativeChart = new Chart(myChart5, {
 type:'pie', //doughnut
 data:{
   labels:[
   'Nie pracuje',
   'Pracuje i korzysta z kompuera w pracy',
   'Pracuje i nie korzysta z komputera w pracy'
   ],

   datasets:[{
     label:'Zatrudnienie',
     data:[
      unemployed, 
      withcomputer, 
      withoutcomputer
     ],
     backgroundColor:[
      'rgba(125, 209, 112, 0.6)',
      'rgba(354, 162, 35, 0.6)',
      'rgba(151, 52, 192, 0.6)'

     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
   title:{
     display:true,
     text:'Zatrudnienie wśród uczestników',
     fontSize:25
   },
   legend:{
     display:true,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function science_lovers_pie(yes, no){
  let myChart6 = document.getElementById('myChart6').getContext('2d');
   let NativeChart = new Chart(myChart6, {
 type:'pie', //doughnut
 data:{
   labels:[
   'Woli przedmioty ścisłe',
   'Woli przedmioty humanistyczne'
   ],

   datasets:[{
     label:'Ukierunkowanie',
     data:[
      yes,
      no
     ],
     backgroundColor:[
      'rgba(255, 99, 132, 0.6)',
      'rgba(54, 162, 235, 0.6)',
      'rgba(255, 206, 86, 0.6)'
     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
   title:{
     display:true,
     text:'Ukierunkowanie wśród uczestników',
     fontSize:25
   },
   legend:{
     display:true,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function age_chart(label, amount){
  let myChart7 = document.getElementById('myChart7').getContext('2d');
   let AgeChart = new Chart(myChart7, {
 type:'bar', //doughnut
 data:{
   labels:
  label
   ,

   datasets:[{
     label: 'Wiek',
     data:
     amount
     ,
     backgroundColor:[
      'rgba(25, 99, 232, 0.6)',
      'rgba(154, 62, 235, 0.6)',
      'rgba(255, 206, 86, 0.6)'
     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true,
                 },
        scaleLabel: {
              display: true,
              labelString: 'Ilość uczestników'
            }
        },],
        xAxes: [{scaleLabel: {
          display: true,
          labelString: 'Wiek'
        }}]
    
},
   title:{
     display:true,
     text:'Wiek wśród uczestników',
     fontSize:25
   },
   legend:{
     display:false,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function rollover_chart(rollover, norollover){
  let myChart8 = document.getElementById('myChart8').getContext('2d');
   let RolloverChart = new Chart(myChart8, {
 type:'pie', //doughnut
 data:{
   labels:[
   'Występuje rollover',
   'Nie występuje rollover'
   ],

   datasets:[{
     label:'Rollover',
     data:[
      rollover,
      norollover
     ],
     backgroundColor:[
      'rgba(255, 99, 132, 0.6)',
      'rgba(54, 162, 235, 0.6)',
      'rgba(255, 206, 86, 0.6)'
     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
   title:{
     display:true,
     text:'Występowanie rollover`u',
     fontSize:25
   },
   legend:{
     display:true,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function asit_chart(label, amount){
  let myChart9 = document.getElementById('myChart9').getContext('2d');
   let AsitChart = new Chart(myChart9, {
 type:'bar', //doughnut
 data:{
   labels:
  label
   ,

   datasets:[{
     label: 'Średni czas znaku',
     data:
     amount
     ,
     backgroundColor:[
      'rgba(254, 33, 33, 0.6)',
      'rgba(219, 221, 33, 0.6)',
      'rgba(44, 210, 27, 0.6)'
     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
  scales: {
      yAxes: [{
          
          ticks: {
            beginAtZero: true
          },
      scaleLabel: {
            display: true,
            labelString: 'Ilość uczestników'
          }
      },],
      xAxes: [{scaleLabel: {
        display: true,
        labelString: 'Średni czas znaku [ms]'
      }}]
  
},
   title:{
     display:true,
     text:'Średni czas znaku (ASIT)',
     fontSize:25
   },
   legend:{
     display:false,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function ec_chart(label, amount){
  let myChart10 = document.getElementById('myChart10').getContext('2d');
   let EcChart = new Chart(myChart10, {
 type:'bar', //doughnut
 data:{
   labels:
  label
   ,

   datasets:[{
     label: 'Ilość poprawionych błędów',
     data:
     amount
     ,
     backgroundColor:[
      'rgba(27, 221, 190, 0.6)',
      'rgba(221, 114, 27, 0.6)',
      'rgba(67, 30, 126, 0.6)'
     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
  scales: {
      yAxes: [{
          ticks: {
              beginAtZero: true,
              
          },
      scaleLabel: {
            display: true,
            labelString: 'Ilość uczestników'
          }
      },],
      xAxes: [{scaleLabel: {
        display: true,
        labelString: 'Poprawione błędy'
      }}]
    
},
   title:{
     display:true,
     text:'Poprawione błędy (EC)',
     fontSize:25
   },
   legend:{
     display:false,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function enc_chart(label, amount){
  let myChart11 = document.getElementById('myChart11').getContext('2d');
   let EncChart = new Chart(myChart11, {
 type:'bar', //doughnut
 data:{
   labels:
  label
   ,

   datasets:[{
     label: 'Ilość niepoprawionych błędów',
     data:
     amount
     ,
     backgroundColor:[
      'rgba(47, 156, 55, 0.6)',
      'rgba(234, 245, 45, 0.6)',
      'rgba(178, 33, 86, 0.6)'
     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
  scales: {
      yAxes: [{
          ticks: {
              beginAtZero: true,
              
          },
      scaleLabel: {
            display: true,
            labelString: 'Ilość uczestników'
          }
      },],
      xAxes: [{scaleLabel: {
        display: true,
        labelString: 'Niepoprawione błędy'
      }}]
    
},
   title:{
     display:true,
     text:'Niepoprawione błędy (ENC)',
     fontSize:25
   },
   legend:{
     display:false,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function caps_usage_chart(caps, shift){
  let myChart12 = document.getElementById('myChart12').getContext('2d');
   let CapsChart = new Chart(myChart12, {
 type:'doughnut', //doughnut
 data:{
   labels:[
   'Caps Lock',
   'Shift'
   ],

   datasets:[{
     label:'Duże litery',
     data:[
      caps,
      shift
     ],
     backgroundColor:[
      'rgba(7, 163, 187, 0.6)',
      'rgba(224, 33, 235, 0.6)'     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
   title:{
     display:true,
     text:'W jaki sposób uczestnicy piszą wielkie litery?',
     fontSize:25
   },
   legend:{
     display:true,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function science_human_asit_chart(science, human){
  let myChart13 = document.getElementById('myChart13').getContext('2d');
   let CapsChart = new Chart(myChart13, {
 type:'bar', //doughnut
 data:{
   labels:[
   'Ścisłowcy',
   'Humaniści'
   ],

   datasets:[{
     label:'Średni czas znaku',
     data:[
      science,
      human
     ],
     backgroundColor:[
      'rgba(134, 28, 201, 0.6)',
      'rgba(234, 223, 17, 0.6)'     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 
 options:{
  scales: {
      yAxes: [{
          ticks: {
              beginAtZero: true,
              },
      scaleLabel: {
            display: true,
            labelString: 'Średni czas znaku [ms]'
          }
      },]
    
},
   title:{
     display:true,
     text:'Średni czas znaku (ASIT) a ukierunkowanie',
     fontSize:25
   },
   legend:{
     display:false,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function hand_asit_chart(right, left){
  let myChart14 = document.getElementById('myChart14').getContext('2d');
   let CapsChart = new Chart(myChart14, {
 type:'bar', //doughnut
 data:{
   labels:[
   'Praworęczni',
   'Leworęczni'
   ],

   datasets:[{
     label:'Średni czas znaku',
     data:[
      right,
      left
     ],
     backgroundColor:[
      'rgba(51, 233, 167, 0.6)',
      'rgba(231, 167, 89, 0.6)'     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
  scales: {
      yAxes: [{
          ticks: {
              beginAtZero: true,
              },
      scaleLabel: {
            display: true,
            labelString: 'Średni czas znaku [ms]'
          }
      },]
    
},
   title:{
     display:true,
     text:'Średni czas znaku (ASIT) a ręka wiodąca',
     fontSize:25
   },
   legend:{
     display:false,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function age_vs_enc_chart(label, amount){
  let myChart15 = document.getElementById('myChart15').getContext('2d');
   let AsitChart = new Chart(myChart15, {
 type:'bar', //doughnut
 data:{
   labels:
  label
   ,

   datasets:[{
     label: 'Ilość poprawionych błędów',
     data:
     amount
     ,
     backgroundColor:[
      'rgba(170, 255, 89, 0.6)',
      'rgba(89, 132, 255, 0.6)',
      'rgba(255, 89, 89, 0.6)'
     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
  scales: {
      yAxes: [{
          ticks: {
              beginAtZero: true
              
          },
      scaleLabel: {
            display: true,
            labelString: 'Ilość poprawionych błędów'
          }
      },],
      xAxes: [{scaleLabel: {
        display: true,
        labelString: 'Wiek'
      }}]
    
},
   title:{
     display:true,
     text:'Ilość poprawionych błędów (EC) a wiek',
     fontSize:25
   },
   legend:{
     display:false,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function age_vs_asit_chart(label, amount){
  let myChart16 = document.getElementById('myChart16').getContext('2d');
   let AsitChart = new Chart(myChart16, {
 type:'bar', //doughnut
 data:{
   labels:
  label
   ,

   datasets:[{
     label: 'Średni czas znaku',
     data:
     amount
     ,
     backgroundColor:[
      'rgba(77, 108, 67, 1)',
      'rgba(201, 230, 30, 0.6)',
      'rgba(2, 13, 155, 0.6)'
     
     ],
     fill: false,
     borderColor: 'rgb(75, 192, 192)',
     tension: 0.1,
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
  scales: {
      yAxes: [{
          ticks: {
              beginAtZero: false,
              
          },
      scaleLabel: {
            display: true,
            labelString: 'Średni czas znaku [ms]'
          }
      },],
      xAxes: [{scaleLabel: {
        display: true,
        labelString: 'Wiek'
      }}]
    
},
   title:{
     display:true,
     text:'Średni czas znaku (ASIT) a wiek',
     fontSize:25
   },
   legend:{
     display:false,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function lang_enc_chart(polish, notpolish){
  let myChart17 = document.getElementById('myChart17').getContext('2d');
   let CapsChart = new Chart(myChart17, {
 type:'bar', //doughnut
 data:{
   labels:[
   'Polski',
   'Inny'
   ],

   datasets:[{
     label:'Niepoprawione błędy',
     data:[
      polish,
      notpolish
     ],
     backgroundColor:[
      'rgba(118, 123, 116, 0.6)',
      'rgba(192, 140, 231, 0.6)'     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
  scales: {
      yAxes: [{
          ticks: {
              beginAtZero: true
          },
      scaleLabel: {
            display: true,
            labelString: 'Niepoprawione błędy'
          }
      },]
    
},
   title:{
     display:true,
     text:'Wpływ języka ojczystego na ilość niepoprawionych błędów (ENC)',
     fontSize:25
   },
   legend:{
     display:false,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function lang_ec_chart(polish, notpolish){
  let myChart18 = document.getElementById('myChart18').getContext('2d');
   let CapsChart = new Chart(myChart18, {
 type:'pie', //doughnut
 data:{
   labels:[
   'Polski',
   'Inny'
   ],

   datasets:[{
     label:'Poprawione błędy',
     data:[
      polish,
      notpolish
     ],
     backgroundColor:[
      'rgba(226, 150, 40, 0.6)',
      'rgba(40, 208, 226, 0.6)'     
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 
 options:{
   title:{
     display:true,
     text:'Wpływ języka ojczystego na ilość poprawionych błędów',
     fontSize:25
   },
   legend:{
     display:true,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function so_sa_sch_chart(so,sa,sch){
  let myChart19 = document.getElementById('myChart19').getContext('2d');
   let CapsChart = new Chart(myChart19, {
 type:'doughnut',
 data:{
   labels:[
   'Pominięcie znaku',
   'Dodanie znaku',
   'Zamiana znaku'
   ],

   datasets:[{
     label:'Niepoprawione błędy',
     data:[
      so,
      sa,
      sch
     ],
     backgroundColor:[
      'rgba(150, 226, 40, 0.6)',
      'rgba(226, 115, 40, 0.6)',
      'rgba(0, 29, 252, 0.6)'    
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
   title:{
     display:true,
     text:'Rodzaje niepoprawionych błędów wśród uczestników',
     fontSize:25
   },
   legend:{
     display:true,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function long_lostalt_invalidcase_other_chart(lostAlt, longAlt, invalidCase, other){
  let myChart20 = document.getElementById('myChart20').getContext('2d');
   let CapsChart = new Chart(myChart20, {
 type:'doughnut',
 data:{
   labels:[
   'Pominięcie Alt',
   'Przedłużenie Alt',
   'Nieprawidłowa wielkość znaku',
   'Inne'
   ],

   datasets:[{
     label:'Niepoprawione błędy',
     data:[
      lostAlt, 
      longAlt, 
      invalidCase, 
      other
     ],
     backgroundColor:[
      'rgba(252, 0, 228, 0.6)',
      'rgba(0, 252, 150, 0.6)',
      'rgba(244, 252, 0, 0.6)'    
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
   title:{
     display:true,
     text:'Sposoby zamiany znaków wśród uczestników',
     fontSize:25
   },
   legend:{
     display:true,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}
function education_asit_chart(primary, high, student, graduate, undergraduate){
  let myChart21 = document.getElementById('myChart21').getContext('2d');
   let CapsChart = new Chart(myChart21, {
 type:'horizontalBar',
 data:{
   labels:[
    'Uczeń szkoły podstawowej',
    'Uczeń szkoły ponadpodstawowej',
    'Student',
    'Absolwent uczelni wyższej',
    'Nie ukończył studiów'
   ],

   datasets:[{
     label:'Średni czas znaku [ms]',
     data:[
      primary, 
      high, 
      student, 
      graduate, 
      undergraduate
     ],
     backgroundColor:[
      'rgba(0, 176, 252, 0.6)',
      'rgba(252, 40, 0, 0.7)',
      'rgba(250, 252, 0, 0.5)',
      'rgba(218, 0, 252, 0.5)',
      'rgba(3, 252, 0, 0.5)'   
     ],
     borderWidth:1,
     borderColor:'#777',
     hoverBorderWidth:3,
     hoverBorderColor:'#000'
   }]
 },
 options:{
  scales: {
      yAxes: [{
          ticks: {
              beginAtZero: true,
              },
      scaleLabel: {
            display: true            
          }
      },],
      xAxes: [{scaleLabel: {
        display: true,
        labelString: 'Średni czas znaku'
      }}]
    
},
   title:{
     display:true,
     text:'Średni czas znaku a wykształcenie uczestników',
     fontSize:25
   },
   legend:{
     display:false,
     position:'right',
     labels:{
       fontColor:'#000'
     }
   },
   layout:{
     padding:{
       left:50,
       right:0,
       bottom:0,
       top:0
     }
   },
   tooltips:{
     enabled:true
   }
 }
});
}