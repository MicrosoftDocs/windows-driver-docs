---
title: C28118
description: irq-exceeds-caller
ms.assetid: 
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28118

warning: C28118: Copying a whole IRP stack entry leaves certain fields initialized that should be cleared or updated.

The current function is permitted to run at an IRQ level 
above the maximum permitted for %func% (%level%). 
Prior function calls or annotation are inconsistent with 
use of that function

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>The current function may need <em>IRQL_requires_max</em>, or it may be that the limit is set by some prior call.</p></td>
</tr>
</tbody>
</table>

The function being called is limited to being called at 
or below some IRQL.  The calling (current) function is 
allowed to run at some higher IRQL, and making that call 
could cause the called function to run at an IRQL it 
cannot operate at.

Note that PREfast will attempt to infer what it can about 
the current IRQ level, and this warning is generated only
when it has inferred enough about the IRQ level to detect 
the error.  Inference may come from the signature of the 
function being analyzed or prior calls along the current 
path.
