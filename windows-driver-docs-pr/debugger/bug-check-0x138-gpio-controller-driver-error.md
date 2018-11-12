---
title: Bug Check 0x138 GPIO_CONTROLLER_DRIVER_ERROR
description: The GPIO_CONTROLLER_DRIVER_ERROR bug check has a value of 0x00000138. This bug check indicates that the GPIO class extension driver encountered a fatal error.
ms.assetid: 4025D968-10F9-4F2F-953F-914A4BE7D883
keywords: ["Bug Check 0x138 GPIO_CONTROLLER_DRIVER_ERROR", "GPIO_CONTROLLER_DRIVER_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- GPIO_CONTROLLER_DRIVER_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x138: GPIO\_CONTROLLER\_DRIVER\_ERROR


The GPIO\_CONTROLLER\_DRIVER\_ERROR bug check has a value of 0x00000138. This bug check indicates that the GPIO class extension driver encountered a fatal error.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## GPIO\_CONTROLLER\_DRIVER\_ERROR Parameters


*Parameter 1* indicates the type of violation. The meaning of the other parameters depends on the value of *Parameter 1*.

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
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>GSIV</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The GPIO controller managing the specific GSIV is not registered.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Context value</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A client driver specified an invalid context to a lock or unlock request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Indicates whether a critical transition is being requested.</p></td>
<td align="left"><p>Indicates whether the bank is already in F1 due to a non-critical transition.</p></td>
<td align="left"><p>Indicates whether the bank is already in F1 due to a critical transition.</p></td>
<td align="left"><p>PoFx requested that the GPIO controller send a bank through an inappropriate F1 power state and/or a critical transition.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Indicates whether a critical transition is being requested.</p></td>
<td align="left"><p>Indicates whether the bank is in F1 due to a non-critical transition.</p></td>
<td align="left"><p>Indicates whether the bank is in F1 due to a critical transition.</p></td>
<td align="left"><p>PoFx requested that the GPIO controller send a bank through an inappropriate F0 power state and/or a critical transition.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>5</p></td>
<td align="left"><p>NTSTATUS</p></td>
<td align="left"><p>GPIO device extension</p></td>
<td align="left"><p>GPIO interrupt parameters</p></td>
<td align="left"><p>An on-Soc GPIO interrupt operation failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>6</p></td>
<td align="left"><p>NTSTATUS</p></td>
<td align="left"><p>GPIO device extension</p></td>
<td align="left"><p>GPIO IO parameters</p></td>
<td align="left"><p>An on-Soc GPIO IO operation failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>7</p></td>
<td align="left"><p>Revision ID</p></td>
<td align="left"><p>Function Index</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A _DSM method returned malformed data.</p></td>
</tr>
</tbody>
</table>

 

 

 




