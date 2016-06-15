---
title: Setting Up a Storage Class Driver's Device Extension
author: windows-driver-content
description: Setting Up a Storage Class Driver's Device Extension
ms.assetid: 9d050d23-39c0-406e-9f4b-2e95d388f5cf
keywords: ["storage class drivers WDK , device extensions", "class drivers WDK storage , device extensions", "device extensions WDK storage"]
---

# Setting Up a Storage Class Driver's Device Extension


## <span id="ddk_setting_up_a_storage_class_drivers_device_extension_kg"></span><span id="DDK_SETTING_UP_A_STORAGE_CLASS_DRIVERS_DEVICE_EXTENSION_KG"></span>


In the [Device Extensions](https://msdn.microsoft.com/library/windows/hardware/ff543119) of each device object created by a storage class driver, that driver provides storage for whatever driver-determined data it uses to manage I/O requests for the device, such as the pointer to the PDO passed to [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521), the pointer to the device object returned by [**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300), a back pointer to its own device object, and so forth.

Most storage class drivers also provide storage for the following information:

-   A device-type-specific time-out value

    The class driver can pass the time-out value in SRBs it sends to the port driver, which times SRB\_FUNCTION\_EXECUTE\_SCSI requests (see [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393)) on behalf of each class driver. The port driver returns an SRB with its **SrbStatus** member set to SRB\_STATUS\_TIMEOUT if the interval between when the port driver sends the request to the underlying driver and when the request completes exceeds the specified time-out value.

-   A pointer to the class driver's error-handling routine

    See [Storage Class Driver's IoCompletion Routines](storage-class-driver-s-iocompletion-routines.md) for more information about error-handling in storage class drivers.

-   A count that the driver maintains of bus protocol errors on the device

-   A pointer to a driver-allocated buffer for sense data

    A class driver must allocate memory for returned sense data from cache-aligned, nonpaged pool. For more information about allocating memory for driver buffers, see [Allocating System-Space Memory](https://msdn.microsoft.com/library/windows/hardware/ff540588).

-   A driver-determined default value for **SrbFlags** that the class driver sets in SRBs

-   A pointer to a lookaside list header if the driver sets up a lookaside list for the SRBs it allocates

    See [Using Lookaside Lists](https://msdn.microsoft.com/library/windows/hardware/ff565416) for more information.

-   Pointers to an IRP and an SRB allocated and held in reserve for requests that must succeed even in low memory conditions, for paging operations as well as error recovery operations (such as those performed by a [Storage Class Driver's ReleaseQueue Routine](storage-class-driver-s-releasequeue-routine.md))

-   A pointer to the [**STORAGE\_ADAPTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566346) and [**STORAGE\_DEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566971) data that the port driver collected from the HBA

    For information about how class drivers get and use this data, see [Storage Class Driver's GetDescriptor Routine](storage-class-driver-s-getdescriptor-routine.md).

-   Flags that indicate the previous and current PnP state, to manage transitions between states on the device

-   A flag that indicates the current device power state, to avoid extra work in handling redundant power requests

-   A count of system paging files, if any, on the device, based on paging-notification requests received by the driver (IRP\_MJ\_PNP with [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff550841))

A storage class driver cannot send requests to its device through the storage port driver without using the device object pointer that was returned by [**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300) and stored in the device extension by the driver's *AddDevice* routine.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Setting%20Up%20a%20Storage%20Class%20Driver's%20Device%20Extension%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


