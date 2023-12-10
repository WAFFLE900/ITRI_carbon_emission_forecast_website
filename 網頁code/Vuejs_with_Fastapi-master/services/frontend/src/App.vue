<template>
	<Dialog></Dialog>
	<div style="text-align:center; ">
		<div id="navbar">
			<h1>排碳夯算盤</h1>
		</div>
	</div>
	<br/>
	<n-message-provider>
		<UserProfile />
	</n-message-provider>
	<footer class="footer-distributed" style="position: absolute;">

		<div class="footer-left">

			<h3>
				<img style="width: 30%;" src="./assets/itrilogo.svg">
				<img style="width: 50%;" src="./assets/ADI.svg">
				<br />
				<img style="width: 30%;" src="./assets/digi_logo.png">
			</h3>
			<p class="footer-company-name">工業技術研究院智慧機械中心 © 2022</p>
		</div>

		<div class="footer-center" style="border-left: 10px solid gray;">

			<div>
				<img style="width:50%;" src="./assets/taiwan.png">
				<img style="width:50%;" src="./assets/chengkung.png">
				<img style="width:50%;" src="./assets/ncu-310x207.png">
				<img style="width:50%;" src="./assets/central.png">
				預估參考資料：<img style="width:40%;" src="./assets/en.png">
			</div>

		</div>

	</footer>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import UserProfile from "./components/UserProfile.vue"
import FormInput from "./components/FormInput.vue"
import Dialog from './components/Dialog.vue'

export default defineComponent({
	name: 'App',
	components: {
		UserProfile,
		Dialog
		// FormInput
	}
});

</script>


<style lang="scss">



input {
	pointer-events: none;
}

div[class="n-button-group"] {
	display: none;
}

@import url(https://fonts.googleapis.com/css?family=Open+Sans:400,500,300,700);

* {
	font-family: Open Sans;
}

section {
	width: 100%;
	display: inline-block;
	background: #333;
	height: 50vh;
	text-align: center;
	font-size: 22px;
	font-weight: 700;
	text-decoration: underline;
}

.footer-distributed {
	background: #d1d1d1;
	box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.12);
	box-sizing: border-box;
	width: 100%;
	text-align: left;
	font: bold 16px sans-serif;
	padding: 55px 50px;
	
}

.footer-distributed .footer-left,
.footer-distributed .footer-center,
.footer-distributed .footer-right {
	display: inline-block;
	vertical-align: top;
}

/* Footer left */

.footer-distributed .footer-left {
	width: 40%;
}

/* The company logo */

.footer-distributed h3 {
	color: #ffffff;
	font: normal 36px 'Open Sans', cursive;
	margin: 0;
}

.footer-distributed h3 span {
	color: lightseagreen;
}

/* Footer links */

.footer-distributed .footer-links {
	color: #ffffff;
	margin: 20px 0 12px;
	padding: 0;
}

.footer-distributed .footer-links a {
	display: inline-block;
	line-height: 1.8;
	font-weight: 400;
	text-decoration: none;
	color: inherit;
}

.footer-distributed .footer-company-name {
	color: #222;
	font-size: 14px;
	font-weight: normal;
	margin: 0;
}

/* Footer Center */

.footer-distributed .footer-center {
	width: 35%;
}

.footer-distributed .footer-center i {
	background-color: #33383b;
	color: #ffffff;
	font-size: 25px;
	width: 38px;
	height: 38px;
	border-radius: 50%;
	text-align: center;
	line-height: 42px;
	margin: 10px 15px;
	vertical-align: middle;
}

.footer-distributed .footer-center i.fa-envelope {
	font-size: 17px;
	line-height: 38px;
}

.footer-distributed .footer-center p {
	display: inline-block;
	color: #ffffff;
	font-weight: 400;
	vertical-align: middle;
	margin: 0;
}

.footer-distributed .footer-center p span {
	display: block;
	font-weight: normal;
	font-size: 14px;
	line-height: 2;
}

.footer-distributed .footer-center p a {
	color: lightseagreen;
	text-decoration: none;
	;
}

.footer-distributed .footer-links a:before {
	content: "|";
	font-weight: 300;
	font-size: 20px;
	left: 0;
	color: #fff;
	display: inline-block;
	padding-right: 5px;
}

.footer-distributed .footer-links .link-1:before {
	content: none;
}

/* Footer Right */

.footer-distributed .footer-right {
	position: absolute;
	bottom: 0%;
	width: 20%;

}

.footer-distributed .footer-company-about {
	line-height: 20px;
	color: black;
	font-size: 13px;
	font-weight: normal;
	vertical-align: super;
}

.footer-distributed .footer-company-about span {
	display: block;
	color: #ffffff;
	font-size: 14px;
	font-weight: bold;
	margin-bottom: 20px;
}

.footer-distributed .footer-icons {
	margin-top: 25px;
}

.footer-distributed .footer-icons a {
	display: inline-block;
	width: 35px;
	height: 35px;
	cursor: pointer;
	background-color: #33383b;
	border-radius: 2px;

	font-size: 20px;
	color: #ffffff;
	text-align: center;
	line-height: 35px;

	margin-right: 3px;
	margin-bottom: 5px;
}

/* If you don't want the footer to be responsive, remove these media queries */

@media (max-width: 880px) {

	.footer-distributed {
		font: bold 14px sans-serif;
	}

	.footer-distributed .footer-left,
	.footer-distributed .footer-center,
	.footer-distributed .footer-right {
		display: block;
		width: 100%;
		margin-bottom: 40px;
		text-align: center;
	}

	.footer-distributed .footer-center i {
		margin-left: 0;
	}

}



/* Style the navbar */
#navbar {
	overflow: hidden;
	background-image: linear-gradient(#28313B,#485461);
	color:#fff;
	border-radius: 7px;
	margin-left: auto; 
	margin-right: auto;
	border:3px;
	width:70%;
}
</style>