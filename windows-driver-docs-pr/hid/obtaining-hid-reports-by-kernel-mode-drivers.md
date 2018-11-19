---
title: Obtaining HID Reports by Kernel-Mode Drivers
description: This topic discusses how a kernel-mode driver should use IRP_MJ_READ requests as its main approach for continuously obtaining HID input reports.
ms.assetid: 017481f1-8021-4fd5-ab8e-f09f6006e616
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Obtaining HID Reports by Kernel-Mode Drivers


This topic discusses how a kernel-mode driver should use [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) requests as its main approach for continuously obtaining HID input reports.

Consecutive read requests return input reports in the order in which they were received from the collection. The driver can also use IOCTL\_HID\_GET\_*Xxx* requests to obtain input and feature reports. However, a driver should only use these I/O requests to obtain the current state of a device. If the driver attempts to use IOCTL\_HID\_GET\_INPUT\_REPORT to continuously obtain input reports, reports can be lost. In addition, some devices might not support IOCTL\_HID\_GET\_INPUT\_REPORT, and will become unresponsive if this request is used.

The following sections provide more information.

### <a href="" id="using-irp-ml-read-requests"></a>Using IRP\_MJ\_READ Requests

Non-WDM Windows 2000 drivers, and drivers for Windows XP and later versions, can use a single IRP for all read requests to a device. However, Windows 2000 WDM drivers must allocate a new IRP for each read request. For general information about how to use and reuse IRPs, see [Handling IRPs](https://msdn.microsoft.com/library/windows/hardware/ff546847) and [Reusing IRPs](https://msdn.microsoft.com/library/windows/hardware/ff561107).

If a driver reuses an IRP, the IRP's [**IoCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine should complete the request with a status of STATUS\_MORE\_PROCESSING\_REQUIRED (and not free the IRP). When the driver no longer requires the IRP, it should complete and free the IRP by calling [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) and [**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113). For example, a driver might typically complete and free the IRP in its [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine, or after a device is removed.

If a driver uses an IRP for only one read request, the IRP's **IoCompletion** routine should complete and free the IRP, and return STATUS\_SUCCESS.

Before a driver can request an input report, it must first allocate a zero-initialized input report buffer from nonpaged memory pool. The size, in bytes, of the buffer is specified by the **InputReportByteLength** member of a HID collection's [**HIDP\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff539697) structure. A driver must then use an MDL to map the input report buffer for a read request. The driver calls [**IoAllocateMdl**](https://msdn.microsoft.com/library/windows/hardware/ff548263) to allocate the MDL for an input report buffer, and sets the read IRP's **Irp-&gt;MdlAddress** member to the MDL address of the input report buffer. The driver should free the report buffer and the MDL when they are no longer required.

In addition to setting the read IRP's MDL address, the driver must also set the I/O stack location of the next lower-level driver. A driver obtains access to the I/O stack location of the next lower-level driver by calling [**IoGetNextIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549266). The driver sets the following members of the I/O stack location:

<a href="" id="parameters-read-length"></a>**Parameters.Read.Length**  
Set to the size, in bytes, of the read buffer. This must be greater than or equal to the value specified by the **InputReportByteLength** member of a HID collection's [**HIDP\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff539697) structure.

<a href="" id="parameters-read-key"></a>**Parameters.Read.Key**  
Set to zero.

<a href="" id="parameters-read-byteoffset-quadpart"></a>**Parameters.Read.ByteOffset.QuadPart**  
Set to zero.

<a href="" id="majorfunction"></a>**MajorFunction**  
Set to IRP\_MJ\_READ.

<a href="" id="fileobject"></a>**FileObject**  
Set to the file object pointer that represents the open file on the HID collection.

After the driver has obtained an input report, it can access control data, as described in [Interpreting HID Reports](interpreting-hid-reports.md).

### <a href="" id="using-ioctl-hid-get-xxx-requests"></a>Using IOCTL\_HID\_GET\_Xxx Requests

A driver can use the following I/O requests to obtain the most current input and feature reports from a HID collection:

<a href="" id="ioctl-hid-get-input-report"></a>[**IOCTL\_HID\_GET\_INPUT\_REPORT**](https://msdn.microsoft.com/library/windows/hardware/ff541126)  
Returns an input report from a HID collection (Windows XP and later versions).

<a href="" id="ioctl-hid-get-feature"></a>[**IOCTL\_HID\_GET\_FEATURE**](https://msdn.microsoft.com/library/windows/hardware/ff541100)  
Returns a feature report from a HID collection.

A driver can request the return of a specific report. To retrieve a specific report using these I/O requests, the driver first allocates the output report buffer, then zero-initializes the buffer, and sets the first byte in the buffer to the specific report ID. For more information, see [Interpreting HID Reports](interpreting-hid-reports.md).

 

 




