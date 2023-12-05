<template>

  <div style="background-color:white; border-radius: 40px; overflow: hidden; margin-left: auto; margin-right: auto; text-align:center; height:auto;width:70%;border:5px black solid; margin-bottom:10px;">
    <h3 style="overflow: hidden; color:black"><b>第一步驟 請選擇您想要的產業別</b></h3>
    <br/>
    <n-select
    :options="options"
    :reset-menu-on-options-change="false"
    style="width: 80%; text-align:center; margin-top: 0px; margin-bottom: 5px;"
    v-model:value="type"
    @update:value="handleUpdateValue"
  />

  </div>


  <br/>
  <div style="background-color:white; border-radius: 40px; overflow: hidden; margin-left: auto; margin-right: auto; text-align:center; height:auto;width:70%;border:5px black solid; margin-bottom:10px;">
    <h3 style="overflow: hidden; color:black"><b>第二步驟 請輸入您的會計科目資料（預設值為該產業別中位數）</b></h3>
  <div style="text-align:center;">
  <b>財務單位：仟元（TWD）</b>
</div>
  <div style="text-align:center; 	margin-left: auto; margin-right: auto;">

  <n-form style="margin: auto; width: 80%; overflow: auto;" :model="model" inline>
    <n-dynamic-input v-model:value="model.dynamicInputValue" item-style="margin-bottom: 0; display:inline-block; padding:3px;" :on-create="onCreate"
      #="{ index, value }">
      <div style="display: flex">
        <!--
          Usually, the path change will cause the form-item verification content
          or rules to be changed, so naive-ui will clear the existing
          verification effect. But this example is a special case, as we know
          the changes in path will not change form-item verification result and
          rules, so set ignore-path-change on form-item
        -->
        <n-form-item ignore-path-change :show-label="false" :path="`dynamicInputValue[${index}].name`"
          :rule="dynamicInputRule">

  
        <n-input v-model:value="model.dynamicInputValue[index].name" placeholder="Name" @keydown.enter.prevent readonly/>

          <!--
           Since pressing enter on the input element will cause the button in the form to be clicked, the default behavior is prevented
          -->
        </n-form-item>
        
        <div style="height: 34px; line-height: 34px; margin: 0 8px">
          =
        </div>
        <n-form-item ignore-path-change :show-label="false" :path="`dynamicInputValue[${index}].value`"
          :rule="dynamicInputRule">

          <n-input v-model:value="model.dynamicInputValue[index].value" placeholder="Value" @keydown.enter.prevent/>
          <div style="height: 34px; line-height: 34px; margin: 0 8px">
          
        </div>
          <!-- <n-slider v-model:value="model.dynamicInputValue[index].value" min="-500000000" max="500000000" :step="5" /> -->
          <n-slider v-model:value="model.dynamicInputValue[index].value" max="100000000" :step="10"/>
    
        </n-form-item>

      </div>

    </n-dynamic-input>
  </n-form>
</div>
</div>
<div style="background-color:white; border-radius: 40px; overflow: hidden; margin-left: auto; margin-right: auto; text-align:center; height:auto;width:70%;border:5px black solid; margin-bottom:10px;">
  <h3 style="overflow: hidden; color:black"><b>第三步驟 請執行計算</b></h3>
  
  <div style="text-align:center;">
    <n-button style="margin-bottom: 5px;" type="success" @click="apicall">
      Run
    </n-button>
  </div>
