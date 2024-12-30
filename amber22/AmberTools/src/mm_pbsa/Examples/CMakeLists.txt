# install to full path inside AmberTools directory
install(DIRECTORY . USE_SOURCE_PERMISSIONS DESTINATION ${CMAKE_INSTALL_POSTFIX}AmberTools/src/mm_pbsa/Examples/ COMPONENT Tests ${TESTS_EXCLUDE_OPTION})
