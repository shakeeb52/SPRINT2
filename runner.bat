cd C:\Users\Shakib\PycharmProjects\SPRINT2
behave -f allure_behave.formatter:AllureFormatter -o ./allure_reports ./features
behave --junit --junit-directory jreports features/flipkart.feature
behave -f json.pretty -o JSON_REPORTS features/flipkart.feature