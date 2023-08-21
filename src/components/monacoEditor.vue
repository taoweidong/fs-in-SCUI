<template>
	<div class="wrapper">
		<el-row type="flex" justify="center">
			<el-col :span="14">
				<el-form :inline="true">
					<el-form-item label="Language">
						<el-select v-model="language" placeholder="选择语言" @change="handleLanguage">
							<el-option v-for="(languageItem, key) in languageOptions" :key="key" :label="languageItem"
								:value="languageItem">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item label="Theme">
						<el-select v-model="editorTheme" placeholder="设置主题" @change="handleTheme">
							<el-option label="Visual Studio Dark" value="vs-dark"></el-option>
							<el-option label="Visual Studio" value="vs"></el-option>
							<el-option label="High Contrast Dark" value="hc-black"></el-option>
						</el-select>
					</el-form-item>
				</el-form>
				<div id="codeEditBox"></div>
				<el-button @click="handleCode">点击运行</el-button>
				<el-button @click="handleCreateCode">点击自动生成代码</el-button>
				<el-button @click="handleFormat" type="primary"
					v-if="language == 'json' || language == 'sql'">格式化</el-button>
			</el-col>

			<el-col :span="10">
				<el-card class="resultBox" shadow="never">
					<template #header>
						<div class="resultTitle">
							<span>运行结果</span>
						</div>
					</template>
					<div class="result">{{ result }}</div>
				</el-card>
			</el-col>
		</el-row>
	</div>
</template>

<script>
import * as monaco from 'monaco-editor'
import { ref, toRaw } from 'vue'
import $ from 'jquery'
// import { format } from 'sql-formatter'
import {
	pythonCompletion, sqlCompletion, cppCompletion, javaCompletion,
	csharpCompletion
} from "@/utils/completion";

export default {
	setup() {
		const editor = ref(null)
		const result = ref("展示运行结果～～～")
		const editorTheme = ref("vs-dark")
		const language = ref("java")
		const languageOptions = ref(["bat", "cpp", "csharp", "css", "dockerfile", "go", "graphql", "html", "ini",
			"java", "javascript", "json", "julia", "kotlin", "less", "markdown", "mysql", "objective-c", "pascal", "pascaligo",
			"perl", "php", "powershell", "python", "r", "redis", "rust", "scala", "scheme", "scss", "shell",
			"sophia", "sql", "swift", "tcl", "typescript", "xml", "yaml"])
		const initEditor = () => {
			// 初始化编辑器，确保dom已经渲染
			editor.value = monaco.editor.create(document.getElementById('codeEditBox'), {
				value: '', //编辑器初始显示文字
				language: language.value, //语言支持自行查阅demo
				theme: editorTheme.value, //官方自带三种主题vs, hc-black, or vs-dark
				selectOnLineNumbers: true,//显示行号
				roundedSelection: false,
				readOnly: false, // 只读
				cursorStyle: 'line', //光标样式
				automaticLayout: true, //自动布局
				glyphMargin: true, //字形边缘
				useTabStops: false,
				fontSize: 15, //字体大小
				autoIndent: true, //自动布局
				quickSuggestionsDelay: 100, //代码提示延时
			});

			// 监听值的变化
			// editor.value.onDidChangeModelContent((val) => {
			//   console.log(val.changes[0].text)
			// })

			// 创建代码提醒
			pythonCompletion
			sqlCompletion
			cppCompletion
			csharpCompletion
			javaCompletion
		}
		$(document).ready(function () {
			initEditor()
		})
		const handleCode = () => {
			let formData = new FormData()
			formData.append("python", toRaw(editor.value).getValue())
			// api.code.getCode(formData).then((res) => {
			// 	result.value = res
			// })
		}
		const handleCreateCode = () => {
			// api.code.createCode(toRaw(editor.value).getModel().getLanguageId()).then((res) => {
			// 	console.log(res)
			// 	toRaw(editor.value).setValue(res)
			// })
		}
		const handleTheme = () => {
			monaco.editor.setTheme(editorTheme.value)
		}
		const handleLanguage = (item) => {
			language.value = item
			monaco.editor.setModelLanguage(toRaw(editor.value).getModel(), language.value)
			// console.log(toRaw(editor.value).getModel().getLanguageId())
		}
		const handleFormat = () => {
			let lan = toRaw(editor.value).getModel().getLanguageId()
			console.log(lan)
			let content = toRaw(editor.value).getValue()
			if (lan == 'sql') {
				toRaw(editor.value).setValue(content)
			}
			else if (lan == 'json') {
				toRaw(editor.value).trigger('anyString', 'editor.action.formatDocument')
				toRaw(editor.value).setValue(content)
			}
		}
		return {
			editor,
			handleCode,
			result,
			handleCreateCode,
			handleTheme,
			editorTheme,
			language,
			handleLanguage,
			languageOptions,
			handleFormat
		}
	},
}
</script>

<style scoped>
.wrapper {
	margin: 20px auto;
}

#codeEditBox {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	height: 400px;
	padding: 0;
	overflow: hidden;
	margin-bottom: 15px;
}

.resultBox {
	margin-top: 50px;
	height: 400px;
}

.resultBox .resultTitle {
	color: #409EFF;
}

.resultBox .result {
	font-size: 15px;
	color: #969696;
}
</style>
