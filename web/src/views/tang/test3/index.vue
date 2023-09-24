<template>
	<el-main>
		<vxe-form v-model:collapseStatus="collapseStatus" :data="formData" :rules="formRules" title-align="right"
			title-width="100" prevent-submit title-colon custom-layout>
			<!-- <vxe-input v-model="filterName" type="search" placeholder="试试全表搜索" @keyup="searchEvent"></vxe-input> -->
			<div style="border: 1px dashed green;padding: 10px;">
				<vxe-form-item title="昵称" field="nickname"
					:title-prefix="{ message: '左边图标', icon: 'vxe-icon-question-circle-fill' }">
					<template #default="{ data }">
						<vxe-input v-model="data.nickname" placeholder="请输入昵称" clearable></vxe-input>
					</template>
				</vxe-form-item>
				<vxe-form-item title="性别" field="sex" :item-render="{}"
					:title-prefix="{ message: '左边图标', icon: 'vxe-icon-user-fill' }"
					:title-suffix="{ message: '右边图标', icon: 'vxe-icon-warning-triangle' }">
					<template #title>
						<span style="color: red;">标题</span>
					</template>
					<template #default="{ data }">
						<vxe-select v-model="data.sex" placeholder="请选择性别" clearable>
							<vxe-option value="1" label="女"></vxe-option>
							<vxe-option value="2" label="男"></vxe-option>
						</vxe-select>
					</template>
				</vxe-form-item>
				<vxe-form-item title="年龄" field="age" :item-render="{}"
					:title-suffix="{ message: '右边图标', icon: 'vxe-icon-setting-fill' }">
					<template #default="{ data }">
						<vxe-input v-model="data.age" type="integer" placeholder="请输入年龄" clearable></vxe-input>
					</template>
				</vxe-form-item>
				<vxe-form-item title="是否禁用" field="active" :item-render="{}">
					<template #default="{ data }">
						<vxe-switch v-model="data.active" open-label="是" close-label="否"></vxe-switch>
					</template>
				</vxe-form-item>

				<vxe-form-item title="日期" field="date" :item-render="{}" folding>
					<template #default="{ data }">
						<vxe-input v-model="data.date" type="date" placeholder="请选择日期" clearable></vxe-input>
					</template>
				</vxe-form-item>
				<vxe-form-item title="兴趣爱好" field="flagList" :item-render="{}" folding>
					<template #default="{ data }">
						<vxe-checkbox-group v-model="data.flagList">
							<vxe-checkbox label="1" content="爬山"></vxe-checkbox>
							<vxe-checkbox label="2" content="跑步"></vxe-checkbox>
							<vxe-checkbox label="3" content="听歌"></vxe-checkbox>
						</vxe-checkbox-group>
					</template>
				</vxe-form-item>
			</div>
			<div>
				<vxe-form-item align="center" collapse-node>
				</vxe-form-item>
			</div>
		</vxe-form>
		<vxe-table border height="300" :column-config="{ useKey: true }" :row-config="{ useKey: true }" :data="list">
			<vxe-column type="seq" width="80"></vxe-column>
			<vxe-column field="name" title="Name" type="html"></vxe-column>
			<vxe-column field="role" title="Role" type="html"></vxe-column>
			<vxe-column field="age" title="Age" type="html"></vxe-column>
			<vxe-column field="address" title="Address" type="html"></vxe-column>
			<template #empty>
				<span style="color: red;">
					<img src="https://n.sinaimg.cn/sinacn17/w120h120/20180314/89fc-fyscsmv5911424.gif">
					<p>没有更多数据了！</p>
				</span>
			</template>
		</vxe-table>
	</el-main>
</template>

<script>
export default {
	name: "test3",
	data() {
		return {
			list: [],
			date: '',
			collapseStatus: true,
			filterName: '',
			formData: {
				name: '',
				nickname: '',
				sex: '',
				age: 30,
				status: '1',
				date: '',
				active: false,
				flagList: []
			},
			formRules: {
				name: [
					{ required: true, message: '请输入' }
				],
				nickname: [
					{ required: true, message: '请输入' }
				]
			},
			allAlign: null,
			tableData: [
				{ id: 10001, name: 'Test1', role: 'Develop', sex: '0', age: 28, amount: 888, address: 'test abc' },
				{ id: 10002, name: 'Test2', role: 'Test', sex: '1', age: 22, amount: 666, address: 'Guangzhou' },
				{ id: 10003, name: 'Test3', role: 'PM', sex: '1', age: 32, amount: 89, address: 'Shanghai' },
				{ id: 10004, name: 'Test4', role: 'Designer', sex: '0', age: 23, amount: 1000, address: 'test abc' },
				{ id: 10005, name: 'Test5', role: 'Develop', sex: '0', age: 30, amount: 999, address: 'Shanghai' },
				{ id: 10006, name: 'Test6', role: 'Designer', sex: '0', age: 21, amount: 998, address: 'test abc' },
				{ id: 10007, name: 'Test7', role: 'Test', sex: '1', age: 29, amount: 2000, address: 'test abc' },
				{ id: 10008, name: 'Test8', role: 'Develop', sex: '1', age: 35, amount: 999, address: 'test abc' },
				{ id: 10009, name: 'Test9', role: 'Test', sex: '1', age: 26, amount: 2000, address: 'test abc' },
				{ id: 100010, name: 'Test10', role: 'Develop', sex: '1', age: 21, amount: 666, address: 'test abc' }
			]
		}
	},
	created() {
		this.list = this.tableData
	},
	methods: {
		searchEvent() {
			const filterVal = String(this.filterName).trim().toLowerCase()
			if (filterVal) {
				const filterRE = new RegExp(filterVal, 'gi')
				const searchProps = ['name', 'role', 'age', 'address']
				const rest = this.tableData.filter(item => searchProps.some(key => String(item[key]).toLowerCase().indexOf(filterVal) > -1))
				this.list = rest.map(row => {
					const item = Object.assign({}, row)
					searchProps.forEach(key => {
						item[key] = String(item[key]).replace(filterRE, match => `<span class="keyword-lighten">${match}</span>`)
					})
					return item
				})
			} else {
				this.list = this.tableData
			}
		},
		handleAdd() {
			this.tableData[0].name.push("新增Tag标签");
		},
		handleClose2(event, name) {
			console.log("触发删除", event, name)
		}
	},
}
</script>
