---
title: Porting WMI
description: Porting WMI
ms.assetid: 10843A15-3F6F-4DB5-A43B-4D9964DD3312
---

# Porting WMI


\[Applies to KMDF only\]

An [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813) request represents a request for WMI data. WDM drivers handle such requests by implementing a [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412) function and registering as a WMI data provider. WDM drivers that do not respond to such requests implement a *DispatchSystemControl* routine that simply passes the IRPs down to the next lower driver.

For KMDF drivers, the framework provides default handling for [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813). Drivers that do not provide WMI data are not required to include any WMI-related code. Instead, the framework passes the request to the next lower driver on behalf of the driver.

For implementation details, see [Supporting WMI in KMDF Drivers](supporting-wmi-in-kmdf-drivers.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Porting%20WMI%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




