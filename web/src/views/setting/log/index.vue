<template>
	<el-container>
		<el-main class="nopadding">
			<scTable ref="table" :apiObj="apiObj" stripe highlightCurrentRow @row-click="rowClick">
				<el-table-column label="序号" prop="id" width="180"></el-table-column>
				<el-table-column label="请求接口" prop="re_url" width="150"></el-table-column>
				<el-table-column label="请求方法" prop="re_method" width="150"></el-table-column>
				<el-table-column label="用户" prop="re_user" width="150"></el-table-column>
				<el-table-column label="请求内容" prop="re_content" show-overflow-tooltip="true"></el-table-column>
				<el-table-column label="请求结果" prop="rp_content" show-overflow-tooltip="true" width="150"></el-table-column>
				<el-table-column label="客户端IP" prop="re_ip" width="150"></el-table-column>
				<el-table-column label="请求时间" prop="re_time" width="170"></el-table-column>
				<el-table-column label="请求耗时" prop="access_time" width="170"></el-table-column>
			</scTable>
		</el-main>
	</el-container>
</template>

<script>

export default {
	name: 'log',
	data() {
		return {
			apiObj: this.$API.auth.operation,
		}
	},
	methods: {
		upsearch() {

		},
		rowClick(row) {
			console.log(row)
		}
	}
}
</script>

<style></style>
