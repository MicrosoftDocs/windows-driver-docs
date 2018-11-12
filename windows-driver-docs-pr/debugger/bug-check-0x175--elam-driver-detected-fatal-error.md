---
title: Bug Check 0x178 ELAM_DRIVER_DETECTED_FATAL_ERROR
description: The ELAM_DRIVER_DETECTED_FATAL_ERROR bug check has a value of 0x00000178. This indicates that ELAM driver detected a fatal error.
ms.assetid: 4D37FE16-0189-426C-8015-9F14DA3C52F6
keywords: ["Bug Check 0x178 ELAM_DRIVER_DETECTED_FATAL_ERROR", "ELAM_DRIVER_DETECTED_FATAL_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ELAM_DRIVER_DETECTED_FATAL_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x178: ELAM\_DRIVER\_DETECTED\_FATAL\_ERROR


The ELAM\_DRIVER\_DETECTED\_FATAL\_ERROR bug check has a value of 0x00000178. This indicates that ELAM driver detected a fatal error.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## ELAM\_DRIVER\_DETECTED\_FATAL\_ERROR Parameters


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
<td align="left">Type of the failure.
<p>0x0 : TPM attestation could not be revoked</p>
2 - Pointer to the BDCB_IMAGE_INFORMATION structure for the driver being inspected
3 - TBS_RESULT failure code
<p>0x10000 : ELAM-vendor defined failure</p>
2 - (Optional) ELAM vendor supplied value
3 - (Optional) ELAM vendor supplied value</td>
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
<td align="left">(Optional) ELAM vendor supplied general purpose data block</td>
</tr>
</tbody>
</table>

 

 

 




