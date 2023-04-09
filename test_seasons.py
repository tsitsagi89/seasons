import seasons
from datetime import date
import pytest


def main():
    test_birthdate()
    test_birthdate_system_exit()
    test_getWords()

def test_birthdate():
    assert seasons.get_birthdate("1989-04-03") == (date.today() - date(1989, 4, 3)).days * 24 * 60

def test_birthdate_system_exit():
    with pytest.raises(SystemExit) as e:
        seasons.get_birthdate("03.04.1989")
    assert e.type == SystemExit
    assert e.value.code == "Invalid date"

def test_getWords():
    assert seasons.getWords(17890560) == 'Seventeen Million Eight Hundred Ninety Thousand Five Hundred Sixty'
    assert seasons.getWords(1) == 'One'


if __name__ == "__main__":
    main()