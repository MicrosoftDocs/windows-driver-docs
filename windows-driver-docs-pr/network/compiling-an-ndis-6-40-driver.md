---
title: Compiling an NDIS 6.40 driver
description: This section explains how to compile an NDIS 6.40 driver
ms.date: 03/02/2023
---

# Compiling an NDIS 6.40 Driver


The WDK for Windows 8.1 supports header versioning. Header versioning makes sure that NDIS 6.40 drivers use the appropriate NDIS 6.40 data structures at compile time.

Add the following compiler settings to the Visual Studio project for your driver:

-   For a miniport driver, add NDIS640\_MINIPORT=1.

-   For a filter or protocol driver, add NDIS640=1.

For information on building a driver with the Windows 8.1 release of the WDK, see [Building a Driver](../develop/building-a-driver.md).

For information on converting an driver's build files to a Visual Studio project , see [Creating a Driver From Existing Source Files](../develop/creating-a-driver-from-existing-source-files.md).

 

