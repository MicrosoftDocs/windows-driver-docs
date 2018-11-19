---
title: KsTimedPinSetDeviceState rule ()
description: The KsTimedPinSetDeviceState rule specifies that a AVStream (KS) miniport driver makes state transitions using the AVStream minidriver's AVStrMiniPinSetDeviceState routine within the required time.
ms.assetid: 2BDA0358-A3B1-4A47-AA08-8B086041BC52
ms.date: 05/21/2018
keywords: ["KsTimedPinSetDeviceState rule ()"]
topic_type:
- apiref
api_name:
- KsTimedPinSetDeviceState
api_type:
- NA
ms.localizationpriority: medium
---

# KsTimedPinSetDeviceState rule ()


The KsTimedPinSetDeviceState rule specifies that a AVStream (KS) miniport driver makes state transitions using the AVStream minidriver's [*AVStrMiniPinSetDeviceState*](https://msdn.microsoft.com/library/windows/hardware/ff556359) routine within the required time.

|              |     |
|--------------|-----|
| Driver model | KS  |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00082001) |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>To verify this rule, open a Command Prompt window. Enter a Driver Verifier command and specify <strong>/domain ks</strong>.</p>
<p>For example:</p>
<p><strong>verifier /domain ks</strong> [<em>options</em>] <strong>/driver</strong> <em>&lt;yourdriver&gt;</em></p>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a>.</p></td>
</tr>
</tbody>
</table>

 

See also
--------

[*AVStrMiniPinSetDeviceState*](https://msdn.microsoft.com/library/windows/hardware/ff556359)
 

 





