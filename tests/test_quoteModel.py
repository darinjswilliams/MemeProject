from src.QuoteEngine.QuoteModel import QuoteModel


class Test_QuoteModel:

    def setup_method(self, method):
        print(f'setup_method: {method.__name__}')
        self.body = None
        self.author = None
        self.quoteModel = QuoteModel(self.body, self.author)

    def test_quote_model(self):
        """Test to make sure we can create a quote model"""
        assert isinstance(self.quoteModel, QuoteModel)

    def test_quote_model_body(self):
        """Test to verify model name"""
        expected_name = self.quoteModel.__str__()
        assert expected_name == 'QuoteModel(None, None)'