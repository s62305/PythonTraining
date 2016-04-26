# Initialization, command line and configuration hooks:
pytest_load_initial_conftests
pytest_cmdline_preparse(config, args)
pytest_cmdline_parse(pluginmanager, args)
pytest_namespace()
pytest_addoption(parser)
pytest_cmdline_main(config)
pytest_configure(config)
pytest_unconfigure(config)

# Collection hooks:
pytest_ignore_collect(path, config)
pytest_collect_directory(path, parent)
pytest_collect_file(path, parent)
pytest_pycollect_makeitem(collector, name, obj)
pytest_generate_tests(metafunc)
pytest_collection_modifyitems(session, config, items)

# Reporting hooks:
pytest_collectstart(collector)
pytest_itemcollected(item)
pytest_collectreport(report)
pytest_deselected(items)
pytest_report_header(config, startdir)
pytest_report_teststatus(report)
pytest_terminal_summary(terminalreporter)
pytest_runtest_logreport(report)
pytest_assertrepr_compare(config, op, left, right)

# Debugging/Interaction hooks:
pytest_internalerror(excrepr, excinfo)
pytest_keyboard_interrupt(excinfo)
pytest_exception_interact(node, call, report)
pytest_enter_pdb(config)