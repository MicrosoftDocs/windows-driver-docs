---
title: IRP\_MJ\_CLOSE
author: windows-driver-content
description: Every driver must handle close requests in a DispatchClose routine, with the possible exception of a driver whose device cannot be disabled or removed from the machine without bringing down the system.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: 109819a8-3787-448d-a766-5d53dbcf55f4
keywords:
 - IRP_MJ_CLOSE Kernel-Mode Driver Architecture
---

# IRP\_MJ\_CLOSE


Every driver must handle close requests in a [*DispatchClose*](https://msdn.microsoft.com/library/windows/hardware/ff543255) routine, with the possible exception of a driver whose device cannot be disabled or removed from the machine without bringing down the system. A disk driver whose device holds the system page file is an example of such a driver. Note that the driver of such a device also cannot be unloaded dynamically.

When Sent
---------

Receipt of this request indicates that the last handle of the file object that is associated with the target device object has been closed and released. All outstanding I/O requests have been completed or canceled.

## Input Parameters


None

## Output Parameters


None

Operation
---------

Many device and intermediate drivers merely set STATUS\_SUCCESS in the I/O status block of the IRP and complete the close request. However, what a given driver does on receipt of a close request depends on the driver's design. In general, a driver should undo whatever actions it takes on receipt of the [**IRP\_MJ\_CREATE**](irp-mj-create.md) request. Device drivers whose device objects are exclusive, such as a serial driver, also can reset the hardware on receipt of a close request.

The **IRP\_MJ\_CLOSE** request is not necessarily sent in the context of the process that closed the file object handle. If the driver must release process-specific resources, such as user memory, that the driver previously locked or mapped, it must do so in response to an [**IRP\_MJ\_CLEANUP**](irp-mj-cleanup.md) request.

The **IRP\_MJ\_CLOSE** request will always be sent at PASSIVE\_LEVEL.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[*DispatchClose*](https://msdn.microsoft.com/library/windows/hardware/ff543255)

[**IRP\_MJ\_CLEANUP**](irp-mj-cleanup.md)

[**IRP\_MJ\_CREATE**](irp-mj-create.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MJ_CLOSE%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


