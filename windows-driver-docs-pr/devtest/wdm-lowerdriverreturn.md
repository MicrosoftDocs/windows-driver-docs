---
title: LowerDriverReturn rule (wdm)
description: The LowerDriverReturn rule specifies that after using PoCallDriver or IoCallDriver to call a lower driver, the driver saves the return status from the call and passes the return status that it received to the dispatch routine.
ms.assetid: 0b437591-c613-481a-a4f9-36a5cc208cb0
keywords: ["LowerDriverReturn rule (wdm)"]
topic_type:
- apiref
api_name:
- LowerDriverReturn
api_type:
- NA
---

# LowerDriverReturn rule (wdm)


The **LowerDriverReturn** rule specifies that after using [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) or [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to call a lower driver, the driver saves the return status from the call and passes the return status that it received to the dispatch routine.

These conditions are not applied if the driver calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) or [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>LowerDriverReturn</strong> rule.</p>
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

[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422)
[**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679)
[**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686)
[**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700)
[**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480)
[**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
 

 





