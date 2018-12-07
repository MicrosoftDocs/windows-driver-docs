---
title: Handling Requests to Storage Peripherals
description: Handling Requests to Storage Peripherals
ms.assetid: 3859588e-fc39-4323-a901-8771874e64d2
keywords:
- storage class drivers WDK , peripherals
- class drivers WDK storage , peripherals
- peripherals WDK storage
- storage peripherals WDK
- peripherals WDK storage , about storage peripherals
- storage peripherals WDK , about storage peripherals
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




