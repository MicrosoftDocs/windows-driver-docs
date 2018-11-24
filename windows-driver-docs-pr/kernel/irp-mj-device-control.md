---
title: IRP_MJ_DEVICE_CONTROL
description: Every driver whose device objects belong to a particular device type (see Specifying Device Types) is required to support this request in a DispatchDeviceControl routine, if a set of system-defined I/O control codes (IOCTLs) exists for the type.
ms.date: 08/12/2017
ms.assetid: c6436b34-22bd-4e65-bfb0-b2c4d9962e29
keywords:
 - IRP_MJ_DEVICE_CONTROL Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MJ\_DEVICE\_CONTROL


Every driver whose device objects belong to a particular device type (see [Specifying Device Types](https://msdn.microsoft.com/library/windows/hardware/ff563821)) is required to support this request in a [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine, if a set of system-defined I/O control codes (IOCTLs) exists for the type. For more info about IOCTLs, see [Introduction to I/O Control Codes](introduction-to-i-o-control-codes.md).

Higher-level drivers usually pass these requests on to an underlying device driver. Each device driver in a driver stack is assumed to support this request, along with a set of device type-specific, public or private IOCTLs. For more information about IOCTLs for specific device types, see device type-specific documentation in the Microsoft Windows Driver Kit (WDK).

When Sent
---------

Any time following the successful completion of a create request.

## Input Parameters


The I/O control code is contained at **Parameters.DeviceIoControl.IoControlCode** in the driver's I/O stack location of the IRP.

Other input parameters depend on the I/O control code's value. For more information, see [Buffer Descriptions for I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff540663).

## Output Parameters


Output parameters depend on the I/O control code's value. For more information, see [Buffer Descriptions for I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff540663).

Operation
---------

A driver receives this I/O control code because user-mode thread has called the Microsoft Win32 [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function, or a higher-level kernel-mode driver has set up the request. Possibly, a user-mode driver has called **DeviceIoControl**, passing in a driver-defined (also called *private*) I/O control code, to request device- or driver-specific support from a closely coupled, kernel-mode device driver.

On receipt of a device I/O control request, a higher-level driver usually passes the IRP on to the next-lower driver. However, there are some exceptions to this practice. For example, a class driver that has stored configuration information obtained from the underlying port driver might complete certain IOCTL\_*XXX* requests without passing the IRP down to the corresponding port driver.

On receipt of a device I/O control request, a device driver examines the I/O control code to determine how to satisfy the request. For most public I/O control codes, device drivers transfer a small amount of data to or from the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

For general information about I/O control codes for **IRP\_MJ\_DEVICE\_CONTROL** or [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](irp-mj-internal-device-control.md) requests, see [Using I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff565406). See also [Device Type-Specific I/O Requests](https://msdn.microsoft.com/library/windows/hardware/ff543205).

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


[*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287)

 

 




