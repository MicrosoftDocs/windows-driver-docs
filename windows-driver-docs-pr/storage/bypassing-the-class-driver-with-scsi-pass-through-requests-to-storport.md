---
title: Bypassing the Class Driver with SCSI Pass-Through Requests to Storport
description: Bypassing the Class Driver with SCSI Pass-Through Requests to Storport
ms.assetid: 1162a1e7-a4f8-446f-8106-527f9b916382
---

# Bypassing the Class Driver with SCSI Pass-Through Requests to Storport


In most cases, a class driver mediates all communication between Storport and higher-level drivers and applications. Some target devices, however, do not have a class driver. Drivers for such devices must communicate directly with Storport by using a class of requests called "pass-through" requests. To use a pass-through request, the higher-level component is required to set up the CDB that is used in the request, rather than relying on the class driver to do so.

If a class driver is present and the device is claimed, then "pass-through" request must be directed to the class driver by opening the appropriate device handle. If there is no class driver for a device and the device is not claimed, then the "pass-through" request may be sent directly to the adapter, again, by opening the appropriate device handle.

A SCSI pass-through request consists of an IRP of type IRP\_MJ\_DEVICE\_CONTROL with an IOCTL code of [**IOCTL\_SCSI\_PASS\_THROUGH**](https://msdn.microsoft.com/library/windows/hardware/ff560519) or [**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**](https://msdn.microsoft.com/library/windows/hardware/ff560521). If the request passes through a class driver, the class driver is obligated to set the **MinorFunction** code of the IRP to IRP\_MJ\_DEVICE\_CONTROL. Storport checks this value to determine whether a pass-through request bypassed the class driver. It is an application error to send a pass-through request directly to Storport if the target device has been claimed by a storage class driver.

Storport does not check the validity of the SCSI command that is embedded in a pass-through request.

For a discussion of SCSI pass-through requests from the perspective of a storage class driver, see [Handling SCSI Pass-Through Requests](handling-scsi-pass-through-requests.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Bypassing%20the%20Class%20Driver%20with%20SCSI%20Pass-Through%20Requests%20to%20Storport%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




