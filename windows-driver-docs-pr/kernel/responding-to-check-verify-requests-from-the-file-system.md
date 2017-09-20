---
title: Responding to Check-Verify Requests from the File System
author: windows-driver-content
description: Responding to Check-Verify Requests from the File System
ms.assetid: 227e65d6-d746-4b16-978d-4d42be9aeb2c
keywords: ["removable media WDK kernel , check-verify requests", "check-verify requests WDK removable media", "media change requests WDK removable media", "checking removable media changes", "verifying removable media changes"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Responding to Check-Verify Requests from the File System


## <a href="" id="ddk-responding-to-check-verify-requests-from-the-file-system-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Responding%20to%20Check-Verify%20Requests%20from%20the%20File%20System%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


