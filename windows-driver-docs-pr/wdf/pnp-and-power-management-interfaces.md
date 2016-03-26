---
title: PnP and Power Management Interfaces
description: PnP and Power Management Interfaces
ms.assetid: b80228f7-50be-4551-870b-2d7e2b5db239
keywords: ["Plug and Play WDK UMDF , power management interfaces", "PnP WDK UMDF , power management interfaces", "power management WDK UMDF , interfaces"]
---

# PnP and Power Management Interfaces


\[This topic applies to UMDF 1.*x*.\]

When a new device arrives in the system, the framework calls the [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) method to notify the UMDF driver of the arrival and passes the [**IWDFDriver**](https://msdn.microsoft.com/library/windows/hardware/ff558893) and [**IWDFDeviceInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff556965) interfaces in the call. The driver calls the [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899) method to create a framework device object for the device.

When drivers create a framework device object, they can register the following interfaces so that the framework notifies the driver—by calling the methods associated with the interfaces—when Plug and Play (PnP) and power management (PM) events occur.

[**IPnpCallback**](https://msdn.microsoft.com/library/windows/hardware/ff556762)

[**IPnpCallbackSelfManagedIo**](https://msdn.microsoft.com/library/windows/hardware/ff556776)

[**IPnpCallbackHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556764)

[**IPowerPolicyCallbackWakeFromS0**](https://msdn.microsoft.com/library/windows/hardware/ff556815)

[**IPowerPolicyCallbackWakeFromSx**](https://msdn.microsoft.com/library/windows/hardware/ff556825)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20PnP%20and%20Power%20Management%20Interfaces%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




