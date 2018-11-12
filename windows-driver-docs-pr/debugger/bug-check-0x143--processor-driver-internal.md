---
title: Bug Check 0x143 PROCESSOR_DRIVER_INTERNAL
description: The PROCESSOR_DRIVER_INTERNAL bug check has a value of 0x00000143. This indicates that the Processor Power Management (PPM) driver encountered a fatal error.
ms.assetid: B61A1DF1-4454-4418-866F-FD9EC96F6906
keywords: ["Bug Check 0x143 PROCESSOR_DRIVER_INTERNAL", "PROCESSOR_DRIVER_INTERNAL"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- PROCESSOR_DRIVER_INTERNAL
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x143: PROCESSOR\_DRIVER\_INTERNAL


The PROCESSOR\_DRIVER\_INTERNAL bug check has a value of 0x00000143. This indicates that the Processor Power Management (PPM) driver encountered a fatal error.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## PROCESSOR\_DRIVER\_INTERNAL Parameters


| Parameter | Description                                                              |
|-----------|--------------------------------------------------------------------------|
| 1         | 1 - Power Engine Plugin(PEP) failed to accept a required notification    |
| 2         | PEP runtime Notification type                                            |
| 3         | Pointer to notification message                                          |
| 4         | Pointer to processor device context (FDO\_DATA) issuing the notification |

 

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
<td align="left">2 - Power Engine Plugin (PEP) returned invalid processor idle state</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left"><p>Type of invalid state</p>
<p>0x0 : PEP requested too many processors for coordinated idle state</p>
Parameter 3 - Number of processors requested to participate in coordinated idle transitions
Parameter 4 - Pointer to processor device context (FDO_DATA)
<p>0x1 : PEP requested processor to be in an invalid idle state</p>
Parameter 3 - Idle state index requested
Parameter 4 - Pointer to processor device context (FDO_DATA) corresponding to the invalid idle state
<p>0x2 : PEP requested the platform to be in an invalid idle state</p>
Parameter 3 - Platform idle state index requested
Parameter 4 - Pointer to processor device context (FDO_DATA) corresponding to the invalid idle state</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">Refer to parameter 2</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Refer to parameter 2</td>
</tr>
</tbody>
</table>

 

Cause
-----

The processor driver detected an irreconcilable condition which prompted it to bugcheck. This likely happens during the processor idle and perf-state change execution, which may involve other entities such has kernel, HAL and the Power Engine Plugin (PEP). Information from bugcheck will help identify which of the assumptions made by the processor driver in dealing with other entities was violated. The root cause may lie in other entities and a dump file may reveal more information to ascertain the reason for the bugcheck.

 

 




