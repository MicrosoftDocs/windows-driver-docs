---
title: Sending HID Reports by Kernel-Mode Drivers
description: Sending HID Reports by Kernel-Mode Drivers
ms.assetid: ff3d090f-cf76-40a7-9215-8440a592f303
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Sending HID Reports by Kernel-Mode Drivers


A kernel-mode driver should use [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) requests as its main approach to continuously send output report to a HID collection. Drivers can also use IOCTL\_HID\_SET\_*Xxx* requests to send output reports and feature reports to a collection. However, a driver should only use these I/O requests to set the current state of a collection. Some devices might not support [**IOCTL\_HID\_SET\_OUTPUT\_REPORT**](https://msdn.microsoft.com/library/windows/hardware/ff541196) and will become unresponsive if this request is used.

For more information, see [Using IRP\_MJ\_WRITE Requests](#using-irp-mj-write-requests) and [Using IOCTL\_HID\_SET\_Xxx Requests](#using-ioctl-hid-set-xxx-requests).

### <a href="" id="using-irp-mj-write-requests"></a>Using IRP\_MJ\_WRITE Requests

Non-WDM Windows 2000 drivers, and drivers for Windows XP and later versions, can use a single IRP for all write requests sent to a collection. However, Windows 2000 WDM drivers must allocate a new IRP for each write request. For more information about how to use and reuse IRPs, see [Handling IRPs](https://msdn.microsoft.com/library/windows/hardware/ff546847) and [Reusing IRPs](https://msdn.microsoft.com/library/windows/hardware/ff561107).

If the driver reuses a write IRP, the IRP's [**IoCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine should complete the request with a status of STATUS\_MORE\_PROCESSING\_REQUIRED (and not free the IRP). When the driver no longer requires the IRP, it should complete and free the IRP by calling [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) and [**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113). For example, a driver might typically complete and free the IRP in its [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine, or after a device is removed.

If a driver uses an IRP for only one write request, the IRP's [**IoCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine should complete and free the IRP, and return STATUS\_SUCCESS.

Before sending an output report, a driver must first initialize and set an output report buffer, as described in [Initializing HID Reports](initializing-hid-reports.md). The driver must then use an MDL to map the output report buffer for a write request. A driver calls [**IoAllocateMdl**](https://msdn.microsoft.com/library/windows/hardware/ff548263) to allocate the MDL for an output report, and sets a write IRP's **Irp-&gt;MdlAddress** member to the MDL address of the output report buffer. The driver must free the report buffer and the MDL when they are no longer required.

In addition to setting the write IRP's MDL address, the driver must also set the I/O stack location of the next lower-level driver. A driver obtains access to the I/O stack location of the next lower-level driver by calling [**IoGetNextIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549266). The driver sets the following members of the I/O stack location:

<a href="" id="parameters-write-length"></a>**Parameters.Write.Length**  
Set to the length, in bytes, of an output report. This should be set to the length of a HID collection's output reports, as specified by the **OutputReportByteLength** member of a collection's [**HIDP\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff539697) structure.

<a href="" id="parameters-write-key"></a>**Parameters.Write.Key**  
Set to zero.

<a href="" id="parameters-write-byteoffset-quadpart"></a>**Parameters.Write.ByteOffset.QuadPart**  
Set to zero.

<a href="" id="majorfunction"></a>**MajorFunction**  
Set to IRP\_MJ\_WRITE.

<a href="" id="fileobject"></a>**FileObject**  
Set to the file object pointer that represents the open file on the HID collection.

### <a href="" id="using-ioctl-hid-set-xxx-requests"></a>Using IOCTL\_HID\_SET\_Xxx Requests

A driver can also use the following I/O requests to send output and feature reports to a HID collection:

<a href="" id="ioctl-hid-set-output-report"></a>[**IOCTL\_HID\_SET\_OUTPUT\_REPORT**](https://msdn.microsoft.com/library/windows/hardware/ff541196)  
Sends an output report to a collection (Windows XP and later versions).

<a href="" id="ioctl-hid-set-feature"></a>[**IOCTL\_HID\_SET\_FEATURE**](https://msdn.microsoft.com/library/windows/hardware/ff541176)  
Sends a feature report to a collection.

 

 




