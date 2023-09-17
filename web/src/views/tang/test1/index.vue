<template>
	<el-main>
		<vxe-toolbar>
			<template #buttons>
				<vxe-button @click="allAlign = 'left'">居左</vxe-button>
				<vxe-button @click="allAlign = 'center'">居中</vxe-button>
				<vxe-button @click="allAlign = 'right'">居右</vxe-button>
			</template>
		</vxe-toolbar>

		<vxe-table :align="allAlign" :data="tableData">
			<vxe-column type="seq" width="60"></vxe-column>
			<vxe-column field="name" title="Name">
				<template #default="{ row }">
					<Tag v-for="item in row.name" :key="item" :name="item" closable @on-close="handleClose2">标签{{ item }}
					</Tag>
					<Button icon="ios-add" type="dashed" size="small" @click="handleAdd">添加标签</Button>
				</template>
			</vxe-column>
			<vxe-column field="sex" title="Sex"></vxe-column>
			<vxe-column field="age" title="Age"></vxe-column>
		</vxe-table>
	</el-main>
</template>

<script>
export default {
	data() {
		return {
			allAlign: null,
			tableData: [
				{ id: 10001, name: ['Test1', 'Test1'], role: 'Develop', sex: 'Man', age: 28, address: 'test abc' },
				{ id: 10002, name: ['Test1', 'Test1'], role: 'Test', sex: 'Women', age: 22, address: 'Guangzhou' },
				{ id: 10003, name: ['Test1', 'Test1'], role: 'PM', sex: 'Man', age: 32, address: 'Shanghai' },
				{ id: 10004, name: ['Test1', 'Test1'], role: 'Designer', sex: 'Women', age: 24, address: 'Shanghai' }
			]
		}
	},
	methods: {
		handleAdd() {
			this.tableData[0].name.push("新增Tag标签");
		},
		handleClose2(event, name) {
			console.log("触发删除", event, name)
		}
	},
}
</script>
