---
title: Bug Check 0xBFF BC_BTHMINI_VERIFIER_FAULT
description: The BC_BTHMINI_VERIFIER_FAULT bug check has a value of 0x00000BFF. This indicates that The Bluetooth miniport extensible driver verifier has caught a violation.
ms.assetid: 4BB54209-89EA-455D-B850-CC2A96A43C87
keywords: ["Bug Check 0xBFF BC_BTHMINI_VERIFIER_FAULT", "BC_BTHMINI_VERIFIER_FAULT"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- BC_BTHMINI_VERIFIER_FAULT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xBFF: BC\_BTHMINI\_VERIFIER\_FAULT


The BC\_BTHMINI\_VERIFIER\_FAULT bug check has a value of 0x00000BFF. This indicates that The Bluetooth miniport extensible driver verifier has caught a violation.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## BC\_BTHMINI\_VERIFIER\_FAULT Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">1</td>
<td align="left"><p>The subtype of the Bluetooth verifier fault.</p>
<div class="code">
<code>0x1 : An attempt was made to return a packet with type that mis-matched its original request.
                  2 - Returned packet type
                  3 - Expected packet type
                  4 - Reserved
            0x2 : An attempt was made to return an unexpected status code and caused the packet to be discarded.
                  2 - Unexpected return status
                  3 - Reserved
                  4 - Reserved
            0x3 : Incorrect output buffer size was returned to indicate number of bytes written by the lower transport driver.
                  2 - Unexpected buffer size
                  3 - Expected buffer size
                  4 - Reserved</code>
</div></td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">See parameter 1</td>
</tr>
</tbody>
</table>



Resolution
----------

Parameter 1 describes the type of violation. Look at the call stack to determine the misbehaving driver.








