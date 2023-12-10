<template>
    <!-- <p>可以根据自己要求修改css样式

        <a href="javascript:void(0)" @click="one">点击这里打开窗口</a>

    </p> -->

    <div id="light" class="white_content">

        
        <n-alert title="使用前提醒" type="success">
        </n-alert>
        <p>1.本系統提供溫室氣體(碳排放當量)預估值，結果<span style="color:red"><b>僅供使用者參考</b></span>。使用者欲進行完整碳盤查，請依照相關規範並配合驗證機構進行。</p>
        <p>2.本系統為DigiTalent x TCA(2022) 研習成果，智財權歸屬財團法人工業技術研究院。相關技術資訊(含產品、技術或服務)，<span style="color:red"><b>在未經正式授權下，請勿任意擴散、複製、抄襲、引用。</b></span></p>
        <button href="javascript:void(0)" @click="two">同意</button>

    </div>

    <div id="fade" class="black_overlay">

    </div>

</template>    
<script>
import { defineComponent, ref } from 'vue'

export default defineComponent({
    name: 'Dialog',
    setup() {
        const one = () => {

            document.getElementById('light').style.display = 'block';

            document.getElementById('fade').style.display = 'block'

        }

        const two = () => {

            document.getElementById('light').style.display = 'none';

            document.getElementById('fade').style.display = 'none'

        }


        return{
            one,
            two,
        }
    }
})

</script>

<style>
div[class=black_overlay] {
    position: absolute;
    top: 0%;
    left: 0%;
    width: 100%;
    height: 100%;
    background-color: black;
    z-index: 1001;
    -moz-opacity: 0.6;
    opacity: .60;
    filter: alpha(opacity=60);
}



div[class=white_content] {
    position: absolute;
    top: 25%;
    left: 25%;
    width: 50%;
    height: 50%;
    padding: 16px;
    border: 16px solid #68be8d;
    background-color: white;
    z-index: 1002;
    overflow: auto;
}
</style>