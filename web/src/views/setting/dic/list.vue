<template>
	<el-dialog :title="titleMap[mode]" v-model="visible" :width="400" destroy-on-close @closed="$emit('closed')">
		<el-form :model="form" :rules="rules" ref="dialogForm" label-width="100px" label-position="left">
			<el-form-item label="所属字典" prop="dic">
				<el-cascader disabled v-model="form.dic" :options="dic" :props="dicProps" :show-all-levels="false"
					clearable style="width: 200px;"></el-cascader>
			</el-form-item>
			<el-form-item label="项名称" prop="name">
				<el-input v-model="form.name" clearable style="width: 200px;"></el-input>
			</el-form-item>
			<el-form-item label="键值" prop="code">
				<el-input v-model="form.code" clearable style="width: 200px;"></el-input>
			</el-form-item>
			<el-form-item label="是否有效" prop="status">
				<el-switch v-model="form.status" active-value="1" inactive-value="0" style="width: 200px;"></el-switch>
			</el-form-item>
			<el-form-item label="序号" prop="sort">
				<el-input-number v-model="form.sort" :min="1" :max="10" style="width: 200px;" />
			</el-form-item>
		</el-form>
		<template #footer>
			<el-button @click="visible = false">取 消</el-button>
			<el-button type="primary" :loading="isSaveing" @click="submit()">保 存</el-button>
		</template>
	</el-dialog>
</template>

<script>
export default {
	emits: ['success', 'closed'],
	data() {
		return {
			mode: "add",
			titleMap: {
				add: '新增项',
				edit: '编辑项'
			},
			visible: false,
			isSaveing: false,
			form: {
				id: "",
				dic: "",
				name: "",
				code: "",
				status: true,
				sort: 1
			},
			rules: {
				dic: [
					{ required: true, message: '请选择所属字典' }
				],
				name: [
					{ required: true, message: '请输入项名称' }
				],
				code: [
					{ required: true, message: '请输入键值' }
				],
				sort: [
					{ required: true, message: '请输入序号' }
				]
			},
			dic: [],
			dicProps: {
				value: "id",
				label: "name",
				emitPath: false,
				checkStrictly: true
			}
		}
	},
	mounted() {
		if (this.params) {
			this.form.dic = this.params.code
		}
		this.getDic()
	},
	methods: {
		//显示
		open(mode = 'add') {
			this.mode = mode;
			this.visible = true;
			return this;
		},
		//获取字典列表
		async getDic() {
			var res = await this.$API.system.dic.tree.get();
			this.dic = res.data;
		},
		//表单提交方法
		submit() {
			this.$refs.dialogForm.validate(async (valid) => {
				if (valid) {
					this.isSaveing = true;
					var res = await this.$API.system.dic.save_sub.post(this.form);
					this.isSaveing = false;
					if (res.code == 200) {
						this.$emit('success', this.form, this.mode)
						this.visible = false;
						this.$message.success("操作成功")
					} else {
						this.$alert(res.message, "提示", { type: 'error' })
					}
				}
			})
		},
		//表单注入数据
		setData(data) {
			this.form.id = data.id
			this.form.name = data.name
			this.form.code = data.code
			this.form.status = data.status
			this.form.dic = data.dic
			this.form.sort = data.sort
		}
	}
}
</script>

<style></style>
