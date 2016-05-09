---
title: Passing an I/O Operation Down the Minifilter Driver Instance Stack
author: windows-driver-content
description: Passing an I/O Operation Down the Minifilter Driver Instance Stack
ms.assetid: b2661e1e-2190-4def-be6c-27057c631304
keywords: ["preoperation callback routines WDK file system minifilter , passing down driver instance stack", "passing I/O ops down minifilter driver stack WDK file system"]
---

# Passing an I/O Operation Down the Minifilter Driver Instance Stack


## <span id="ddk_passing_an_io_operation_down_the_minifilter_instance_stack_if"></span><span id="DDK_PASSING_AN_IO_OPERATION_DOWN_THE_MINIFILTER_INSTANCE_STACK_IF"></span>


When a minifilter driver's [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) or work routine returns an I/O operation to the filter manager, the filter manager sends the operation to minifilter drivers below the current minifilter driver in the minifilter driver instance stack and to legacy filters and the file system for further processing.

A minifilter driver's preoperation callback routine returns an I/O operation to the filter manager for further processing by returning one of the following status values:

-   FLT\_PREOP\_SUCCESS\_NO\_CALLBACK (all operation types)

-   FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK (all operation types)

-   FLT\_PREOP\_SYNCHRONIZE (IRP-based I/O operations only)

**Note**   Although FLT\_PREOP\_SYNCHRONIZE should be returned only for IRP-based I/O operations, you can return this status value for other operation types. If it is returned for an I/O operation that is not an IRP-based I/O operation, the filter manager treats this return value as if it were FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK.

 

Alternatively, the work routine for an operation that was pended in a preoperation callback routine returns an I/O operation to the filter manager by passing one of the preceding status values in the *CallbackStatus* parameter when it calls [**FltCompletePendedPreOperation**](https://msdn.microsoft.com/library/windows/hardware/ff541913) to resume processing for the pended I/O operation.

This section includes:

[Returning FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK](returning-flt-preop-success-with-callback.md)

[Returning FLT\_PREOP\_SUCCESS\_NO\_CALLBACK](returning-flt-preop-success-no-callback.md)

[Returning FLT\_PREOP\_SYNCHRONIZE](returning-flt-preop-synchronize.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Passing%20an%20I/O%20Operation%20Down%20the%20Minifilter%20Driver%20Instance%20Stack%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


