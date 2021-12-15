---
title: Setting Up a Storage Class Driver's Device Extension
description: Setting Up a Storage Class Driver's Device Extension
keywords:
- storage class drivers WDK , device extensions
- class drivers WDK storage , device extensions
- device extensions WDK storage
ms.date: 04/20/2017
---

# Setting Up a Storage Class Driver's Device Extension


## <span id="ddk_setting_up_a_storage_class_drivers_device_extension_kg"></span><span id="DDK_SETTING_UP_A_STORAGE_CLASS_DRIVERS_DEVICE_EXTENSION_KG"></span>


In the [Device Extensions](../kernel/device-extensions.md) of each device object created by a storage class driver, that driver provides storage for whatever driver-determined data it uses to manage I/O requests for the device, such as the pointer to the PDO passed to [**AddDevice**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device), the pointer to the device object returned by [**IoAttachDeviceToDeviceStack**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack), a back pointer to its own device object, and so forth.

Most storage class drivers also provide storage for the following information:

-   A device-type-specific time-out value

    The class driver can pass the time-out value in SRBs it sends to the port driver, which times SRB\_FUNCTION\_EXECUTE\_SCSI requests (see [**SCSI\_REQUEST\_BLOCK**](/windows-hardware/drivers/ddi/srb/ns-srb-_scsi_request_block)) on behalf of each class driver. The port driver returns an SRB with its **SrbStatus** member set to SRB\_STATUS\_TIMEOUT if the interval between when the port driver sends the request to the underlying driver and when the request completes exceeds the specified time-out value.

-   A pointer to the class driver's error-handling routine

    See [Storage Class Driver's IoCompletion Routines](storage-class-driver-s-iocompletion-routines.md) for more information about error-handling in storage class drivers.

-   A count that the driver maintains of bus protocol errors on the device

-   A pointer to a driver-allocated buffer for sense data

    A class driver must allocate memory for returned sense data from cache-aligned, nonpaged pool. For more information about allocating memory for driver buffers, see [Allocating System-Space Memory](../kernel/allocating-system-space-memory.md).

-   A driver-determined default value for **SrbFlags** that the class driver sets in SRBs

-   A pointer to a lookaside list header if the driver sets up a lookaside list for the SRBs it allocates

    See [Using Lookaside Lists](../kernel/using-lookaside-lists.md) for more information.

-   Pointers to an IRP and an SRB allocated and held in reserve for requests that must succeed even in low memory conditions, for paging operations as well as error recovery operations (such as those performed by a [Storage Class Driver's ReleaseQueue Routine](storage-class-driver-s-releasequeue-routine.md))

-   A pointer to the [**STORAGE\_ADAPTER\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_adapter_descriptor) and [**STORAGE\_DEVICE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_device_descriptor) data that the port driver collected from the HBA

    For information about how class drivers get and use this data, see [Storage Class Driver's GetDescriptor Routine](storage-class-driver-s-getdescriptor-routine.md).

-   Flags that indicate the previous and current PnP state, to manage transitions between states on the device

-   A flag that indicates the current device power state, to avoid extra work in handling redundant power requests

-   A count of system paging files, if any, on the device, based on paging-notification requests received by the driver (IRP\_MJ\_PNP with [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](../kernel/irp-mn-device-usage-notification.md))

A storage class driver cannot send requests to its device through the storage port driver without using the device object pointer that was returned by [**IoAttachDeviceToDeviceStack**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack) and stored in the device extension by the driver's *AddDevice* routine.

 

