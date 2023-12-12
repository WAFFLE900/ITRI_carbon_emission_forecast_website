# ITRI_carbon_emission_forecast_website 排碳夯算盤

排碳夯算盤主要是利用公開資料（政府Open Data、公開資訊觀測站及各企業財報）推估出一個描述企業排碳情況的模型，幫助審查機關快速掌握企業的排碳情況，也能幫助中小企業快速評估審查成本。
我們選擇使用使用 XGboost regressor 來建立預測模型，並且在模型表現中，樣本內的 86 家廠商資料和樣本外的五家公司碳排估計之準確率皆達到 98% 以上。

demo 影片（預設值為該產業的中位數）：https://reurl.cc/kaGk8K
