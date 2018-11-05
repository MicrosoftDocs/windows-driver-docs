---
title: Event Filters
description: Event Filters
ms.assetid: 91f2a483-8971-42de-a6c5-cc25409279a5
keywords: ["Debugger Engine API, event filters"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Event Filters


*Event filters* provide simple event filtering; they influence how the debugger engine proceeds after an event occurs in a target. When an event occurs, the engine determines whether that event matches an event filter. If it does, the break status for the event filter influences whether the debugger will break into the target. If the event is an exception event, the handling status determines whether the exception should be considered handled or not-handled in the target.

**Note**   If more sophisticated event filtering is required, event callbacks can be used.

 

Event filters are divided into three categories.

1.  *Specific event filters*. These are the filters for all the non-exception events. See [**DEBUG\_FILTER\_XXX**](https://msdn.microsoft.com/library/windows/hardware/ff541490) for a list of these events.

2.  *Specific exception filters*. The first specific exception filter is the *default exception filter*. The rest are filters for those exceptions for which the engine has built-in filters. See [**Specific Exceptions**](https://msdn.microsoft.com/library/windows/hardware/ff558784) for a list of the specific exception filters.

3.  *Arbitrary exception filters*. These are filters for exception events that have been added manually.

The filters in categories 1 and 2 are collectively known as *specific filters*, and the filters in categories 2 and 3 are collectively known as *exception filters*. The number of filters in each category is returned by [**GetNumberEventFilters**](https://msdn.microsoft.com/library/windows/hardware/ff547899).

An event matches a specific event filter if the type of the event is the same as the type of the filter. Some event filters have an additional parameter which further restricts the events they match.

An exception event matches an exception filter if the exception code for the exception event is the same as the exception code for the exception filter. If there is no exception filter with the same exception code as the exception event, the exception event will be handled by the default exception filter.

### <span id="commands_and_parameters"></span><span id="COMMANDS_AND_PARAMETERS"></span>Commands and Parameters

Event filters can have a debugger command associated with them. This command is executed by the engine when an event matching the filter occurs. [**GetEventFilterCommand**](https://msdn.microsoft.com/library/windows/hardware/ff546611) and [**SetEventFilterCommand**](https://msdn.microsoft.com/library/windows/hardware/ff556678) can be used to get and set this command. For exception filters, this command is executed on the first-chance of the exception. A separate second-chance command can be executed upon the second-chance exception event. To get and set the second-chance command, use [**GetExceptionFilterSecondCommand**](https://msdn.microsoft.com/library/windows/hardware/ff546653) and [**SetExceptionSecondChanceCommand**](https://msdn.microsoft.com/library/windows/hardware/ff556687).

The parameters for specific event filters and exception filters are returned by [**GetSpecificFilterParameters**](https://msdn.microsoft.com/library/windows/hardware/ff548398) and [**GetExceptionFilterParameters**](https://msdn.microsoft.com/library/windows/hardware/ff556683). The break status and handling status for event filters can be set using [**SetSpecificFilterParameters**](https://msdn.microsoft.com/library/windows/hardware/ff556795) and **SetExceptionFilterParameters**.

**SetExceptionFilterParameters** can also be used to add and remove arbitrary exception filters.

A short description of specific filters is returned by [**GetEventFilterText**](https://msdn.microsoft.com/library/windows/hardware/ff546618).

Some specific filters take arguments that restrict which events the filter matches. [**GetSpecificFilterArgument**](https://msdn.microsoft.com/library/windows/hardware/ff548386) and [**SetSpecificFilterArgument**](https://msdn.microsoft.com/library/windows/hardware/ff556791) will get and set arguments for those specific filters which support arguments. If a specific filter has no argument, there is no restriction on which events it matches. The following table lists the event filters that take arguments and how they restrict the events which match them:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event</th>
<th align="left">Match criteria</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Create Process</p></td>
<td align="left"><p>The name of the created process must match the argument.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Exit Process</p></td>
<td align="left"><p>The name of the exited process must match the argument.1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Load Module</p></td>
<td align="left"><p>The name of the loaded module must match the argument.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Unload Module</p></td>
<td align="left"><p>The base address of the unloaded module must be the same as the argument.2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Target Output</p></td>
<td align="left"><p>The debug output from the target must match the argument.3</p></td>
</tr>
</tbody>
</table>

 

**Note**  
1.  The argument uses the [string wildcard syntax](string-wildcard-syntax.md) and is compared with the image name (ignoring path) when the event occurs. If the name of the module or process is not available, it is considered a match.

2.  The argument is an expression that is evaluated by the engine when the argument is set.

3.  The argument uses the string wildcard syntax and is compared with the debug output from the target. If the output is not known, it is considered a match.

 

### <span id="index_and_exception_code"></span><span id="INDEX_AND_EXCEPTION_CODE"></span>Index and Exception Code

Each event filter has an index. The index is a number between zero and one less than the total number of filters (inclusive). The index range for each category of filters can be found from the *SpecificEvents*, *SpecificExceptions*, and *ArbitraryExceptions* values returned by [**GetNumberEventFilters**](https://msdn.microsoft.com/library/windows/hardware/ff547899), as described in the following table:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event Filters</th>
<th align="left">Index of first filter</th>
<th align="left">Number of filters</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Specific event filters</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p><em>SpecificEvents</em></p></td>
</tr>
<tr class="even">
<td align="left"><p>specific exception filters</p></td>
<td align="left"><p><em>SpecificEvents</em></p></td>
<td align="left"><p><em>SpecificExceptions</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p>arbitrary exception filters</p></td>
<td align="left"><p><em>SpecificEvents</em> + <em>SpecificExceptions</em></p></td>
<td align="left"><p><em>ArbitraryExceptions</em></p></td>
</tr>
</tbody>
</table>

 

The indices for the specific event filters are found in the first table located in the topic [**DEBUG\_FILTER\_XXX**](https://msdn.microsoft.com/library/windows/hardware/ff541490). The index of the default exception filter (the first specific exception filter) is *SpecificEvents*. When an arbitrary exception filter is removed, the indices of the other arbitrary exception filters can change.

The exception filters are usually specified by exception code. However, some methods require the index of the exception. To find the index of an exception filter for a given exception, use [**GetExceptionFilterParameters**](https://msdn.microsoft.com/library/windows/hardware/ff546650) to iterate over all the exception filters until you find the one with the same exception code as the exception. The exception codes for the specific exception filters can be found in the topic [**Specific Exceptions**](https://msdn.microsoft.com/library/windows/hardware/ff558784).

### <span id="system_errors"></span><span id="SYSTEM_ERRORS"></span>System Errors

When a system error occurs, the engine will break into the debugger or print the error to the output stream, if the error occurs at or below specified levels. These levels are returned by [**GetSystemErrorControl**](https://msdn.microsoft.com/library/windows/hardware/ff549215) and can be changed using [**SetSystemErrorControl**](https://msdn.microsoft.com/library/windows/hardware/ff556806).

 

 





