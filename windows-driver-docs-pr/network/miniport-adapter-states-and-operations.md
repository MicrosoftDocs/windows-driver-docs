---
title: Miniport Adapter States and Operations
description: Miniport Adapter States and Operations
ms.assetid: b47e2cbe-9da3-4600-9afe-b082e60b87fb
keywords:
- miniport adapters WDK networking , states
- adapters WDK networking , states
- miniport adapters WDK networking , operations
- adapters WDK networking , operations
- Halted state WDK networking
- Shutdown state WDK networking
- Initializing state WDK ne
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Adapter States and Operations





For each adapter that it manages, an NDIS 6.0 or later miniport driver must support the following set of operational states:

<a href="" id="halted"></a>Halted  
The Halted state is the initial state of all adapters. When an adapter is in the Halted state, NDIS can call the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function to initialize the adapter.

<a href="" id="shutdown"></a>Shutdown  
In the Shutdown state, a system shutdown and restart must occur before the system can use the adapter again.

<a href="" id="initializing"></a>Initializing  
In the Initializing state, a miniport driver completes any operations that are required to initialize an adapter.

<a href="" id="paused"></a>Paused  
In the Paused state, the adapter does not indicate received network data or accept send requests.

<a href="" id="restarting"></a>Restarting  
In the Restarting state, a miniport driver completes any operations that are required to restart send and receive operations for an adapter.

<a href="" id="running"></a>Running  
In the Running state, a miniport driver performs send and receive processing for an adapter.

<a href="" id="pausing"></a>Pausing  
In the Pausing state, a miniport driver completes any operations that are required to stop send and receive operations for an adapter.

In the following table, the headings are the adapter states. Major events are listed in the first column. The rest of the entries in the table specify the next state that the adapter enters after an event occurs within a state. The blank entries represent invalid event/state combinations.

<table>
<colgroup>
<col width="12%" />
<col width="12%" />
<col width="12%" />
<col width="12%" />
<col width="12%" />
<col width="12%" />
<col width="12%" />
<col width="12%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event \ State</th>
<th align="left">Halted</th>
<th align="left">Shutdown</th>
<th align="left">Initializing</th>
<th align="left">Paused</th>
<th align="left">Restarting</th>
<th align="left">Running</th>
<th align="left">Pausing</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559389" data-raw-source="[&lt;em&gt;MiniportInitializeEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559389)"><em>MiniportInitializeEx</em></a></p></td>
<td align="left"><p>Initializing</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Initialize is complete</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Paused</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559449" data-raw-source="[&lt;em&gt;MiniportShutdownEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559449)"><em>MiniportShutdownEx</em></a></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Shutdown</p></td>
<td align="left"><p>Shutdown</p></td>
<td align="left"><p>Shutdown</p></td>
<td align="left"><p>Shutdown</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559388" data-raw-source="[&lt;em&gt;MiniportHaltEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559388)"><em>MiniportHaltEx</em></a></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Halted</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559435" data-raw-source="[&lt;em&gt;MiniportRestart&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559435)"><em>MiniportRestart</em></a></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Restarting</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Restart is complete</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Running</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559418" data-raw-source="[&lt;em&gt;MiniportPause&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559418)"><em>MiniportPause</em></a></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Pausing</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Pause is complete</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Paused</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Initialize failed</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Halted</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Restart failed</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Paused</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Send and receive operations</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Running</p></td>
<td align="left"><p>Pausing</p></td>
</tr>
<tr class="even">
<td align="left"><p>OID requests</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Paused</p></td>
<td align="left"><p>Restarting</p></td>
<td align="left"><p>Running</p></td>
<td align="left"><p>Pausing</p></td>
</tr>
</tbody>
</table>

 

**Note**  The events listed in the preceding table are the primary events for an NDIS 6.0 or later adapter.

 

**Note**  The reset operation does not affect miniport adapter operational states. The state of the adapter might change while a reset operation is in progress. For example, NDIS might call a driver's pause handler when there is a reset operation in progress. In this case, the driver can complete either the reset or the pause operation in any order while following the normal requirements for each operation. For a reset operation, the driver can fail transmit request packets or it can keep them queued and complete them later. However, you should note that an overlying driver cannot complete a pause operation while its transmit packets are pending.

 

The primary miniport driver events are defined as follows:

<a href="" id="miniportinitializeex"></a>MiniportInitializeEx  
NDIS called the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function to initialize an adapter. For more information about adapter initialization, see [Initializing a Miniport Adapter](initializing-a-miniport-adapter.md).

<a href="" id="initialize-is-complete"></a>Initialize is complete  
After [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) returns successfully, the initialize operation is complete and the adapter is in the Paused state.

<a href="" id="miniportshutdownex"></a>MiniportShutdownEx  
NDIS called the driver's [*MiniportShutdownEx*](https://msdn.microsoft.com/library/windows/hardware/ff559449) function to shutdown an adapter. For more information, see [Miniport Adapter Shutdown](miniport-adapter-shutdown.md).

<a href="" id="miniporthaltex"></a>MiniportHaltEx  
NDIS called the driver's [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function to halt an adapter. For more information, see [Halting a Miniport Adapter](halting-a-miniport-adapter.md).

<a href="" id="miniportrestart"></a>MiniportRestart  
NDIS called the driver's [**MiniportRestart**](https://msdn.microsoft.com/library/windows/hardware/ff559435) function to restart a paused adapter. Because an adapter is in the Paused state after initialization, this event is also required to start the adapter after adapter initialization is complete. For more information, see [Starting an Adapter](starting-an-adapter.md).

<a href="" id="restart-is-complete"></a>Restart is complete  
After the driver is ready to handle send and receive operations, the restart operation is complete and the adapter is in the Running state.

<a href="" id="miniportpause"></a>MiniportPause  
NDIS called the driver's [*MiniportPause*](https://msdn.microsoft.com/library/windows/hardware/ff559418) function to pause an adapter. For more information, see [Pausing an Adapter](pausing-an-adapter.md).

<a href="" id="pause-is-complete"></a>Pause is complete  
After the driver has completed all operations that are necessary to stop send and receive operations, the pause operation is complete and the adapter is in the Paused state.

**Note**  The driver must wait for NDIS to return all its outstanding receive indications before the pause operation is complete.

 

<a href="" id="initialize-failed"></a>Initialize failed  
If NDIS calls a driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function and the initialization attempt fails, the adapter returns to the Halted state.

<a href="" id="restart-failed"></a>Restart failed  
If NDIS calls a driver's [**MiniportRestart**](https://msdn.microsoft.com/library/windows/hardware/ff559435) function and the restart attempt fails, the adapter remains in the Paused state.

<a href="" id="send-and-receive-operations"></a>Send and Receive Operations  
A driver must handle send and receive operations in the Running and Pausing states. For more information about send and receive operations, see [Miniport Driver Send and Receive Operations](miniport-driver-send-and-receive-operations.md).

<a href="" id="oid-requests"></a>OID Requests  
A driver must handle OID Requests in the Running, Restarting, Paused, and Pausing states. For more information about OID requests, see [OID Requests for an Adapter](miniport-adapter-oid-requests.md).

## Related topics


[Halting a Miniport Adapter](halting-a-miniport-adapter.md)

[Initializing a Miniport Adapter](initializing-a-miniport-adapter.md)

[Miniport Adapter Shutdown](miniport-adapter-shutdown.md)

[Miniport Driver Send and Receive Operations](miniport-driver-send-and-receive-operations.md)

[Pausing an Adapter](pausing-an-adapter.md)

[Starting an Adapter](starting-an-adapter.md)

 

 






