---
title: Sending I/O Requests Synchronously
description: Sending I/O Requests Synchronously
ms.assetid: e7e9f2d2-afc5-439b-8a04-72d117114fae
keywords:
- general I/O targets WDK KMDF , sending I/O requests to
- sending I/O requests WDK KMDF
- sending I/O requests WDK KMDF , synchronous
- synchronously sending I/O requests WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sending I/O Requests Synchronously





The following table lists the I/O target object methods that your driver can call to send I/O requests synchronously to an I/O target. For detailed information about how to use these methods, see the methods' reference pages.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Method</th>
<th align="left">Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548669" data-raw-source="[&lt;strong&gt;WdfIoTargetSendReadSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548669)"><strong>WdfIoTargetSendReadSynchronously</strong></a></p></td>
<td align="left"><p>Sends a read request</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548672" data-raw-source="[&lt;strong&gt;WdfIoTargetSendWriteSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548672)"><strong>WdfIoTargetSendWriteSynchronously</strong></a></p></td>
<td align="left"><p>Sends a write request</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548660" data-raw-source="[&lt;strong&gt;WdfIoTargetSendIoctlSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548660)"><strong>WdfIoTargetSendIoctlSynchronously</strong></a></p></td>
<td align="left"><p>Sends a device control request</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548656" data-raw-source="[&lt;strong&gt;WdfIoTargetSendInternalIoctlSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548656)"><strong>WdfIoTargetSendInternalIoctlSynchronously</strong></a></p></td>
<td align="left"><p>Sends an internal device control request</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548651" data-raw-source="[&lt;strong&gt;WdfIoTargetSendInternalIoctlOthersSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548651)"><strong>WdfIoTargetSendInternalIoctlOthersSynchronously</strong></a></p></td>
<td align="left"><p>Sends a non-standard internal device control request</p></td>
</tr>
</tbody>
</table>

 

You can also send requests synchronously by calling [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027), but you have to format the request first by following the rules that are described in [Sending I/O Requests Asynchronously](sending-i-o-requests-asynchronously.md).

Sending I/O requests to an I/O target synchronously is simpler to program than sending I/O requests [asynchronously](sending-i-o-requests-asynchronously.md). However, you should use the following guidelines to help you decide if synchronous I/O is appropriate for your driver:

-   You can use synchronous I/O if your driver does not send many I/O requests and if system or device performance is not reduced because your driver waits for each I/O request to complete.

-   If your driver must handle many I/O requests in short periods of time, you probably cannot allow your driver to wait for each request to complete before sending the next request. Otherwise, your driver might lose data or reduce the performance of its device (and, possibly, the entire system). In such cases, asynchronous I/O might be the better choice.

-   Synchronous I/O is useful for handling operations that must start and finish without additional concurrent activity. Such operations might include resetting a USB pipe or reading device registers.

-   Most times, your driver should specify a time-out value when it calls an object method that sends an I/O request synchronously. If your driver does not specify a time-out value, and if a device or a lower-level driver fails to respond, your driver can stall. As a result, the user can experience an unresponsive application. In addition, other drivers might not be able to obtain system resources, such as [work items](using-framework-work-items.md), if your driver is not releasing them.

-   If drivers above and below yours in the stack require operations to proceed synchronously, your driver should use synchronous I/O. Therefore, you should learn about the requirements of other drivers that might exist in the driver stack.

The following example shows how to send a synchronous I/O control (IOCTL) request:

```cpp
NTSTATUS                status;
    WDF_MEMORY_DESCRIPTOR   inputDesc, outputDesc;
    PWDF_MEMORY_DESCRIPTOR  pInputDesc = NULL, pOutputDesc = NULL;
    ULONG_PTR               bytesReturned;

    UNREFERENCED_PARAMETER(FileObject);

    if (InputBuffer) {
        WDF_MEMORY_DESCRIPTOR_INIT_BUFFER(&inputDesc,
                                    InputBuffer,
                                    InputBufferLength);
        pInputDesc = &inputDesc;
    }

    if (OutputBuffer) {
        WDF_MEMORY_DESCRIPTOR_INIT_BUFFER(&outputDesc,
                                    OutputBuffer,
                                    OutputBufferLength);
        pOutputDesc = &outputDesc;
    }

    status = WdfIoTargetSendIoctlSynchronously(
                        IoTarget,
                        WDF_NO_HANDLE, // Request
                        IoctlControlCode,
                        pInputDesc,
                        pOutputDesc,
                        NULL, // PWDF_REQUEST_SEND_OPTIONS
                        &bytesReturned);
    if (!NT_SUCCESS(status)) {
         DEBUGP(MP_ERROR,
        ("WdfIoTargetSendIoctlSynchronously failed 0x%x\n",
          status));
    }

    *BytesReadOrWritten = (ULONG)bytesReturned;
```

 

 





