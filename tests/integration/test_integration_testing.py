import pytest
from processing import remove_links,remove_hastags,remove_numbers,remove_users
from text_processing.text_preprocessor import TextPreprocessor

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Check out this #awesome link: http://example.com", "Check out this  link: "),
        ("No hashtags or links here!", "No hashtags or links here!"),
        (123, 123),  
    ],
)
def test_remove_hashtags_and_links(input_text, expected_output):
    processed_text = remove_hastags(remove_links(input_text))
    assert processed_text == expected_output
    
    
@pytest.mark.parametrize("input_text, expected_output", [
    ("Testing @user123 regex 456removal", "Testing  regex removal"),
    ("No changes needed", "No changes needed"),
    ("1234567890", ""),
    ("@user1 @user2 @user3", '  '),
])
def test_remove_numbers_and_users(input_text, expected_output):
    processed_text = remove_numbers(remove_users(input_text))
    assert processed_text == expected_output

##################################################

@pytest.mark.parametrize("text, expected", [
    ("running", "run"),
    ("jumps", "jump"),
    ("The cats are running in the garden", "the cat are run in the garden"),
    ("He jumps over tall buildings easily", "he jump over tall build easili"),
    ("They are playing in the playground", "they are play in the playground"),
])
def test_stem_and_lemmatize_integration(text, expected):
    preprocessor = TextPreprocessor(apply_stemming=True, apply_lemmatization=True)
    processed_text = preprocessor.stem_text(text)
    processed_text = preprocessor.lemmatize_text(processed_text)
    assert processed_text == expected