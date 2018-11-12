---
title: Bug Check 0xBFE BC_BLUETOOTH_VERIFIER_FAULT
description: The BC_BLUETOOTH_VERIFIER_FAULT bug check has a value of 0x00000BFE. This indicates that a driver has caused a violation.
ms.assetid: EC1368CE-46A2-4B69-8405-3118503D35C2
keywords: ["Bug Check 0xBFE BC_BLUETOOTH_VERIFIER_FAULT", "BC_BLUETOOTH_VERIFIER_FAULT"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- BC_BLUETOOTH_VERIFIER_FAULT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xBFE: BC\_BLUETOOTH\_VERIFIER\_FAULT


The BC\_BLUETOOTH\_VERIFIER\_FAULT bug check has a value of 0x00000BFE. This indicates that a driver has caused a violation.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## BC\_BLUETOOTH\_VERIFIER\_FAULT Parameters


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
<code>0x1 : An attempt was made to submit a Bluetooth Request Block that is already in use
                  2 - Brb pointer
                  3 - Reserved
                  4 - Reserved
            0x2 : An attempt was made to free a Bluetooth Request Block that is in use
                  2 - Brb pointer
                  3 - Reserved
                  4 - Reserved
            0x3 : An attempt was made to allocate or initialize an invalid BRB type
                  2 - Brb pointer
                  3 - pdo extension (if available)
                  4 - Reserved
            0x4 : Invalid Bluetooth Request Block pointer was submitted
                  2 - Brb pointer
                  3 - Reserved
                  4 - Reserved
            0x5 : A Bluetooth Request Block with an invalid size was submitted
                  2 - Brb pointer
                  3 - Actual Size
                  4 - Expected Size
            0x6 : The IOCTL_BTH_GET_DEVICE_INFO was called with invalid parameters
                  2 - Reserved
                  3 - Reserved
                  4 - Reserved
            0x7 : BRB_L2CA_UNREGISTER_SERVER was submitted with an invalid server handle
                  2 - Server handle
                  3 - Reserved
                  4 - Reserved
            0x8 : BRB_L2CA_CLOSE_CHANNEL was submitted with an invalid channel handle
                  2 - Brb pointer
                  3 - Channel handle
                  4 - Reserved
            0x9 : BRB_SCO_UNREGISTER_SERVER was submitted with an invalid server handle
                  2 - Server handle
                  3 - Reserved
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








