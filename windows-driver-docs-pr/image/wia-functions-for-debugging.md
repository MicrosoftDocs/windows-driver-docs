---
title: WIA Functions for Debugging
description: WIA Functions for Debugging
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Functions for Debugging





You can use the following function to log trace messages, warning messages, and error messages when you are developing your WIA minidriver.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgdump" data-raw-source="[&lt;strong&gt;wiauDbgDump&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgdump)"><strong>wiauDbgDump</strong></a></p></td>
<td><p>Logs a message containing one or more data values.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgerror" data-raw-source="[&lt;strong&gt;wiauDbgError&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgerror)"><strong>wiauDbgError</strong></a></p></td>
<td><p>Logs an error message.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgerrorhr" data-raw-source="[&lt;strong&gt;wiauDbgErrorHr&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgerrorhr)"><strong>wiauDbgErrorHr</strong></a></p></td>
<td><p>Logs a message containing an HRESULT and its error message string.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgflags" data-raw-source="[&lt;strong&gt;wiauDbgFlags&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgflags)"><strong>wiauDbgFlags</strong></a></p></td>
<td><p>Determines whether a particular debugging flag is set.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbghelper" data-raw-source="[&lt;strong&gt;wiauDbgHelper&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbghelper)"><strong>wiauDbgHelper</strong></a></p></td>
<td><p>Formats a message and writes it to a log file or the debugger.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbghelper2" data-raw-source="[&lt;strong&gt;wiauDbgHelper2&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbghelper2)"><strong>wiauDbgHelper2</strong></a></p></td>
<td><p>Writes a message to a log file, or debugger, or both.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbginit" data-raw-source="[&lt;strong&gt;wiauDbgInit&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbginit)"><strong>wiauDbgInit</strong></a></p></td>
<td><p>Initializes WIA debugging.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacyerror" data-raw-source="[&lt;strong&gt;wiauDbgLegacyError&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacyerror)"><strong>wiauDbgLegacyError</strong></a></p></td>
<td><p>Logs an error message.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacyerror2" data-raw-source="[&lt;strong&gt;wiauDbgLegacyError2&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacyerror2)"><strong>wiauDbgLegacyError2</strong></a></p></td>
<td><p>Logs an error message.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacyhresult2" data-raw-source="[&lt;strong&gt;wiauDbgLegacyHresult2&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacyhresult2)"><strong>wiauDbgLegacyHresult2</strong></a></p></td>
<td><p>Logs a default message containing an HRESULT.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacytrace" data-raw-source="[&lt;strong&gt;wiauDbgLegacyTrace&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacytrace)"><strong>wiauDbgLegacyTrace</strong></a></p></td>
<td><p>Logs a trace message.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacytrace2" data-raw-source="[&lt;strong&gt;wiauDbgLegacyTrace2&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacytrace2)"><strong>wiauDbgLegacyTrace2</strong></a></p></td>
<td><p>Logs a trace message.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacywarning" data-raw-source="[&lt;strong&gt;wiauDbgLegacyWarning&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacywarning)"><strong>wiauDbgLegacyWarning</strong></a></p></td>
<td><p>Logs a warning message.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgsetflags" data-raw-source="[&lt;strong&gt;wiauDbgSetFlags&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgsetflags)"><strong>wiauDbgSetFlags</strong></a></p></td>
<td><p>Sets debugging flags.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgtrace" data-raw-source="[&lt;strong&gt;wiauDbgTrace&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgtrace)"><strong>wiauDbgTrace</strong></a></p></td>
<td><p>Logs a trace message.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgwarning" data-raw-source="[&lt;strong&gt;wiauDbgWarning&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgwarning)"><strong>wiauDbgWarning</strong></a></p></td>
<td><p>Logs a warning message.</p></td>
</tr>
</tbody>
</table>

 

