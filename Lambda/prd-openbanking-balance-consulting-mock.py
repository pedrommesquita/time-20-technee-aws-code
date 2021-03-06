import json

def lambda_handler(event, context):
    return_json = '''{
    "data": {
    "paidInstalments": 73,
    "contractOutstandingBalance": 100000.04,
    "releases": [
      {
        "paymentId": "XlthLXpBLVowLTldW2EtekEtWjAtOVwtXXswLDk5fSQ",
        "isOverParcelPayment": true,
        "instalmentId": "WGx0aExYcEJMVm93TFRsZFcyRXRla0V0V2pBdE9Wd3RYWH",
        "paidDate": "2021-05-21",
        "currency": "BRL",
        "paidAmount": 100000.04,
        "overParcel": {
          "fees": [
            {
              "feeName": "Reavaliação periódica do bem",
              "feeCode": "aval_bem",
              "feeAmount": 100000.04
            }
          ],
          "charges": [
            {
              "chargeType": "JUROS_REMUNERATORIOS_POR_ATRASO",
              "chargeAdditionalInfo": "Informações adicionais",
              "chargeAmount": 100000.04
            }
          ]
        }
      }
    ]
  },
  "links": {
    "self": "https://api.itau.com.br/open-banking/api/v1/resource",
    "first": "https://api.itau.com.br/open-banking/api/v1/resource",
    "prev": "https://api.itau.com.br/open-banking/api/v1/resource",
    "next": "https://api.itau.com.br/open-banking/api/v1/resource",
    "last": "https://api.itau.com.br/open-banking/api/v1/resource"
  },
  "meta": {
    "totalRecords": 1,
    "totalPages": 1,
    "requestDateTime": "2021-05-21T08:30:00Z"
  }
  }'''
    j = json.loads(return_json)
    return {
        'statusCode': 200,
        'body': j
    }
