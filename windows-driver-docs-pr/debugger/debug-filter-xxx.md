---
title: DEBUG\_FILTER\_XXX
description: DEBUG\_FILTER\_XXX
ms.assetid: 1f8f738b-7b2b-419a-949e-b71f937de02d
ms.author: domars
ms.date: 12/07/2017
keywords: ["DEBUG_FILTER_XXX Windows Debugging"]
topic_type:
- apiref
api_name:
- DEBUG_FILTER_XXX
api_location:
- DbgEng.h
api_type:
- HeaderDef
ms.localizationpriority: medium
---

# DEBUG\_FILTER\_XXX


The DEBUG\_FILTER\_*XXX* constants are used for three different purposes: to specify individual specific event filters, to specify the break status of an event filter, and to specify the handling status of an exception filter.

### <span id="specific_event_filter"></span><span id="SPECIFIC_EVENT_FILTER"></span>Specific Event Filter

The following constants are used to specify specific event filters.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Event</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DEBUG_FILTER_CREATE_THREAD</p></td>
<td align="left"><p>Create Thread</p></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_FILTER_EXIT_THREAD</p></td>
<td align="left"><p>Exit Thread</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DEBUG_FILTER_CREATE_PROCESS</p></td>
<td align="left"><p>Create Process</p></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_FILTER_EXIT_PROCESS</p></td>
<td align="left"><p>Exit Process</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DEBUG_FILTER_LOAD_MODULE</p></td>
<td align="left"><p>Load Module</p></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_FILTER_UNLOAD_MODULE</p></td>
<td align="left"><p>Unload Module</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DEBUG_FILTER_SYSTEM_ERROR</p></td>
<td align="left"><p>System Error</p></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_FILTER_INITIAL_BREAKPOINT</p></td>
<td align="left"><p>Initial Break Point</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DEBUG_FILTER_INITIAL_MODULE_LOAD</p></td>
<td align="left"><p>Initial Module Load</p></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_FILTER_DEBUGGEE_OUTPUT</p></td>
<td align="left"><p>Target Output</p></td>
</tr>
</tbody>
</table>

 

### <span id="break_status"></span><span id="BREAK_STATUS"></span>Break Status

The following constants are used to specify the break status of an event filter.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DEBUG_FILTER_BREAK</p></td>
<td align="left"><p>The event will break into the debugger.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_FILTER_SECOND_CHANCE_BREAK</p></td>
<td align="left"><p>The event will break into the debugger if it is a second chance exception.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DEBUG_FILTER_OUTPUT</p></td>
<td align="left"><p>A notification of the event will be printed to the debugger console.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_FILTER_IGNORE</p></td>
<td align="left"><p>The event is ignored.</p></td>
</tr>
</tbody>
</table>

 

Additionally, for an arbitrary exception filter, setting the break status to DEBUG\_FILTER\_REMOVE, removes the event filter.

### <span id="handling_status"></span><span id="HANDLING_STATUS"></span>Handling Status

The following constants are used to specify the handling status of an exception filter.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DEBUG_FILTER_GO_HANDLED</p></td>
<td align="left"><p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-exception" data-raw-source="[&lt;em&gt;exception&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-exception)"><em>exception</em></a> has been handled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_FILTER_GO_NOT_HANDLED</p></td>
<td align="left"><p>The exception has not been handled.</p></td>
</tr>
</tbody>
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

 

 





