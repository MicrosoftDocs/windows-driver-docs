---
title: Storage Class Driver's RemoveDevice Routine
description: Storage Class Driver's RemoveDevice Routine
ms.assetid: fbcbfbab-676a-43d3-aa63-0ea5e5f265d2
keywords:
- RemoveDevice
- query-remove requests WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Class Driver's RemoveDevice Routine


## <span id="ddk_storage_class_drivers_removedevice_routine_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_REMOVEDEVICE_ROUTINE_KG"></span>


When a device is about to be removed, the PnP manager first calls the class driver's [**DispatchPnP**](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine with a PnP query-remove request (IRP\_MJ\_PNP with [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705). The storage class driver should fail the query-remove request in any of the following cases:

-   The device contains the system paging file or hibernation file.

-   The driver is running a long operation which should not be canceled (for example, rewinding or formatting a tape).

-   There are outstanding handles to the device (CREATEs).

The storage class driver might also fail a query-remove request if the device is claimed for crash dump, because removing such a device disables crash dump.

If the storage class driver returns STATUS\_SUCCESS in response to a query-remove request, the PnP manager then calls the class driver's *DispatchPnP* routine with a PnP remove request (IRP\_MJ\_PNP with [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738)). The storage class driver's *DispatchPnP* routine either calls an internal *RemoveDevice* routine or implements the same functionality inline.

A storage class driver's *RemoveDevice* routine must do the following:

-   Release any outstanding resources, such as memory or events, allocated by the driver.

-   Delete symbolic links, if any, created by the driver.

-   Delete the device object (FDO).

-   Forward the request to the next-lower driver.

If the storage class driver created PDOs at startup (for example, to represent partitions on a partitioned media device), such PDOs have already been removed when the PnP manager sends the remove request to the storage class driver.

Even after a device object has been deleted, if it has a nonzero reference count the device object persists in the system until its reference count reaches zero, then disappears silently. A storage class driver must not attempt to use the device object pointer after the device object has been deleted.

For more information about handling a remove request, see [Removing a Device](https://msdn.microsoft.com/library/windows/hardware/ff561046).

 

 




