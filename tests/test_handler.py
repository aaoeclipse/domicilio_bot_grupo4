import unittest
import lambda_function


class TestHandlerCase(unittest.TestCase):

    def test_correr_una_orden_de_pizza_con_agua(self):
        event={
            "currentIntent": {
            "slots": {
                "number": "1",
                "salon": "A201",
                "producto": "Pizza",
                "bebida": "Agua",
                "tarjeta": "515930483000957"
                }
            }
        }
        
        result = lambda_function.lambda_handler(event, None)
        print(result)
        # self.assertEqual(result['statusCode'], 200)
        # self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn("Gracias por su orden de " + event['currentIntent']['slots']['number'] + " " + event['currentIntent']['slots']['producto'] + " al salon " + event['currentIntent']['slots']['salon'], result['dialogAction']['message']['content'])
        # self.assertIn('Hello from '+event['Country'], result['body'])

    def test_error_en_tarjeta(self):
        event={
            "currentIntent": {
            "slots": {
                "number": "1",
                "salon": "A201",
                "producto": "Pizza",
                "bebida": "Agua",
                "tarjeta": "12312"
                }
            }
        }
        result = lambda_function.lambda_handler(event, None)

        # self.assertEqual(result['statusCode'], 400)
        # self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn("Lamentablemente no se logro procesar la orden. Favor verificar el numero de tarjeta", result['dialogAction']['message']['content'])



if __name__ == '__main__':
    unittest.main()