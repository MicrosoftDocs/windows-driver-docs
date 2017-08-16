---
title: IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL
author: windows-driver-content
description: In general, any replacement for an existing driver that supports internal device control requests should handle this request in a DispatchInternalDeviceControl routine.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: fb3d4534-9c6f-4956-b702-5752f9798600
keywords:
 - IRP_MJ_INTERNAL_DEVICE_CONTROL Kernel-Mode Driver Architecture
---

# IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL


In general, any replacement for an existing driver that supports internal device control requests should handle this request in a [*DispatchInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543326) routine. Such a driver must support at least the same set of internal I/O control codes as the driver it replaces. Otherwise, existing higher-level drivers might not work with the new driver.

Drivers that replace certain lower-level system drivers are required to handle this request. For example, a replacement for the system parallel port driver must continue to support existing parallel class drivers. Note that certain system drivers that handle this request cannot be replaced, in particular, the system-supplied SCSI and video port drivers.

When Sent
---------

Any time after the successful completion of a create request.

## Input Parameters


The I/O control code is contained at **Parameters.DeviceIoControl.IoControlCode** in the I/O stack location of the IRP.

Other input parameters depend on the I/O control code's value. For more information, see [Buffer Descriptions for I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff540663).

## Output Parameters


Output parameters depend on the I/O control code's value. For more information, see [Buffer Descriptions for I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff540663).

Operation
---------

Drivers receive **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests when another driver calls either [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) or [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) to create a request.

This I/O control code has been defined for communication between paired and layered kernel-mode drivers, such as one or more class drivers layered over a port driver. The higher-level driver sets up IRPs with device- or driver-specific I/O control codes, requesting support from the next-lower driver.

The requested operation is device- or driver-specific.

For general information about I/O control codes for [**IRP\_MJ\_DEVICE\_CONTROL**](irp-mj-device-control.md) or **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests, see [Using I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff565406). See also [Device Type-Specific I/O Requests](https://msdn.microsoft.com/library/windows/hardware/ff543205).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[*DispatchInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543326)

[**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257)

[**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MJ_INTERNAL_DEVICE_CONTROL%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


