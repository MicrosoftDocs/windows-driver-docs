---
title: Porting a Driver from WDM to WDF
description: The topics in this section describe how to convert an existing WDM driver to a Kernel-Mode Driver Framework (KMDF) driver or a User-Mode Driver Framework (UMDF) version 2 driver.
ms.assetid: 3B4D677D-2FCC-45A1-95B4-DA9CA9D7B452
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting a Driver from WDM to WDF


The topics in this section describe how to convert an existing WDM driver to a Kernel-Mode Driver Framework (KMDF) driver or a User-Mode Driver Framework (UMDF) version 2 driver.

Architecturally, Windows Driver Frameworks (WDF) drivers are similar to WDM drivers. A WDM driver consists of a [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) function, various dispatch routines that the operating system calls to service I/O requests, and additional driver-specific utility functions. A WDF driver consists of a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff540807) function, various event callback functions that the framework calls to service I/O requests, and additional driver-specific utility functions. However, within this broad structure, the two models have important differences.

## In this section


-   [Which Drivers Can Be Ported and Where](which-drivers-can-be-ported.md)
-   [WDM Concepts for WDF Drivers](wdm-concepts-for-kmdf-drivers.md)
-   [Differences Between WDM and WDF](differences-between-wdm-and-kmdf.md)
-   [Preparing for Porting](general-guidelines-for-porting.md)
-   [Steps in Porting](how-to-port.md)
-   [Summary of KMDF and WDM Equivalents](summary-of-kmdf-and-wdm-equivalents.md)

 

 





