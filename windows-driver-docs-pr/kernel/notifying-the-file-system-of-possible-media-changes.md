---
title: Notifying the File System of Possible Media Changes
author: windows-driver-content
description: Notifying the File System of Possible Media Changes
MS-HAID:
- 'Other\_c694d732-fa95-4841-8d61-2a55ee787905.xml'
- 'kernel.notifying\_the\_file\_system\_of\_possible\_media\_changes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b1956370-ec9c-4a43-90a8-12705d28e314
keywords: ["removable media WDK kernel , notifying of media changes", "notifications WDK removable media", "media change notifications WDK removable media"]
---

# Notifying the File System of Possible Media Changes


## <a href="" id="ddk-notifying-the-file-system-of-possible-media-changes-kg"></a>


A removable-media device driver must ensure that the media is not changed for the device represented by the **DeviceObject** (input to every driver routine that is sent an IRP) whenever the driver processes an IRP that requests a transfer to/from the media or a device I/O control operation that affects the media. The best possible time to check for changed media is just after the transition from a no-media-present state to a media-present state if the physical device always notifies the driver about these state changes.

If its physical device indicates that the state of the media might have changed before the driver begins an I/O operation or during an operation, the driver must do the following:

1.  Ensure that the volume is mounted by checking the VPB\_MOUNTED flag in the [*VPB*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-vpb). (If the volume is not mounted, the driver must not set the DO\_VERIFY\_VOLUME bit. The driver should set **IoStatus.Status** to STATUS\_IO\_DEVICE\_ERROR, set **IoStatus.Information** to zero, and call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with the IRP.)

2.  Set the **Flags** in the **DeviceObject** by ORing **Flags** with DO\_VERIFY\_VOLUME.

3.  Set the **IoStatus** block in the IRP to the following:
    -   **Status** set to STATUS\_VERIFY\_REQUIRED
    -   **Information** set to zero

4.  Before completing any IRP with an **IoStatus** block in which the **Status** field is not set to STATUS\_SUCCESS, the driver must call [**IoIsErrorUserInduced**](https://msdn.microsoft.com/library/windows/hardware/ff549375), which returns a Boolean **TRUE** for any of the following **Status** values:

    -   STATUS\_VERIFY\_REQUIRED
    -   STATUS\_NO\_MEDIA\_IN\_DEVICE
    -   STATUS\_WRONG\_VOLUME
    -   STATUS\_UNRECOGNIZED\_MEDIA
    -   STATUS\_MEDIA\_WRITE\_PROTECTED
    -   STATUS\_IO\_TIMEOUT
    -   STATUS\_DEVICE\_NOT\_READY

    If **IoIsErrorUserInduced** returns **TRUE**, the driver must call [**IoSetHardErrorOrVerifyDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549707) so the FSD can open a dialog box to the user, who can then choose to supply the correct media, retry the original request, or cancel the requested operation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Notifying%20the%20File%20System%20of%20Possible%20Media%20Changes%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


