import pytest
from selene import browser, be, have


def test_positive_search():
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').type('fc barcelona').press_enter()
    browser.element('[href="FC Barcelona website"]')

def test_negative_search():
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').type('34555555555555555555555555555555555555555555555555555555555555555555555555').press_enter()
    browser.element('html').should(have.text('ничего не найдено'))

