<template>
	<el-container>
		<el-header>
			<div>
				<h1>Hello World!</h1>
			</div>
		</el-header>


		<el-main>
			<monacoEditor></monacoEditor>
		</el-main>
	</el-container>
</template>
<script>
import monacoEditor from '@/components/monacoEditor.vue'
export default {
	name: '',
	components: {
		monacoEditor
	},
	mixins: [],
	props: {

	},
	data() {
		return {

		}
	},
	computed: {

	},
	watch: {

	},
	mounted() {

	},
	methods: {

	}
};
</script>
<style lang='' scoped>
</style>
