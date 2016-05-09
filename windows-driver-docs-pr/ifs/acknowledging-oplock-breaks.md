---
title: Acknowledging Oplock Breaks
description: Acknowledging Oplock Breaks
ms.assetid: ea5bcd1e-d22c-4f80-89e4-1a61e43959dd
---

# Acknowledging Oplock Breaks


## <span id="oplock_break_conditions"></span><span id="OPLOCK_BREAK_CONDITIONS"></span>


There are different types of acknowledgments that the owner of an oplock can return. Similar to the [grant requests](granting-oplocks.md), these acknowledgments are sent as file system control codes (that is, [FSCTL](http://go.microsoft.com/fwlink/p/?linkid=124238)s). They are:

-   FSCTL\_OPLOCK\_BREAK\_ACKNOWLEDGE
    -   This FSCTL indicates that the oplock owner has completed stream synchronization and they accept the level to which the oplock was broken (either Level 2 or None).
-   FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2
    -   This FSCTL indicates that the oplock owner has completed stream synchronization but does not want a Level 2 oplock. Instead, the oplock should be broken to None (that is, the oplock is to be relinquished entirely).
-   FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING
    -   For a Level 1 oplock, this FSCTL indicates that the oplock owner has completed stream synchronization and is relinquishing the oplock entirely (no Level 2 oplock may result from this acknowledgment).

    <!-- -->

    -   For a Batch or Filter oplock, this FSCTL indicates that the oplock owner intends to close the stream handle on which the oplock was granted. Operations blocked, awaiting acknowledgment of the oplock break, continue to wait until the oplock owner's handle is closed.
-   FSCTL\_REQUEST\_OPLOCK
    -   By specifying REQUEST\_OPLOCK\_INPUT\_FLAG\_ACK in the **Flags** member of the REQUEST\_OPLOCK\_INPUT\_BUFFER structure passed as the *lpInBuffer* parameter of [DeviceIoControl](http://go.microsoft.com/fwlink/p/?linkid=124239), this FSCTL is used to acknowledge breaks of Windows 7 oplocks. The acknowledgment is required only if the REQUEST\_OPLOCK\_OUTPUT\_FLAG\_ACK\_REQUIRED flag is set in the **Flags** member of the REQUEST\_OPLOCK\_OUTPUT\_BUFFER structure passed as the *lpOutBuffer* parameter of [DeviceIoControl](http://go.microsoft.com/fwlink/p/?linkid=124239). In a similar manner, [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) and [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) can be used to acknowledge Windows 7 oplocks from kernel-mode. For more information, see [**FSCTL\_REQUEST\_OPLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff545530).

A related FSCTL code is FSCTL\_OPLOCK\_BREAK\_NOTIFY. This code is used when the caller wants to be notified when an oplock break on the given stream completes. This call may block. When the FSCTL\_OPLOCK\_BREAK\_NOTIFY call returns STATUS\_SUCCESS, this signifies one of the following:

-   No oplock granted.

-   No oplock break was in progress at the time of the call.

-   Any oplock break that was in progress is now complete.

To send an acknowledgment when no acknowledgment is expected is an error and the acknowledgment FSCTL IRP is failed with STATUS\_INVALID\_OPLOCK\_PROTOCOL.

Closing the handle of the file for which the oplock break is requested will implicitly acknowledge the break. In the case of an oplock break for a sharing violation, the oplock holder can close the file handle, which acknowledges the oplock break, and prevent a sharing violation for the other user of the file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Acknowledging%20Oplock%20Breaks%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




