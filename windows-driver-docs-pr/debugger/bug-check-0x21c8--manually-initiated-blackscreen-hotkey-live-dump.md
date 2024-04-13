---
title: Bug Check 0x21C8 MANUALLY_INITIATED_BLACKSCREEN_HOTKEY_LIVE_DUMP
description: The MANUALLY_INITIATED_BLACKSCREEN_HOTKEY_LIVE_DUMP live dump has a value of 0x0000021C8. This indicates that the system was configured to capture a live dump and the the user had pressed the black screen hotkey (CTRL + SHIFT + WIN + B).
keywords: ["Bug Check 0x21C8 MANUALLY_INITIATED_BLACKSCREEN_HOTKEY_LIVE_DUMP", "MANUALLY_INITIATED_BLACKSCREEN_HOTKEY_LIVE_DUMP"]
ms.date: 11/01/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- MANUALLY_INITIATED_BLACKSCREEN_HOTKEY_LIVE_DUMP
api_type:
- NA
---

# Bug Check 0x21C8: MANUALLY\_INITIATED\_BLACKSCREEN\_HOTKEY\_LIVE\_DUMP

The MANUALLY\_INITIATED\_BLACKSCREEN\_HOTKEY\_LIVE\_DUMP live dump has a value of 0x000021C8. This indicates that the system was configured to capture a live dump and the user had pressed the black screen hotkey (CTRL + SHIFT + WIN + B). The live dump may help determine the root cause of black screen observed by the user.

(This code can never be used for a real bug check; it is used to identify live dumps.)

## MANUALLY\_INITIATED\_BLACKSCREEN\_HOTKEY\_LIVE\_DUMP Parameters

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
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">Reserved</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">Reserved</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Reserved</td>
</tr>
</tbody>
</table>

## Resolution
The [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.
 

## See also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)
 

 




