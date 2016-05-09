---
title: Accessing User Buffers in a Preoperation Callback Routine
author: windows-driver-content
description: Accessing User Buffers in a Preoperation Callback Routine
ms.assetid: 16e6a9e0-3a92-471f-98e6-9a4e8eb7d4a6
keywords: ["preoperation callback routines WDK file system minifilter , buffers"]
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
        ReadMdl = &amp;CallbackData->Iopb->Parameters.Read.MdlAddress;
    }
    ```

    However, the IRP\_MN\_MDL flag can be set only for read and write operations. It is best to use [**FltDecodeParameters**](https://msdn.microsoft.com/library/windows/hardware/ff541956) to retrieve an MDL, because the routine checks for a valid MDL for any operation. In the following example, only the MDL parameter is returned if valid.

    ```ManagedCPlusPlus
    NTSTATUS status;
    PMDL *ReadMdl = NULL;
    PVOID ReadAddress = NULL;

    status = FltDecodeParameters(CallbackData, &amp;ReadMdl, NULL, NULL, NULL);
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Accessing%20User%20Buffers%20in%20a%20Preoperation%20Callback%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


