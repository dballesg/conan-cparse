# =============================================================================
# CParser
# =============================================================================
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

project(CParser VERSION 1.0 LANGUAGES CXX)

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/conanbuildinfo.cmake) #Clion, with conanbuildinfo.cmake in build folder
    include(${CMAKE_CURRENT_SOURCE_DIR}/conanbuildinfo.cmake)
else()
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) # Not CLion
endif()
conan_basic_setup()

# -----------------------------------------------------------------------------
# PROJECT CODE
# -----------------------------------------------------------------------------
# Get the *.cpp files from the code directory
file(GLOB_RECURSE ${PROJECT_NAME}_SOURCE_FILES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp")
# Get the *h and .hpp files from the code directory
file(GLOB_RECURSE ${PROJECT_NAME}_HEADERS_FILES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "${CMAKE_CURRENT_SOURCE_DIR}/*.h*")

# Prints the list of the project's found source code files.
message( STATUS "     Header Files:" )
foreach(hdrfileName ${${PROJECT_NAME}_HEADERS_FILES})
	MESSAGE(STATUS "        ${hdrfileName}")
endforeach(hdrfileName)	
message( STATUS "     Source Files:" )
foreach(srcfileName ${${PROJECT_NAME}_SOURCE_FILES})
	MESSAGE(STATUS "        ${srcfileName}")
endforeach(srcfileName)

add_library(${PROJECT_NAME} STATIC ${${PROJECT_NAME}_SOURCE_FILES} ${${PROJECT_NAME}_HEADERS_FILES})

# C++11 Standard
set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 11)