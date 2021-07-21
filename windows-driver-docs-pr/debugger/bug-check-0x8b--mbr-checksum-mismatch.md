---
title: Bug Check 0x8B MBR_CHECKSUM_MISMATCH
description: The MBR_CHECKSUM_MISMATCH bug check has a value of 0x0000008B. This bug check indicates that a mismatch has occurred in the MBR checksum.
keywords: ["Bug Check 0x8B MBR_CHECKSUM_MISMATCH", "MBR_CHECKSUM_MISMATCH"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- MBR_CHECKSUM_MISMATCH
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x8B: MBR\_CHECKSUM\_MISMATCH


The MBR\_CHECKSUM\_MISMATCH bug check has a value of 0x0000008B. This bug check indicates that a mismatch has occurred in the MBR checksum.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## MBR\_CHECKSUM\_MISMATCH Parameters


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
<td align="left"><p>The disk signature from MBR</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The MBR checksum that the OS Loader calculates</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The MBR checksum that the system calculates</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

## Cause

The MBR\_CHECKSUM\_MISMATCH bug check occurs during the boot process when the MBR checksum that the Microsoft Windows operating system calculates does not match the checksum that the loader passes in.

This error typically indicates a virus.

## Resolution

There are many forms of viruses and not all can be detected. Typically, the newer viruses usually can be detected only by a virus scanner that has recently been upgraded. You should boot with a write-protected disk that contains a virus scanner and try to clean out the infection.

 

 




