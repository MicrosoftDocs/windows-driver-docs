---
title: Protocol Binding States and Operations
description: Protocol Binding States and Operations
ms.assetid: 669b3de1-7f6b-4e63-8943-c8eaadfa80fc
keywords:
- protocol drivers WDK networking , binding operational states
- NDIS protocol drivers WDK , binding operation states
- binding states WDK networking
- protocol drivers WDK networking , events
- NDIS protocol drivers WDK , events
- events WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Protocol Binding States and Operations





An NDIS protocol driver must support the following operational states for each binding that the driver manages:

<a href="" id="unbound"></a>Unbound  
The Unbound state is the initial state of a binding. In this state, the protocol driver waits for NDIS to call the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function.

<a href="" id="opening"></a>Opening  
In the Opening state, a protocol driver allocates resources for the binding and attempts to open the adapter.

<a href="" id="running"></a>Running  
In the Running state, a protocol driver performs send and receive processing for a binding.

<a href="" id="closing"></a>Closing  
In the Closing state, the protocol driver closes the binding to the adapter and then releases the resources for the binding.

<a href="" id="pausing"></a>Pausing  
In the Pausing state, a protocol driver completes any operations that are required to stop send and receive operations for a binding.

<a href="" id="paused"></a>Paused  
In the Paused state, the protocol driver does not perform send or receive operations for a binding.

<a href="" id="restarting"></a>Restarting  
In the Restarting state, a protocol driver completes any operations that are required to restart send and receive operations for a binding.

In the following table, the headings represent the binding states, and events are listed in the first column. The rest of the entries in the table specify the next state that the binding enters after an event occurs within a state. The blank entries represent invalid event/state combinations.

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
<th align="left">Unbound</th>
<th align="left">Opening</th>
<th align="left">Closing</th>
<th align="left">Paused</th>
<th align="left">Restarting</th>
<th align="left">Running</th>
<th align="left">Pausing</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>ProtocolBindAdapterEx</em></p></td>
<td align="left"><p>Opening</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Bind failed</p></td>
<td align="left"></td>
<td align="left"><p>Unbound</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Bind is complete</p></td>
<td align="left"></td>
<td align="left"><p>Paused</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><em>ProtocolUnbindAdapterEx</em></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Closing</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Unbind is complete</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Unbound</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>PnP pause</p></td>
<td align="left"></td>
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
<td align="left"></td>
<td align="left"><p>Paused</p></td>
</tr>
<tr class="even">
<td align="left"><p>PnP restart</p></td>
<td align="left"></td>
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
<td align="left"></td>
<td align="left"><p>Running</p></td>
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
<td align="left"><p>Closing</p></td>
<td align="left"><p>Paused</p></td>
<td align="left"><p>Restarting</p></td>
<td align="left"><p>Running</p></td>
<td align="left"><p>Pausing</p></td>
</tr>
</tbody>
</table>

 

**Note**  The events listed in the preceding table are the primary events for an NDIS protocol binding. Additional events will be added to this table as the information becomes available.

 

The primary binding events are defined as follows:

<a href="" id="protocolbindadapterex"></a>*ProtocolBindAdapterEx*  
After NDIS calls the driver's [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function, the binding enters the Opening state. For more information, see [Binding to an Adapter](binding-to-an-adapter.md).

<a href="" id="bind-failed"></a>Bind failed  
If the protocol driver fails to bind to the adapter, the binding returns to the Unbound state.

<a href="" id="bind-is-complete"></a>Bind is complete  
If the driver successfully opens the adapter, the binding enters the Paused state. The driver completes the bind operation.

<a href="" id="protocolunbindadapterex"></a>*ProtocolUnbindAdapterEx*  
After NDIS calls the driver's [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) hander, the binding enters the *Closing* state. For more information, see [Unbinding from an Adapter](unbinding-from-an-adapter.md).

<a href="" id="unbind-is-complete"></a>Unbind is complete  
After the driver completes the unbind operation, the binding enters the Unbound state.

<a href="" id="pnp-pause"></a>PnP Pause  
After NDIS sends the protocol driver a network Plug and Play (PnP) pause event notification, the binding enters the Pausing state. For more information see [Pausing a Binding](pausing-a-binding.md).

<a href="" id="pause-is-complete"></a>Pause is complete  
After the driver has completed all operations that are required to stop send and receive operations, the pause operation is complete and the binding is in the Paused state.

**Note**  The driver must wait for all its outstanding send requests to complete before the pause operation is complete.

 

<a href="" id="pnp-restart"></a>PnP Restart  
After NDIS sends the protocol driver a network PnP restart event notification, the binding enters the Restarting state. For more information, see [Restarting a Binding](restarting-a-binding.md).

<a href="" id="restart-is-complete"></a>Restart is complete  
After the driver is ready to handle send and receive operations, the restart operation is complete and the binding is in the Running state.

<a href="" id="restart-failed"></a>Restart failed  
If NDIS sends the protocol driver a network PnP restart event notification and the restart attempt fails, the binding returns to the Paused state.

<a href="" id="send-and-receive-operations"></a>Send and Receive Operations  
A protocol driver must handle send and receive operations in the Running and Pausing states. For more information about send and receive operations, see [Protocol Driver Send and Receive Operations](protocol-driver-send-and-receive-operations.md).

<a href="" id="oid-requests"></a>OID Requests  
A protocol driver can initiate OID requests to set or query information in underlying drivers. A protocol driver can initiate OID requests from all states, except Unbound and Opening.

## Related topics


[Writing NDIS Protocol Drivers](writing-ndis-protocol-drivers.md)

 

 






