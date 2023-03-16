---
title: Bug Check 0x15F CONNECTED_STANDBY_WATCHDOG_TIMEOUT_LIVEDUMP
description: The CONNECTED_STANDBY_WATCHDOG_TIMEOUT_LIVEDUMP live dump has a value of 0x0000015F. This indicates that a connected standby watchdog timeout has occurred.
keywords: ["Bug Check 0x15F CONNECTED_STANDBY_WATCHDOG_TIMEOUT_LIVEDUMP", "CONNECTED_STANDBY_WATCHDOG_TIMEOUT_LIVEDUMP"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- CONNECTED_STANDBY_WATCHDOG_TIMEOUT_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x15F: CONNECTED\_STANDBY\_WATCHDOG\_TIMEOUT\_LIVEDUMP


The CONNECTED\_STANDBY\_WATCHDOG\_TIMEOUT\_LIVEDUMP live dump has a value of 0x0000015F. This indicates that a connected standby watchdog timeout has occurred.

(This code can never be used for a real bug check; it is used to identify live dumps.)

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


## Cause

This machine is exhibiting behavior that reduces screen-off battery life. Typically this is caused by CPU activity, device activity, or devices being in an insufficient idle state.

## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)
 

 




