from presidio_analyzer import AnalyzerEngine, PatternRecognizer
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import AnonymizerConfig
# text: "His name is Mr. Jones and his phone number is 212-555-5555 and 212-555-4444"

text_to_anonymize = input("")

class PII():
    def get_2_phone_numbers(self,text):
        analyzer = AnalyzerEngine()
        analyzer_results = analyzer.analyze(text=text, entities=["PHONE_NUMBER"], language='en')
        titles_recognizer = PatternRecognizer(supported_entity="TITLE",deny_list=["Mr.","Mrs.","Miss"])

        print(analyzer_results)

        analyzer.registry.add_recognizer(titles_recognizer)

        analyzer_results = analyzer.analyze(text=text,
        entities=["TITLE"],
        language="en")
        print(analyzer_results)

        analyzer_results = analyzer.analyze(text=text, language='en')

        anonymizer = AnonymizerEngine()

        anonymized_results = anonymizer.anonymize(
            text=text,
            analyzer_results=analyzer_results,    
            anonymizers_config={"DEFAULT": AnonymizerConfig("replace", {"new_value": "<ANONYMIZED>"}), 
                                "PHONE_NUMBER": AnonymizerConfig("mask", {"type": "mask", "masking_char" : "*", "chars_to_mask" : 12, "from_end" : True}),
                                "TITLE": AnonymizerConfig("redact", {})}
        )

        print(anonymized_results)


pii = PII()
pii.get_2_phone_numbers(text_to_anonymize)