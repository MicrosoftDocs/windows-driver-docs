---
title: Failing an I/O Operation in a Postoperation Callback Routine
author: windows-driver-content
description: Failing an I/O Operation in a Postoperation Callback Routine
ms.assetid: 45897bca-1573-42c5-ad00-3198b7362d9e
keywords: ["postoperation callback routines WDK file system minifilter , failing operations", "failing I/O operations WDK file system minifilter"]
---

# Failing an I/O Operation in a Postoperation Callback Routine


## <span id="ddk_failing_an_io_operation_in_a_postoperation_callback_routine_if"></span><span id="DDK_FAILING_AN_IO_OPERATION_IN_A_POSTOPERATION_CALLBACK_ROUTINE_IF"></span>


A minifilter driver's [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107) can fail a successful I/O operation, but simply failing an I/O operation does not undo the effect of the operation. The minifilter driver is responsible for performing any processing that is needed to undo the operation.

For example, a minifilter driver's post-create callback routine can fail a successful IRP\_MJ\_CREATE operation by performing the following steps:

1.  Calling [**FltCancelFileOpen**](https://msdn.microsoft.com/library/windows/hardware/ff541784) to close the file that was created or opened by the create operation. Note that **FltCancelFileOpen** does not undo any modifications to the file. For example, **FltCancelFileOpen** does not delete a newly created file or restore a truncated file to its previous size.

2.  Setting the callback data structure's **IoStatus.Status** field to the final NTSTATUS value for the operation. This value must be a valid error NTSTATUS value, such as STATUS\_ACCESS\_DENIED.

3.  Setting the callback data structure's **IoStatus.Information** field to zero.

4.  Returning FLT\_POSTOP\_FINISHED\_PROCESSING.

When setting the callback data structure's **IoStatus.Status** field to the final NTSTATUS value for the operation, the minifilter driver must specify a valid error NTSTATUS value. Note that minifilter drivers cannot specify STATUS\_FLT\_DISALLOW\_FAST\_IO; only the filter manager can use this NTSTATUS value.

Callers of [**FltCancelFileOpen**](https://msdn.microsoft.com/library/windows/hardware/ff541784) must be running at IRQL &lt;= APC\_LEVEL. However, a minifilter driver can safely call this routine from a post-create callback routine, because, for IRP\_MJ\_CREATE operations, the postoperation callback routine is called at IRQL = PASSIVE\_LEVEL, in the context of the thread that originated the create operation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Failing%20an%20I/O%20Operation%20in%20a%20Postoperation%20Callback%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


