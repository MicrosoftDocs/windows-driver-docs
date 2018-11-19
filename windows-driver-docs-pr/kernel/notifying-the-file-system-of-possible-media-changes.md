---
title: Notifying the File System of Possible Media Changes
description: Notifying the File System of Possible Media Changes
ms.assetid: b1956370-ec9c-4a43-90a8-12705d28e314
keywords: ["removable media WDK kernel , notifying of media changes", "notifications WDK removable media", "media change notifications WDK removable media"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Notifying the File System of Possible Media Changes





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

 

 




