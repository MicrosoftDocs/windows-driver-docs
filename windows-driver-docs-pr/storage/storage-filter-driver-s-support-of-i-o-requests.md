---
title: Storage Filter Driver's Support of I/O Requests
author: windows-driver-content
description: Storage Filter Driver's Support of I/O Requests
ms.assetid: 2899bf91-584f-47fe-9d5c-3feb07b8707e
keywords: ["storage filter drivers WDK , I/O request support", "filter drivers WDK storage , I/O request support", "SFD WDK storage , I/O request support", "IRPs WDK storage"]
---

# Storage Filter Driver's Support of I/O Requests


## <span id="ddk_storage_filter_driver_s_support_of_i_o_requests_kg"></span><span id="DDK_STORAGE_FILTER_DRIVER_S_SUPPORT_OF_I_O_REQUESTS_KG"></span>


A higher-level storage filter driver (SFD) intercepts IRPs from user applications and higher-level drivers and modifies them as needed before passing them to the next-lower driver (a storage class driver or another filter driver). Such an SFD supplies device-specific support for requests that require special handling, such as translating data sent to or returned from the device in a nonstandard format, or programming the device in response to an [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) request.

A lower-level SFD monitors SRBs and/or IRPs issued by a storage class driver and modifies them as needed before passing them to the next-lower driver (a storage port driver or another filter driver).

Both higher- and lower-level SFDs can let the lower drivers process all I/O requests that require no special handling.

Like a storage class driver, an SFD has the following requirements common to all higher-level kernel-mode drivers:

-   It must supply a set of *Dispatch* routines to which the I/O manager and/or still higher-level drivers can send IRPs for appropriate I/O operations. An SFD must support the same set of IRP\_MJ\_XXX as the storage class driver for its type of device.

-   For [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) requests, it must support as many of the class driver-supported I/O control codes as its physical device can handle and, if possible, emulate support for any remaining I/O control codes in the driver.

-   It must have a [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, an [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, an [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine, and *Dispatch* routines to handle PnP and power IRPs and can have any other standard higher-level driver routine, such as [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines, as necessary.

-   It must follow the rules for processing PnP, power management, and system control IRPs.

If its device has special features, an SFD can support a set of driver-defined I/O control codes in addition to the system-required set of device-type-specific I/O control codes for [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) requests.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Filter%20Driver's%20Support%20of%20I/O%20Requests%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


