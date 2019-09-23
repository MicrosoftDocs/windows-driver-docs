---
title: MdlAfterReqCompletedReadA rule (kmdf)
description: The MdlAfterReqCompletedReadA rule specifies that within the EvtIoRead callback function, the memory descriptor list (MDL) object retrieved cannot be accessed after the I/O request is completed.
ms.assetid: 3e7c40a0-882e-45eb-8cf1-bee1096379ad
ms.date: 05/21/2018
keywords: ["MdlAfterReqCompletedReadA rule (kmdf)"]
topic_type:
- apiref
api_name:
- MdlAfterReqCompletedReadA
api_type:
- NA
ms.localizationpriority: medium
---

# MdlAfterReqCompletedReadA rule (kmdf)


The **MdlAfterReqCompletedReadA** rule specifies that within the [*EvtIoRead*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfio/nc-wdfio-evt_wdf_io_queue_io_read) callback function, the memory descriptor list (MDL) object retrieved cannot be accessed after the I/O request is completed.

Within the driver's *EvtIoRead* callback function, the request buffer that was retrieved by calling the [**WdfRequestRetrieveOutputWdmMdl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputwdmmdl) method cannot be accessed after calling [**WdfRequestComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcomplete), [**WdfRequestCompleteWithInformation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcompletewithinformation), or [**WdfRequestCompleteWithPriorityBoost**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcompletewithpriorityboost) on the I/O request.

This rule considers the following functions:

[**WDF\_MEMORY\_DESCRIPTOR\_INIT\_MDL**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfmemory/nf-wdfmemory-wdf_memory_descriptor_init_mdl)
[**MmGetMdlByteCount**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-mmgetmdlbytecount)
[**MmGetSystemAddressForMdlSafe**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer)
[**MmGetMdlVirtualAddress**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer)
[**IoBuildPartialMdl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iobuildpartialmdl) (first and second parameter)
[**KeFlushIoBuffers**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keflushiobuffers)
[**MmGetMdlPfnArray**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer)
[**MmGetMdlByteOffset**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer)
[**MmPrepareMdlForReuse**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer)
[**WdfDmaTransactionInitialize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitialize)

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>MdlAfterReqCompletedReadA</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**WDF\_MEMORY\_DESCRIPTOR\_INIT\_MDL**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfmemory/nf-wdfmemory-wdf_memory_descriptor_init_mdl)
[**WdfDmaTransactionInitialize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitialize)
[**WdfRequestComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcomplete)
[**WdfRequestCompleteWithInformation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcompletewithinformation)
[**WdfRequestCompleteWithPriorityBoost**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcompletewithpriorityboost)
[**WdfRequestRetrieveOutputWdmMdl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputwdmmdl)
[**IoBuildPartialMdl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iobuildpartialmdl)
[**KeFlushIoBuffers**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keflushiobuffers)
[**MmGetMdlByteCount**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-mmgetmdlbytecount)
[**MmGetMdlByteOffset**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer)
[**MmGetMdlPfnArray**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer)
[**MmGetMdlVirtualAddress**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer)
[**MmGetSystemAddressForMdlSafe**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer)
[**MmPrepareMdlForReuse**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer)








