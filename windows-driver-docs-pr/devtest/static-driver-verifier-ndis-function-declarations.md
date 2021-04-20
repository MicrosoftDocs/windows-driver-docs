---
title: Static Driver Verifier NDIS Function Declarations
description: Static Driver Verifier NDIS Function Declarations
keywords:
- SDV WDK , NDIS
- NDIS rules for SDV
- SDV WDK , NDIS rules
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Static Driver Verifier NDIS Function Declarations


To enable SDV to verify your NDIS driver, you must declare each callback function, by using a callback function role type. The callback function role types are defined in the Ndis.h header file and are included when you build your driver with that header file.

You must declare the driver's callback functions before you declare the callback function definitions. The following code example shows the function role type declaration for the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) callback function. This callback function must be declared by using the MINIPORT\_INITIALIZE role type. In this example, the callback function is called *myMiniportInitializeEx*.

```
#include <ndis.h>  
MINIPORT_INITIALIZE myMiniportInitializeEx
```

If a callback function has a function prototype declaration, you must replace the function prototype with the function role type declaration. For more information about the function role type declarations, see the [Using Function Role Type Declarations](using-function-role-type-declarations.md) topic.

The following table shows the callback function role types and the NDIS callback functions that they are associated with.

### <span id="required_function_declarations"></span><span id="REQUIRED_FUNCTION_DECLARATIONS"></span>Required Function Declarations

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">NDIS miniport driver callback function</th>
<th align="left">Role type name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_add_device" data-raw-source="[&lt;em&gt;MiniportAddDevice&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_add_device)"><em>MiniportAddDevice</em></a></p></td>
<td align="left"><p>MINIPORT_ADD_DEVICE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_direct_oid_request" data-raw-source="[&lt;em&gt;MiniportCancelDirectOidRequest&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_direct_oid_request)"><em>MiniportCancelDirectOidRequest</em></a></p></td>
<td align="left"><p>MINIPORT_CANCEL_DIRECT_OID_REQUEST</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_oid_request" data-raw-source="[&lt;em&gt;MiniportCancelOidRequest&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_oid_request)"><em>MiniportCancelOidRequest</em></a></p></td>
<td align="left"><p>MINIPORT_CANCEL_OID_REQUEST</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_send" data-raw-source="[&lt;em&gt;MiniportCancelSend&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_send)"><em>MiniportCancelSend</em></a></p></td>
<td align="left"><p>MINIPORT_CANCEL_SEND</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_check_for_hang" data-raw-source="[&lt;em&gt;MiniportCheckForHangEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_check_for_hang)"><em>MiniportCheckForHangEx</em></a></p></td>
<td align="left"><p>MINIPORT_CHECK_FOR_HANG</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_device_pnp_event_notify" data-raw-source="[&lt;em&gt;MiniportDevicePnPEventNotify&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_device_pnp_event_notify)"><em>MiniportDevicePnPEventNotify</em></a></p></td>
<td align="left"><p>MINIPORT_DEVICE_PNP_EVENT_NOTIFY</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_direct_oid_request" data-raw-source="[&lt;em&gt;MiniportDirectOidRequest&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_direct_oid_request)"><em>MiniportDirectOidRequest</em></a></p></td>
<td align="left"><p>MINIPORT_DIRECT_OID_REQUEST</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_disable_interrupt" data-raw-source="[&lt;em&gt;MiniportDisableInterruptEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_disable_interrupt)"><em>MiniportDisableInterruptEx</em></a></p></td>
<td align="left"><p>MINIPORT_DISABLE_INTERRUPT</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_disable_message_interrupt" data-raw-source="[&lt;em&gt;MiniportDisableMessageInterrupt&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_disable_message_interrupt)"><em>MiniportDisableMessageInterrupt</em></a></p></td>
<td align="left"><p>MINIPORT_DISABLE_MESSAGE_INTERRUPT</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_unload" data-raw-source="[&lt;em&gt;MiniportDriverUnload&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_unload)"><em>MiniportDriverUnload</em></a></p></td>
<td align="left"><p>MINIPORT_UNLOAD</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_enable_interrupt" data-raw-source="[&lt;em&gt;MiniportEnableInterruptEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_enable_interrupt)"><em>MiniportEnableInterruptEx</em></a></p></td>
<td align="left"><p>MINIPORT_ENABLE_INTERRUPT</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_enable_message_interrupt" data-raw-source="[&lt;em&gt;MiniportEnableMessageInterrupt&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_enable_message_interrupt)"><em>MiniportEnableMessageInterrupt</em></a></p></td>
<td align="left"><p>MINIPORT_ENABLE_MESSAGE_INTERRUPT</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp" data-raw-source="[&lt;em&gt;MiniportFilterResourceRequirements&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp)"><em>MiniportFilterResourceRequirements</em></a></p></td>
<td align="left"><p>MINIPORT_FILTER_RESOURCE_REQUIREMENTS</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt" data-raw-source="[&lt;em&gt;MiniportHaltEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt)"><em>MiniportHaltEx</em></a></p></td>
<td align="left"><p>MINIPORT_HALT</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize" data-raw-source="[&lt;em&gt;MiniportInitializeEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize)"><em>MiniportInitializeEx</em></a></p></td>
<td align="left"><p>MINIPORT_INITIALIZE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_isr" data-raw-source="[&lt;em&gt;MiniportInterrupt&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_isr)"><em>MiniportInterrupt</em></a></p></td>
<td align="left"><p>MINIPORT_ISR</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_interrupt_dpc" data-raw-source="[&lt;em&gt;MiniportInterruptDPC&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_interrupt_dpc)"><em>MiniportInterruptDPC</em></a></p></td>
<td align="left"><p>MINIPORT_INTERRUPT_DPC</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_message_interrupt" data-raw-source="[&lt;em&gt;MiniportMessageInterrupt&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_message_interrupt)"><em>MiniportMessageInterrupt</em></a></p></td>
<td align="left"><p>MINIPORT_MESSAGE_INTERRUPT</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_message_interrupt_dpc" data-raw-source="[&lt;em&gt;MiniportMessageInterruptDPC&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_message_interrupt_dpc)"><em>MiniportMessageInterruptDPC</em></a></p></td>
<td align="left"><p>MINIPORT_MESSAGE_INTERRUPT_DPC</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request" data-raw-source="[&lt;em&gt;MiniportOidRequest&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request)"><em>MiniportOidRequest</em></a></p></td>
<td align="left"><p>MINIPORT_OID_REQUEST</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pause" data-raw-source="[&lt;em&gt;MiniportPause&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pause)"><em>MiniportPause</em></a></p></td>
<td align="left"><p>MINIPORT_PAUSE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_process_sg_list" data-raw-source="[&lt;em&gt;MiniportProcessSGList&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_process_sg_list)"><em>MiniportProcessSGList</em></a></p></td>
<td align="left"><p>MINIPORT_PROCESS_SG_LIST</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_remove_device" data-raw-source="[&lt;em&gt;MiniportRemoveDevice&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_remove_device)"><em>MiniportRemoveDevice</em></a></p></td>
<td align="left"><p>MINIPORT_REMOVE_DEVICE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_reset" data-raw-source="[&lt;em&gt;MiniportResetEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_reset)"><em>MiniportResetEx</em></a></p></td>
<td align="left"><p>MINIPORT_RESET</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_restart" data-raw-source="[&lt;em&gt;MiniportRestart&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_restart)"><em>MiniportRestart</em></a></p></td>
<td align="left"><p>MINIPORT_RESTART</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_return_net_buffer_lists" data-raw-source="[&lt;em&gt;MiniportReturnNetBufferLists&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_return_net_buffer_lists)"><em>MiniportReturnNetBufferLists</em></a></p></td>
<td align="left"><p>MINIPORT_RETURN_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_send_net_buffer_lists" data-raw-source="[&lt;em&gt;MiniportSendNetBufferLists&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_send_net_buffer_lists)"><em>MiniportSendNetBufferLists</em></a></p></td>
<td align="left"><p>MINIPORT_SEND_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options" data-raw-source="[&lt;em&gt;MiniportSetOptions&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options)"><em>MiniportSetOptions</em></a></p></td>
<td align="left"><p>MINIPORT_SET_OPTIONS</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_allocate_shared_mem_complete" data-raw-source="[&lt;em&gt;MiniportSharedMemoryAllocateComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_allocate_shared_mem_complete)"><em>MiniportSharedMemoryAllocateComplete</em></a></p></td>
<td align="left"><p>MINIPORT_ALLOCATE_SHARED_MEM_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_shutdown" data-raw-source="[&lt;em&gt;MiniportShutdownEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_shutdown)"><em>MiniportShutdownEx</em></a></p></td>
<td align="left"><p>MINIPORT_SHUTDOWN</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp" data-raw-source="[&lt;em&gt;MiniportStartDevice&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp)"><em>MiniportStartDevice</em></a></p></td>
<td align="left"><p>MINIPORT_START_DEVICE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_synchronize_interrupt" data-raw-source="[&lt;em&gt;MiniportSynchronizeInterrupt&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_synchronize_interrupt)"><em>MiniportSynchronizeInterrupt</em></a></p></td>
<td align="left"><p>MINIPORT_SYNCHRONIZE_INTERRUPT</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_synchronize_interrupt" data-raw-source="[&lt;em&gt;MiniportSynchronizeMessageInterrupt&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_synchronize_interrupt)"><em>MiniportSynchronizeMessageInterrupt</em></a></p></td>
<td align="left"><p>MINIPORT_SYNCHRONIZE_MESSAGE_INTERRUPT</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">NDIS other callback function</th>
<th align="left">Role type name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>NDIS_IO_WORKITEM_ROUTINE</p>
<p><em>Routine</em></p>
<p><em>Routine</em> is the callback routine that is specified in the second parameter to the <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisqueueioworkitem" data-raw-source="[&lt;strong&gt;NdisQueueIoWorkItem&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisqueueioworkitem)"><strong>NdisQueueIoWorkItem</strong></a> function.</p></td>
<td align="left"><p>NDIS_IO_WORKITEM_FUNCTION</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_timer_function" data-raw-source="[&lt;em&gt;NetTimerCallback&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_timer_function)"><em>NetTimerCallback</em></a></p></td>
<td align="left"><p>NDIS_TIMER_FUNCTION</p></td>
</tr>
</tbody>
</table>

 

