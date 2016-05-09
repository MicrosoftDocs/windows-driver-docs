---
title: How Completion Processing Is Performed
author: windows-driver-content
description: How Completion Processing Is Performed
ms.assetid: 5741c226-9781-4d9a-b6dd-d8ecc17c4c6f
keywords: ["IRP completion routines WDK file system , processing stages"]
---

# How Completion Processing Is Performed


## <span id="ddk_how_completion_processing_is_performed_if"></span><span id="DDK_HOW_COMPLETION_PROCESSING_IS_PERFORMED_IF"></span>


Completion processing is performed in two stages. The first stage is performed in an arbitrary thread context, at IRQL &lt;= DISPATCH\_LEVEL. In this stage, the following tasks are performed:

-   Each completion routine registered for the IRP is called in turn, beginning with the lowest IRP stack location. If a completion routine returns STATUS\_MORE\_PROCESSING\_REQUIRED, completion processing is halted.

-   If the IRP contains a memory descriptor list (MDL), any physical pages mapped by the MDL are unlocked.

-   The second phase of I/O completion is queued to the target (requesting) thread as a special kernel APC.

The second stage is performed in the context of the thread that originated the I/O request. It is executed as a special kernel APC and therefore runs at IRQL APC\_LEVEL. In this stage, the following tasks are performed:

-   If the IRP represents a buffered operation, the contents of **Irp-&gt;AssociatedIrp.SystemBuffer** are copied to **Irp-&gt;UserBuffer**.

-   If the IRP contains an MDL, the MDL is freed.

-   The contents of **Irp-&gt;IoStatus** are copied to **Irp-&gt;UserIosb** so that the originator of the I/O request can see the final status of the operation.

-   If an event has been supplied in **Irp-&gt;UserEvent**, it is signaled. Otherwise, if there is a file object for this IRP, its event is signaled.

-   If the IRP was created by calling [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) or [**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330), it is dequeued from the thread's pending I/O request list.

-   A user APC is queued, if the caller requested one.

-   The IRP is freed.

**Note**   If completion processing for an IRP is halted because a completion routine returned STATUS\_MORE\_PROCESSING\_REQUIRED, it can be resumed by calling [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) on the same IRP. When this happens, first-stage processing resumes, beginning with the completion routine for the driver immediately above the one whose completion routine returned STATUS\_MORE\_PROCESSING\_REQUIRED.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20How%20Completion%20Processing%20Is%20Performed%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


