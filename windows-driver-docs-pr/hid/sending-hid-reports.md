---
title: Sending HID Reports
description: This article describes how user-mode applications and kernel-mode drivers send HID reports to a HID collection.
keywords:
- reports WDK HID , sending
- sending reports
- WriteFile WDK HID
- IRP_MJ_WRITE requests WDK HID
- IOCTL_HID_SET_Xxx requests WDK HID
- HID reports WDK , sending
ms.date: 09/17/2024
---

# Sending HID reports

This article describes how user-mode applications and kernel-mode drivers send HID reports to a [HID collection](hid-collections.md).

## Send HID reports by user-mode applications

User-mode applications use [WriteFile](/windows/win32/api/fileapi/nf-fileapi-writefile) to continuously send output reports to a HID collection. You can also use **HidD_SetXxx** routines to send output reports and feature reports to a collection. However, only use **HidD_SetXxx** routines to set the current state of a collection. Some devices might not support [HidD_SetOutputReport](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_setoutputreport) and become unresponsive if this routine is used.

## WriteFile routine

Use write requests to send output reports to a HID collection. After a user-mode application creates an output report, it can send an output report to a collection using [WriteFile](/windows/win32/api/fileapi/nf-fileapi-writefile).

## HidD_SetXxx routines

Use these [HIDClass support routines](/windows-hardware/drivers/ddi/_hid/#hidclass-support-routines) to send HID reports to a HID collection:

- [HidD_SetOutputReport](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_setoutputreport): Sends an output report to a HID collection (Windows XP and later versions).
- [HidD_SetFeature](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_setfeature): Sends a feature report to a HID collection.

## Send HID reports by kernel-mode drivers

Kernel mode drivers use [IRP_MJ_WRITE](../ifs/irp-mj-write.md) requests to continuously send output report to a HID collection. You can also use **IOCTL_HID_SET_Xxx** requests to send output reports and feature reports to a collection. However, only use **IOCTL_HID_SET_Xxx** requests to set the current state of a collection. Some devices might not support [IOCTL_HID_SET_OUTPUT_REPORT](/windows-hardware/drivers/ddi/hidclass/ni-hidclass-ioctl_hid_set_output_report) and become unresponsive if this request is used.

## IRP_MJ_WRITE requests

Non-WDM Windows 2000 drivers, and drivers for Windows XP and later versions, can use a single IRP for all write requests sent to a collection. However, Windows 2000 WDM drivers must allocate a new IRP for each write request. For more information about how to use and reuse IRPs, see [Handling IRPs](../kernel/handling-irps.md) and [Reusing IRPs](../kernel/reusing-irps.md).

If the driver reuses a write IRP, the IRP's [IoCompletion](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine should complete the request with a status of **STATUS_MORE_PROCESSING_REQUIRED** (and not free the IRP). When the driver no longer requires the IRP, it should complete and free the IRP by calling [IoCompleteRequest](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) and [IoFreeIrp](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreeirp). For example, a driver might typically complete and free the IRP in its [Unload](../kernel/unload-routine-functionality.md) routine, or after a device is removed.

If a driver uses an IRP for only one write request, the IRP's **IoCompletion** routine should complete and free the IRP, and return **STATUS_SUCCESS**.

When a driver sends an output report, it must first initialize and set an output report buffer, as described in [Initializing HID Reports](initializing-hid-reports.md). The driver must then use an MDL to map the output report buffer for a write request. A driver calls [IoAllocateMdl](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocatemdl) to allocate the MDL for an output report, and sets a write **IRP's Irp->MdlAddress** member to the MDL address of the output report buffer. The driver must free the report buffer and the MDL when they're no longer required.

In addition to setting the write IRP's MDL address, the driver must also set the I/O stack location of the next lower-level driver. A driver obtains access to the I/O stack location of the next lower-level driver by calling [IoGetNextIrpStackLocation](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetnextirpstacklocation). The driver sets the following members of the I/O stack location:

- **Parameters.Write.Length**: Set to the length, in bytes, of an output report. Set this member to the length of a HID collection's output reports, as specified by the *OutputReportByteLength* member of a collection's **HIDP_CAPS** structure.
- **Parameters.Write.Key**: Set to zero.
- **Parameters.Write.ByteOffset.QuadPart**: Set to zero.
- **MajorFunction**: Set to `IRP_MJ_WRITE`.
- **FileObject**: Set to the file object pointer that represents the open file on the HID collection.

## IOCTL_HID_SET_Xxx requests

You can also use the following I/O requests to send output and feature reports to a HID collection:

- [IOCTL_HID_SET_OUTPUT_REPORT](/windows-hardware/drivers/ddi/hidclass/ni-hidclass-ioctl_hid_set_output_report): Sends an output report to a collection (Windows XP and later versions).
- [IOCTL_HID_SET_FEATURE](/windows-hardware/drivers/ddi/hidclass/ni-hidclass-ioctl_hid_set_feature): Sends a feature report to a collection.
