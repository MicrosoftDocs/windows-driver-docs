---
title: DEBUG\_ATTACH\_XXX
description: The DEBUG\_ATTACH\_*XXX* bit-flags described in this topic control how the debugger engine attaches to a user-mode process.
ms.author: domars
ms.date: 08/10/2018
topic_type:
- apiref
api_name:
- DEBUG_ATTACH_XXX
api_location:
- DbgEng.h
api_type:
- HeaderDef
ms.localizationpriority: medium
---

# DEBUG\_ATTACH\_XXX

The DEBUG\_ATTACH\_*XXX* bit-flags described in this topic control how the debugger engine attaches to a user-mode process. For the DEBUG_ATTACH_XXX options used when attaching to a kernel target, see the [IDebugClient::AttachKernel method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugclient-attachkernel).

The possible values include the following.

<table>
<tr>
<th>Constant</th>
<th>Description</th>
</tr>
<tr VALIGN="top">
<td align="left" width="40%"><a id="DEBUG_ATTACH_NONINVASIVE"></a><a id="debug_attach_noninvasive"></a><dl>
<dt><b>DEBUG_ATTACH_NONINVASIVE</b></dt>
</dl>
</td>
<td align="left" width="60%">
<p>Attach to the target noninvasively.  For more information about noninvasive debugging, see <a href="https://docs.microsoft.com/windows-hardware/drivers/debugger/noninvasive-debugging--user-mode-" data-raw-source="[Noninvasive Debugging (User Mode)](https://docs.microsoft.com/windows-hardware/drivers/debugger/noninvasive-debugging--user-mode-)">Noninvasive Debugging (User Mode)</a>.</p>
<p>If this flag is set, then the flags DEBUG_ATTACH_EXISTING, DEBUG_ATTACH_INVASIVE_NO_INITIAL_BREAK, and DEBUG_ATTACH_INVASIVE_RESUME_PROCESS must not be set.</p>
</td>
</tr>
<tr VALIGN="top">
<td align="left" width="40%"><a id="DEBUG_ATTACH_EXISTING"></a><a id="debug_attach_existing"></a><dl>
<dt><b>DEBUG_ATTACH_EXISTING</b></dt>
</dl>
</td>
<td align="left" width="60%">
<p>Re-attach to an application to which a debugger has already attached (and possibly abandoned).  For more information about re-attaching to targets, see <a href="https://docs.microsoft.com/windows-hardware/drivers/debugger/-attach--attach-to-process-" data-raw-source="[.attach (Attach to Process)](https://docs.microsoft.com/windows-hardware/drivers/debugger/-attach--attach-to-process-)">.attach (Attach to Process)</a>.</p>
<p>If this flag is set, then the other DEBUG_ATTACH_<i>XXX</i> flags must not be set.</p>
</td>
</tr>
<tr VALIGN="top">
<td align="left" width="40%"><a id="DEBUG_ATTACH_NONINVASIVE_NO_SUSPEND"></a><a id="debug_attach_noninvasive_no_suspend"></a><dl>
<dt><b>DEBUG_ATTACH_NONINVASIVE_NO_SUSPEND</b></dt>
</dl>
</td>
<td align="left" width="60%">
<p>Do not suspend the target&#39;s threads when attaching noninvasively.</p>
<p>If this flag is set, then the flag DEBUG_ATTACH_NONINVASIVE must also be set.</p>
</td>
</tr>
<tr VALIGN="top">
<td align="left" width="40%"><a id="DEBUG_ATTACH_INVASIVE_NO_INITIAL_BREAK"></a><a id="debug_attach_invasive_no_initial_break"></a><dl>
<dt><b>DEBUG_ATTACH_INVASIVE_NO_INITIAL_BREAK</b></dt>
</dl>
</td>
<td align="left" width="60%">
<p>(Windows XP and later)  Do not request an initial break-in when attaching to the target.</p>
<p>If this flag is set, then the flags DEBUG_ATTACH_NONINVASIVE and DEBUG_ATTACH_EXISTING must not be set.</p>
</td>
</tr>
<tr VALIGN="top">
<td align="left" width="40%"><a id="DEBUG_ATTACH_INVASIVE_RESUME_PROCESS"></a><a id="debug_attach_invasive_resume_process"></a><dl>
<dt><b>DEBUG_ATTACH_INVASIVE_RESUME_PROCESS</b></dt>
</dl>
</td>
<td align="left" width="60%">
<p>Resume all of the target&#39;s threads when attaching invasively.</p>
<p>If this flag is set, then the flags DEBUG_ATTACH_NONINVASIVE and DEBUG_ATTACH_EXISTING must not be set.</p>
</td>
</tr>
</table>


Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">DbgEng.h (include DbgEng.h)</td>
</tr>
</tbody>
</table>

 

 





