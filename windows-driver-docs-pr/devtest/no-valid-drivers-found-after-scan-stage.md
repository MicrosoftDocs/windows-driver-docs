---
title: No Valid Drivers found after Scan Stage
description: No Valid Drivers found after Scan Stage
ms.assetid: aaf4f39b-82ab-40c3-ac49-5a20c8796051
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# No Valid Drivers found after Scan Stage


This error indicates a general failure to verify the driver. SDV reports this error in the following situations:

-   SDV reports this error when it cannot interpret the driver code, typically because a driver is not WDM-compliant or KMDF-compliant or it is not written in C. For more information, see [Supported Drivers](supported-drivers.md).

-   SDV reports this error when it is not run in the correct build configuration or platform, or if, for some other reason, SDV did not find or did not compile and build the driver's source files.

-   SDV reports this error when it cannot detect any entry points in the driver. To verify that SDV found the entry points that the driver supports, see the [Sdv-map.h](sdv-map-h.md). For information, see [Scanning the Driver](scanning-the-driver.md).

To identify the problem, verify that you have selected the correct build configuration and platform for your driver.

Next, to confirm that the driver compiles and builds correctly. Next, correct any compiler errors and run SDV again.

For information about the Build and Scan steps, see [Verification Process](verification-process.md).

 

 





