---
title: Obtaining HID Reports
description: Obtaining HID Reports
keywords:
- reports WDK HID , obtaining
- ReadFile WDK HID
- IRP_MJ_READ requests WDK HID
- IOCTL_HID_GET_Xxx requests WDK HID
- HID reports WDK , obtaining
ms.date: 09/10/2020
ms.localizationpriority: medium
---

# Obtaining HID Reports

This section describes how user-mode applications and kernel-mode drivers obtain HID reports from a [HID collection](hid-collections.md).

## Obtaining HID Reports by user-mode applications

This topic discusses the obtaining of HID input reports or HID feature reports, by user-mode applications using [ReadFile](/windows/win32/api/fileapi/nf-fileapi-readfile) or the **HidD_Get**Xxx routines.

However, an application should only use the **HidD_Get**Xxx routines to obtain the current state of a device. If an application attempts to use [HidD_GetInputReport](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getinputreport) to continuously obtain input reports, the reports can be lost. In addition, some devices might not support **HidD_GetInputReport**, and will become unresponsive if this routine is used.

### Using ReadFile

An application uses the open file handle it obtained by using **CreateFile** to open a file on the collection. When the application calls **ReadFile**, it does not have to specify overlapped I/O because the [HID Client Drivers](keyboard-and-mouse-hid-client-drivers.md) buffers reports in a ring buffer. However, an application can use overlapped I/O to have more than one outstanding read request.

### Using HidD_GetXxx Routines

An application can use the following [HIDClass support routines](/windows-hardware/drivers/ddi/_hid/#hidclass-support-routines) to obtain the most current input reports and feature reports from a HID collection:

- [HidD_GetInputReport](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getinputreport) Returns an input report from a HID collection (Windows XP and later versions).

- [HidD_GetFeature](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getfeature) Returns a feature report from a HID collection.

An application can request the return of a specific report. To retrieve a specific report using these routines, the application allocates the report output buffer, zero-initializes the buffer, and sets the first byte in the buffer to the specific report ID. For more information, see [Initializing HID Reports](initializing-hid-reports.md).

## Obtaining HID Reports by kernel-mode drivers

This topic discusses how a kernel-mode driver should use [IRP_MJ_READ](../ifs/irp-mj-read.md) requests as its main approach for continuously obtaining HID input reports.

Consecutive read requests return input reports in the order in which they were received from the collection. The driver can also use **IOCTL_HID_GET_Xxx** requests to obtain input and feature reports. However, a driver should only use these I/O requests to obtain the current state of a device. If the driver attempts to use [IOCTL_HID_GET_INPUT_REPORT](/windows-hardware/drivers/ddi/hidclass/ni-hidclass-ioctl_hid_get_input_report) to continuously obtain input reports, reports can be lost. In addition, some devices might not support **IOCTL_HID_GET_INPUT_REPORT**, and will become unresponsive if this request is used.

### Using IRP_MJ_READ Requests

Non-WDM Windows 2000 drivers, and drivers for Windows XP and later versions, can use a single IRP for all read requests to a device. However, Windows 2000 WDM drivers must allocate a new IRP for each read request. For general information about how to use and reuse IRPs, see [Handling IRPs](../kernel/handling-irps.md) and [Reusing IRPs](../kernel/reusing-irps.md).

If a driver reuses an IRP, the IRP's [IoCompletion](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine should complete the request with a status of **STATUS_MORE_PROCESSING_REQUIRED** (and not free the IRP). When the driver no longer requires the IRP, it should complete and free the IRP by calling [IoCompleteRequest](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) and [IoFreeIrp](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreeirp). For example, a driver might typically complete and free the IRP in its [Unload](../kernel/unload-routine-functionality.md) routine, or after a device is removed.

If a driver uses an IRP for only one read request, the IRP's **IoCompletion** routine should complete and free the IRP, and return **STATUS_SUCCESS**.

Before a driver can request an input report, it must first allocate a zero-initialized input report buffer from nonpaged memory pool. The size, in bytes, of the buffer is specified by the **InputReportByteLength** member of a HID collection's [HIDP_CAPS](/windows-hardware/drivers/ddi/hidpi/ns-hidpi-_hidp_caps) structure. A driver must then use an MDL to map the input report buffer for a read request. The driver calls [IoAllocateMdl](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocatemdl) to allocate the MDL for an input report buffer, and sets the read IRP's **Irp->MdlAddress** member to the MDL address of the input report buffer. The driver should free the report buffer and the MDL when they are no longer required.

In addition to setting the read IRP's MDL address, the driver must also set the I/O stack location of the next lower-level driver. A driver obtains access to the I/O stack location of the next lower-level driver by calling [IoGetNextIrpStackLocation](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetnextirpstacklocation). The driver sets the following members of the I/O stack location:

**Parameters.Read.Length**<br>
Set to the size, in bytes, of the read buffer. This must be greater than or equal to the value specified by the InputReportByteLength member of a HID collection's [HIDP_CAPS](/windows-hardware/drivers/ddi/hidpi/ns-hidpi-_hidp_caps) structure.

**Parameters.Read.Key**<br>
Set to zero.

**Parameters.Read.ByteOffset.QuadPart**<br>
Set to zero.

**MajorFunction**<br>
Set to IRP_MJ_READ.

**FileObject**<br>
Set to the file object pointer that represents the open file on the HID collection.

After the driver has obtained an input report, it can access control data, as described in [Interpreting HID Reports](interpreting-hid-reports.md).

### Using IOCTL_HID_GET_Xxx Requests

A driver can use the following I/O requests to obtain the most current input and feature reports from a HID collection:

- [IOCTL_HID_GET_INPUT_REPORT](/windows-hardware/drivers/ddi/hidclass/ni-hidclass-ioctl_hid_get_input_report)
Returns an input report from a HID collection (Windows XP and later versions).

- [IOCTL_HID_GET_FEATURE](/windows-hardware/drivers/ddi/hidclass/ni-hidclass-ioctl_hid_get_feature)
Returns a feature report from a HID collection.

A driver can request the return of a specific report. To retrieve a specific report using these I/O requests, the driver first allocates the output report buffer, then zero-initializes the buffer, and sets the first byte in the buffer to the specific report ID.

For more information, see [Interpreting HID Reports](interpreting-hid-reports.md).
