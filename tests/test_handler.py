import unittest
import lambda_function


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        event={'Country':'USA'}
        result = lambda_function.lambda_handler(event, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Hello from '+event['Country'], result['body'])
        event={
            "slots": {
                "number": "1",
                "salon": "A201",
                "producto": "Pizza",
                "bebida": "Agua",
                "tarjeta": "515930483000957"
            }
        }
        result = lambda_function.lambda_handler(event, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn("Gracias por su orden de " + event['amount'] + " " + event['product'] + " al salon " + event['salon'], result['content'])
        # self.assertIn('Hello from '+event['Country'], result['body'])

if __name__ == '__main__':
    unittest.main()