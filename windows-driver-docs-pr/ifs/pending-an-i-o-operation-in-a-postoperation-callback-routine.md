---
title: Pending an I/O Operation in a Postoperation Callback Routine
description: Pending an I/O Operation in a Postoperation Callback Routine
ms.assetid: 126e13fb-51f6-4dcc-aa13-850921b3c752
keywords: ["postoperation callback routines WDK file system minifilter , pending operations", "pending I/O operations in callback routines WDK file system"]
---

# Pending an I/O Operation in a Postoperation Callback Routine


## <span id="ddk_pending_an_io_operation_in_a_postoperation_callback_routine_if"></span><span id="DDK_PENDING_AN_IO_OPERATION_IN_A_POSTOPERATION_CALLBACK_ROUTINE_IF"></span>


A minifilter driver's [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107) can pend an I/O operation by performing the following steps:

1.  Calling [**FltAllocateDeferredIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff541720) to allocate a work item for the I/O operation.

2.  Calling [**FltQueueDeferredIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff543449) to post the I/O operation to a system work queue.

3.  Returning FLT\_POSTOP\_MORE\_PROCESSING\_REQUIRED.

Note that the call to **FltQueueDeferredIoWorkItem** will fail if any of the following conditions are true:

-   The operation is not an IRP-based I/O operation.

-   The operation is a paging I/O operation.

-   The **TopLevelIrp** field of the current thread is not **NULL**. (For more information about how to find the value of this field, see [**IoGetTopLevelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548405).)

-   The target instance for the I/O operation is being torn down. (The filter manager indicates this situation by setting the FLTFL\_POST\_OPERATION\_DRAINING flag in the *Flags* input parameter to the postoperation callback routine.)

Minifilter drivers must be prepared to handle this failure. If your minifilter driver cannot handle such failures, you should consider using the technique that is described in [Returning FLT\_PREOP\_SYNCHRONIZE](returning-flt-preop-synchronize.md) instead of pending the I/O operation.

After the minifilter driver's postoperation callback routine returns FLT\_POSTOP\_MORE\_PROCESSING\_REQUIRED, the filter manager will not perform any further completion processing for the I/O operation until the minifilter driver's work routine calls [**FltCompletePendedPostOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541897) to return control of the operation to the filter manager. The filter manager will not perform any further processing in this situation even if the work routine sets a failure NTSTATUS value in the **IoStatus.Status** field of the callback data structure for the operation.

The work routine that dequeues and performs completion processing for the I/O operation must call **FltCompletePendedPostOperation** to return control of the operation to the filter manager.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Pending%20an%20I/O%20Operation%20in%20a%20Postoperation%20Callback%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




