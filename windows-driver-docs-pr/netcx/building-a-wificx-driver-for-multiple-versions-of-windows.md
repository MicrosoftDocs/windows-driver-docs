---
title: Building a WiFiCx driver for multiple versions of Windows
description: Describes how to build a WiFiCx driver for multiple versions of Windows.
ms.date: 03/31/2023
---

# Building a WiFiCx driver for multiple versions of Windows

WiFiCx allows you to build a driver once and use the resulting binary on multiple versions of Windows. Your driver can both run on future versions of Windows and  run on past versions, back to Windows 11, version 21H2.

To run your driver on older versions of Windows you must:
 
1. Specify the minimum version required.
1. Perform a runtime check before invoking an API or accessing a structure or field that may or may not be present.

**Note:** This feature is optional and a driver should only enable it to build a driver that uses the latest WiFiCx functionality while remaining loadable on earlier versions of Windows that do not have the latest WiFiCx functionality.


## WiFiCx version overview

| Operating system | KMDF version | Supported NetAdapterCx version | Supported WiFiCx version |
| --- | --- | --- | --- |
| Windows 11, versions 21H2 and 22H2 | 1.33 | 2.2 | Supports WiFiCx 1.0 |
| Windows 11 22H2, Moment 3 | 1.33 | 2.2+ | Supports WiFiCx 1.0, WiFiCx 1.1, WiFiCx 1.2 |


## Specify the minimum version required

IHVs have the choice to control the **WIFI_MINIMUM_VERSION_REQUIRED**. For example, to run your WiFiCx 1.1 or 1.2 version driver with WiFiCx 1.0, set **WIFI_MINIMUM_VERSION_REQUIRED** to **0**.

```cpp
C_DEFINES=$(C_DEFINES) -DRPC_NO_WINDOWS_H /DWIFI_MINIMUM_VERSION_REQUIRED=0
```


## Check if functionality is present

Prior to every use of an API, structure, or member that may or may not be present, you must call one of the following macros, which are defined in WifiFuncEnum.h:

```cpp
BOOLEAN
WIFI_IS_FUNCTION_AVAILABLE (
    FunctionName
    );

BOOLEAN
WIFI_IS_STRUCTURE_AVAILABLE (
    StructName
    );

BOOLEAN
WIFI_IS_FIELD_AVAILABLE (
    StructName,
    FieldName
    );
```

## NetAdapterCx version dependency

1. To load a WiFiCx-based driver on Windows 11, versions 21H2 and 22H2, the NetAdapterCx version has to be forced to **2.2**.
1. To load a WiFiCx-based driver on Windows 11 22H2, Moment 3 and later, the NetAdapterCx version has to be forced to **2.2+** (or use the latest version).
