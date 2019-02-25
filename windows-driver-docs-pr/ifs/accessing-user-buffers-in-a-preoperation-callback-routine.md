---
title: Accessing User Buffers in a Preoperation Callback Routine
description: Accessing User Buffers in a Preoperation Callback Routine
ms.assetid: 16e6a9e0-3a92-471f-98e6-9a4e8eb7d4a6
keywords:
- preoperation callback routines WDK file system minifilter , buffers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing User Buffers in a Preoperation Callback Routine


## <span id="ddk_accessing_user_buffers_in_a_preoperation_callback_routine_if"></span><span id="DDK_ACCESSING_USER_BUFFERS_IN_A_PREOPERATION_CALLBACK_ROUTINE_IF"></span>


A minifilter driver's [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) should treat a buffer in an IRP-based I/O operation as follows:

-   Check whether an MDL exists for the buffer. The MDL pointer can be found in the *MdlAddress* or *OutputMdlAddress* parameter in the [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) for the operation. Minifilter drivers can call [**FltDecodeParameters**](https://msdn.microsoft.com/library/windows/hardware/ff541956) to query for the MDL pointer.

    One method for obtaining a valid MDL is to look for the IRP\_MN\_MDL flag in the **MinorFunction** member of the I/O parameter block, [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638), in the callback data. The following example shows how to check for the IRP\_MN\_MDL flag.

    ```ManagedCPlusPlus
    NTSTATUS status;
    PMDL *ReadMdl = NULL;
    PVOID ReadAddress = NULL;

    if (FlagOn(CallbackData->Iopb->MinorFunction, IRP_MN_MDL))
    {
        ReadMdl = &CallbackData->Iopb->Parameters.Read.MdlAddress;
    }
    ```

    However, the IRP\_MN\_MDL flag can be set only for read and write operations. It is best to use [**FltDecodeParameters**](https://msdn.microsoft.com/library/windows/hardware/ff541956) to retrieve an MDL, because the routine checks for a valid MDL for any operation. In the following example, only the MDL parameter is returned if valid.

    ```ManagedCPlusPlus
    NTSTATUS status;
    PMDL *ReadMdl = NULL;
    PVOID ReadAddress = NULL;

    status = FltDecodeParameters(CallbackData, &ReadMdl, NULL, NULL, NULL);
    ```

-   If an MDL exists for the buffer, call [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) to obtain the system address for the buffer and then use this address to access the buffer.

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

-   If there is no MDL for the buffer, use the buffer address to access the buffer. To ensure that a user-space buffer address is valid, the minifilter driver must use a routine such as [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876) or [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879), enclosing all buffer references in **try**/**except** blocks.

A preoperation callback routine should treat a buffer in a fast I/O operation as follows:

-   Use the buffer address to access the buffer (because a fast I/O operation cannot have an MDL).

-   To ensure that a user-space buffer address is valid, the minifilter driver must use a routine such as **ProbeForRead** or **ProbeForWrite**, enclosing all buffer references in **try**/**except** blocks.

For operations that can be fast I/O or IRP-based, all buffer references should be enclosed in **try**/**except** blocks. Although you do not have to enclose these references for IRP-based operations that use buffered I/O, the **try**/**except** blocks are a safe precaution.

 

 




