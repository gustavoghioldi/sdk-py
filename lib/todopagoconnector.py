from suds.client import Client

###########################################
diccionario = 
{
	'Merchant':'305',
	'MERCHANT': '305',
	'Security': '1234567890ABCDEF1234567890ABCDEF',
	'EncodingMethod': 'XML',
	'OPERATIONID':'982379847',
	'CURRENCYCODE':'032',
	'AMOUNT':'1234'
}
#############################################

#client = Client('http://localhost:8280/services/Authorize?wsdl', location='http://localhost:8280/services/Authorize', cache=None)
#list_of_methods = [method for method in client.wsdl.services[0].ports[0].methods]

#print list_of_methods

#response = client.service.SendAuthorizeRequest(Security = '1234567890ABCDEF1234567890ABCDEF',
 #Payload="<request></request>")

#print response
#print response


class TodoPagoConnector:
	def __init__(self, authorization, wsdl, end_point):
		self._authorization = authorization
		self._wsdl = wsdl
		self._end_point = end_point
	
	######################################################################################	
	###Methodo publico que llama a la primera funcion del servicio SendAuthorizeRequest###
	######################################################################################
	def sendAuthorizeRequest(self, optionsAuthorize):

		payload = self._get_payload(optionsAuthorize);
		self._getClientSoap()
		return self.cliente.service.SendAuthorizeRequest(
			Security = optionsAuthorize['Security'],
 			Merchant = optionsAuthorize['Merchant'],
 			EncodingMethod = 'XML',
 			Payload=payload)


	#####################################################################################	
	###Methodo publico que llama a la segunda funcion del servicio GetAuthorizeRequest###
	#####################################################################################
	def getAuthorizeRequest(self, optionsAnwser):
		self._getClientSoap()
		return self.cliente.service.GetAuthorizeRequest(
			Security = optionsAnwser['Security'],
			Merchant = optionsAnwser['Merchant'],
			RequestKey = optionsAnwser['RequestKey'],
			AnswerKey = optionsAnwser['AnswerKey']
			)
	
	################################################################
	###Methodo publico que descubre todas las promociones de pago###
	################################################################
	def getAllPaymentMethods(self):
		self._getClientSoap()#no va a funcionar por que cambia el wsdl y el end point	
		return  self.cliente.service.GetAll();
	
	########################	
	###Metodos privados ####
	########################
	def _getClientSoap(self):
	self.cliente =  Client(self._wsdl, 
			location=self._end_point,
			headers={'Authorization': self._authorization}, 
			cache=None)		

	def _get_payload(self,diccionario):
		xmlpayload = "<Request>"
		for key in diccionario:
			xmlpayload += "<"+key+">"+diccionario[key]+"</"+key+">"
		xmlpayload += "</Request>"
		return xmlpayload

###este es el ejemplo
dicionario = {
'Merchant':'305',
'MERCHANT': '305',
'Security': '1234567890ABCDEF1234567890ABCDEF',
'EncodingMethod': 'XML',
'OPERATIONID':'98237984733',
'CURRENCYCODE':'032',
'AMOUNT':'1234'
}

http_header = {'Authorization':'PRISMA 912EC803B2CE49E4A541068D495AB570'}
wsdls = {"Authorization":""}

try:
	tpc = TodoPagoConnector
	('PRISMA 912EC803B2CE49E4A541068D495AB570',
	 'http://localhost:8280/services/Authorize?wsdl',
	 'http://localhost:8280/services/Authorize')
	tpc.sendAuthorizeRequest(diccionario)
except:
	print ("no se puede conectar")
