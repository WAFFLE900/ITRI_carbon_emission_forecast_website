<template>
    <n-form ref="formRef" :model="model" :rules="rules">
      <n-form-item path="sepal_length" label="sepal_length">
        <n-input v-model:value="model.sepal_length" @keydown.enter.prevent />
      </n-form-item>
      <n-form-item path="sepal_width" label="sepal_width">
        <n-input
          v-model:value="model.sepal_width"
          @input="handlePasswordInput"
          @keydown.enter.prevent
        />
      </n-form-item>
      <n-form-item path="petal_length" label="petal_length">
      <n-input v-model:value="model.petal_length" @keydown.enter.prevent />
      </n-form-item>

      <n-form-item path="petal_width" label="petal_width">
      <n-input v-model:value="model.petal_width" @keydown.enter.prevent />
      </n-form-item>


      <n-row :gutter="[0, 24]">
        <n-col :span="24">
          <div style="display: flex; justify-content: flex-end">
            <n-button
              :disabled="model.sepal_length === null && model.sepal_width === null && model.petal_length === null && model.petal_width === null"
              round
              type="primary"
              @click="apicall"
            >
              Validate
            </n-button>
          </div>
        </n-col>
      </n-row>
    </n-form>
    <p>結果:{{msg}}</p>
    <pre>{{ JSON.stringify(model, null, 2) }}
  </pre>
  
  </template>
  
  <script lang="ts">
    console.log("讀取貓")
  import { defineComponent, ref, inject} from 'vue'
  import {
    FormInst,
    FormItemInst,
    FormItemRule,
    FormValidationError,
    useMessage,
    FormRules
  } from 'naive-ui'
  
  interface ModelType {
    sepal_length: number | null
    sepal_width: number | null
    petal_length: number | null
    petal_width: number | null
  }
  
  export default({
    name:"FormInput",
    setup () {
      const formRef = ref<FormInst | null>(null)
      const message = useMessage()

      const modelRef = ref<ModelType>({
        sepal_length: null,
        sepal_width: null,
        petal_length: null,
        petal_width: null
      })

      const rules: FormRules = {
        sepal_length: [
          {
            required: true,
            validator (rule: FormItemRule, value: string) {
              if (!value) {
                return new Error('sepal_length is required')
              }
              return true
            },
            trigger: ['input', 'blur']
          }
        ],
        sepal_width: [
          {
            required: true,
            validator (rule: FormItemRule, value: string) {
              if (!value) {
                return new Error('sepal_width is required')
              }
              return true
            },
            trigger: ['input', 'blur']
          }
        ],
        petal_length: [
          {
            required: true,
            validator (rule: FormItemRule, value: string) {
              if (!value) {
                return new Error('petal_length is required')
              }
              return true
            },
            trigger: ['input', 'blur']
          }
        ],
        petal_width: [
          {
            required: true,
            validator (rule: FormItemRule, value: string) {
              if (!value) {
                return new Error('petal_width is required')
              }
              return true
            },
            trigger: ['input', 'blur']
          }
        ]
      }


    const msg = ref('')
    const axios:any = inject('axios')

    const apicall = () =>{
      console.log(modelRef.value)
      axios.post('/predict-result', {
                        content: JSON.stringify(modelRef.value)
                    }, {
                        headers: {
                            'Content-type': 'application/json',
                        }}).then((res:any)=>{
        msg.value = res.data
      }).catch((error:any) => {
        console.log(error)
      })

      // let url = "http://localhost:5000/add";
      // const options = {
      //   method: "POST",
      //   headers: { "content-type": "application/json"},
      //   timeout: 2000000,
      //   body: {stop, prompt},
      //   url,
      // };
      // axios(options)
    }

      return {
        formRef,
        model: modelRef,
        rules,
        msg,
        apicall,
        handleValidateButtonClick (e: MouseEvent) {
          e.preventDefault()
          formRef.value?.validate(
            (errors: Array<FormValidationError> | undefined) => {
              if (!errors) {
                message.success('Valid')
              } else {
                console.log(errors)
                message.error('Invalid')
              }
            }
          )
        }
      }
    }
  })
  </script>

<style lang="scss">
  #app form[class$="n-form"]{ 
    width: 20%;
  }
</style>