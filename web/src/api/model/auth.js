import config from "@/config"
import http from "@/utils/request"

export default {
	token: {
		url: `${config.API_URL}/auth/token`,
		name: "登录获取TOKEN",
		post: async function(data={}){
			return await http.post(this.url, data);
		}
	},
	operation: {
		url: `${config.API_URL}/auth/operation`,
		name: "登录操作日志",
		get: async function(params){
			return await http.get(this.url, params);
		}
	}
}