</div>
  <br/>
  
  <div style=" border-radius: 40px; overflow: hidden; margin-left: auto; margin-right: auto; text-align:center; background-image: linear-gradient(#28313B,#485461); width:70%;border:3px; margin-bottom:10px;">
    <h2 style="color:white;">預測結果</h2>
    <div style="height:30px"><h2 style="color:white;"><b>{{msg}}</b></h2></div>
    <p style="color:white;">此產業碳排放量中位數：{{CO2}}</p>
    <p style="color:white;">排放量單位：CO2e公噸</p>
    <hr/>
    <h3 style="color:white;">估計碳稅（費）</h3>
    <p style="color:white;">台灣國內碳費試算：{{tw_CO2}} （TWD）</p>
    <p style="color:white;">歐盟邊境碳稅(CBAM)：{{eu_CO2}} （EUR）</p>
    <p style="color:white;">美國清潔競爭法案(CCA)：{{us_CO2}} （USD）</p>
    <p style="color:white;"><strong>碳稅（費）主要徵收人：1. CBAM 2. CCA 3.環保署</strong></p>
  </div>

  <div style="background-color:white; border-radius: 40px; overflow: hidden; margin-left: auto; margin-right: auto; text-align:center; height:auto;width:70%;border:5px black solid; margin-bottom:10px;">
    <h2 style="overflow: hidden; color:black"><b>更多資訊</b></h2>
    <hr style="margin-bottom:0px; background-color:black; border:2px black solid;;">
    <br/>
    <a style="margin:1%; margin-top: 0px;" target="_blank" href="https://pj.ftis.org.tw/CFC/CFC/Login?ReturnUrl=%2FCFC%2FCFC%2FIndex">
      <img style="width:15%;height:auto;" src="../assets/source1.png">
    </a>
    <a style="margin:1%; margin-top: 0px;" target="_blank" href="https://www.go-moea.tw/">
      <img style="width:15%; height:auto;" src="../assets/source2.png">
    </a>
    <a style="margin:1%;" target="_blank" href="https://www.ice.com/index">
      <img style="width:15%; height:auto;" src="../assets/source3.png">
    </a>
    <a style="margin:1%;" target="_blank" href="https://www.eia.gov/environment/emissions/state/">
      <img style="width:15%; height:auto;" src="../assets/source4.png">
    </a>
    <a style="margin:1%;" target="_blank" href="https://ghgregistry.epa.gov.tw/ghg_rwd/Main/Index">
      <img style="width:15%; height:auto;" src="../assets/source5.png">
    </a>
  </div>
  <center>
    
    <h4>網頁瀏覽人數</h4>
    <a href="https://www.hitwebcounter.com" target="_blank">
  <img src="https://hitwebcounter.com/counter/counter.php?page=8073175&style=0011&nbdigits=5&type=page&initCount=0" title="Free Counter" Alt="web counter"   border="0" />
  </a>  
  <h4>Since November 2022</h4>
  <a href="mailto:jeddy.hwang@itri.org.tw"><strong>Feedback & Contact</strong></a>
  </center>
  <!-- <h2>Request data</h2>
  <p>type:{{ type }}</p>
  <pre>{{ JSON.stringify(model.dynamicInputValue, null, 2) }}</pre> -->
</template>

<script lang="ts">
import { defineComponent, ref, inject, toRaw } from 'vue'
import { FormRules, useMessage, SelectOption } from 'naive-ui'


