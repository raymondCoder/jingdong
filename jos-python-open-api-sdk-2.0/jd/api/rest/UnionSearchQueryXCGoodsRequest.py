from jd.api.base import RestApi

class UnionSearchQueryXCGoodsRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.skuIds = None
			self.cid1 = None
			self.cid2 = None
			self.cid3 = None
			self.pageIndex = None
			self.pageSize = None
			self.keyword = None
			self.pricefrom = None
			self.priceto = None
			self.commissionShareStart = None
			self.commissionShareEnd = None
			self.owner = None
			self.sortName = None
			self.sort = None
			self.isPG = None
			self.pingouPriceStart = None
			self.pingouPriceEnd = None
			self.shopId = None

		def getapiname(self):
			return 'jingdong.union.search.queryXCGoods'




