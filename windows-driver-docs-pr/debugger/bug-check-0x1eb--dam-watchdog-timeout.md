---
title: Bug Check 0x1EB DAM_WATCHDOG_TIMEOUT
description: The DAM_WATCHDOG_TIMEOUT bug check has a value of 0x000001EB. This indicates that the Desktop Activity Moderator (DAM) was unable to unfreeze non-exempt user session processes within the allocated time period after the device resumed from modern standby.
keywords: ["Bug Check 0x1EB DAM_WATCHDOG_TIMEOUT", "DAM_WATCHDOG_TIMEOUT"]
ms.date: 04/07/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- DAM_WATCHDOG_TIMEOUT
api_type:
- NA
---

# Bug Check 0x1EB: DAM\_WATCHDOG\_TIMEOUT

The DAM\_WATCHDOG\_TIMEOUT bug check has a value of 0x000001EB. This indicates that the Desktop Activity Moderator (DAM) was unable to unfreeze non-exempt user session processes within the allocated time period after the device resumed from modern standby.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## DAM\_WATCHDOG\_TIMEOUT Parameters


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
<td align="left">Pointer to the DAM user session delay context.</td>
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
