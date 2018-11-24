---
title: Compiling an NDIS 6.40 driver
description: This section explains how to compile an NDIS 6.40 driver
ms.assetid: AF027939-06C7-435C-90D9-82272CED6A84
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Compiling an NDIS 6.40 Driver


The WDK for Windows 8.1 supports header versioning. Header versioning makes sure that NDIS 6.40 drivers use the appropriate NDIS 6.40 data structures at compile time.

Add the following compiler settings to the Visual Studio project for your driver:

-   For a miniport driver, add NDIS640\_MINIPORT=1.

-   For a filter or protocol driver, add NDIS640=1.

For information on building a driver with the Windows 8.1 release of the WDK, see [Building a Driver](https://msdn.microsoft.com/windows-drivers/develop/building_a_driver).

For information on converting an driver's build files to a Visual Studio project , see [Creating a Driver From Existing Source Files](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_from_existing_source_files).

 

 





