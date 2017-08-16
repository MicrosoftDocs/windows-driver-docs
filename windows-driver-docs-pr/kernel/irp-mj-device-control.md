---
title: IRP\_MJ\_DEVICE\_CONTROL
author: windows-driver-content
description: Every driver whose device objects belong to a particular device type (see Specifying Device Types) is required to support this request in a DispatchDeviceControl routine, if a set of system-defined I/O control codes (IOCTLs) exists for the type.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: c6436b34-22bd-4e65-bfb0-b2c4d9962e29
keywords:
 - IRP_MJ_DEVICE_CONTROL Kernel-Mode Driver Architecture
---

# IRP\_MJ\_DEVICE\_CONTROL


Every driver whose device objects belong to a particular device type (see [Specifying Device Types](https://msdn.microsoft.com/library/windows/hardware/ff563821)) is required to support this request in a [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine, if a set of system-defined I/O control codes ([*IOCTLs*](https://msdn.microsoft.com/library/windows/hardware/ff556290#wdkgloss-ioctl)) exists for the type.

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MJ_DEVICE_CONTROL%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


