---
title: Handling SCSI Pass-Through Requests
description: Handling SCSI Pass-Through Requests
keywords:
- peripherals WDK storage , SCSI pass-through requests
- storage peripherals WDK , SCSI pass-through requests
- SCSI pass-through requests WDK storage
- pass-through requests WDK storage
ms.date: 04/20/2017
---

# Handling SCSI Pass-Through Requests


## <span id="ddk_handling_scsi_pass_through_requests_kg"></span><span id="DDK_HANDLING_SCSI_PASS_THROUGH_REQUESTS_KG"></span>


A class driver that generates an [**IOCTL\_SCSI\_PASS\_THROUGH**](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) request or an [**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through_direct) request is responsible for the following:

-   Setting the length of the user buffer at **Parameters.DeviceIoControl.InputBufferLength** to at least **sizeof**(SCSI\_PASS\_THROUGH) or **sizeof**(SCSI\_PASS\_THROUGH\_DIRECT)

-   Setting up the storage port driver's I/O stack location as usual

-   Setting the **MinorFunction** in the IRP to IRP\_MJ\_DEVICE\_CONTROL, which marks the request as having been processed by a storage class driver.

On receipt of an IOCTL\_SCSI\_PASS\_THROUGH or IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT request from a higher-level driver, a storage class driver's [**DispatchDeviceControl**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine is responsible for checking the validity of the embedded SCSI command (CDB) and, if the command is valid for its device, sending the request to the storage port driver.

If the port driver's I/O stack location for an IOCTL\_SCSI\_PASS\_THROUGH or IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT request does not have its **MinorFunction** field set with IRP\_MJ\_DEVICE\_CONTROL, the port driver assumes the request came directly from an application and that no class driver exists for the target device type. It is an application error to send such a request directly to the port driver for a device that has been claimed by a storage class driver.

The port driver does not check the validity of the SCSI command embedded in such a pass-through request.

 

