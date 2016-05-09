---
title: Storage Class Driver's RemoveDevice Routine
author: windows-driver-content
description: Storage Class Driver's RemoveDevice Routine
ms.assetid: fbcbfbab-676a-43d3-aa63-0ea5e5f265d2
keywords: ["RemoveDevice", "query-remove requests WDK storage"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Class%20Driver's%20RemoveDevice%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


