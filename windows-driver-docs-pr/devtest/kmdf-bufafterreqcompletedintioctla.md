---
title: BufAfterReqCompletedIntIoctlA rule (kmdf)
description: The BufAfterReqCompletedIntIoctlA rule verifies that after a request is completed, its buffer cannot be accessed (inside EvtIoInternalDeviceControl callback only).
ms.assetid: 3635DB6D-00C7-44DD-B05A-7EAA16B18937
keywords: ["BufAfterReqCompletedIntIoctlA rule (kmdf)"]
topic_type:
- apiref
api_name:
- BufAfterReqCompletedIntIoctlA
api_type:
- NA
---

# BufAfterReqCompletedIntIoctlA rule (kmdf)


The **BufAfterReqCompletedIntIoctlA** rule verifies that after a request is completed, its buffer cannot be accessed (inside [*EvtIoInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541768) callback only). The buffer was retrieved by calling [**WdfRequestRetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550014) or [**WdfRequestRetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550018) or [**WdfRequestRetrieveUnsafeUserInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550022) or [**WdfRequestRetrieveUnsafeUserOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550024).

Within the [*EvtIoInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541768) I/O queue event callback function, the request buffer retrieved by calling [**WdfRequestRetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550014) or [**WdfRequestRetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550018) or [**WdfRequestRetrieveUnsafeUserInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550022) or [**WdfRequestRetrieveUnsafeUserOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550024) cannot be accessed after the [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945), [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948), or [**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949) methods have been called on the request. The following possible buffer access functions are considered: [**RtlMoveMemory**](https://msdn.microsoft.com/library/windows/hardware/ff562030) (with the buffer as a 1st and 2nd parameter), [**RtlZeroMemory**](https://msdn.microsoft.com/library/windows/hardware/ff563610), [**RtlCompareMemory**](https://msdn.microsoft.com/library/windows/hardware/ff561778), [**ZwReadFile**](https://msdn.microsoft.com/library/windows/hardware/ff567072), [**ZwWriteFile**](https://msdn.microsoft.com/library/windows/hardware/ff567121), [**WDF\_MEMORY\_DESCRIPTOR\_INIT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff552393), [**WdfMemoryCreatePreallocated**](https://msdn.microsoft.com/library/windows/hardware/ff548712), [**WdfMemoryAssignBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548697), [**WdfMemoryCopyFromBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548701), [**WdfMemoryCopyToBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548703).

|              |      |
|--------------|------|
| Driver model | KMDF |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>BufAfterReqCompletedIntIoctlA</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**WDF\_MEMORY\_DESCRIPTOR\_INIT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff552393)
[**WdfMemoryAssignBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548697)
[**WdfMemoryCopyFromBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548701)
[**WdfMemoryCopyToBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548703)
[**WdfMemoryCreatePreallocated**](https://msdn.microsoft.com/library/windows/hardware/ff548712)
[**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945)
[**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948)
[**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)
[**WdfRequestRetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550014)
[**WdfRequestRetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550018)
[**WdfRequestRetrieveUnsafeUserInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550022)
[**WdfRequestRetrieveUnsafeUserOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550024)
[**RtlCompareMemory**](https://msdn.microsoft.com/library/windows/hardware/ff561778)
[**RtlMoveMemory**](https://msdn.microsoft.com/library/windows/hardware/ff562030)
[**RtlZeroMemory**](https://msdn.microsoft.com/library/windows/hardware/ff563610)
[**ZwReadFile**](https://msdn.microsoft.com/library/windows/hardware/ff567072)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20BufAfterReqCompletedIntIoctlA%20rule%20%28kmdf%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




