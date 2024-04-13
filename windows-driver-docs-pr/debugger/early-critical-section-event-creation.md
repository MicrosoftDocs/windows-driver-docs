---
title: Early Critical Section Event Creation
description: Early critical section event creation
keywords: ["Early critical section event creation (global flag)"]
ms.date: 05/23/2017
---

# Early critical section event creation


## <span id="ddk_early_critical_section_event_creation_dtools"></span><span id="DDK_EARLY_CRITICAL_SECTION_EVENT_CREATION_DTOOLS"></span>


The **Early critical section event creation** flag creates event handles when a critical section is initialized, rather than waiting until the event is needed.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>cse</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x10000000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_CRITSEC_EVENT_CREATION</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag, image file registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

When Windows cannot create an event, it generates the exception during initialization and the calls to enter and leave the critical section do not fail.

Because this flag uses a significant amount of nonpaged pool memory, use it only on very reliable systems that have sufficient memory.

 

 