---
title: Handling SCSI Pass-Through Requests
author: windows-driver-content
description: Handling SCSI Pass-Through Requests
ms.assetid: 61f8dc02-b5ae-4be5-b7e1-d8207304ef7c
keywords: ["peripherals WDK storage , SCSI pass-through requests", "storage peripherals WDK , SCSI pass-through requests", "SCSI pass-through requests WDK storage", "pass-through requests WDK storage"]
---

# Handling SCSI Pass-Through Requests


## <span id="ddk_handling_scsi_pass_through_requests_kg"></span><span id="DDK_HANDLING_SCSI_PASS_THROUGH_REQUESTS_KG"></span>


A class driver that generates an [**IOCTL\_SCSI\_PASS\_THROUGH**](https://msdn.microsoft.com/library/windows/hardware/ff560519) request or an [**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**](https://msdn.microsoft.com/library/windows/hardware/ff560521) request is responsible for the following:

-   Setting the length of the user buffer at **Parameters.DeviceIoControl.InputBufferLength** to at least **sizeof**(SCSI\_PASS\_THROUGH) or **sizeof**(SCSI\_PASS\_THROUGH\_DIRECT)

-   Setting up the storage port driver's I/O stack location as usual

-   Setting the **MinorFunction** in the IRP to IRP\_MJ\_DEVICE\_CONTROL, which marks the request as having been processed by a storage class driver.

On receipt of an IOCTL\_SCSI\_PASS\_THROUGH or IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT request from a higher-level driver, a storage class driver's [**DispatchDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine is responsible for checking the validity of the embedded SCSI command (CDB) and, if the command is valid for its device, sending the request to the storage port driver.

If the port driver's I/O stack location for an IOCTL\_SCSI\_PASS\_THROUGH or IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT request does not have its **MinorFunction** field set with IRP\_MJ\_DEVICE\_CONTROL, the port driver assumes the request came directly from an application and that no class driver exists for the target device type. It is an application error to send such a request directly to the port driver for a device that has been claimed by a storage class driver.

The port driver does not check the validity of the SCSI command embedded in such a pass-through request.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Handling%20SCSI%20Pass-Through%20Requests%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


