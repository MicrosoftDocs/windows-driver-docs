---
title: Bypass a Class Driver with SCSI Pass-Through Requests to Storport
description: Bypass a Class Driver with SCSI Pass-Through Requests to Storport
ms.assetid: 1162a1e7-a4f8-446f-8106-527f9b916382
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bypass a Class Driver with SCSI Pass-Through Requests to Storport

In most cases, a class driver mediates all communication between Storport and higher-level drivers and applications. Some target devices, however, do not have a class driver. Drivers for such devices must communicate directly with Storport by using a class of requests called "pass-through" requests. To use a pass-through request, the higher-level component is required to set up the CDB that is used in the request, rather than relying on the class driver to do so.

If a class driver is present and the device is claimed, then "pass-through" request must be directed to the class driver by opening the appropriate device handle. If there is no class driver for a device and the device is not claimed, then the "pass-through" request may be sent directly to the adapter, again, by opening the appropriate device handle.

A SCSI pass-through request consists of an IRP of type IRP\_MJ\_DEVICE\_CONTROL with an IOCTL code of [**IOCTL\_SCSI\_PASS\_THROUGH**](https://msdn.microsoft.com/library/windows/hardware/ff560519) or [**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**](https://msdn.microsoft.com/library/windows/hardware/ff560521). If the request passes through a class driver, the class driver is obligated to set the **MinorFunction** code of the IRP to IRP\_MJ\_DEVICE\_CONTROL. Storport checks this value to determine whether a pass-through request bypassed the class driver. It is an application error to send a pass-through request directly to Storport if the target device has been claimed by a storage class driver.

Storport does not check the validity of the SCSI command that is embedded in a pass-through request.

For a discussion of SCSI pass-through requests from the perspective of a storage class driver, see [Handling SCSI Pass-Through Requests](handling-scsi-pass-through-requests.md).

 

 




