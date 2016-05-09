---
title: Writing Preoperation and Postoperation Callback Routines
description: Writing Preoperation and Postoperation Callback Routines
ms.assetid: ad706d01-7a14-4730-8189-c465637987dc
keywords: ["file system minifilter drivers WDK , preoperation callback routine", "minifilter drivers WDK , preoperation callback routine", "preoperation callback routines WDK file system minifilter , about preoperation callback routines", "postoperation callback routines WDK file system minifilter , about postoperation callback routines", "file system minifilter drivers WDK , postoperation callback routines", "minifilter drivers WDK , postoperation callback routines", "preoperation callback routines WDK file system minifilter", "postoperation callback routines WDK file system minifilter", "I/O WDK file systems", "callback routines WDK file system", "filtering I/O operations WDK file system minifilter"]
---

# Writing Preoperation and Postoperation Callback Routines


## <span id="ddk_writing_preoperation_and_postoperation_callback_routines_if"></span><span id="DDK_WRITING_PREOPERATION_AND_POSTOPERATION_CALLBACK_ROUTINES_IF"></span>


In its **DriverEntry** routine, a minifilter driver can register up to one [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) and up to one [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107) for each type of I/O operation that it needs to filter.

Unlike a legacy file system filter driver, a minifilter driver can choose which types of I/O operations to filter. A minifilter driver can register a preoperation callback routine for a given type of I/O operation without registering a postoperation callback, and vice versa. The minifilter driver receives only those I/O operations for which it has registered a preoperation or postoperation callback routine.

A *preoperation callback routine* is similar to a dispatch routine in the legacy filter driver model. When the filter manager processes an I/O operation, it calls the preoperation callback routine of each minifilter driver in the minifilter driver instance stack that has registered one for this type of I/O operation. The topmost minifilter driver in the stack--that is, the one whose instance has the highest altitude--receives the operation first. When that minifilter driver finishes processing the operation, it returns the operation to the filter manager, which then passes the operation to the next-highest minifilter driver, and so on. When all minifilter drivers in the minifilter driver instance stack have processed the I/O operation--unless a minifilter driver has completed the I/O operation--the filter manager sends the operation to legacy filters and the file system.

A *postoperation callback routine* is similar to a completion routine in the legacy filter driver model. Completion processing for an I/O operation begins when the I/O manager passes the operation to the file system and legacy filters that have registered completion routines for the operation. After these completion routines have finished, the filter manager performs completion processing for the operation. The filter manager then calls the postoperation callback routine of each minifilter driver in the minifilter driver instance stack that has registered one for this type of I/O operation. The bottom minifilter driver in the stack--that is, the one whose instance has the lowest altitude--receives the operation first. When that minifilter driver finishes processing the operation, it returns it to the filter manager, which then passes the operation to the next-lowest minifilter driver, and so on.

This section includes:

[Registering Preoperation and Postoperation Callback Routines](registering-preoperation-and-postoperation-callback-routines.md)

[Filtering I/O Operations in a Minifilter Driver](filtering-i-o-operations-in-a-minifilter-driver.md)

[Writing Preoperation Callback Routines](writing-preoperation-callback-routines.md)

[Writing Postoperation Callback Routines](writing-postoperation-callback-routines.md)

[Modifying the Parameters for an I/O Operation](modifying-the-parameters-for-an-i-o-operation.md)

[Determining the Buffering Method for an I/O Operation](determining-the-buffering-method-for-an-i-o-operation.md)

[Accessing the User Buffers for an I/O Operation](accessing-the-user-buffers-for-an-i-o-operation.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Writing%20Preoperation%20and%20Postoperation%20Callback%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




