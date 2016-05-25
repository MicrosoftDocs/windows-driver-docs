---
title: Disallowing a Fast I/O Operation in a Preoperation Callback Routine
author: windows-driver-content
description: Disallowing a Fast I/O Operation in a Preoperation Callback Routine
ms.assetid: 20797d8c-ffcf-46df-b870-839d5c02d2d4
keywords: ["preoperation callback routines WDK file system minifilter , disallowing fast I/O", "disallow fast I/O operations WDK file system minifilter", "fast I/O disallowed WDK file system"]
---

# Disallowing a Fast I/O Operation in a Preoperation Callback Routine


## <span id="ddk_disallowing_a_fast_io_operation_in_a_preoperation_callback_routine"></span><span id="DDK_DISALLOWING_A_FAST_IO_OPERATION_IN_A_PREOPERATION_CALLBACK_ROUTINE"></span>


In certain circumstances, a minifilter driver might choose to disallow a fast I/O operation instead of completing it. Disallowing a fast I/O operation prevents the fast I/O path from being used for the operation.

Like completing an I/O operation, disallowing a fast I/O operation means to halt processing on it and return it to the filter manager. However, disallowing a fast I/O operation is different from completing it. If a minifilter driver disallows a fast I/O operation that was issued by the I/O manager, the I/O manager may reissue the same operation as an equivalent IRP-based operation.

When a minifilter driver's [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) disallows a fast I/O operation, the filter manager does the following:

-   Does not send the operation to minifilter drivers below the current minifilter driver, to legacy filters, or to the file system.

-   Calls the [**postoperation callback routines**](https://msdn.microsoft.com/library/windows/hardware/ff551107) of the minifilter drivers above the current minifilter driver in the minifilter driver instance stack.

-   Does not call the current minifilter driver's postoperation callback routine for the operation, if one exists.

A minifilter driver disallows a fast I/O operation by returning FLT\_PREOP\_DISALLOW\_FASTIO from the preoperation callback routine for the operation.

The preoperation callback routine should not set the callback data structure's **IoStatus.Status** field, because the filter manager automatically sets this field to STATUS\_FLT\_DISALLOW\_FAST\_IO.

FLT\_PREOP\_DISALLOW\_FASTIO can only be returned for fast I/O operations. To determine whether an operation is a fast I/O operation, see [**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645).

Minifilter drivers cannot return FLT\_PREOP\_DISALLOW\_FASTIO for IRP\_MJ\_SHUTDOWN, IRP\_MJ\_VOLUME\_MOUNT, or IRP\_MJ\_VOLUME\_DISMOUNT operations.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Disallowing%20a%20Fast%20I/O%20Operation%20in%20a%20Preoperation%20Callback%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