### <span id="recommended_function_declarations"></span><span id="RECOMMENDED_FUNCTION_DECLARATIONS"></span>Recommended Function Declarations

The following function role types are not currently used in SDV rules for NDIS drivers; however, they are likely to be used the future. These function role types are fully supported in Windows 7 and we recommended that you use their specific function role types to declare these callbacks.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">NDIS filter driver callback function</th>
<th align="left">Role type name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach" data-raw-source="[&lt;em&gt;FilterAttach&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach)"><em>FilterAttach</em></a></p></td>
<td align="left"><p>FILTER_ATTACH</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_cancel_direct_oid_request" data-raw-source="[&lt;em&gt;FilterCancelDirectOidRequest&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_cancel_direct_oid_request)"><em>FilterCancelDirectOidRequest</em></a></p></td>
<td align="left"><p>FILTER_CANCEL_DIRECT_OID_REQUEST</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_cancel_send_net_buffer_lists" data-raw-source="[&lt;em&gt;FilterCancelSendNetBufferLists&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_cancel_send_net_buffer_lists)"><em>FilterCancelSendNetBufferLists</em></a></p></td>
<td align="left"><p>FILTER_CANCEL_SEND_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_cancel_oid_request" data-raw-source="[&lt;em&gt;FilterCancelOidRequest&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_cancel_oid_request)"><em>FilterCancelOidRequest</em></a></p></td>
<td align="left"><p>FILTER_CANCEL_OID_REQUEST</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_detach" data-raw-source="[&lt;em&gt;FilterDetach&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_detach)"><em>FilterDetach</em></a></p></td>
<td align="left"><p>FILTER_DETACH</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_device_pnp_event_notify" data-raw-source="[&lt;em&gt;FilterDevicePnPEventNotify&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_device_pnp_event_notify)"><em>FilterDevicePnPEventNotify</em></a></p></td>
<td align="left"><p>FILTER_DEVICE_PNP_EVENT_NOTIFY</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_direct_oid_request" data-raw-source="[&lt;em&gt;FilterDirectOidRequest&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_direct_oid_request)"><em>FilterDirectOidRequest</em></a></p></td>
<td align="left"><p>FILTER_DIRECT_OID_REQUEST</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_direct_oid_request_complete" data-raw-source="[&lt;em&gt;FilterDirectOidRequestComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_direct_oid_request_complete)"><em>FilterDirectOidRequestComplete</em></a></p></td>
<td align="left"><p>FILTER_DIRECT_OID_REQUEST_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/network/unloading-a-filter-driver" data-raw-source="[&lt;em&gt;FilterDriverUnload&lt;/em&gt;](../network/unloading-a-filter-driver.md)"><em>FilterDriverUnload</em></a></p></td>
<td align="left"><p>DRIVER_UNLOAD</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_net_pnp_event" data-raw-source="[&lt;em&gt;FilterNetPnPEvent&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_net_pnp_event)"><em>FilterNetPnPEvent</em></a></p></td>
<td align="left"><p>FILTER_NET_PNP_EVENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request" data-raw-source="[&lt;em&gt;FilterOidRequest&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request)"><em>FilterOidRequest</em></a></p></td>
<td align="left"><p>FILTER_OID_REQUEST</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request_complete" data-raw-source="[&lt;em&gt;FilterOidRequestComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request_complete)"><em>FilterOidRequestComplete</em></a></p></td>
<td align="left"><p>FILTER_OID_REQUEST_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_pause" data-raw-source="[&lt;em&gt;FilterPause&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_pause)"><em>FilterPause</em></a></p></td>
<td align="left"><p>FILTER_PAUSE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_receive_net_buffer_lists" data-raw-source="[&lt;em&gt;FilterReceiveNetBufferLists&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_receive_net_buffer_lists)"><em>FilterReceiveNetBufferLists</em></a></p></td>
<td align="left"><p>FILTER_RECEIVE_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_restart" data-raw-source="[&lt;em&gt;FilterRestart&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_restart)"><em>FilterRestart</em></a></p></td>
<td align="left"><p>FILTER_RESTART</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_return_net_buffer_lists" data-raw-source="[&lt;em&gt;FilterReturnNetBufferLists&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_return_net_buffer_lists)"><em>FilterReturnNetBufferLists</em></a></p></td>
<td align="left"><p>FILTER_RETURN_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_send_net_buffer_lists" data-raw-source="[&lt;em&gt;FilterSendNetBufferLists&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_send_net_buffer_lists)"><em>FilterSendNetBufferLists</em></a></p></td>
<td align="left"><p>FILTER_SEND_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_send_net_buffer_lists_complete" data-raw-source="[&lt;em&gt;FilterSendNetBufferListsComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_send_net_buffer_lists_complete)"><em>FilterSendNetBufferListsComplete</em></a></p></td>
<td align="left"><p>FILTER_SEND_NET_BUFFER_LISTS_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_set_module_options" data-raw-source="[&lt;em&gt;FilterSetModuleOptions&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_set_module_options)"><em>FilterSetModuleOptions</em></a></p></td>
<td align="left"><p>FILTER_SET_MODULE_OPTIONS</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options" data-raw-source="[&lt;em&gt;FilterSetOptions&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options)"><em>FilterSetOptions</em></a></p></td>
<td align="left"><p>FILTER_SET_OPTIONS</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_status" data-raw-source="[&lt;em&gt;FilterStatus&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_status)"><em>FilterStatus</em></a></p></td>
<td align="left"><p>FILTER_STATUS</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">CoNDIS miniport driver callback function</th>
<th align="left">Role type name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_activate_vc" data-raw-source="[&lt;em&gt;MiniportCoActivateVc&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_activate_vc)"><em>MiniportCoActivateVc</em></a></p></td>
<td align="left"><p>MINIPORT_CO_ACTIVATE_VC</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_create_vc" data-raw-source="[&lt;em&gt;MiniportCoCreateVc&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_create_vc)"><em>MiniportCoCreateVc</em></a></p></td>
<td align="left"><p>MINIPORT_CO_CREATE_VC</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_deactivate_vc" data-raw-source="[&lt;em&gt;MiniportCoDeactivateVc&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_deactivate_vc)"><em>MiniportCoDeactivateVc</em></a></p></td>
<td align="left"><p>MINIPORT_CO_DEACTIVATE_VC</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_delete_vc" data-raw-source="[&lt;em&gt;MiniportCoDeleteVc&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_delete_vc)"><em>MiniportCoDeleteVc</em></a></p></td>
<td align="left"><p>MINIPORT_CO_DELETE_VC</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request" data-raw-source="[&lt;em&gt;MiniportCoOidRequest&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request)"><em>MiniportCoOidRequest</em></a></p></td>
<td align="left"><p>MINIPORT_CO_OID_REQUEST</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_send_net_buffer_lists" data-raw-source="[&lt;em&gt;MiniportCoSendNetBufferLists&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_send_net_buffer_lists)"><em>MiniportCoSendNetBufferLists</em></a></p></td>
<td align="left"><p>MINIPORT_CO_SEND_NET_BUFFER_LISTS</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">NDIS protocol driver callback function</th>
<th align="left">Role type name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex" data-raw-source="[&lt;em&gt;ProtocolBindAdapterEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex)"><em>ProtocolBindAdapterEx</em></a></p></td>
<td align="left"><p>PROTOCOL_BIND_ADAPTER_EX</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_close_adapter_complete_ex" data-raw-source="[&lt;em&gt;ProtocolCloseAdapterCompleteEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_close_adapter_complete_ex)"><em>ProtocolCloseAdapterCompleteEx</em></a></p></td>
<td align="left"><p>PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_direct_oid_request_complete" data-raw-source="[&lt;em&gt;ProtocolDirectOidRequestComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_direct_oid_request_complete)"><em>ProtocolDirectOidRequestComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_DIRECT_OID_REQUEST_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_net_pnp_event" data-raw-source="[&lt;em&gt;ProtocolNetPnPEvent&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_net_pnp_event)"><em>ProtocolNetPnPEvent</em></a></p></td>
<td align="left"><p>PROTOCOL_NET_PNP_EVENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_oid_request_complete" data-raw-source="[&lt;em&gt;ProtocolOidRequestComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_oid_request_complete)"><em>ProtocolOidRequestComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_OID_REQUEST_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_open_adapter_complete_ex" data-raw-source="[&lt;em&gt;ProtocolOpenAdapterCompleteEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_open_adapter_complete_ex)"><em>ProtocolOpenAdapterCompleteEx</em></a></p></td>
<td align="left"><p>PROTOCOL_OPEN_ADAPTER_COMPLETE_EX</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_receive_net_buffer_lists" data-raw-source="[&lt;em&gt;ProtocolReceiveNetBufferLists&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_receive_net_buffer_lists)"><em>ProtocolReceiveNetBufferLists</em></a></p></td>
<td align="left"><p>PROTOCOL_RECEIVE_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_send_net_buffer_lists_complete" data-raw-source="[&lt;em&gt;ProtocolSendNetBufferListsComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_send_net_buffer_lists_complete)"><em>ProtocolSendNetBufferListsComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_SEND_NET_BUFFER_LISTS_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options" data-raw-source="[&lt;em&gt;ProtocolSetOptions&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options)"><em>ProtocolSetOptions</em></a></p></td>
<td align="left"><p>PROTOCOL_SET_OPTIONS</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_status_ex" data-raw-source="[&lt;em&gt;ProtocolStatusEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_status_ex)"><em>ProtocolStatusEx</em></a></p></td>
<td align="left"><p>PROTOCOL_STATUS_EX</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_unbind_adapter_ex" data-raw-source="[&lt;em&gt;ProtocolUnbindAdapterEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_unbind_adapter_ex)"><em>ProtocolUnbindAdapterEx</em></a></p></td>
<td align="left"><p>PROTOCOL_UNBIND_ADAPTER_EX</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_uninstall" data-raw-source="[&lt;em&gt;ProtocolUninstall&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_uninstall)"><em>ProtocolUninstall</em></a></p></td>
<td align="left"><p>PROTOCOL_UNINSTALL</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">NDIS protocol CL callback function</th>
<th align="left">Role type name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_add_party_complete" data-raw-source="[&lt;em&gt;ProtocolClAddPartyComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_add_party_complete)"><em>ProtocolClAddPartyComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_ADD_PARTY_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_call_connected" data-raw-source="[&lt;em&gt;ProtocolClCallConnected&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_call_connected)"><em>ProtocolClCallConnected</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_CALL_CONNECTED</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_close_af_complete" data-raw-source="[&lt;em&gt;ProtocolClCloseAfComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_close_af_complete)"><em>ProtocolClCloseAfComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_CLOSE_AF_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_close_call_complete" data-raw-source="[&lt;em&gt;ProtocolClCloseCallComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_close_call_complete)"><em>ProtocolClCloseCallComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_CLOSE_CALL_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_deregister_sap_complete" data-raw-source="[&lt;em&gt;ProtocolClDeregisterSapComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_deregister_sap_complete)"><em>ProtocolClDeregisterSapComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_DEREGISTER_SAP_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_drop_party_complete" data-raw-source="[&lt;em&gt;ProtocolClDropPartyComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_drop_party_complete)"><em>ProtocolClDropPartyComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_DROP_PARTY_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_incoming_call" data-raw-source="[&lt;em&gt;ProtocolClIncomingCall&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_incoming_call)"><em>ProtocolClIncomingCall</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_INCOMING_CALL</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_incoming_call_qos_change" data-raw-source="[&lt;em&gt;ProtocolClIncomingCallQoSChange&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_incoming_call_qos_change)"><em>ProtocolClIncomingCallQoSChange</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_INCOMING_CALL_QOS_CHANGE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_incoming_close_call" data-raw-source="[&lt;em&gt;ProtocolClIncomingCloseCall&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_incoming_close_call)"><em>ProtocolClIncomingCloseCall</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_INCOMING_CLOSE_CALL</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_incoming_drop_party" data-raw-source="[&lt;em&gt;ProtocolClIncomingDropParty&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_incoming_drop_party)"><em>ProtocolClIncomingDropParty</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_INCOMING_DROP_PARTY</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_make_call_complete" data-raw-source="[&lt;em&gt;ProtocolClMakeCallComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_make_call_complete)"><em>ProtocolClMakeCallComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_MAKE_CALL_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_modify_call_qos_complete" data-raw-source="[&lt;em&gt;ProtocolClModifyCallQoSComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_modify_call_qos_complete)"><em>ProtocolClModifyCallQoSComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_MODIFY_CALL_QOS_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_notify_close_af" data-raw-source="[&lt;em&gt;ProtocolClNotifyCloseAf&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_notify_close_af)"><em>ProtocolClNotifyCloseAf</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_NOTIFY_CLOSE_AF</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_open_af_complete_ex" data-raw-source="[&lt;em&gt;ProtocolClOpenAfComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_open_af_complete_ex)"><em>ProtocolClOpenAfComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_OPEN_AF_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_open_af_complete_ex" data-raw-source="[&lt;em&gt;ProtocolClOpenAfCompleteEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_open_af_complete_ex)"><em>ProtocolClOpenAfCompleteEx</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_OPEN_AF_COMPLETE_EX</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_register_sap_complete" data-raw-source="[&lt;em&gt;ProtocolClRegisterSapComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_register_sap_complete)"><em>ProtocolClRegisterSapComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CL_REGISTER_SAP_COMPLETE</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">CoNDIS CM callback function</th>
<th align="left">Role type name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_activate_vc_complete" data-raw-source="[&lt;em&gt;ProtocolCmActivateVcComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_activate_vc_complete)"><em>ProtocolCmActivateVcComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CM_ACTIVATE_VC_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_add_party" data-raw-source="[&lt;em&gt;ProtocolCmAddParty&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_add_party)"><em>ProtocolCmAddParty</em></a></p></td>
<td align="left"><p>PROTOCOL_CM_ADD_PARTY</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_close_af" data-raw-source="[&lt;em&gt;ProtocolCmCloseAf&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_close_af)"><em>ProtocolCmCloseAf</em></a></p></td>
<td align="left"><p>PROTOCOL_CM_CLOSE_AF</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_close_call" data-raw-source="[&lt;em&gt;ProtocolCmCloseCall&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_close_call)"><em>ProtocolCmCloseCall</em></a></p></td>
<td align="left"><p>PROTOCOL_CM_CLOSE_CALL</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_deactivate_vc_complete" data-raw-source="[&lt;em&gt;ProtocolCmDeactivateVcComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_deactivate_vc_complete)"><em>ProtocolCmDeactivateVcComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CM_DEACTIVATE_VC_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_deregister_sap" data-raw-source="[&lt;em&gt;ProtocolCmDeregisterSap&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_deregister_sap)"><em>ProtocolCmDeregisterSap</em></a></p></td>
<td align="left"><p>PROTOCOL_CM_DEREGISTER_SAP</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_drop_party" data-raw-source="[&lt;em&gt;ProtocolCmDropParty&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_drop_party)"><em>ProtocolCmDropParty</em></a></p></td>
<td align="left"><p>PROTOCOL_CM_DROP_PARTY</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_incoming_call_complete" data-raw-source="[&lt;em&gt;ProtocolCmIncomingCallComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_incoming_call_complete)"><em>ProtocolCmIncomingCallComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CM_INCOMING_CALL_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_make_call" data-raw-source="[&lt;em&gt;ProtocolCmMakeCall&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_make_call)"><em>ProtocolCmMakeCall</em></a></p></td>
<td align="left"><p>PROTOCOL_CM_MAKE_CALL</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_modify_qos_call" data-raw-source="[&lt;em&gt;ProtocolCmModifyCallQoS&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_modify_qos_call)"><em>ProtocolCmModifyCallQoS</em></a></p></td>
<td align="left"><p>PROTOCOL_CM_MODIFY_QOS_CALL</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_notify_close_af_complete" data-raw-source="[&lt;em&gt;ProtocolCmNotifyCloseAfComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_notify_close_af_complete)"><em>ProtocolCmNotifyCloseAfComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CM_NOTIFY_CLOSE_AF_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_open_af" data-raw-source="[&lt;em&gt;ProtocolCmOpenAf&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_open_af)"><em>ProtocolCmOpenAf</em></a></p></td>
<td align="left"><p>PROTOCOL_CM_OPEN_AF</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_reg_sap" data-raw-source="[&lt;em&gt;ProtocolCmRegisterSap&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_reg_sap)"><em>ProtocolCmRegisterSap</em></a></p></td>
<td align="left"><p>PROTOCOL_CM_REG_SAP</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">CoNDIS CO callback function</th>
<th align="left">Role type name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_af_register_notify" data-raw-source="[&lt;em&gt;ProtocolCoAfRegisterNotify&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_af_register_notify)"><em>ProtocolCoAfRegisterNotify</em></a></p></td>
<td align="left"><p>PROTCOL_CO_AF_REGISTER_NOTIFY</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_create_vc" data-raw-source="[&lt;em&gt;ProtocolCoCreateVc&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_create_vc)"><em>ProtocolCoCreateVc</em></a></p></td>
<td align="left"><p>PROTOCOL_CO_CREATE_VC</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_delete_vc" data-raw-source="[&lt;em&gt;ProtocolCoDeleteVc&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_delete_vc)"><em>ProtocolCoDeleteVc</em></a></p></td>
<td align="left"><p>PROTOCOL_CO_DELETE_VC</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_oid_request_complete" data-raw-source="[&lt;em&gt;ProtocolCoOidRequest&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_oid_request_complete)"><em>ProtocolCoOidRequest</em></a></p></td>
<td align="left"><p>PROTOCOL_CO_OID_REQUEST</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_oid_request_complete" data-raw-source="[&lt;em&gt;ProtocolCoOidRequestComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_oid_request_complete)"><em>ProtocolCoOidRequestComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CO_OID_REQUEST_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_receive_net_buffer_lists" data-raw-source="[&lt;em&gt;ProtocolCoReceiveNetBufferLists&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_receive_net_buffer_lists)"><em>ProtocolCoReceiveNetBufferLists</em></a></p></td>
<td align="left"><p>PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_send_net_buffer_lists_complete" data-raw-source="[&lt;em&gt;ProtocolCoSendNetBufferListsComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_send_net_buffer_lists_complete)"><em>ProtocolCoSendNetBufferListsComplete</em></a></p></td>
<td align="left"><p>PROTOCOL_CO_SEND_NET_BUFFER_LISTS_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_status_ex" data-raw-source="[&lt;em&gt;ProtocolCoStatusEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_status_ex)"><em>ProtocolCoStatusEx</em></a></p></td>
<td align="left"><p>PROTOCOL_CO_STATUS_EX</p></td>
</tr>
</tbody>
</table>

 

