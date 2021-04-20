---
title: Building IddCx 1.4 drivers
description: How to build IddCx version 1.4 indirect display drivers
ms.date: 09/28/2020
keywords:
- Building indirect display drivers, version 1.4
- Building IDDs, version 1.4
ms.localizationpriority: medium
---

# Building IddCx 1.4 drivers

Due to changes made in IddCx 1.3 for Windows 10 version 1809, an indirect display driver (IDD) built against IddCx v1.4 can run on Windows 10 version 1809 using runtime checks to verify whether DDI changes in IddCx 1.4 are available on that system. See [Building a WDF driver for multiple versions of Windows](../wdf/building-a-wdf-driver-for-multiple-versions-of-windows.md)
for more information.

Starting in IddCx 1.4, an IddCx driver can be built to install on Windows 10, version 1803 and later by doing the following. NOTE: this driver will not load on Windows 10, versions 1607 through 1709.

* Build and link the driver using the IddCx 1.4 headers and libraries from the [Windows Driver Kit](../download-the-wdk.md) (WDK).
* Set IDDCX_MINIMUM_VERSION_REQUIRED to 3 in the build environment. This tells the OS the minimum IddCx version that the driver was built for, 1.3 in this case.
* When initializing IddCx structures, use the corresponding *XXX*_INIT macro. For example, use the IDD_CX_CLIENT_CONFIG_INIT() macro to initialize an IDD_CX_CLIENT_CONFIG structure. The macro uses runtime code to set the Size field to the correct size for the IddCx version the driver is running on.
* Use the IDD_IS_FIELD_AVAILABLE() macro to determine whether a structure passed to the driver from IddCx has that field defined. NOTE: IddCx 1.4 did not extend any existing structures passed from IddCx to the driver so this macro does not need to be used in IddCx 1.4.
* Use the IDD_IS_FUNCTION_AVAILABLE() macro to determine whether a given IddCx function is available on the OS the driver is running on. For example, use IDD_IS_FUNCTION_AVAILABLE(IddCxAdapterSetRenderAdapter) to determine if IddCxAdapterSetRenderAdapter() is support on this OS.

The following table summarizes the IddCx versions supported by different OS releases.

| OS Version  | IddCx version shipped with OS | IddCx version of drivers that can run |
| ----------  | ----------------------------- | ----------------------------- |
| 1607 (RS1)  | 1.0  | 1.0 |
| 1703 (RS2)  | 1.0  | 1.0 |
| 1709 (RS3)  | 1.2  | 1.0 and 1.2 |
| 1803 (RS4)  | 1.3  | 1.0-1.3 and 1.4 above(*) |
| 1809 (RS5)  | 1.3  | 1.0-1.3 and 1.4 above(*) |
| 1903 (19H1) | 1.4  | 1.0-1.3 and 1.4 above(*) |
| 1909 (19H2) | 1.4  | 1.0-1.3 and 1.4 above(*) |
| 2004 (20H1) | 1.4  | 1.0-1.3 and 1.4 above(*) |
| N/A         | 1.6  | 1.0-1.3 and 1.4 above(*) |

**\*** An IddCx 1.4 and above IDD needs to use the dynamic macros such as IDD_IS_FUNCTION_AVAILABLE() in order to decide at runtime which OS functionality it can call. These dynamic macros are defined in *iddcx.h*.

To support all possible version of Windows:

* Write an IddCx 1.0 driver for Windows 10, versions 1607 through 1709.
* Write a single IddCx 1.4 or above driver for Windows 10, version 1803 and later.
