---
title: DEBUG\_TYPEOPTS\_XXX
description: The type options affect how the engine formats numbers and strings for output.
ms.assetid: 1c39fb80-d51b-43a6-8a68-8479022baf8a
ms.author: domars
ms.date: 12/07/2017
topic_type:
- apiref
api_name:
- DEBUG_TYPEOPTS_UNICODE_DISPLAY
- DEBUG_TYPEOPTS_LONGSTATUS_DISPLAY
- DEBUG_TYPEOPTS_FORCERADIX_OUTPUT
api_location:
- DbgEng.h
api_type:
- HeaderDef
ms.localizationpriority: medium
---

# DEBUG\_TYPEOPTS\_XXX


The type options affect how the engine formats numbers and strings for output.

The options are represented by a bit-set with the following bit flags.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Constant</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><span id="DEBUG_TYPEOPTS_UNICODE_DISPLAY"></span><span id="debug_typeopts_unicode_display"></span>
<strong>DEBUG_TYPEOPTS_UNICODE_DISPLAY</strong></td>
<td align="left"><p>When this bit is set, USHORT pointers and arrays are output as Unicode characters.</p>
<p>This is equivalent to the debugger command <strong>.enable_unicode 1</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><span id="DEBUG_TYPEOPTS_LONGSTATUS_DISPLAY"></span><span id="debug_typeopts_longstatus_display"></span>
<strong>DEBUG_TYPEOPTS_LONGSTATUS_DISPLAY</strong></td>
<td align="left"><p>When this bit is set, LONG integers are output in the default base instead of decimal.</p>
<p>This is equivalent to the debugger command <strong>.enable_long_status 1</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><span id="DEBUG_TYPEOPTS_FORCERADIX_OUTPUT"></span><span id="debug_typeopts_forceradix_output"></span>
<strong>DEBUG_TYPEOPTS_FORCERADIX_OUTPUT</strong></td>
<td align="left"><p>When this bit is set, integers (except for LONG integers) are output in the default base instead of decimal.</p>
<p>This is equivalent to the debugger command <strong>.force_radix_output 1</strong>.</p></td>
</tr>
</tbody>
</table>

Remarks
-------

By default, all of the type formatting options are turned off.

For more information about types, see [Types](https://msdn.microsoft.com/library/windows/hardware/ff558931).

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

 

 





