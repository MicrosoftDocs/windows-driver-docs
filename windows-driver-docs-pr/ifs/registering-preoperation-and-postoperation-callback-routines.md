---
title: Registering Preoperation and Postoperation Callback Routines
description: Registering Preoperation and Postoperation Callback Routines
ms.assetid: 9f89ca46-8a8f-422f-9dbe-2620b944a3ae
keywords:
- preoperation callback routines WDK file system minifilter , registering
- postoperation callback routines WDK file system minifilter , registering
- registering callback routines
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering Preoperation and Postoperation Callback Routines


## <span id="ddk_registering_preoperation_and_postoperation_callback_routines_if"></span><span id="DDK_REGISTERING_PREOPERATION_AND_POSTOPERATION_CALLBACK_ROUTINES_IF"></span>


To register [**preoperation callback routines**](https://msdn.microsoft.com/library/windows/hardware/ff551109) and [**postoperation callback routines**](https://msdn.microsoft.com/library/windows/hardware/ff551107), a minifilter driver makes a single call to [**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305) in its **DriverEntry** routine. For the *Registration* parameter in **FltRegisterFilter**, the minifilter driver passes a pointer to an [**FLT\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544811) structure. The **OperationRegistration** member of this structure contains a pointer to an array of [**FLT\_OPERATION\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544668) structures, one for each type of I/O operation that the minifilter driver must filter.

Each FLT\_OPERATION\_REGISTRATION structure in the array, except for the last one, contains the following information:

-   The major function code for the operation. See [FLT_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_parameters) for information on I/O operations, and their request-type-specific parameters.

-   For read and write operations (IRP\_MJ\_READ and IRP\_MJ\_WRITE), a set of flags that specify whether to ignore cached I/O or paging I/O or both for IRP-based I/O operations

-   Entry points for up to one preoperation callback routine and one postoperation callback routine

The last element in the array must be {IRP\_MJ\_OPERATION\_END}.

The following code example, which is taken from the Scanner sample minifilter driver, shows an array of FLT\_OPERATION\_REGISTRATION structures. The Scanner sample minifilter driver registers preoperation and postoperation callback routines for IRP\_MJ\_CREATE and preoperation callback routines for IRP\_MJ\_CLEANUP and IRP\_MJ\_WRITE operations.

```cpp
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

 

 




