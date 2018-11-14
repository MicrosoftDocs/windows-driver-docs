---
title: Bug Check 0x125 NMR_INVALID_STATE
description: The NMR_INVALID_STATE bug check has a value of 0x00000125. This indicates that NMR (network module registrar) has detected an invalid state. See parameter 1 for the state type.
ms.assetid: DD80FC61-8211-46A0-9D44-CF1E729B12D4
keywords: ["Bug Check 0x125 NMR_INVALID_STATE", "NMR_INVALID_STATE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- NMR_INVALID_STATE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x125: NMR\_INVALID\_STATE


The NMR\_INVALID\_STATE bug check has a value of 0x00000125. This indicates that NMR (network module registrar) has detected an invalid state. See parameter 1 for the state type.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## NMR\_INVALID\_STATE Parameters


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
<td align="left"><p>The subtype of the bugcheck.</p>
<p>0x0 : Machine Check Exception</p>
<p>Parameter 2 - Address of the WHEA_ERROR_RECORD structure.</p>
<p>Parameter 3 - High order 32-bits of the MCi_STATUS value.</p>
<p>Parameter 4 - Low order 32-bits of the MCi_STATUS value.</p>
<p>0x1 : Corrected Machine Check</p>
Parameter 2 - Address of the WHEA_ERROR_RECORD structure.
<p>0x2 : Corrected Platform Error</p>
Parameter 2 - Address of the WHEA_ERROR_RECORD structure.
<p>0x3 : Non-maskable Interrupt</p>
Parameter 2 - Address of the WHEA_ERROR_RECORD structure.
<p>0x4 : PCI Express Error</p>
Parameter 2 - Address of the WHEA_ERROR_RECORD structure.
<p>0x5 : Generic Error</p>
Parameter 2 - Address of the WHEA_ERROR_RECORD structure.
<p>0x6 : INIT Error</p>
Parameter 2 - Address of the WHEA_ERROR_RECORD structure.
<p>0x7 : BOOT Error</p>
Parameter 2 - Address of the WHEA_ERROR_RECORD structure.
<p>0x8 : SCI Generic Error</p>
Parameter 2 - Address of the WHEA_ERROR_RECORD structure.
<p>0x9 : Itanium Machine Check Abort</p>
Parameter 2 - Address of the WHEA_ERROR_RECORD structure.
Parameter 3 - Length in bytes of the SAL log.
Parameter 4 - Address of the SAL log.
<p>0xa : Itanium Corrected Machine Check</p>
Parameter 2 - Address of the WHEA_ERROR_RECORD structure.
<p>0xb : Itanium Corrected Platform Error</p>
Parameter 2 - Address of the WHEA_ERROR_RECORD structure.</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">Pointer to the NMI Handle</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">Pointer to the expected type, when available</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Reserved</td>
</tr>
</tbody>
</table>

 

 

 




