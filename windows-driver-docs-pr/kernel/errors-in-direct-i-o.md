---
title: Errors in Direct I/O
description: Errors in Direct I/O
ms.assetid: 9efc2875-3402-4e2e-871b-3cc1d8f45360
keywords: ["reliability WDK kernel , direct I/O", "direct I/O WDK kernel", "I/O WDK kernel , direct I/O", "zero-length buffers WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Errors in Direct I/O





The most common direct I/O problem is failing to handle zero-length buffers correctly. Because the I/O manager does not create MDLs for zero-length transfers, a zero-length buffer results in a **NULL** value at **Irp-&gt;MdlAddress**.

To map the address space, drivers should use [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559), which returns **NULL** if mapping fails, as it will if a driver passes a **NULL** **MdlAddress**. Drivers should always check for a **NULL** return before attempting to use the returned address.

Direct I/O involves double-mapping the user's address space to a system address buffer, so that two different virtual addresses have the same physical address. Double-mapping has the following consequences, which can sometimes cause problems for drivers:

-   The offset into the virtual page of the user's address becomes the offset into the system page.

    Access beyond the end of these system buffers may go unnoticed for long periods of time depending on the page granularity of the mapping. Unless a caller's buffer is allocated near the end of a page, data written beyond the end of the buffer will nevertheless appear in the buffer, and the caller will be unaware that any error has occurred. If the end of the buffer coincides with the end of a page, the system virtual addresses beyond the end could point to anything or could be invalid. Such problems can be extremely difficult to find.

-   If the calling process has another thread that modifies the user's mapping of the memory, the contents of the system buffer will change when the user's memory mapping changes.

    In this situation, using the system buffer to store scratch data can cause problems. Two fetches from the same memory location might yield different values.

    The following code snippet receives a string in a direct I/O request, then tries to convert that string to uppercase characters:

    ```cpp
    PWCHAR  PortName = NULL;

    PortName = (PWCHAR)MmGetSystemAddressForMdlSafe(irp->MdlAddress, NormalPagePriority);

    //
    // Null-terminate the PortName so that RtlInitUnicodeString will not
    // be invalid.
    //
    PortName[Size / sizeof(WCHAR) - 1] = UNICODE_NULL;

    RtlInitUnicodeString(&AdapterName, PortName);
    ```

    Because the buffer might not be correctly formed, the code attempts to force a Unicode **NULL** as the last buffer character. However, if the underlying physical memory is doubly mapped to both a user- and a kernel-mode address, another thread in the process can overwrite the buffer as soon as this write operation completes.

    Conversely, if the **NULL** is not present, then the call to **RtlInitUnicodeString** can exceed the range of the buffer and possibly cause a bug check if it falls outside the system mapping.

If a driver creates and maps its own MDL, it should ensure that it accesses the MDL only with the method for which it has probed. That is, when the driver calls [**MmProbeAndLockPages**](https://msdn.microsoft.com/library/windows/hardware/ff554664), it specifies an access method (**IoReadAccess**, **IoWriteAccess**, or **IoModifyAccess**). If the driver specifies **IoReadAccess**, it must not later attempt to write to the system buffer made available by [**MmGetSystemAddressForMdl**](https://msdn.microsoft.com/library/windows/hardware/ff554556) or [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559).

 

 




