<template>
	<el-container>
		<el-aside width="300px" v-loading="showDicloading">
			<el-container>
				<el-header>
					<el-input placeholder="输入关键字进行过滤" v-model="dicFilterText" clearable></el-input>
				</el-header>
				<el-main class="nopadding">
					<el-tree ref="dic" class="menu" node-key="id" :data="dicList" :props="dicProps"
						:highlight-current="true" :expand-on-click-node="false" :filter-node-method="dicFilterNode"
						@node-click="dicClick">
						<template #default="{ node, data }">
							<span class="custom-tree-node">
								<span class="label">{{ node.label }}</span>
								<span class="code">{{ data.code }}</span>
								<span class="do">
									<el-button-group>
										<el-button icon="el-icon-edit" size="small" @click.stop="dicEdit(data)"></el-button>
										<el-button icon="el-icon-delete" size="small"
											@click.stop="dicDel(node, data)"></el-button>
									</el-button-group>
								</span>
							</span>
						</template>
					</el-tree>
				</el-main>
				<el-footer style="height:51px;">
					<el-button type="primary" size="small" icon="el-icon-plus" style="width: 100%;"
						@click="addDic">字典分类</el-button>
				</el-footer>
			</el-container>
		</el-aside>
		<el-container class="is-vertical">
			<el-header>
				<div class="left-panel">
					<el-button type="primary" icon="el-icon-plus" @click="addInfo"></el-button>
					<el-button type="danger" plain icon="el-icon-delete" :disabled="selection.length == 0"
						@click="batch_del"></el-button>
					<el-select v-model="value" placeholder="Select">
						<el-option v-for="item in options" :key="item.key" :label="item.label" :value="item.key" />
					</el-select>
				</div>
			</el-header>
			<el-main class="nopadding">
				<scTable ref="table" :apiObj="listApi" row-key="id" :params="listApiParams"
					@selection-change="selectionChange" stripe :paginationLayout="'prev, pager, next'">
					<el-table-column type="selection" width="50"></el-table-column>
					<!-- <el-table-column label="" width="60">
						<template #default>
							<el-tag class="move" style="cursor: move;"><el-icon-d-caret
									style="width: 1em; height: 1em;" /></el-tag>
						</template>
					</el-table-column> -->
					<el-table-column label="名称" prop="name" width="150"></el-table-column>
					<el-table-column label="键值" prop="code" width="150"></el-table-column>
					<el-table-column label="是否有效" prop="status" width="100">
						<template #default="scope">
							<el-switch v-model="scope.row.status" @change="changeSwitch($event, scope.row)"></el-switch>
						</template>
					</el-table-column>
					<el-table-column label="序号" prop="sort" width="150"></el-table-column>
					<el-table-column label="操作" fixed="right" align="right" width="120">
						<template #default="scope">
							<el-button-group>
								<el-button text type="primary" size="small"
									@click="table_edit(scope.row, scope.$index)">编辑</el-button>
								<el-popconfirm title="确定删除吗？" @confirm="table_del(scope.row, scope.$index)">
									<template #reference>
										<el-button text type="primary" size="small">删除</el-button>
									</template>
								</el-popconfirm>
							</el-button-group>
						</template>
					</el-table-column>
				</scTable>
			</el-main>
		</el-container>
	</el-container>

	<dic-dialog v-if="dialog.dic" ref="dicDialog" @success="handleDicSuccess" @closed="dialog.dic = false"></dic-dialog>

	<list-dialog v-if="dialog.list" ref="listDialog" @success="handleListSuccess"
		@closed="dialog.list = false"></list-dialog>
</template>

<script>
import dicDialog from './dic'
import listDialog from './list'
import Sortable from 'sortablejs'

