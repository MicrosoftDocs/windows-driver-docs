---
title: Framework Device Object
author: windows-driver-content
description: Framework Device Object
ms.assetid: 6be47eac-d6e4-43d1-bf2d-d49dcb2273c0
keywords: ["UMDF objects WDK , device objects", "framework objects WDK UMDF , device objects", "device objects WDK UMDF", "IWDFDevice"]
---

# Framework Device Object


\[This topic applies to UMDF 1.*x*.\]

The framework device object is exposed to drivers by the [IWDFDevice](https://msdn.microsoft.com/library/windows/hardware/ff556917) interface. The framework device object is the framework representation of the device on the system. Each device object has a parent driver object.

When a new device arrives in the system, the framework calls the [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) method to notify the driver of the arrival and passes the [IWDFDriver](https://msdn.microsoft.com/library/windows/hardware/ff558893) and [IWDFDeviceInitialize](https://msdn.microsoft.com/library/windows/hardware/ff556965) interfaces in the call. The driver can call methods of the IWDFDeviceInitialize interface to initialize the new device. For example, the driver calls the [**IWDFDeviceInitialize::RetrieveDevicePropertyStore**](https://msdn.microsoft.com/library/windows/hardware/ff556982) method to query for the device information that is provided as part of device installation. The driver can then call the [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899) method to configure and create the device object.

When drivers create a framework device object, they can register their [IPnpCallback](https://msdn.microsoft.com/library/windows/hardware/ff556762), [IPnpCallbackSelfManagedIo](https://msdn.microsoft.com/library/windows/hardware/ff556776), [IPnpCallbackHardware](https://msdn.microsoft.com/library/windows/hardware/ff556764), [IFileCallbackCleanup](https://msdn.microsoft.com/library/windows/hardware/ff554902), and [IFileCallbackClose](https://msdn.microsoft.com/library/windows/hardware/ff554907) interfaces. The framework then notifies the driver when file cleanup and close and Plug and Play (PnP) and power management (PM) events occur. For more information about supporting PnP and PM, see [PnP and Power Management in UMDF-based Drivers](pnp-and-power-management-in-umdf-drivers.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Device%20Object%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




