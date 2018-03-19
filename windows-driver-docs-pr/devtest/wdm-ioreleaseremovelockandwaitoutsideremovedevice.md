---
title: IoReleaseRemoveLockAndWaitOutsideRemoveDevice rule (wdm)
description: The IoReleaseRemoveLockAndWaitOutsideRemoveDevice rule specifies that IoReleaseRemoveLockAndWait should not be called outside IRP\_MJ\_PNP with IRP\_MN\_REMOVE\_DEVICE for a PnP driver.
ms.assetid: 5787B14D-1793-4B39-A569-9A1308257A26
keywords: ["IoReleaseRemoveLockAndWaitOutsideRemoveDevice rule (wdm)"]
topic_type:
- apiref
api_name:
- IoReleaseRemoveLockAndWaitOutsideRemoveDevice
api_type:
- NA
---

# IoReleaseRemoveLockAndWaitOutsideRemoveDevice rule (wdm)


The **IoReleaseRemoveLockAndWaitOutsideRemoveDevice** rule specifies that [**IoReleaseRemoveLockAndWait**](https://msdn.microsoft.com/library/windows/hardware/ff549567) should not be called outside IRP\_MJ\_PNP with IRP\_MN\_REMOVE\_DEVICE for a PnP driver.

|              |     |
|--------------|-----|
| Driver model | WDM |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoReleaseRemoveLockAndWaitOutsideRemoveDevice</strong> rule.</p>
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

[**IoReleaseRemoveLockAndWait**](https://msdn.microsoft.com/library/windows/hardware/ff549567)
See also
--------

[Using Remove Locks](https://msdn.microsoft.com/library/windows/hardware/ff565504)
 

 





