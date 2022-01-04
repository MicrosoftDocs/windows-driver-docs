---
title: Compiling an NDIS 6.30 driver
description: This section explains how to compile an NDIS 6.30 driver
ms.date: 04/20/2017
---

# Compiling an NDIS 6.30 Driver


In the Windows 8 release of the Windows Driver Kit (WDK), the driver development environment is integrated into Visual Studio. Most of the tools you need for coding, building, testing, debugging, deploying, and releasing a driver are available in the Visual Studio user interface. This is a departure from previous releases of the WDK where the various stages of the driver life cycle were performed as separate tasks with stand-alone tools.

The WDK for Windows 8 supports header versioning. Header versioning makes sure that NDIS 6.30 drivers use the appropriate NDIS 6.30 data structures at compile time. Add the following compiler settings to the Visual Studio project for your driver:

-   For a miniport driver, add NDIS630\_MINIPORT=1.

-   For a filter or protocol driver, add NDIS630=1.

For information on building a driver with the Windows 8 release of the WDK, see [Building a Driver](../develop/building-a-driver.md).

For information on converting an driver's build files to a Visual Studio project , see [Creating a Driver From Existing Source Files](/windows-hardware/drivers).

 

