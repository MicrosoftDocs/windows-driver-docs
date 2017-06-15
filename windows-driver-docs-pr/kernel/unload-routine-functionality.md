---
title: Unload Routine Functionality
author: windows-driver-content
description: Unload Routine Functionality
MS-HAID:
- 'DrvComps\_f97832d2-ad12-47f9-9ac7-0158f96eac25.xml'
- 'kernel.unload\_routine\_functionality'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a36b4687-df1d-498f-b9f3-d13ae2a9a3cd
keywords: ["Unload routines WDK kernel , functionality"]
---

# Unload Routine Functionality


## <a href="" id="ddk-unload-routine-functionality-kg"></a>


The responsibilities of a driver's [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine depend on whether the driver supports PnP or not.

Just as the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routines of PnP drivers are usually simple, so are their *Unload* routines, as described in [A PnP Driver's Unload Routine](pnp-driver-s-unload-routine.md).

A non-PnP driver's *Unload* routine must free device objects and release driver-allocated resources. In short, it must undo the work performed by its corresponding **DriverEntry** and [*Reinitialize*](https://msdn.microsoft.com/library/windows/hardware/ff561022) routines in initializing the driver, its devices, and its resources. See [A Non-PnP Driver's Unload Routine](non-pnp-driver-s-unload-routine.md) for details.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Unload%20Routine%20Functionality%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


