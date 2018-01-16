---
title: DEBUG\_FILTER\_XXX
description: DEBUG\_FILTER\_XXX
ms.assetid: 1f8f738b-7b2b-419a-949e-b71f937de02d
ms.author: domars
ms.date: 12/07/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["DEBUG_FILTER_XXX Windows Debugging"]
topic_type:
- apiref
api_name:
- DEBUG_FILTER_XXX
api_location:
- DbgEng.h
api_type:
- HeaderDef
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
<td align="left"><p>The [<em>exception</em>](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-exception) has been handled.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20DEBUG_FILTER_XXX%20%20RELEASE:%20%2811/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




