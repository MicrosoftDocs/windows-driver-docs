---
title: Returning Status from Dispatch Routines
author: windows-driver-content
description: Returning Status from Dispatch Routines
ms.assetid: 76bd651a-344f-4e22-a435-b62fdf2d7ddc
keywords: ["IRP dispatch routines WDK file system , returning status", "status values WDK file system", "success status values WDK file system", "returning status WDK file system"]
---

# Returning Status from Dispatch Routines


## <span id="ddk_returning_status_from_dispatch_routines_if"></span><span id="DDK_RETURNING_STATUS_FROM_DISPATCH_ROUTINES_IF"></span>


Except when completing an IRP, a dispatch routine that does not set a completion routine should always return the NTSTATUS value returned by [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336). Unless this value is STATUS\_PENDING, it must match the value of **Irp-&gt;IoStatus.Status** set by the driver that completed the IRP.

A dispatch routine that sets a completion routine that might post the IRP to a work queue should do one of the following:

-   Return the NTSTATUS value that was returned by **IoCallDriver**.

-   Wait for the completion routine to signal an event and return the value of **Irp-&gt;IoStatus.Status**.

-   Mark the IRP pending, post it to a work queue, and return STATUS\_PENDING.

-   If the completion routine might post the IRP to a work queue, the dispatch routine must mark the IRP pending and return STATUS\_PENDING.

Which of these behaviors is correct, or even possible, depends on the specific operation. Some operations, such as directory change notification, cannot be made synchronous; and some, such as oplocks, cannot be made asynchronous.

For more information about returning status from a dispatch routine, see [Constraints on Dispatch Routines](constraints-on-dispatch-routines.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Returning%20Status%20from%20Dispatch%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


