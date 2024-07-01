# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_robotie_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED robotie_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(robotie_FOUND FALSE)
  elseif(NOT robotie_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(robotie_FOUND FALSE)
  endif()
  return()
endif()
set(_robotie_CONFIG_INCLUDED TRUE)

# output package information
if(NOT robotie_FIND_QUIETLY)
  message(STATUS "Found robotie: 0.0.0 (${robotie_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'robotie' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${robotie_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(robotie_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${robotie_DIR}/${_extra}")
endforeach()
