---
title: Handling PnP Requests to Storage Peripherals
description: Handling PnP Requests to Storage Peripherals
ms.assetid: 9c7ea576-11e6-46d7-b04c-ce412a0fc569
keywords: ["peripherals WDK storage , PnP requests", "storage peripherals WDK , PnP requests", "PnP WDK storage", "Plug and Play WDK storage"]
---

# Handling PnP Requests to Storage Peripherals


## <span id="ddk_handling_pnp_requests_to_storage_peripherals_kg"></span><span id="DDK_HANDLING_PNP_REQUESTS_TO_STORAGE_PERIPHERALS_KG"></span>


A storage class driver's *DispatchPnP* routine is responsible for the following in response to PnP requests:

-   Starting its device in response to a start request (IRP\_MJ\_PNP with IRP\_MN\_START\_DEVICE). See [Handling PnP Start in a Storage Class Driver](handling-pnp-start-in-a-storage-class-driver.md).

-   Removing its device in response to a remove request (IRP\_MJ\_PNP with IRP\_MN\_REMOVE\_DEVICE). See [Storage Class Driver's RemoveDevice Routine](storage-class-driver-s-removedevice-routine.md).

-   If its device can contain the system paging file, maintaining a count of paging path notifications in its device extension in response to a paging-notification request (IRP\_MJ\_PNP with [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff550841)) and forwarding the request to the next-lower driver.

-   Handling query-remove and query-stop requests and, if the device contains the system paging file or hibernation file, failing such requests. A driver might also fail a query-remove request if its device is claimed for crash dump, because removing such a device disables crash dump.

The storage class driver forwards PnP query, cancel, and stop requests (except for failed query requests) to the next-lower driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Handling%20PnP%20Requests%20to%20Storage%20Peripherals%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




