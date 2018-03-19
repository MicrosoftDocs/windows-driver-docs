---
title: ParentObjectCheck rule (kmdf)
description: The ParentObjectCheck rule specifies that driver should call WdfMemoryCreate specifying a parent object using a WDF\_OBJECT\_ATTRIBUTES structure.
ms.assetid: E0597996-9067-40C3-8DE9-1048B2227F07
keywords: ["ParentObjectCheck rule (kmdf)"]
topic_type:
- apiref
api_name:
- ParentObjectCheck
api_type:
- NA
---

# ParentObjectCheck rule (kmdf)


The **ParentObjectCheck** rule specifies that driver should call [**WdfMemoryCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548706) specifying a parent object using a [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure. If driver doesn’t set a parent object for the framework memory object then the framework sets the driver as the default parent, so that unless the driver deletes the framework memory object explicitly it’ll remain in the memory until the driver object unloads.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ParentObjectCheck</strong> rule.</p>
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

[**WdfMemoryCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548706)
 

 





