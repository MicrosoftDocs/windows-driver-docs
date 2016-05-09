---
title: Accessing the User Buffers for an I/O Operation
author: windows-driver-content
description: Accessing the User Buffers for an I/O Operation
ms.assetid: 0f4334bf-eec9-4667-af02-537e3357d872
keywords: ["buffers WDK file system minifilter", "FLT_PARAMETERS", "memory descriptor lists WDK file system minifilter", "MDLs WDK file systems", "I/O WDK file systems", "IRP-based I/O operations WDK file system minifilter"]
---

# Accessing the User Buffers for an I/O Operation


## <span id="ddk_accessing_the_user_buffers_for_an_io_operation_if"></span><span id="DDK_ACCESSING_THE_USER_BUFFERS_FOR_AN_IO_OPERATION_IF"></span>


The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for an I/O operation contains the operation-specific parameters for the operation, including buffer addresses and memory descriptor lists (MDL) for any buffers that are used in the operation.

For IRP-based I/O operations, the buffers for the operation can be specified by using:

-   MDL only (typically for paging I/O)

-   Buffer address only

-   Buffer address and MDL

For fast I/O operations, only the user-space buffer address is specified. Fast I/O operations that have buffers always use neither buffered nor direct I/O and thus never have MDL parameters.

The following topics provide guidelines for handling buffer addresses and MDLs for IRP-based and fast I/O operations in minifilter driver [**preoperation callback routines**](https://msdn.microsoft.com/library/windows/hardware/ff551109) and [**postoperation callback routines**](https://msdn.microsoft.com/library/windows/hardware/ff551107):

[Accessing User Buffers in a Preoperation Callback Routine](accessing-user-buffers-in-a-preoperation-callback-routine.md)

[Accessing User Buffers in a Postoperation Callback Routine](accessing-user-buffers-in-a-postoperation-callback-routine.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Accessing%20the%20User%20Buffers%20for%20an%20I/O%20Operation%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


