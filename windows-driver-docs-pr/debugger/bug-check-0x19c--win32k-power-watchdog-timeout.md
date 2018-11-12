---
title: Bug Check 0x19C WIN32K_POWER_WATCHDOG_TIMEOUT
description: The WIN32K_POWER_WATCHDOG_TIMEOUT bug check has a value of 0x0000019C. This indicates that Win32k did not turn the monitor on in a timely manner.
ms.assetid: 55907359-C282-43F0-92FE-5DC248BF9D02
keywords: ["Bug Check 0x19C WIN32K_POWER_WATCHDOG_TIMEOUT", "WIN32K_POWER_WATCHDOG_TIMEOUT"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- WIN32K_POWER_WATCHDOG_TIMEOUT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x19C: WIN32K\_POWER\_WATCHDOG\_TIMEOUT


The WIN32K\_POWER\_WATCHDOG\_TIMEOUT bug check has a value of 0x0000019C. This indicates that Win32k did not turn the monitor on in a timely manner.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## WIN32K\_POWER\_WATCHDOG\_TIMEOUT Parameters


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
<td align="left"><p>Failure type (win32kbase!POWER_WATCHDOG_TYPE)</p>
<div class="code">
<code>0x10 : The power request queue is not making progress
              2 - Pointer to the thread processing power requests, if any
              3 - Pointer to the win32k user lock
              4 - Pointer to the power request (win32kbase!PPOWERREQUEST) being
                  processed, if any
          0x20 : Calling PO to set power state
              2 - Pointer to the power request worker thread              
              3 - Reserved
              4 - Reserved
          0x30 : Calling GDI to power on
              2 - Pointer to the power request worker thread
              3 - Reserved
              4 - Reserved
          0x40 : Calling DWM to render
              2 - Pointer to the power request worker thread
              3 - Reserved
              4 - Reserved
          0x50 : Calling monitor driver to power on
              2 - Pointer to the power request worker thread
              3 - Reserved
              4 - Reserved</code>
</div></td>
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
<td align="left">See parameter 1</td>
</tr>
</tbody>
</table>










