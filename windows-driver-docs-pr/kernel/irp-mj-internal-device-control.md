---
title: IRP_MJ_INTERNAL_DEVICE_CONTROL
description: In general, any replacement for an existing driver that supports internal device control requests should handle this request in a DispatchInternalDeviceControl routine.
ms.date: 08/12/2017
keywords:
 - IRP_MJ_INTERNAL_DEVICE_CONTROL Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL


In general, any replacement for an existing driver that supports internal device control requests should handle this request in a [*DispatchInternalDeviceControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine. Such a driver must support at least the same set of internal I/O control codes as the driver it replaces. Otherwise, existing higher-level drivers might not work with the new driver.

Drivers that replace certain lower-level system drivers are required to handle this request. For example, a replacement for the system parallel port driver must continue to support existing parallel class drivers. Note that certain system drivers that handle this request cannot be replaced, in particular, the system-supplied SCSI and video port drivers.

## When Sent

Any time after the successful completion of a create request.

## Input Parameters


The I/O control code is contained at **Parameters.DeviceIoControl.IoControlCode** in the I/O stack location of the IRP.

Other input parameters depend on the I/O control code's value. For more information, see [Buffer Descriptions for I/O Control Codes](./buffer-descriptions-for-i-o-control-codes.md).

## Output Parameters


Output parameters depend on the I/O control code's value. For more information, see [Buffer Descriptions for I/O Control Codes](./buffer-descriptions-for-i-o-control-codes.md).

## Operation

Drivers receive **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests when another driver calls either [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest) or [**IoAllocateIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp) to create a request.

This I/O control code has been defined for communication between paired and layered kernel-mode drivers, such as one or more class drivers layered over a port driver. The higher-level driver sets up IRPs with device- or driver-specific I/O control codes, requesting support from the next-lower driver.

The requested operation is device- or driver-specific.

For general information about I/O control codes for [**IRP\_MJ\_DEVICE\_CONTROL**](irp-mj-device-control.md) or **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests, see [Using I/O Control Codes](./introduction-to-i-o-control-codes.md). See also [Device Type-Specific I/O Requests](./device-type-specific-i-o-requests.md).

## Requirements

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


[*DispatchInternalDeviceControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

[**IoAllocateIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp)

[**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest)

