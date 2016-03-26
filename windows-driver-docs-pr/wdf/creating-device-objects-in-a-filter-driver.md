---
title: Creating Device Objects in a Filter Driver
description: Creating Device Objects in a Filter Driver
ms.assetid: f5a4851d-7caf-467d-9500-11f341fdf680
keywords: ["PnP WDK KMDF , filter drivers", "Plug and Play WDK KMDF , filter drivers", "power management WDK KMDF , filter drivers", "filter drivers WDK KMDF", "filter DOs WDK KMDF"]
---

# Creating Device Objects in a Filter Driver


Each [filter driver](https://msdn.microsoft.com/library/windows/hardware/ff545890) creates a framework device object for each of its supported devices that exists on the system. Because these device objects are created by filter drivers, they are called filter device objects (Filter DOs). Each Filter DO is a filter driver's representation of a device.

Filter drivers, like function drivers, provide an [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function that receives a handle to a [**WDFDEVICE\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure. The driver can call the same set of [framework device object initialization methods](https://msdn.microsoft.com/library/windows/hardware/dn265631#device-init-methods) that function drivers call to store information in the WDFDEVICE\_INIT structure. Like function drivers, filter drivers can also call [framework FDO initialization methods](https://msdn.microsoft.com/library/windows/hardware/dn265631#fdo-init-methods).

A small number of filter drivers enumerate child software-only devices. Such filter drivers can call [framework PDO initialization methods](https://msdn.microsoft.com/library/windows/hardware/dn265631#pdo-init-methods).

Filter drivers must call [**WdfFdoInitSetFilter**](https://msdn.microsoft.com/library/windows/hardware/ff547273).

The final step in creating a device object is to call [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Creating%20Device%20Objects%20in%20a%20Filter%20Driver%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




