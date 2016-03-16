---
title: Adding a Device
description: Adding a Device
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 233e3315-3044-42d7-867c-0a9e153eb53b
keywords: ["User Mode Driver Framework WDK adding devices", "UMDF WDK adding devices", "user mode drivers WDK UMDF adding devices", "installing devices WDK UMDF", "adding devices WDK UMDF"]
---

# Adding a Device


\[This topic applies to UMDF 1.*x*.\]

The framework adds a device object for each device loaded in the driver host process. To add the device, the framework calls the driver's [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) method and passes the [IWDFDriver](https://msdn.microsoft.com/library/windows/hardware/ff558893) and [IWDFDeviceInitialize](https://msdn.microsoft.com/library/windows/hardware/ff556965) interfaces in the call. The supplied **IWDFDeviceInitialize** interface is only valid before the driver calls [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899). The driver can call the following methods of **IWDFDeviceInitialize** to perform the following operations:

-   The driver calls the [**IWDFDeviceInitialize::RetrieveDevicePropertyStore**](https://msdn.microsoft.com/library/windows/hardware/ff556982) method to retrieve the [IWDFNamedPropertyStore](https://msdn.microsoft.com/library/windows/hardware/ff560164) interface for the device property store. The driver can use **IWDFNamedPropertyStore** to retrieve and set properties for the device.

-   The driver calls the [**IWDFDeviceInitialize::SetLockingConstraint**](https://msdn.microsoft.com/library/windows/hardware/ff556991) method to specify how its callback functions are called by the framework.

-   The driver calls the [**IWDFDeviceInitialize::SetFilter**](https://msdn.microsoft.com/library/windows/hardware/ff556985) method to enable the device as a filter device.

After the driver uses [IWDFDeviceInitialize](https://msdn.microsoft.com/library/windows/hardware/ff556965) to initialize the device, the driver passes a pointer to **IWDFDeviceInitialize** in a call to the [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899) method to create a [UMDF device object](framework-device-object.md) for the device. After the framework device object is created, the driver makes calls to the [**IWDFDevice::CreateIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff557020) method to create read and write I/O queues. In these **IWDFDevice::CreateIoQueue** calls, the driver must identify how it receives requests from the I/O queue. For more information, see [Configuring Dispatch Mode for an I/O Queue](configuring-dispatch-mode-for-an-i-o-queue.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Adding%20a%20Device%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




