---
title: Porting a Driver from WDM to WDF
description: The topics in this section describe how to convert an existing WDM driver to a Kernel-Mode Driver Framework (KMDF) driver or a User-Mode Driver Framework (UMDF) version 2 driver.
ms.assetid: 3B4D677D-2FCC-45A1-95B4-DA9CA9D7B452
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Porting%20a%20Driver%20from%20WDM%20to%20WDF%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




