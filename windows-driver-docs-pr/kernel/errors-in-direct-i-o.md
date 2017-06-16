---
title: Errors in Direct I/O
author: windows-driver-content
description: Errors in Direct I/O
ms.assetid: 9efc2875-3402-4e2e-871b-3cc1d8f45360
keywords: ["reliability WDK kernel , direct I/O", "direct I/O WDK kernel", "I/O WDK kernel , direct I/O", "zero-length buffers WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Errors in Direct I/O


## <a href="" id="ddk-errors-in-direct-i-o-kg"></a>


The most common direct I/O problem is failing to handle zero-length buffers correctly. Because the I/O manager does not create MDLs for zero-length transfers, a zero-length buffer results in a **NULL** value at **Irp-&gt;MdlAddress**.

To map the address space, drivers should use [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559), which returns **NULL** if mapping fails, as it will if a driver passes a **NULL** **MdlAddress**. Drivers should always check for a **NULL** return before attempting to use the returned address.

Direct I/O involves double-mapping the user's address space to a system address buffer, so that two different virtual addresses have the same physical address. Double-mapping has the following consequences, which can sometimes cause problems for drivers:

-   The offset into the virtual page of the user's address becomes the offset into the system page.

    Access beyond the end of these system buffers may go unnoticed for long periods of time depending on the page granularity of the mapping. Unless a caller's buffer is allocated near the end of a page, data written beyond the end of the buffer will nevertheless appear in the buffer, and the caller will be unaware that any error has occurred. If the end of the buffer coincides with the end of a page, the system virtual addresses beyond the end could point to anything or could be invalid. Such problems can be extremely difficult to find.

-   If the calling process has another thread that modifies the user's mapping of the memory, the contents of the system buffer will change when the user's memory mapping changes.

    In this situation, using the system buffer to store scratch data can cause problems. Two fetches from the same memory location might yield different values.

    The following code snippet receives a string in a direct I/O request, then tries to convert that string to uppercase characters:

    ```
    PWCHAR  PortName = NULL;

    PortName = (PWCHAR)MmGetSystemAddressForMdlSafe(irp->MdlAddress, NormalPagePriority);

    //
    // Null-terminate the PortName so that RtlInitUnicodeString will not
    // be invalid.
    //
    PortName[Size / sizeof(WCHAR) - 1] = UNICODE_NULL;

    RtlInitUnicodeString(&amp;AdapterName, PortName);
    ```

    Because the buffer might not be correctly formed, the code attempts to force a Unicode **NULL** as the last buffer character. However, if the underlying physical memory is doubly mapped to both a user- and a kernel-mode address, another thread in the process can overwrite the buffer as soon as this write operation completes.

    Conversely, if the **NULL** is not present, then the call to **RtlInitUnicodeString** can exceed the range of the buffer and possibly cause a bug check if it falls outside the system mapping.

If a driver creates and maps its own MDL, it should ensure that it accesses the MDL only with the method for which it has probed. That is, when the driver calls [**MmProbeAndLockPages**](https://msdn.microsoft.com/library/windows/hardware/ff554664), it specifies an access method (**IoReadAccess**, **IoWriteAccess**, or **IoModifyAccess**). If the driver specifies **IoReadAccess**, it must not later attempt to write to the system buffer made available by [**MmGetSystemAddressForMdl**](https://msdn.microsoft.com/library/windows/hardware/ff554556) or [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Errors%20in%20Direct%20I/O%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


