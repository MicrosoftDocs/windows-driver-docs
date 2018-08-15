---
title: MdlAfterReqCompletedReadA rule (kmdf)
description: The MdlAfterReqCompletedReadA rule specifies that within the EvtIoRead callback function, the memory descriptor list (MDL) object retrieved cannot be accessed after the I/O request is completed.
ms.assetid: 3e7c40a0-882e-45eb-8cf1-bee1096379ad
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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


The **MdlAfterReqCompletedReadA** rule specifies that within the [*EvtIoRead*](https://msdn.microsoft.com/library/windows/hardware/ff541776) callback function, the memory descriptor list (MDL) object retrieved cannot be accessed after the I/O request is completed.

Within the driver's *EvtIoRead* callback function, the request buffer that was retrieved by calling the [**WdfRequestRetrieveOutputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550021) method cannot be accessed after calling [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945), [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948), or [**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949) on the I/O request.

This rule considers the following functions:

[**WDF\_MEMORY\_DESCRIPTOR\_INIT\_MDL**](https://msdn.microsoft.com/library/windows/hardware/ff552396)
[**MmGetMdlByteCount**](https://msdn.microsoft.com/library/windows/hardware/ff554530)
[**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559)
[**MmGetMdlVirtualAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554539)
[**IoBuildPartialMdl**](https://msdn.microsoft.com/library/windows/hardware/ff548324) (first and second parameter)
[**KeFlushIoBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff552041)
[**MmGetMdlPfnArray**](https://msdn.microsoft.com/library/windows/hardware/ff554537)
[**MmGetMdlByteOffset**](https://msdn.microsoft.com/library/windows/hardware/ff554533)
[**MmPrepareMdlForReuse**](https://msdn.microsoft.com/library/windows/hardware/ff554660)
[**WdfDmaTransactionInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff547099)
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>MdlAfterReqCompletedReadA</strong> rule.</p>
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

[**WDF\_MEMORY\_DESCRIPTOR\_INIT\_MDL**](https://msdn.microsoft.com/library/windows/hardware/ff552396)
[**WdfDmaTransactionInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff547099)
[**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945)
[**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948)
[**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)
[**WdfRequestRetrieveOutputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550021)
[**IoBuildPartialMdl**](https://msdn.microsoft.com/library/windows/hardware/ff548324)
[**KeFlushIoBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff552041)
[**MmGetMdlByteCount**](https://msdn.microsoft.com/library/windows/hardware/ff554530)
[**MmGetMdlByteOffset**](https://msdn.microsoft.com/library/windows/hardware/ff554533)
[**MmGetMdlPfnArray**](https://msdn.microsoft.com/library/windows/hardware/ff554537)
[**MmGetMdlVirtualAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554539)
[**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559)
[**MmPrepareMdlForReuse**](https://msdn.microsoft.com/library/windows/hardware/ff554660)
 

 