export default defineComponent({
  setup() {
    function numberWithCommas(x:number) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }

    var CO2 = ref(0)
    const axios: any = inject('axios')
    const msg = ref("")
    const tw_CO2 = ref()
    const eu_CO2 = ref()
    const us_CO2 = ref()

    const model = ref({
      dynamicInputValue: [{ value: 0, name: ''}],
      type:''
    })
    const type = ref('請選擇產業別')

    // 舊特徵
    // const feature = ['存貨', '不動產廠房及設備', '商譽及無形資產合計', '預付投資款','應付帳款及票據'
    //        ,'普通股股本','資本公積合計','營業成本','營業費用','研究發展費','處分不動產廠房設備（含預付）－CFI',
    //        '折舊－CFO','攤提－CFO','購置不動產廠房設備（含預付）－CFI','員工人數']

    const feature = ['普通股股本', '營業費用', '研究發展費', '不動產廠房及設備', '存貨']
    var i = 0
    for (i = 0; i<feature.length; i++){
      model.value.dynamicInputValue[i].name = feature[i]
      
      if(i < feature.length-1){
        model.value.dynamicInputValue.push({ value: 0, name: '' })
      }
    }

    console.log(model.value.dynamicInputValue)
    const optionsRef = ref([
      {
        label: '上市塑膠工業',
        value: 'high1'
      },
      {
        label: '上市鋼鐵工業',
        value: 'high2'
      },
      {
        label: "上市光電業",
        value: 'low1'
      },
      {
        label: '上市塑膠工業',
        value: 'low2'
      },
      {
        label: '上市其他電子業',
        value: 'low3'
      },
      {
        label: '上市化學工業',
        value: 'low4'
      },
      {
        label: '上市半導體業',
        value: 'low5'
      },
      {
        label: '上市橡膠工業',
        value: 'low6'
      },
      {
        label: '上市水泥工業',
        value: 'low7'
      },
      {
        label: '上市油電燃氣業',
        value: 'low8'
      },
      {
        label: '上市玻璃陶瓷',
        value: 'low9'
      },      
      {
        label: '上市紡織纖維',
        value: 'low10'
      },
      {
        label: '上市通信網路業',
        value: 'low11'
      },
      {
        label: '上市造紙工業',
        value: 'low12'
      },
      // {
      //   label: '上市通信網路業',
      //   value: 'low13'
      // },
      // {
      //   label: '上市造紙工業',
      //   value: 'low14'
      // },
      {
        label: '上市電器電纜',
        value: 'low15'
      },
      {
        label: '上市電子零件組業',
        value: 'low16'
      },
      {
        label: '上市食品工業',
        value: 'low17'
      },
      {
        label: '上市其他',
        value: 'low18'
      },
      {
        label: '上櫃光電業',
        value: 'low19'
      },
      {
        label: '上櫃半導體業',
        value: 'low20'
      },
      {
        label: '上櫃油電燃氣業',
        value: 'low21'
      },
      {
        label: '上櫃紡織纖維',
        value: 'low22'
      },
      {
        label: '上櫃鋼鐵工業',
        value: 'low23'
      },
      {
        label: '上櫃電子零組件業',
        value: 'low24'
      },
      {
        label: '上櫃食品工業',
        value: 'low25'
      },                                
    ])


    const apicall = () => {

      const typevalue = toRaw(type.value)
      model.value['type'] = typevalue
      let data = toRaw(model.value)

      console.log(data)


      // http://ec2-35-79-153-51.ap-northeast-1.compute.amazonaws.com:5000/predict-result
      // /predict-result
      axios.post('http://ec2-35-79-153-51.ap-northeast-1.compute.amazonaws.com:5000/predict-result', {
        content: JSON.stringify(data)
      }, {
        headers: {
          'Content-type': 'application/json',
          'Origin-Trial': 'AjzPO+Elv9dJT7g3D5EQQMxdnQ4J2+9LSDQmKYyrbx59byWK0cOrD7Ys84MMyX+mj1ymKG1zwB9BBIDpCI+Qmw4AAACZeyJvcmlnaW4iOiJodHRwOi8vZWMyLTM1LTc5LTE1My01MS5hcC1ub3J0aGVhc3QtMS5jb21wdXRlLmFtYXpvbmF3cy5jb206ODAiLCJmZWF0dXJlIjoiUHJpdmF0ZU5ldHdvcmtBY2Nlc3NOb25TZWN1cmVDb250ZXh0c0FsbG93ZWQiLCJleHBpcnkiOjE2NzUyMDk1OTl9'
        }
      }).then((res: any) => {
        msg.value = res.data
        tw_CO2.value = res.data * 300
        eu_CO2.value = res.data * 74.032
        us_CO2.value = Math.max(res.data - 249.7, 0) * 55

        tw_CO2.value = numberWithCommas(Math.round(tw_CO2.value))
        eu_CO2.value = numberWithCommas(Math.round(eu_CO2.value))
        us_CO2.value = numberWithCommas(Math.round(us_CO2.value))
      }).catch((error: any) => {
        console.log(error.response.data)
      })
    }


    const  t1 = [31713487, 2295545, 803112, 16671283, 1214498]

    const t2 = [1307525, 185026, 22763, 2825363, 232321]
    
    const t3 = [1764674, 1628689, 202667, 1991122, 3024281]

    const t4 = [9348394, 1255551, 68872, 11743979, 2462714]

    const t5 = [17742963, 5049750, 3120716, 15801128, 6201435]

    const t6 = [45452273, 6745982, 3403, 46559758, 14818313]

    const t7 = [19880225, 9304061, 2288381, 52491175, 9548093]

    const t8 = [5632932, 403995, 0, 3315302, 3539095]

    const t9 = [5800815, 207088, 0, 687850, 8056]

    const t10 = [4289393, 1404424, 25565, 4671966, 2039276]

    const t11 = [3257782, 688882, 86545, 3588634, 2022217]

    const t12 = [1840812, 261625, 155136, 2020998, 357083]

    const t13 = [10956937, 5140344, 103681, 28364337, 6747772]

    const t14 = [5727457, 786912, 6062, 9142989, 3338683]

    const t15 = [33659883, 4468364, 98387, 22393612, 23638376]

    const t16 = [837060, 544208, 66377, 430342, 308559]

    const t17 = [28231971, 55147344, 486028, 65541549, 15475552]

    const t18 = [11231063, 5185066, 1950301, 4517421, 1871428]

    const t19 = [2947863, 479475, 210049, 3349865, 621042]

    const t20 = [1159139, 113449, 6329, 1547326, 140131]

    const t21 = [1184552, 233154, 19460, 2654719, 1322176]

    const t22 = [4033653, 585490, 58001, 6648680, 3385175]

    const t23 = [4164112, 600823, 27993, 8872235, 835401]

    const t24 = [1689203, 266999, 8329, 2208930, 603419]



    // const  t1 = [1214498, 16671283, 500020, 0, 2299968, 31713487, 2579113, 15286430, 
    // 2295545, 803112, 85977, 2358326, 105637, -2837344, 27602]
    // const t2 = [232321, 2825363, 100140, 0, 203458, 1307525, 646168, 1641518, 185026, 22763, 442, 179290, 4481, -247387, 352]
    // const t3 = [3024281, 1991122, 20777, 0, 4938686, 1764674, 881799, 19202786, 1628689, 202667, 6166, 111472, 19791, -224909, 1614]
    // const t4 = [2462714, 11743979, 140534, 0, 1359221, 9348394, 508313, 22001915, 1255551, 102319, 4373, 723423, 18821, -531292, 777]
    // const t5 = [6201435, 15801128, 120551, 0, 1969739, 17742963, 684587, 18078067, 5049750, 3120716, 2900, 1941486, 86090, -1809245, 1624]
    // const t6 = [14818313, 46559758, 18651, 0, 7113056, 45452273, 5024812, 107611112, 6745982, 3403, 19328, 4232223, 381968, -4641208, 4859]
    // const t7 = [9548093, 52491175, 657767, 0, 4571785, 19880225, 50647, 52401000, 9304061, 2288381, 31978, 6053214, 125326, -4712444, 12730]
    // const t8 = [3539095, 3315302, 3747, 0, 797470, 5632932, 184578, 4201704, 403995, 0, 14933, 311269, 10517, -212502, 816]
    // const t9 = [8056, 687850, 8534, 0, 680216, 5800815, 492087, 2216863, 207088, 0, 1572, 66476, 1744, -236095, 187]
    // const t10 = [2039276, 4671966, 169549, 0, 481486, 4289393, 149422, 3519918, 1404424, 25565, 15732, 534633, 34375, -151540, 2002]
    // const t11 = [2022217, 3588634, 9017, 0, 641246, 3257782, 92151, 7115978, 688882, 86545, 4995, 391402, 2351, -325744, 1820]
    // const t12 = [357083, 2020998, 1889, 0, 237845, 1840812, 103017, 1416098, 261625, 155136, 195, 208514, 656, -147318, 221]
    // const t13 = [6747772, 28364337, 0, 0, 4977424, 10956937, 744319, 30862889, 5140344, 103681, 80909, 2044510, 31400, -2924301, 7659]
    // const t14 = [3338683, 9142989, 3674, 0, 1207682, 5727457, 591470, 21489625, 786912, 6062, 1661, 1109999, 4504, -443259, 1001]
    // const t15 = [23638376, 22393612, 172621, 0, 8209758, 33659883, 15705515, 136522471, 4468364, 98387, 165583, 1954620, 34590, -4207219, 4677]
    // const t16 = [308559, 430342, 4679, 0, 297889, 837060, 436425, 2933578, 544208, 66377, 1970, 89894, 4107, -81511, 2594]
    // const t17 = [15475552, 65541549, 1290742, 0, 15326714, 28231971, 3190282, 133335698, 55147344, 486028, 239943, 8994261, 358377, -7367577, 42135]
    // const t18 = [1871428, 4517421, 8334687, 0, 1212648, 11231063, 10044820, 8844132, 5185066, 1950301, 115829, 760672, 410287, -448884, 2562]
    // const t19 = [621042, 3349865, 27574, 0, 345910, 2947863, 830417, 4304063, 479475, 210049, 2821, 724582, 12589, -513927, 1548]
    // const t20 = [140131, 1547326, 1479, 0, 42323, 1159139, 0, 1336979, 113449, 6329, 0, 148492, 2424, -302669, 150]
    // const t21 = [1322176, 2654719, 5626, 0, 312200, 1184552, 164725, 3406288, 233154, 19460, 5410, 310262, 4756, -431949, 738]
    // const t22 = [3385175, 6648680, 3640, 0, 468882, 4033653, 980381, 10402438, 585490, 58001, 4680, 407033, 7245, -415495, 1092]
    // const t23 = [835401, 8872235, 0, 0, 223738, 4164112, 1738894, 3587060, 600823, 27993, 0, 647272, 1158, -695033, 1068]
    // const t24 = [603419, 2208930, 5404, 0, 207397, 1689203, 62479, 3066115, 266999, 8329, 1893, 135523, 981, -243910, 522]

    const handleUpdateValue = (value: string, option: SelectOption) => {
        //message.info('value: ' + JSON.stringify(value))
        //message.info('option: ' + JSON.stringify(option))
        console.log(option['label'])
        switch(option['label']){
          case '上市光電業':
            CO2.value = 363032
            for(i = 0 ; i < feature.length; i++){
              model.value.dynamicInputValue[i].value = t1[i]
            }
            break
          case '上市其他':
            CO2.value = 354538
            for(i = 0 ; i < feature.length; i++){
              model.value.dynamicInputValue[i].value = t2[i]
            }
            break
          case '上市其他電子業':
            CO2.value = 951
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t3[i]
              }
              break
          case '上市化學工業':
            CO2.value = 207444
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t4[i]
              }
            break
          case '上市半導體業':
            CO2.value = 257184
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t5[i]
              }
            break          
          case '上市塑膠工業':
            CO2.value = 4001638.5
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t6[i]
              }
            break
          case '上市橡膠工業':
            CO2.value = 117375
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t7[i]
              }
            break          
          case '上市水泥工業':
            CO2.value = 672262
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t8[i]
              }
            break
          case '上市油電燃氣業':
            CO2.value = 380757
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t9[i]
              }
            break          
          case '上市玻璃陶瓷':
            CO2.value = 89390
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t10[i]
              }
            break          
          case '上市紡織纖維':
            CO2.value = 97587
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t11[i]
              }
            break          
          case '上市通信網路業':
            CO2.value = 10173
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t12[i]
              }
            break          
          case '上市造紙工業':
            CO2.value = 787823
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t13[i]
              }
            break          
          case '上市鋼鐵工業':
            CO2.value = 278449
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t14[i]
              }
            break          
          case '上市電器電纜':
            CO2.value = 286037.5
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t15[i]
              }
            break
          case '上市電子零組件業':
            CO2.value = 56734
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t16[i]
              }
            break          
          case '上市食品工業':
            CO2.value = 72266.5
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t17[i]
              }
            break          
          case '上櫃光電業':
            CO2.value = 20481.5
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t18[i]
              }
            break          
          case '上櫃半導體業':
            CO2.value = 70495.5
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t19[i]
              }
            break
          case '上櫃油電燃氣業':
            CO2.value = 453688.5
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t20[i]
              }
            break
          case '上櫃紡織纖維':
            CO2.value = 41472
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t21[i]
              }
            break          
          case '上櫃鋼鐵工業':
            CO2.value = 165715.5
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t22[i]
              }
            break
          case '上櫃電子零組件業':
            CO2.value = 207082
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t23[i]
              }
            break
          case '上櫃食品工業':
            CO2.value = 32723.5
            for(i = 0 ; i < feature.length; i++){
                model.value.dynamicInputValue[i].value = t24[i]
              }
            break
        }

      }

    return {
      dynamicInputRule: {
        trigger: 'input',
        validator(rule: unknown, value: string) {
          if (!value) return new Error('Need Input')
          return true
        }
      },
      model,
      onCreate() {
        return {
          name: '',
          value: '',
          
        }
      },
      msg,
      apicall,
      value: ref(50),
      options: optionsRef,
      type,
      handleUpdateValue,
      CO2,
      tw_CO2,
      eu_CO2,
      us_CO2
    }
  }
})
</script>

<style>
 div{
  margin-left: auto; 
	margin-right: auto;
	border:3px;
 }

 a, u {
  text-decoration: none;
}

img:hover{
  opacity: 0.7;
}

</style>