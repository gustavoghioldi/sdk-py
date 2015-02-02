#pip install suds-jurko
from suds.client import Client

#############################################

class TodoPagoConnector:
	def __init__(self, http_header, wsdls, end_point):
		self._http_header = http_header
		self._wsdls = wsdls
		self._end_point = end_point
	
	######################################################################################	
	###Methodo publico que llama a la primera funcion del servicio SendAuthorizeRequest###
	######################################################################################
	def sendAuthorizeRequest(self, options_comercio, options_operacion):

		payload = self._get_payload(options_operacion);
		options_comercio['Payload'] = payload
		xml = self._parse_to_service(options_comercio, 'SendAuthorizeRequest')
		self._getClientSoap('Authorize')
		return self.cliente.service.SendAuthorizeRequest(__inject={'msg': xml})


	#####################################################################################	
	###Methodo publico que llama a la segunda funcion del servicio GetAuthorizeRequest###
	#####################################################################################
	def getAuthorizeAnswer(self, optionsAnwser):
		self._getClientSoap('Authorize')
		xml = self._parse_to_service(optionsAnwser, 'GetAuthorizeAnswer')
		return self.cliente.service.GetAuthorizeAnswer(__inject={'msg': xml})
	
	################################################################
	###Methodo publico que descubre todas las promociones de pago###
	################################################################
	def getAllPaymentMethods(self, optionsGAPM):
		self._getClientSoap('PaymentMethods')
		xml = self._parse_to_service(optionsGAPM, 'GetAll')
		return self.cliente.service.GetAll(__inject={'msg': xml})
	
	################################################################
	###Methodo publico que descubre todas las promociones de pago###
	################################################################
	def getStatus(self, optionsGS):
		self._getClientSoap('Operations')
		xml = self._parse_to_service(optionsGS, 'GetByOperationId')
		return self.cliente.service.GetByOperationId(__inject={'msg': xml})
	
	########################
	###Metodos privados ####
	########################
	def _parse_to_service(self, data, servicio):
		retorno = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:api="http://api.todopago.com.ar"><soapenv:Header/><soapenv:Body>"""
		retorno += "<api:"+servicio+">"
		for key in data:
			retorno += "<api:"+key+">"+data[key]+"</api:"+key+">"
		retorno += "</api:"+servicio+">"
		retorno += """</soapenv:Body></soapenv:Envelope>"""
		return retorno

	def _getClientSoap(self, operacion):
		self.cliente =  Client(self._wsdls[operacion], #se tiene que extraer de un array
			location=self._end_point+operacion, #se tiene que aprmar segun la funcion
			headers=self._http_header, 
			cache=None)		
	
	def _client_soap_header(self, data):
		retorno = "{"
		for key in data:
			retorno += key+" : '"+data[key]+"', "
		retorno += "}, "
		return retorno

	def _get_payload(self,diccionario):
		xmlpayload = "<Request>"
		for key in diccionario:
			xmlpayload += "<"+key+">"+diccionario[key]+"</"+key+">"
		xmlpayload += "</Request>"
		return xmlpayload
