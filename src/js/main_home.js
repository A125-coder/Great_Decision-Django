let caro = document.getElementById('carousel')
let left_btn = document.getElementById('carou_left')
let right_btn = document.getElementById('carou_right')
let text_p = document.querySelectorAll('.text')
let root = document.getElementById('root')
let index = 0
let text_slide = [];

for (let i = 0; i < text_p.length; i ++){
    text_slide[i] = text_p[i];
}

root.innerHTML = text_p[0].innerHTML

left_btn.addEventListener('click', function(){
    index -- ;
        if(index < 0){
            index = (text_slide.length - 1);
        }
        root.innerHTML = text_p[index].innerHTML;
})
right_btn.addEventListener('click', function(){
    index ++ ;
        if(index == text_slide.length){
            index = 0;
        }
        root.innerHTML = text_p[index].innerHTML;
})
root.innerHTML.style.color='#4e4751';
// let buttons = document.querySelectorAll('button')
// for(let i = 0; i<buttons.length; i++){
//     buttons[i].addEventListener('mouseenter', function(){
//         buttons[i].style.backgroundColor='#f7941e';
//         buttons[i].style.border='solid 1px #f7941e';
//         buttons[i].style.color='#fff';
//         buttons[i].style.transition='all .4s linear';
//     })
//     buttons[i].addEventListener('mouseleave', function(){
//         buttons[i].style.backgroundColor='#f3d43d';
//         buttons[i].style.border='solid 1px #f3d43d';
//         buttons[i].style.color='#4e4751';
//         buttons[i].style.transition='all .4s linear';
//     })
// }