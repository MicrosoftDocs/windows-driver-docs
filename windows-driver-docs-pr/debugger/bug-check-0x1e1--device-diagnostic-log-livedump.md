---
title: Bug Check 0x1E1 DEVICE_DIAGNOSTIC_LOG_LIVEDUMP
description: The DEVICE_DIAGNOSTIC_LOG_LIVEDUMP has a value of 0x000001E1 that indicates that a device has encountered an error and generated diagnostic data.
keywords: ["Bug Check 0x1E1 DEVICE_DIAGNOSTIC_LOG_LIVEDUMP", "DEVICE_DIAGNOSTIC_LOG_LIVEDUMP"]
ms.date: 08/24/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- DEVICE_DIAGNOSTIC_LOG_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x1E1: DEVICE\_DIAGNOSTIC\_LOG\_LIVEDUMP

The DEVICE\_DIAGNOSTIC\_LOG\_LIVEDUMP has a value of 0x000001E1. This indicates that a device has encountered an error and generated diagnostic data.

(This code can never be used for a real bug check; it is used to identify live dumps.)

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
<td align="left">Device class.</p>
<p>0x1 : Storage device.</p>
<p>  2 - Storage Issue type.</p>
<p> 0x1 : Device panic.</p>
<p>  3 - IEEE Organization ID.</p>
<p>  4 - Reserved</p>
</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">See description above.</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">See description above.</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">See description above.</td>
</tr>
</tbody>
</table>

 
## Resolution

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.
 

## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)



