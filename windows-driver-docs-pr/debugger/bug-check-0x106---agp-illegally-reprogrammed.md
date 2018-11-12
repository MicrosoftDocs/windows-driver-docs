---
title: Bug Check 0x106 AGP_ILLEGALLY_REPROGRAMMED
description: The AGP_ILLEGALLY_REPROGRAMMED bug check has a value of 0x00000106. This indicates that the Accelerated Graphics Port (AGP) hardware has been reprogrammed by an unauthorized agent.
ms.assetid: 7acccf9b-bc4f-4842-a332-1023ab26f03d
keywords: ["Bug Check 0x106 AGP_ILLEGALLY_REPROGRAMMED", "AGP_ILLEGALLY_REPROGRAMMED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- AGP_ILLEGALLY_REPROGRAMMED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x106: AGP\_ILLEGALLY\_REPROGRAMMED


The AGP\_ILLEGALLY\_REPROGRAMMED bug check has a value of 0x00000106. This indicates that the Accelerated Graphics Port (AGP) hardware has been reprogrammed by an unauthorized agent.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## AGP\_ILLEGALLY\_REPROGRAMMED Parameters


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
<td align="left"><p>1</p></td>
<td align="left"><p>The originally programmed AGP command register value</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The current command register value</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

This bug check is typically caused by an unsigned, or improperly tested, video driver.

Resolution
----------

Check the video manufacturer's Web site for updated display drivers or use VGA mode.

 

 




