from jd.api.base import RestApi

class ServicePromotionCouponGetInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			RestApi.__init__(self,domain, port)
			self.couponUrl = None

		def getapiname(self):
			return 'jingdong.service.promotion.coupon.getInfo'




