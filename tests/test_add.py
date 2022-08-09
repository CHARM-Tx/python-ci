from sample.main import add, main


def test_add_works():
    assert add(2, 7) == 9


def test_main_does_not_error():
    main()
