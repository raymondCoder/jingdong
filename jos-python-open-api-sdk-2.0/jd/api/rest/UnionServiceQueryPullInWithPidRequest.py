from jd.api.base import RestApi

class UnionServiceQueryPullInWithPidRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.unionId = None
			self.childUnionId = None
			self.time = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.UnionService.queryPullInWithPid'




