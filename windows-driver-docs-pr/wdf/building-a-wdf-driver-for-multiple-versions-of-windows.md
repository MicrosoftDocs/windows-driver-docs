---
title: Building a WDF driver for multiple versions of Windows
description: Describes how to buid a WDF driver for multiple versions of Windows.
ms.date: 04/06/2018
---

# Building a WDF driver for multiple versions of Windows

WDF has always allowed you to build a driver once and use the resulting binary on multiple versions of Windows, but before Windows 10 version 1803 (Redstone 4), this was limited to "build on older, run on newer." Starting in Windows 10 version 1803, WDF adds "build on newer, run on older," with the additional benefit of conditional execution. To summarize:
* **Existing**: Binaries built with older versions of the framework run on versions of Windows that include newer versions of the framework, provided major versions match. For example, a driver built with KMDF 1.9 (Windows 7) runs on a Windows 8 system (KMDF 1.11). In the example, the driver is limited to functionality of KMDF 1.9.
* **Added**: Starting in KMDF version 1.25 and UMDF version 2.25 on Windows 10 version 1803, you can build a driver with a newer framework version and the resulting driver binary runs on earlier versions of Windows (at minimum Windows 10 version 1803). In addition, the driver can conditionally use functionality that is only available in newer framework versions.

This means that not only does your driver run on future versions of Windows, as it always has, but it also runs on past versions, back to Windows 10 version 1803.

There are two steps to doing this: specifying build settings in Visual Studio, and performing a runtime check before invoking an API or accessing a structure or field that may or may not be present.

**Note**:
This feature is optional and a driver should only enable it to build a driver that uses the latest WDF functionality while remaining loadable on earlier versions of Windows that do not have the latest WDF functionality.

If you do not set **Version Minor (Target Version)** or **Version Minor (Minimum Required)**, versioning remains the same as before.

## Specifying Minimum Required

The new configuration settings in Visual Studio are:
* **KMDF Version Minor (Minimum Required)**
* **UMDF Version Minor (Minimum Required)**

In accordance with this change, the names of two existing settings were updated:
* **KMDF Version Minor** -> **KMDF Version Minor (Target Version)**
* **UMDF Version Minor** -> **UMDF Version Minor (Target Version)**

If you don't set **Minimum Required**, Visual Studio builds for **Target Version** and up, and does not provide downlevel support. This matches the behavior of the old **Version Minor** properties.

If you do set **Minimum Required**, the following requirements apply:
* 25 <= Minimum Required <= Target Version
* In **Configuration Properties->Driver Settings->General**, set `_NT_TARGET_VERSION` to `0x0A000005` (RS4) or later.

## Checking if functionality is present

Prior to every use of an API, structure, or member that may or may not be present, you must call one of the following macros, which are defined in WdfFuncEnum.h:

```cpp
BOOLEAN
WDF_IS_FUNCTION_AVAILABLE (
    FunctionName
    );

BOOLEAN
WDF_IS_STRUCTURE_AVAILABLE (
    StructName
    );

BOOLEAN
WDF_IS_FIELD_AVAILABLE (
    StructName,
    FieldName
    );
```

Consider the following example.  When WDF v29 is released, it adds a new API: **WdfSomeNewFeature**. If you set **Target Version** to 29 and **Minimum Required** to 25, the resulting driver loads on any framework version from 25 through 29 (and beyond, as long as major version doesn't change), calls version 25 APIs like before, and makes the following check before each call of any v29 API:

```cpp
if (WDF_IS_FUNCTION_AVAILABLE(WdfSomeNewFeature)) {
    WdfSomeNewFeature();
}
```

If you don't do the conditional check, you might see the following:
-	If the API returns NTSTATUS, the call returns a failure code.
-	If the API returns anything other than NTSTATUS:
    - KMDF: The machine bug checks.
    - UMDF: The WudfHost process crashes with a DriverStop error.
-	If Driver Verifier is enabled, the driver crashes as well. This helps to identify the problem in a test environment.
-   Silent memory corruption (when accessing a structure or field).

A driver crash contains the failed driver name, the framework name, and the failed API index. You can retrieve the name of API by looking up the value of WDFFUNCENUM in WdfFuncEnum.h.

For more info about Visual Studio properties for WDF, see [Driver Model Settings Properties for Driver Projects](../develop/driver-model-settings-properties-for-driver-projects.md).
