---
title: PcAddAdapterDevice rule (audio)
description: The PcAddAdapterDevice rule specifies that a PortCls miniport driver correctly uses the PcAddAdapterDevice function, specifically that the DeviceExtensionSize should be either zero (0) or no less than PORT\_CLASS\_DEVICE\_EXTENSION\_SIZE.
ms.assetid: AD020D31-9994-4AD1-A937-E29A594FC9D4
ms.date: 05/21/2018
keywords: ["PcAddAdapterDevice rule (audio)"]
topic_type:
- apiref
api_name:
- PcAddAdapterDevice
api_type:
- NA
ms.localizationpriority: medium
---

# PcAddAdapterDevice rule (audio)


The PcAddAdapterDevice rule specifies that a PortCls miniport driver correctly uses the **PcAddAdapterDevice** function, specifically that the *DeviceExtensionSize* should be either zero (0) or no less than PORT\_CLASS\_DEVICE\_EXTENSION\_SIZE.

|              |       |
|--------------|-------|
| Driver model | Audio |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00071007) |

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
<td align="left"><p>To verify this rule, open a Command Prompt window. Enter a Driver Verifier command and specify <strong>/domain audio</strong>.</p>
<p>For example:</p>
<p><strong>verifier /domain audio</strong> [<em>options</em>] <strong>/driver</strong> <em>&lt;yourdriver&gt;</em></p>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a>.</p></td>
</tr>
</tbody>
</table>

 

 

 





