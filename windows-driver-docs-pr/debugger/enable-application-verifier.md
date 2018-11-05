---
title: Enable application verifier
description: Enable application verifier
ms.assetid: a91e244e-e3b6-4975-8385-1da06cc3ae83
keywords: ["Enable application verifier (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Enable application verifier


## <span id="ddk_enable_application_verifier_dtools"></span><span id="DDK_ENABLE_APPLICATION_VERIFIER_DTOOLS"></span>


The **Enable application verifier** flag enables system features that are used for user-mode application testing, such as page heap verification, lock checks, and handle checks.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>vrf</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x100</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_APPLICATION_VERIFIER</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag, image file registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

This flag enables only the most basic detection features. To test user-mode applications reliably, use Application Verifier (appverif.exe). For more information, see [Application Verifier](application-verifier.md).

 

 





