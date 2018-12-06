---
title: Bypassing the Class Driver with SCSI Pass-Through Requests
description: Bypassing the Class Driver with SCSI Pass-Through Requests
ms.assetid: 7f26e0bc-f01b-4430-aa9f-0f684fdbc2ec
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bypassing the Class Driver with SCSI Pass-Through Requests


## <span id="ddk_bypassing_the_class_driver_with_scsi_pass_through_requests_kg"></span><span id="DDK_BYPASSING_THE_CLASS_DRIVER_WITH_SCSI_PASS_THROUGH_REQUESTS_KG"></span>


In most cases, a class driver mediates all communication between SCSI Port and higher-level drivers and applications. Some target devices, however, do not have a class driver. Drivers for such devices must communicate directly with SCSI Port by using a class of requests called "pass-through" requests. To use a pass-through request, the higher-level component is required to set up the CDB that is used in the request, rather than relying on the class driver to do so.

A SCSI pass-through request consists of an IRP of type IRP\_MJ\_DEVICE\_CONTROL with a IOCTL code of [**IOCTL\_SCSI\_PASS\_THROUGH**](https://msdn.microsoft.com/library/windows/hardware/ff560519) or [**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**](https://msdn.microsoft.com/library/windows/hardware/ff560521). If the request passes through a class driver, the class driver is obligated to set the IRP's **MinorFunction** code to IRP\_MJ\_DEVICE\_CONTROL. SCSI Port checks this value to determine whether a pass-through request bypassed the class driver. It is an application error to send a pass-through request directly to SCSI Port if the target device has been claimed by a storage class driver.

SCSI Port does not check the validity of the SCSI command that is embedded in a pass-through request.

For a discussion of SCSI pass-through requests from the perspective of a storage class driver, see [Handling SCSI Pass-Through Requests](handling-scsi-pass-through-requests.md)

 

 




