---
title: FailD0EntryIoTargetState rule (kmdf)
description: The FailD0EntryIoTargetState rule specifies that an I/O target for a USB continuous reader started within the EvtDeviceD0Entry will get stopped appropriately from the same callback if the EvtDeviceD0Entry fails.
ms.assetid: 7FB616EB-2079-42AE-A724-990EFBF3F84D
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["FailD0EntryIoTargetState rule (kmdf)"]
topic_type:
- apiref
api_name:
- FailD0EntryIoTargetState
api_type:
- NA
---

# FailD0EntryIoTargetState rule (kmdf)


The **FailD0EntryIoTargetState** rule specifies that an I/O target for a USB continuous reader started within the [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) will get stopped appropriately from the same callback if the *EvtDeviceD0Entry* fails.

When [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback function fails, the framework doesn’t execute the driver’s [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) callback function.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>FailD0EntryIoTargetState</strong> rule.</p>
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

[**WdfIoTargetStart**](https://msdn.microsoft.com/library/windows/hardware/ff548677)
[**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680)
[**WdfUsbTargetPipeConfigContinuousReader**](https://msdn.microsoft.com/library/windows/hardware/ff551130)
[**WdfUsbTargetPipeGetIoTarget**](https://msdn.microsoft.com/library/windows/hardware/ff551146)
 

 





