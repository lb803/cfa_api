"""Unit test cases for the Ratings Analyser module"""
import pytest

from cfa_api.lib.keyword_extractor import BonkersKeywordExtractor


@pytest.mark.parametrize("text,limit,expected_result",
                         [("apple apple apple grapes grapes pears", 3,
                           ["apple", "grapes", "pears"]),
                          ("apple apple apple grapes grapes pears", 1,
                           ["apple"]),
                          ("apple apple apple grapes grapes pears", 5,
                           ["apple", "grapes", "pears"]),
                          ])
def test_bonkers_keyword_extractor_valid_input(text: str, limit: int,
                                               expected_result: list[str]) -> None:
    extractor = BonkersKeywordExtractor()
    extracted_words = extractor.extract_keywords(text, limit)

    assert extracted_words == expected_result


@pytest.mark.parametrize("text,limit",
                         [("apple grapes pears coconut mango", 2),
                          ("apple grapes pears coconut mango mango", 2)])
def test_bonkers_keyword_extractor_text_gt_limit(text: str, limit: int) -> None:
    extractor = BonkersKeywordExtractor()
    extracted_words = extractor.extract_keywords(text, limit)

    assert len(extracted_words) == limit


@pytest.mark.parametrize("text,limit",
                         [("apple grapes", 5),
                          ("", 5)])
def test_bonkers_keyword_extractor_text_lt_limit(text: str, limit: int) -> None:
    extractor = BonkersKeywordExtractor()
    extracted_words = extractor.extract_keywords(text, limit)

    assert len(extracted_words) == len(text.split())
