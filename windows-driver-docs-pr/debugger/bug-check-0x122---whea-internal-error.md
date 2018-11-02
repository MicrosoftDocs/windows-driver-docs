---
title: Bug Check 0x122 WHEA_INTERNAL_ERROR
description: The WHEA_INTERNAL_ERROR bug check has a value of 0x00000122.
ms.assetid: b0bf1f27-bfdd-4d5d-aeac-f74f45c6174f
keywords: ["Bug Check 0x122 WHEA_INTERNAL_ERROR", "WHEA_INTERNAL_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- WHEA_INTERNAL_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x122: WHEA\_INTERNAL\_ERROR


The WHEA\_INTERNAL\_ERROR bug check has a value of 0x00000122. This bug check indicates that an internal error in the Windows Hardware Error Architecture (WHEA) has occurred. Errors can result from a bug in the implementation of a platform-specific hardware error driver (PSHED) plug-in supplied by a vendor, the firmware implementation of error records, or the firmware implementation of error injection.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## WHEA\_INTERNAL\_ERROR Parameters


<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause of error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>Size of memory</p></td>
<td align="left"><p>Error source count</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Failed to allocate enough memory for all the error sources in the hardware error source table.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>Number of processors</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Failed to allocate enough memory for a WHEA information block for each processor.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x5</p></td>
<td align="left"><p>Status</p></td>
<td align="left"><p>Phase (The initialization phase for the bug check)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>WHEA failed to allocate enough memory for the error sources, or the error source enumeration failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x6</p></td>
<td align="left"><p>Status</p></td>
<td align="left"><p>Phase</p></td>
<td align="left"><p>Error source type</p></td>
<td align="left"><p>Failed to initialize the error source (Parameter 4) during the phase specified by Parameter 3.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x7</p></td>
<td align="left"><p>Status</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Failed to allocate enough memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x8</p></td>
<td align="left"><p>Number of error sources</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Failed to allocate enough memory for all the error source descriptors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x9</p></td>
<td align="left"><p>Error source type</p></td>
<td align="left"><p>Source ID</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>WHEA received an uncorrected error source from an invalid error source.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xA</p></td>
<td align="left"><p>Error source type</p></td>
<td align="left"><p>Source ID</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Failed to allocate an error record for an uncorrected error.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xB</p></td>
<td align="left"><p>Error source type</p></td>
<td align="left"><p>Source ID</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Failed to populate the error record for an uncorrected error.</p></td>
</tr>
</tbody>
</table>

 

If Parameter 1 is equal to 0x6, 0x9, 0xA, or 0xB, one of the other parameters contains the error source type. The following table gives possible values for the error source type.

| Value | Description                          |
|-------|--------------------------------------|
| 0x00  | Machine check exception              |
| 0x01  | Corrected machine check              |
| 0x02  | Corrected platform error             |
| 0x03  | Non-maskable interrupt               |
| 0x04  | PCI express error                    |
| 0x05  | Other types of error sources/Generic |
| 0x06  | IA64 INIT error source               |
| 0x07  | BOOT error source                    |
| 0x08  | SCI-based generic error source       |
| 0x09  | Itanium machine check abort          |
| 0x0A  | Itanium machine check                |
| 0x0B  | Itanium corrected platform error     |

 

 

 




