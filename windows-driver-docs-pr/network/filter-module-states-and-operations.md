---
title: Filter Module States and Operations
description: Filter Module States and Operations
ms.assetid: b5798865-8332-477b-b155-79a3db6ff6fa
keywords:
- filter drivers WDK networking , states
- NDIS filter drivers WDK , states
- states WDK NDIS filter
- Detached state WDK networking
- Attaching state WDK networking
- Paused state WDK networking
- Restarting state WDK networking
- Running state WDK ne
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Module States and Operations





A filter driver must support the following operational states for each filter module (instance of a filter driver) that the driver manages:

<a href="" id="detached"></a>Detached  
The *Detached* state is the initial state of a filter module. When a filter module is in this state, NDIS can call the filter driver's [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) function to attach the filter module to the driver stack.

<a href="" id="attaching"></a>Attaching  
In the *Attaching* state, a filter driver prepares to attach the filter module to the driver stack.

<a href="" id="paused"></a>Paused  
In the *Paused* state, the filter driver does not perform send or receive operations.

<a href="" id="restarting"></a>Restarting  
In the *Restarting* state, a filter driver completes any operations that are required to restart send and receive operations for a filter module.

<a href="" id="running"></a>Running  
In the *Running* state, a filter driver performs normal send and receive processing for a filter module.

<a href="" id="pausing"></a>Pausing  
In the *Pausing* state, a filter driver completes any operations that are required to stop send and receive operations for a filter module.

In the following table, the headings are the filter module states. Major events are listed in the first column. The rest of the entries in the table specify the next state that the filter module enters after an event occurs within a state. The blank entries represent invalid event/state combinations.

<table style="width:100%;">
<colgroup>
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event/State</th>
<th align="left">Detached</th>
<th align="left">Attaching</th>
<th align="left">Paused</th>
<th align="left">Restarting</th>
<th align="left">Running</th>
<th align="left">Pausing</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Filter attach</p></td>
<td align="left"><p>Attaching</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Attach is complete</p></td>
<td align="left"></td>
<td align="left"><p>Paused</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Filter detach</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Detached</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Filter restart</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Restarting</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Restart is complete</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Running</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Filter pause</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Pausing</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Pause is complete</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Paused</p></td>
</tr>
<tr class="even">
<td align="left"><p>Attach failed</p></td>
<td align="left"></td>
<td align="left"><p>Detached</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Restart failed</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Paused</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Send and Receive</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Running</p></td>
<td align="left"><p>Pausing</p></td>
</tr>
<tr class="odd">
<td align="left"><p>OID Requests</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Paused</p></td>
<td align="left"><p>Restarting</p></td>
<td align="left"><p>Running</p></td>
<td align="left"><p>Pausing</p></td>
</tr>
</tbody>
</table>

 

The primary filter driver events are defined as follows:

<a href="" id="--------filter-attach--------"></a> Filter attach   
NDIS called the driver's [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) function to attach a filter module to a driver stack. For more information about attaching a filter module, see [Attaching a Filter Module](attaching-a-filter-module.md).

<a href="" id="attach-is-complete"></a>Attach is complete  
When a filter module is in the *Attaching* state and the filter driver completes initialization of all the resources that the filter module requires, the filter module enters the *Paused* state.

<a href="" id="--------filter-detach--------"></a> Filter detach   
NDIS called the driver's [*FilterDetach*](https://msdn.microsoft.com/library/windows/hardware/ff549918) function to detach a filter module from a driver stack. For more information, see [Detaching a Filter Module](detaching-a-filter-module.md).

<a href="" id="--------filter-restart--------"></a> Filter restart   
NDIS called the driver's [*FilterRestart*](https://msdn.microsoft.com/library/windows/hardware/ff559435) function to restart a paused filter module. For more information, see [Starting a Filter Module](starting-a-filter-module.md).

<a href="" id="restart-is-complete"></a>Restart is complete  
When the filter module is in the *Restarting* state and the driver is ready to perform send and receive operations, the filter module enters the *Running* state.

<a href="" id="--------filter-pause--------"></a> Filter pause   
NDIS called the driver's [*FilterPause*](https://msdn.microsoft.com/library/windows/hardware/ff549957) function to pause a filter module. For more information, see [Pausing a Filter Module](pausing-a-filter-module.md).

<a href="" id="pause-is-complete"></a>Pause is complete  
After the driver has completed all operations that are required to stop send and receive operations, the pause operation is complete and the filter module is in the *Paused* state.

<a href="" id="attach-failed"></a>Attach failed  
If NDIS calls a driver's [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) function and the attach operation fails (for example, because the required resources are not available), the filter module returns to the *Detached* state.

<a href="" id="restart-failed"></a>Restart failed  
If NDIS calls a driver's [*FilterRestart*](https://msdn.microsoft.com/library/windows/hardware/ff549962) function and the restart attempt fails, the filter module returns to the *Paused* state.

<a href="" id="send-and-receive-operations"></a>Send and Receive Operations  
A driver can handle send and receive operations in the *Running* and *Pausing* states. For more information about send and receive operations, see [Filter Module Send and Receive Operations](filter-module-send-and-receive-operations.md).

<a href="" id="oid-requests"></a>OID Requests  
A driver can handle OID requests in the *Running*, *Restarting*, *Paused*, and *Pausing* states. For more information about OID requests, see [Filter Module OID Requests](filter-module-oid-requests.md).

 

 





