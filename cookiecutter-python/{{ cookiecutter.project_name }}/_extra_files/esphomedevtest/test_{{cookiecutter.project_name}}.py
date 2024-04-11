def test_component(generate_main):
    """
    When the device_class of sensor is set in the yaml file, it should be registered in main
    """
    # Given

    # When
    main_cpp = generate_main("tests/component_tests/test_{{ cookiecutter,project_name }}.yaml")

    # Then
    assert 's_1->set_device_class("voltage");' in main_cpp