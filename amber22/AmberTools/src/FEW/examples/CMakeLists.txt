
# these files get used as datafiles for FEW after they're installed
install(DIRECTORY command_files input_info DESTINATION ${PERL_MODULE_INSTALL_DIR}/FEW_libs/)

# install to full path inside AmberTools directory
install(DIRECTORY . USE_SOURCE_PERMISSIONS DESTINATION ${CMAKE_INSTALL_POSTFIX}AmberTools/src/FEW/examples COMPONENT Tests ${TESTS_EXCLUDE_OPTION})