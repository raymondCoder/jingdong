from jd.api.base import RestApi

class TeamSkulistGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.team_id = None

		def getapiname(self):
			return 'jingdong.team.skulist.get'




