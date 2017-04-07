---
title: Sending HID Reports
author: windows-driver-content
description: Sending HID Reports
MS-HAID:
- 'hidclass\_5fae5f62-ca90-443f-8f35-394ceea29d9f.xml'
- 'hid.sending\_hid\_reports'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a4571b79-847b-4db0-be02-ac2f922162bb
keywords: ["reports WDK HID , sending", "sending reports", "WriteFile WDK HID", "IRP_MJ_WRITE requests WDK HID", "IOCTL_HID_SET_Xxx requests WDK HID", "HID reports WDK , sending"]
---

# Sending HID Reports


## <a href="" id="ddk-sending-hid-reports-kg"></a>


This section describes how user-mode applications and kernel-mode drivers send HID reports to a [HID collection](hid-collections.md).

## Sending HID Reports by Kernel-Mode Drivers


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

## Sending HID Reports by User-Mode Applications


A user-mode application should use WriteFile (as described in the Microsoft Windows SDK) as its main approach to continuously send output reports to a HID collection. An application can also use **HidD\_Set***Xxx* routines to send output reports and feature reports to a collection. However, an application should only use these routines to set the current state of a collection. Some devices might not support **HidD\_SetOutputReport** and will become unresponsive if this routine is used.

For more information, see [Using WriteFile](#using-writefile) and [Using HidD\_SetXxx Routines](#using-hidd-setxxx-routines).

### Using WriteFile

An application should use write requests to send output reports to a HID collection. After a user-mode application has created an output report, it can send an output report to a collection using WriteFile.

### <a href="" id="using-hidd-setxxx-routines"></a>Using HidD\_SetXxx Routines

An application can use the following [HIDClass support routines](https://msdn.microsoft.com/library/windows/hardware/ff538865) to send HID reports to a HID collection:

<a href="" id="hidd-setoutputreport"></a>[**HidD\_SetOutputReport**](https://msdn.microsoft.com/library/windows/hardware/ff539690)  
Sends an output report to a HID collection (Windows XP and later versions).

<a href="" id="hidd-setfeature"></a>[**HidD\_SetFeature**](https://msdn.microsoft.com/library/windows/hardware/ff539684)  
Sends a feature report to a HID collection.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Sending%20HID%20Reports%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