export default {
	name: 'dic',
	components: {
		dicDialog,
		listDialog
	},
	data() {
		return {
			dialog: {
				dic: false,
				info: false
			},
			value: '',
			options: [],
			select_code: '',
			showDicloading: true,
			dicList: [],
			dicFilterText: '',
			dicProps: {
				label: 'name'
			},
			listApi: null,
			listApiParams: {},
			selection: []
		}
	},
	watch: {
		dicFilterText(val) {
			this.$refs.dic.filter(val);
		}
	},
	mounted() {
		this.getDic()
		this.get_init_dict()
	},
	methods: {
		async get_init_dict() {
			var reqData = { code: 'VersionDict' }
			var res = await this.$API.system.dic.get.get(reqData);
			if (res.code == 200) {
				this.options = res.data
			}
		},
		//加载树数据
		async getDic() {
			var res = await this.$API.system.dic.tree.get();
			this.showDicloading = false;
			this.dicList = res.data;
			//获取第一个节点,设置选中 & 加载明细列表
			var firstNode = this.dicList[0];
			if (firstNode) {
				this.$nextTick(() => {
					this.$refs.dic.setCurrentKey(firstNode.id)
				})
				this.listApiParams = {
					code: firstNode.code
				}
				this.select_code = firstNode.code
				this.listApi = this.$API.system.dic.list;
			}
		},
		//树过滤
		dicFilterNode(value, data) {
			if (!value) return true;
			var targetText = data.name + data.code;
			return targetText.indexOf(value) !== -1;
		},
		//树增加
		addDic() {
			this.dialog.dic = true
			this.$nextTick(() => {
				this.$refs.dicDialog.open()
			})
		},
		//编辑树
		dicEdit(data) {
			this.dialog.dic = true
			this.$nextTick(() => {
				var editNode = this.$refs.dic.getNode(data.id);
				var editNodeParentId = editNode.level == 1 ? undefined : editNode.parent.data.id
				data.parentId = editNodeParentId
				this.$refs.dicDialog.open('edit').setData(data)
			})
		},
		//树点击事件
		dicClick(data) {
			this.select_code = data.code
			this.$refs.table.reload({
				code: data.code
			})
		},
		//删除树
		dicDel(node, data) {
			this.$confirm(`确定删除 ${data.name} 项吗？`, '提示', {
				type: 'warning'
			}).then(async () => {
				this.showDicloading = true;

				//删除节点是否为高亮当前 是的话 设置第一个节点高亮
				var dicCurrentKey = this.$refs.dic.getCurrentKey();
				var reqData = { id: [dicCurrentKey] }
				var res = await this.$API.system.dic.delete.post(reqData);
				if (res.code == 200) {
					this.$refs.dic.remove(data.id)
					if (dicCurrentKey == data.id) {
						var firstNode = this.dicList[0];
						if (firstNode) {
							this.$refs.dic.setCurrentKey(firstNode.id);
							this.$refs.table.upData({
								code: firstNode.code
							})
						} else {
							this.listApi = null;
							this.$refs.table.tableData = []
						}
					}
					this.$message.success("删除成功")
				} else {
					this.$alert(res.message, "提示", { type: 'error' })
				}
				this.showDicloading = false;
			}).catch(() => {

			})
		},
		//行拖拽
		rowDrop() {
			const _this = this
			const tbody = this.$refs.table.$el.querySelector('.el-table__body-wrapper tbody')
			Sortable.create(tbody, {
				handle: ".move",
				animation: 300,
				ghostClass: "ghost",
				onEnd({ newIndex, oldIndex }) {
					const tableData = _this.$refs.table.tableData
					const currRow = tableData.splice(oldIndex, 1)[0]
					tableData.splice(newIndex, 0, currRow)
					_this.$message.success("排序成功")
				}
			})
		},
		//添加明细
		addInfo() {
			this.dialog.list = true
			this.$nextTick(() => {
				var dicCurrentKey = this.$refs.dic.getCurrentKey();
				const data = {
					dic: dicCurrentKey,
					sort: 1
				}
				this.$refs.listDialog.open().setData(data)
			})
		},
		//编辑明细
		table_edit(row) {
			this.dialog.list = true
			var dicCurrentKey = this.$refs.dic.getCurrentKey();
			row.dic = dicCurrentKey
			this.$nextTick(() => {
				this.$refs.listDialog.open('edit').setData(row)
			})
		},
		//删除明细
		async table_del(row, index) {
			console.log(row)
			var reqData = { id: [row.id] }
			var res = await this.$API.system.dic.delete.post(reqData);
			if (res.code == 200) {
				this.$refs.table.tableData.splice(index, 1);
				this.$message.success("删除成功")
			} else {
				this.$alert(res.message, "提示", { type: 'error' })
			}
		},
		//批量删除
		async batch_del() {
			this.$confirm(`确定删除选中的 ${this.selection.length} 项吗？`, '提示', {
				type: 'warning'
			}).then(async () => {
				const del_ids = []
				// 刪除数据
				this.selection.forEach(item => {
					del_ids.push(item.id)
				})
				var reqData = { id: del_ids }
				var res = await this.$API.system.dic.delete.post(reqData);
				if (res.code == 200) {
					const loading = this.$loading();
					this.selection.forEach(item => {
						this.$refs.table.tableData.forEach((itemI, indexI) => {
							if (item.id === itemI.id) {
								this.$refs.table.tableData.splice(indexI, 1)
							}
						})
					})
					loading.close();
					this.$message.success("删除成功")
				} else {
					this.$alert(res.message, "提示", { type: 'error' })
				}
			}).catch(() => {

			})
		},
		//提交明细
		saveList() {
			this.$refs.listDialog.submit(async (formData) => {
				this.isListSaveing = true;
				var res = await this.$API.demo.post.post(formData);
				this.isListSaveing = false;
				if (res.code == 200) {
					//这里选择刷新整个表格 OR 插入/编辑现有表格数据
					this.listDialogVisible = false;
					this.$message.success("操作成功")
				} else {
					this.$alert(res.message, "提示", { type: 'error' })
				}
			})
		},
		//表格选择后回调事件
		selectionChange(selection) {
			this.selection = selection;
		},
		//表格内开关事件
		async changeSwitch(val, row) {
			row.status = val
			//3.等待接口返回后改变值
			var reqData = { id: row.id, value: val }
			var res = await this.$API.system.dic.refresh_status.post(reqData);
			if (res.code == 200) {
				this.$refs.table.reload({ code: this.select_code })
				this.$message.success("状态更新成功")
			} else {
				this.$alert(res.message, "提示", { type: 'error' })
			}

		},
		//本地更新数据
		handleDicSuccess(data, mode) {
			console.log(data, mode)
			this.getDic()
		},
		//本地更新数据
		handleListSuccess(data, mode) {
			if (mode == 'add') {
				data.id = new Date().getTime()
				this.$refs.table.tableData.push(data)
			} else if (mode == 'edit') {
				this.$refs.table.tableData.filter(item => item.id === data.id).forEach(item => {
					Object.assign(item, data)
				})
			}
		}
	}
}
</script>

<style scoped>
.menu:deep(.el-tree-node__label) {
	display: flex;
	flex: 1;
	height: 100%;
}

.custom-tree-node {
	display: flex;
	flex: 1;
	align-items: center;
	justify-content: space-between;
	font-size: 14px;
	padding-right: 24px;
	height: 100%;
}

.custom-tree-node .code {
	font-size: 12px;
	color: #999;
}

.custom-tree-node .do {
	display: none;
}

.custom-tree-node:hover .code {
	display: none;
}

.custom-tree-node:hover .do {
	display: inline-block;
}
</style>
