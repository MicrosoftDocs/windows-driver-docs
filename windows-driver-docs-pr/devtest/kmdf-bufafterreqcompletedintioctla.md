---
title: BufAfterReqCompletedIntIoctlA rule (kmdf)
description: The BufAfterReqCompletedIntIoctlA rule verifies that after a request is completed, its buffer cannot be accessed (inside EvtIoInternalDeviceControl callback only).
ms.date: 05/21/2018
keywords: ["BufAfterReqCompletedIntIoctlA rule (kmdf)"]
topic_type:
- apiref
api_name:
- BufAfterReqCompletedIntIoctlA
api_type:
- NA
ms.localizationpriority: medium
---

# BufAfterReqCompletedIntIoctlA rule (kmdf)


The **BufAfterReqCompletedIntIoctlA** rule verifies that after a request is completed, its buffer cannot be accessed (inside [*EvtIoInternalDeviceControl*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_internal_device_control) callback only). The buffer was retrieved by calling [**WdfRequestRetrieveInputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputbuffer) or [**WdfRequestRetrieveOutputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputbuffer) or [**WdfRequestRetrieveUnsafeUserInputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveunsafeuserinputbuffer) or [**WdfRequestRetrieveUnsafeUserOutputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveunsafeuseroutputbuffer).

Within the [*EvtIoInternalDeviceControl*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_internal_device_control) I/O queue event callback function, the request buffer retrieved by calling [**WdfRequestRetrieveInputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputbuffer) or [**WdfRequestRetrieveOutputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputbuffer) or [**WdfRequestRetrieveUnsafeUserInputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveunsafeuserinputbuffer) or [**WdfRequestRetrieveUnsafeUserOutputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveunsafeuseroutputbuffer) cannot be accessed after the [**WdfRequestComplete**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete), [**WdfRequestCompleteWithInformation**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithinformation), or [**WdfRequestCompleteWithPriorityBoost**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithpriorityboost) methods have been called on the request. The following possible buffer access functions are considered: [**RtlMoveMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlmovememory) (with the buffer as a 1st and 2nd parameter), [**RtlZeroMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlzeromemory), [**RtlCompareMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlcomparememory), [**ZwReadFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntreadfile), [**ZwWriteFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntwritefile), [**WDF\_MEMORY\_DESCRIPTOR\_INIT\_BUFFER**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdf_memory_descriptor_init_buffer), [**WdfMemoryCreatePreallocated**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorycreatepreallocated), [**WdfMemoryAssignBuffer**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemoryassignbuffer), [**WdfMemoryCopyFromBuffer**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorycopyfrombuffer), [**WdfMemoryCopyToBuffer**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorycopytobuffer).

**Driver model: KMDF**

## How to test

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>BufAfterReqCompletedIntIoctlA</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

## Applies to

[**WDF\_MEMORY\_DESCRIPTOR\_INIT\_BUFFER**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdf_memory_descriptor_init_buffer)
[**WdfMemoryAssignBuffer**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemoryassignbuffer)
[**WdfMemoryCopyFromBuffer**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorycopyfrombuffer)
[**WdfMemoryCopyToBuffer**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorycopytobuffer)
[**WdfMemoryCreatePreallocated**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorycreatepreallocated)
[**WdfRequestComplete**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete)
[**WdfRequestCompleteWithInformation**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithinformation)
[**WdfRequestCompleteWithPriorityBoost**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithpriorityboost)
[**WdfRequestRetrieveInputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputbuffer)
[**WdfRequestRetrieveOutputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputbuffer)
[**WdfRequestRetrieveUnsafeUserInputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveunsafeuserinputbuffer)
[**WdfRequestRetrieveUnsafeUserOutputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveunsafeuseroutputbuffer)
[**RtlCompareMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlcomparememory)
[**RtlMoveMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlmovememory)
[**RtlZeroMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlzeromemory)
[**ZwReadFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntreadfile)
