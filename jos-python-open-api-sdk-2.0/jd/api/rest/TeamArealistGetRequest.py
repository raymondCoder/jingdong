from jd.api.base import RestApi

class TeamArealistGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.district_id = None

		def getapiname(self):
			return 'jingdong.team.arealist.get'




