---
title: MdlAfterReqCompletedIoctl rule (kmdf)
description: The MdlAfterReqCompletedIoctl rule specifies that within the EvtIoDeviceControl callback function, the memory descriptor list (MDL) cannot be accessed after the I/O request is completed.
ms.assetid: ce82cca4-f0e3-4e84-8599-4094fa1ed4c2
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["MdlAfterReqCompletedIoctl rule (kmdf)"]
topic_type:
- apiref
api_name:
- MdlAfterReqCompletedIoctl
api_type:
- NA
---

# MdlAfterReqCompletedIoctl rule (kmdf)


The **MdlAfterReqCompletedIoctl** rule specifies that within the [*EvtIoDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541758) callback function, the memory descriptor list (MDL) cannot be accessed after the I/O request is completed.

Within the driver's [*EvtIoDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541758) callback function, the MDL that was retrieved by calling the [**WdfRequestRetrieveInputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550016) or [**WdfRequestRetrieveOutputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550021) method cannot be accessed after calling [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945), [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948), or [**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949) on the I/O request.

This rule looks at the following MDL access functions:

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>MdlAfterReqCompletedIoctl</strong> rule.</p>
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

[**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945)
[**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948)
[**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)
[**WdfRequestRetrieveInputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550016)
[**WdfRequestRetrieveOutputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550021)
 

 





