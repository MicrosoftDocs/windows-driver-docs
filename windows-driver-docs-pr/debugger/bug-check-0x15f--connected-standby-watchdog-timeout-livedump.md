---
title: Bug Check 0x15F CONNECTED_STANDBY_WATCHDOG_TIMEOUT_LIVEDUMP
description: The CONNECTED_STANDBY_WATCHDOG_TIMEOUT_LIVEDUMP bug check has a value of 0x0000015F. This indicates that a connected standby watchdog timeout has occurred.
ms.assetid: 4C10AAC1-0B8F-4BBE-B470-55A8ED373687
keywords: ["Bug Check 0x15F CONNECTED_STANDBY_WATCHDOG_TIMEOUT_LIVEDUMP", "CONNECTED_STANDBY_WATCHDOG_TIMEOUT_LIVEDUMP"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CONNECTED_STANDBY_WATCHDOG_TIMEOUT_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x15F: CONNECTED\_STANDBY\_WATCHDOG\_TIMEOUT\_LIVEDUMP


The CONNECTED\_STANDBY\_WATCHDOG\_TIMEOUT\_LIVEDUMP bug check has a value of 0x0000015F. This indicates that a connected standby watchdog timeout has occurred.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## CONNECTED\_STANDBY\_WATCHDOG\_TIMEOUT\_LIVEDUMP Parameters


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
<td align="left"><p>CS watchdog subcode</p>
0x1 : DRIPS watchdog timeout. The system has been in the resiliency phase of connected standby with no activators active and no device constraints unsatisfied for too long without entering DRIPS (deepest runtime idle platform state).
<p>2 - A pointer to additional information (nt!POP_DRIPS_WATCHDOG_METRICS)</p>
<p>3 - Non-DRIPS duration in milliseconds</p>
<p>4 - Reserved</p>
0x2 : DRIPS watchdog device constraint timeout. The system has been in the resiliency phase of connected standby for too long without entering DRIPS (deepest runtime idle platform state) due to an unsatisfied device constraint with no activators active.
<p>2 - nt!TRIAGE_POP_FX_DEVICE Device</p>
<p>3 - Component index</p>
<p>4 - Reserved</p>
0x3 : DRIPS watchdog preveto timeout. The system has been in the resiliency phase of connected standby for too long without entering DRIPS (deepest runtime idle platform state) due to an active PEP pre-veto with no unsatisfied device constraint and with no activators active.
<p>2 - Veto code</p>
<p>3 - A pointer to the veto name string (PWSTR)</p>
<p>4 - A pointer to the PEP PPM callback</p>
0x4 : Deep Sleep Watchdog
<p>2 - Metrics</p>
<p>3 -NonDeepSleepDurationMs</p>
<p>4 - Reserved</p>
0x5 : Deep Sleep Power Setting Watchdog
<p>2 - Metrics</p>
<p>3 -NonDeepSleepDurationMs</p>
<p>4 - Reserved</p></td>
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

 

Cause
-----

This machine is exhibiting behavior that reduces screen-off battery life. Typically this is caused by CPU activity, device activity, or devices being in an insufficient idle state.

 

 




