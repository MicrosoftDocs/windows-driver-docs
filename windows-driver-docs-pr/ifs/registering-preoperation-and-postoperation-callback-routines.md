---
title: Registering Preoperation and Postoperation Callback Routines
description: Registering Preoperation and Postoperation Callback Routines
ms.assetid: 9f89ca46-8a8f-422f-9dbe-2620b944a3ae
keywords: ["preoperation callback routines WDK file system minifilter , registering", "postoperation callback routines WDK file system minifilter , registering", "registering callback routines"]
---

# Registering Preoperation and Postoperation Callback Routines


## <span id="ddk_registering_preoperation_and_postoperation_callback_routines_if"></span><span id="DDK_REGISTERING_PREOPERATION_AND_POSTOPERATION_CALLBACK_ROUTINES_IF"></span>


To register [**preoperation callback routines**](https://msdn.microsoft.com/library/windows/hardware/ff551109) and [**postoperation callback routines**](https://msdn.microsoft.com/library/windows/hardware/ff551107), a minifilter driver makes a single call to [**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305) in its **DriverEntry** routine. For the *Registration* parameter in **FltRegisterFilter**, the minifilter driver passes a pointer to an [**FLT\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544811) structure. The **OperationRegistration** member of this structure contains a pointer to an array of [**FLT\_OPERATION\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544668) structures, one for each type of I/O operation that the minifilter driver must filter.

Each FLT\_OPERATION\_REGISTRATION structure in the array, except for the last one, contains the following information:

-   The major function code for the operation

-   For read and write operations (IRP\_MJ\_READ and IRP\_MJ\_WRITE), a set of flags that specify whether to ignore cached I/O or paging I/O or both for IRP-based I/O operations

-   Entry points for up to one preoperation callback routine and one postoperation callback routine

The last element in the array must be {IRP\_MJ\_OPERATION\_END}.

The following code example, which is taken from the Scanner sample minifilter driver, shows an array of FLT\_OPERATION\_REGISTRATION structures. The Scanner sample minifilter driver registers preoperation and postoperation callback routines for IRP\_MJ\_CREATE and preoperation callback routines for IRP\_MJ\_CLEANUP and IRP\_MJ\_WRITE operations.

```
const FLT_OPERATION_REGISTRATION Callbacks[] = {
    {IRP_MJ_CREATE,
     0,
     ScannerPreCreate,
     ScannerPostCreate},
    {IRP_MJ_CLEANUP,
     0, 
     ScannerPreCleanup,
     NULL},
    {IRP_MJ_WRITE,
     0, 
     ScannerPreWrite,
     NULL},
    {IRP_MJ_OPERATION_END}
};
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Registering%20Preoperation%20and%20Postoperation%20Callback%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




