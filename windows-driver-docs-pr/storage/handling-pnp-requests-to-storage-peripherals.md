---
title: Handling PnP Requests to Storage Peripherals
description: Handling PnP Requests to Storage Peripherals
ms.assetid: 9c7ea576-11e6-46d7-b04c-ce412a0fc569
keywords:
- peripherals WDK storage , PnP requests
- storage peripherals WDK , PnP requests
- PnP WDK storage
- Plug and Play WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling PnP Requests to Storage Peripherals


## <span id="ddk_handling_pnp_requests_to_storage_peripherals_kg"></span><span id="DDK_HANDLING_PNP_REQUESTS_TO_STORAGE_PERIPHERALS_KG"></span>


A storage class driver's *DispatchPnP* routine is responsible for the following in response to PnP requests:

-   Starting its device in response to a start request (IRP\_MJ\_PNP with IRP\_MN\_START\_DEVICE). See [Handling PnP Start in a Storage Class Driver](handling-pnp-start-in-a-storage-class-driver.md).

-   Removing its device in response to a remove request (IRP\_MJ\_PNP with IRP\_MN\_REMOVE\_DEVICE). See [Storage Class Driver's RemoveDevice Routine](storage-class-driver-s-removedevice-routine.md).

-   If its device can contain the system paging file, maintaining a count of paging path notifications in its device extension in response to a paging-notification request (IRP\_MJ\_PNP with [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff550841)) and forwarding the request to the next-lower driver.

-   Handling query-remove and query-stop requests and, if the device contains the system paging file or hibernation file, failing such requests. A driver might also fail a query-remove request if its device is claimed for crash dump, because removing such a device disables crash dump.

The storage class driver forwards PnP query, cancel, and stop requests (except for failed query requests) to the next-lower driver.

 

 




