---
title: Responding to Check-Verify Requests from the File System
description: Responding to Check-Verify Requests from the File System
ms.assetid: 227e65d6-d746-4b16-978d-4d42be9aeb2c
keywords: ["removable media WDK kernel , check-verify requests", "check-verify requests WDK removable media", "media change requests WDK removable media", "checking removable media changes", "verifying removable media changes"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Responding to Check-Verify Requests from the File System





At its discretion, the file system can send an IRP to the device driver's Dispatch entry point for [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) requests with **Parameters.DeviceIoControl.IoControlCode** in the I/O stack location set to the following:

<a href="" id="ioctl-xxx-check-verify"></a>IOCTL\_*XXX*\_CHECK\_VERIFY  
where *XXX* is the type of device, such as DISK, TAPE, or CDROM.

The type DISK includes both unpartitionable (floppy) and partitionable removable-media devices.

If the underlying device driver determines that the media has not changed, the driver should complete the IRP, returning the **IoStatus** block with the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Status</strong></p></td>
<td><p>Set to STATUS_SUCCESS</p></td>
</tr>
<tr class="even">
<td><p><strong>Information</strong></p></td>
<td><p>Set to zero</p></td>
</tr>
</tbody>
</table>

 

In addition, if the device type is DISK or CDROM and the caller specified an output buffer, the driver returns the media change count in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** and sets **Irp-&gt;IoStatus.Information** to **sizeof**(ULONG). By returning this count, the driver gives the caller an opportunity to determine whether the media has changed from its perspective.

If the underlying device driver determines that the media has changed, it takes a different action depending on whether the volume is mounted. If the volume is mounted (the VPB\_MOUNTED flag is set in the VPB), the driver should do the following:

1.  Set the **Flags** in the **DeviceObject** by ORing **Flags** with DO\_VERIFY\_VOLUME.

2.  Set the **IoStatus** block in the IRP to the following:
    -   **Status** set to STATUS\_VERIFY\_REQUIRED
    -   **Information** set to zero

3.  Call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with the input IRP.

If the volume is not mounted, the driver must not set the DO\_VERIFY\_VOLUME bit. The driver should set **IoStatus.Status** to STATUS\_IO\_DEVICE\_ERROR, set **IoStatus.Information** to zero, and call **IoCompleteRequest** with the IRP.

 

 




