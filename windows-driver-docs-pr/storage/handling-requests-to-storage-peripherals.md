---
title: Handling Requests to Storage Peripherals
description: Handling Requests to Storage Peripherals
ms.assetid: 3859588e-fc39-4323-a901-8771874e64d2
keywords: ["storage class drivers WDK , peripherals", "class drivers WDK storage , peripherals", "peripherals WDK storage", "storage peripherals WDK", "peripherals WDK storage , about storage peripherals", "storage peripherals WDK , about storage peripherals"]
---

# Handling Requests to Storage Peripherals


## <span id="ddk_handling_requests_to_storage_peripherals_kg"></span><span id="DDK_HANDLING_REQUESTS_TO_STORAGE_PERIPHERALS_KG"></span>


For all requests that require the storage port driver to execute a request over an underlying bus, the class driver must set up an IRP with a SCSI request block (SRB) containing a SCSI command descriptor block (CDB). Consequently, most storage class drivers have one or more internal *BuildRequest* routines to build SRBs. For more information about such routines, see [Storage Class Driver's BuildRequest Routine](storage-class-driver-s-buildrequest-routine.md).

Storage class drivers also pass on IRP\_MJ\_SCSI requests to the underlying storage port driver. Such a request can originate from a [Storage Filter Drivers](storage-filter-drivers.md).

For [**IOCTL\_SCSI\_PASS\_THROUGH**](https://msdn.microsoft.com/library/windows/hardware/ff560519) requests, described in [Handling SCSI Pass-Through Requests](handling-scsi-pass-through-requests.md), the class driver is responsible for setting the **MinorFunction** code to IRP\_MJ\_DEVICE\_CONTROL in the port driver's I/O stack location of the IRP before passing the IRP\_MJ\_DEVICE\_CONTROL request on to the port driver with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

Every storage class driver is responsible for splitting up transfer requests (IRP\_MJ\_READ and/or IRP\_MJ\_WRITE) that exceed the underlying HBA's capabilities. Consequently, most class drivers also call an internal *SplitTransferRequest* routine, described in [Storage Class Driver's SplitTransferRequest Routine](storage-class-driver-s-splittransferrequest-routine.md), or implement the same functionality in their dispatch routines for read and write requests.

For additional information about handling requests to storage peripherals, see the following topics:

[Handling SCSI Pass-Through Requests](handling-scsi-pass-through-requests.md)

[Handling PnP Requests to Storage Peripherals](handling-pnp-requests-to-storage-peripherals.md)

[Handling Power Requests to Storage Peripherals](handling-power-requests-to-storage-peripherals.md)

[Queuing Storage Requests](queuing-storage-requests.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Handling%20Requests%20to%20Storage%20Peripherals%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




