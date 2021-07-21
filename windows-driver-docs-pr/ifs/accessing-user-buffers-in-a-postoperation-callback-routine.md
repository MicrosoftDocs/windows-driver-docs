---
title: Accessing User Buffers in a Postoperation Callback Routine
description: Accessing User Buffers in a Postoperation Callback Routine
keywords:
- postoperation callback routines WDK file system minifilter , buffers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing User Buffers in a Postoperation Callback Routine


## <span id="ddk_accessing_user_buffers_in_a_postoperation_callback_routine_if"></span><span id="DDK_ACCESSING_USER_BUFFERS_IN_A_POSTOPERATION_CALLBACK_ROUTINE_IF"></span>


A minifilter driver [**postoperation callback routine**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_post_operation_callback) should treat a buffer in an IRP-based I/O operation as follows:

-   Check whether an MDL exists for the buffer. The MDL pointer can be found in the *MdlAddress* or *OutputMdlAddress* parameter in the [**FLT\_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) for the operation. Minifilter drivers can call [**FltDecodeParameters**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdecodeparameters) to query for the MDL pointer.

    One method for obtaining a valid MDL is to look for the IRP\_MN\_MDL flag in the **MinorFunction** member of the I/O parameter block, [**FLT\_IO\_PARAMETER\_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block), in the callback data. The following example shows how to check for the IRP\_MN\_MDL flag.

    ```ManagedCPlusPlus
    NTSTATUS status;
    PMDL *ReadMdl = NULL;
    PVOID ReadAddress = NULL;

    if (FlagOn(CallbackData->Iopb->MinorFunction, IRP_MN_MDL))
    {
        ReadMdl = &CallbackData->Iopb->Parameters.Read.MdlAddress;
    }
    ```

    However, the IRP\_MN\_MDL flag can be set only for read and write operations. It is best to use [**FltDecodeParameters**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdecodeparameters) to retrieve an MDL, because the routine checks for a valid MDL for any operation. In the following example, only the MDL parameter is returned if valid.

    ```ManagedCPlusPlus
    NTSTATUS status;
    PMDL *ReadMdl = NULL;
    PVOID ReadAddress = NULL;

    status = FltDecodeParameters(CallbackData, &ReadMdl, NULL, NULL, NULL);
    ```

-   If an MDL exists for the buffer, call [**MmGetSystemAddressForMdlSafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdlsafe) to obtain the system address for the buffer and then use this address to access the buffer. (**MmGetSystemAddressForMdlSafe** can be called at IRQL &lt;= DISPATCH\_LEVEL.)

    Continuing from the previous example, the following code obtains the system address.

    ```ManagedCPlusPlus
    if (*ReadMdl != NULL)
    {
        ReadAddress = MmGetSystemAddressForMdlSafe(*ReadMdl, NormalPagePriority);
        if (ReadAddress == NULL)
        {
            CallbackData->IoStatus.Status = STATUS_INSUFFICIENT_RESOURCES;
            CallbackData->IoStatus.Information = 0;
        }
    }
    ```

-   If there is no MDL for the buffer, check whether the system buffer flag is set for the operation by using the [**FLT\_IS\_SYSTEM\_BUFFER**](/previous-versions/ff544663(v=vs.85)) macro.

    -   If the FLT\_IS\_SYSTEM\_BUFFER macro returns **TRUE**, the operation uses buffered I/O, and the buffer can safely be accessed at IRQL = DISPATCH\_LEVEL.

    -   If the FLT\_IS\_SYSTEM\_BUFFER macro returns **FALSE**, the buffer cannot safely be accessed at IRQL = DISPATCH\_LEVEL. If the postoperation callback routine can be called at DISPATCH\_LEVEL, it must call [**FltDoCompletionProcessingWhenSafe**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdocompletionprocessingwhensafe) to pend the operation until it can be processed at IRQL &lt;= APC\_LEVEL. The callback routine that is pointed to by the *SafePostCallback* parameter of **FltDoCompletionProcessingWhenSafe** should first call [**FltLockUserBuffer**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltlockuserbuffer) to lock the buffer and then call [**MmGetSystemAddressForMdlSafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdlsafe) to obtain the system address for the buffer.

A postoperation callback routine should treat a buffer in a fast I/O operation as follows:

-   Use the buffer address to access the buffer (because a fast I/O operation cannot have an MDL).

-   To ensure that a user-space buffer address is valid, the minifilter driver must use a routine such as [**ProbeForRead**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforread) or [**ProbeForWrite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforwrite), enclosing all buffer references in **try**/**except** blocks.

-   The postoperation callback routine for a fast I/O operation is guaranteed to be called in the correct thread context.

-   The postoperation callback routine for a fast I/O operation is guaranteed to be called at IRQL &lt;= APC\_LEVEL, so it can safely call routines such as [**FltLockUserBuffer**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltlockuserbuffer).

The following example code fragment checks for the system buffer or fast I/O flags for a directory control operation and defers completion processing if necessary.

```CSS
if (*DirectoryControlMdl == NULL)
{
    if (FLT_IS_SYSTEM_BUFFER(CallbackData) || FLT_IS_FASTIO_OPERATION(CallbackData))
    {
        dirBuffer = CallbackData->Iopb->Parameters.DirectoryControl.QueryDirectory.DirectoryBuffer;
    }
    else
    {
        // Defer processing until safe.
        if (!FltDoCompletionProcessingWhenSafe(CallbackData, FltObjects, CompletionContext, Flags, ProcessPostDirCtrlWhenSafe, &retValue))
        {
            CallbackData->IoStatus.Status = STATUS_UNSUCCESSFUL;
            CallbackData->IoStatus.Information = 0;
        }
    }
}
```

For operations that can be either fast I/O or IRP-based, all buffer references should be enclosed in **try**/**except** blocks. Although you do not have to enclose these references for IRP-based operations that use buffered I/O, the **try**/**except** blocks are a safe precaution.

 

