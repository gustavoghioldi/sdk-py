from todopagoconnector import TodoPagoConnector
optionsSAR_comercio = {
'Merchant': '350',
'EncodingMethod': 'XML',
'Security': '1234567890ABCDEF1234567890ABCDEF'}
optionsSAR_operacion = {
'MERCHANT': "305",
'OPERATIONID': "ABCDEF-1234-12221-FDE1-00000200",
'CURRENCYCODE': "032",
'AMOUNT': "50"
}

optionsGAA = {
'Security': '1234567890ABCDEF1234567890ABCDEF',
'Merchant': "305",
'RequestKey': '8496472a-8c87-e35b-dcf2-94d5e31eb12f',
'AnswerKey': '8496472a-8c87-e35b-dcf2-94d5e31eb12f'
}

optionsGAPM = {
'MERCHANT': '305'
}
optionsGS = {
'MERCHANT': '305',
'OPERATIONID': '141120084707'
}

j_header_http = {
'Authorization':'PRISMA 912EC803B2CE49E4A541068D495AB570',
}

j_wsdls = {
'Operations': 'http://localhost:8280/services/Operations?wsdl',
'Authorize': 'http://localhost:8280/services/Authorize?wsdl',
'PaymentMethods': 'http://localhost:8280/services/PaymentMethods?wsdl'}




tpc = TodoPagoConnector(j_header_http, j_wsdls, 'http://localhost:8280/services/')
print tpc.sendAuthorizeRequest(optionsSAR_comercio, optionsSAR_operacion)
print tpc.getAuthorizeAnswer(optionsGAA)
print tpc.getAllPaymentMethods(optionsGAPM)
print tpc.getStatus(optionsGS)