---
title: Registering Preoperation and Postoperation Callback Routines
description: Registering Preoperation and Postoperation Callback Routines
keywords:
- preoperation callback routines WDK file system minifilter , registering
- postoperation callback routines WDK file system minifilter , registering
- registering callback routines
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering Preoperation and Postoperation Callback Routines


## <span id="ddk_registering_preoperation_and_postoperation_callback_routines_if"></span><span id="DDK_REGISTERING_PREOPERATION_AND_POSTOPERATION_CALLBACK_ROUTINES_IF"></span>


To register [**preoperation callback routines**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_pre_operation_callback) and [**postoperation callback routines**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_post_operation_callback), a minifilter driver makes a single call to [**FltRegisterFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltregisterfilter) in its **DriverEntry** routine. For the *Registration* parameter in **FltRegisterFilter**, the minifilter driver passes a pointer to an [**FLT\_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_registration) structure. The **OperationRegistration** member of this structure contains a pointer to an array of [**FLT\_OPERATION\_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_operation_registration) structures, one for each type of I/O operation that the minifilter driver must filter.

Each FLT\_OPERATION\_REGISTRATION structure in the array, except for the last one, contains the following information:

-   The major function code for the operation. See [FLT_PARAMETERS](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) for information on I/O operations, and their request-type-specific parameters.

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

 

