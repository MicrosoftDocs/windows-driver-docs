---
title: Static Driver Verifier NDIS Function Declarations
description: Static Driver Verifier NDIS Function Declarations
ms.assetid: f8d11a99-0fd0-45cf-b583-8f8833b21f79
keywords: ["SDV WDK , NDIS", "NDIS rules for SDV", "SDV WDK , NDIS rules"]
---

# Static Driver Verifier NDIS Function Declarations


To enable SDV to verify your NDIS driver, you must declare each callback function, by using a callback function role type. The callback function role types are defined in the Ndis.h header file and are included when you build your driver with that header file.

You must declare the driver's callback functions before you declare the callback function definitions. The following code example shows the function role type declaration for the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) callback function. This callback function must be declared by using the MINIPORT\_INITIALIZE role type. In this example, the callback function is called *myMiniportInitializeEx*.

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
<td align="left"><p>[<em>MiniportAddDevice</em>](https://msdn.microsoft.com/library/windows/hardware/ff559332)</p></td>
<td align="left"><p>MINIPORT_ADD_DEVICE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportCancelDirectOidRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff559335)</p></td>
<td align="left"><p>MINIPORT_CANCEL_DIRECT_OID_REQUEST</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportCancelOidRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff559339)</p></td>
<td align="left"><p>MINIPORT_CANCEL_OID_REQUEST</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportCancelSend</em>](https://msdn.microsoft.com/library/windows/hardware/ff559342)</p></td>
<td align="left"><p>MINIPORT_CANCEL_SEND</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportCheckForHangEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559346)</p></td>
<td align="left"><p>MINIPORT_CHECK_FOR_HANG</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportDevicePnPEventNotify</em>](https://msdn.microsoft.com/library/windows/hardware/ff559369)</p></td>
<td align="left"><p>MINIPORT_DEVICE_PNP_EVENT_NOTIFY</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportDirectOidRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff559371)</p></td>
<td align="left"><p>MINIPORT_DIRECT_OID_REQUEST</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportDisableInterruptEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559375)</p></td>
<td align="left"><p>MINIPORT_DISABLE_INTERRUPT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportDisableMessageInterrupt</em>](https://msdn.microsoft.com/library/windows/hardware/ff559376)</p></td>
<td align="left"><p>MINIPORT_DISABLE_MESSAGE_INTERRUPT</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportDriverUnload</em>](https://msdn.microsoft.com/library/windows/hardware/ff559378)</p></td>
<td align="left"><p>MINIPORT_UNLOAD</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportEnableInterruptEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559380)</p></td>
<td align="left"><p>MINIPORT_ENABLE_INTERRUPT</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportEnableMessageInterrupt</em>](https://msdn.microsoft.com/library/windows/hardware/ff559383)</p></td>
<td align="left"><p>MINIPORT_ENABLE_MESSAGE_INTERRUPT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportFilterResourceRequirements</em>](https://msdn.microsoft.com/library/windows/hardware/ff559384)</p></td>
<td align="left"><p>MINIPORT_FILTER_RESOURCE_REQUIREMENTS</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportHaltEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559388)</p></td>
<td align="left"><p>MINIPORT_HALT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportInitializeEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559389)</p></td>
<td align="left"><p>MINIPORT_INITIALIZE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportInterrupt</em>](https://msdn.microsoft.com/library/windows/hardware/ff559395)</p></td>
<td align="left"><p>MINIPORT_ISR</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportInterruptDPC</em>](https://msdn.microsoft.com/library/windows/hardware/ff559398)</p></td>
<td align="left"><p>MINIPORT_INTERRUPT_DPC</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportMessageInterrupt</em>](https://msdn.microsoft.com/library/windows/hardware/ff559407)</p></td>
<td align="left"><p>MINIPORT_MESSAGE_INTERRUPT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportMessageInterruptDPC</em>](https://msdn.microsoft.com/library/windows/hardware/ff559411)</p></td>
<td align="left"><p>MINIPORT_MESSAGE_INTERRUPT_DPC</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportOidRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff559416)</p></td>
<td align="left"><p>MINIPORT_OID_REQUEST</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportPause</em>](https://msdn.microsoft.com/library/windows/hardware/ff559418)</p></td>
<td align="left"><p>MINIPORT_PAUSE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportProcessSGList</em>](https://msdn.microsoft.com/library/windows/hardware/ff559420)</p></td>
<td align="left"><p>MINIPORT_PROCESS_SG_LIST</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportRemoveDevice</em>](https://msdn.microsoft.com/library/windows/hardware/ff559427)</p></td>
<td align="left"><p>MINIPORT_REMOVE_DEVICE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportResetEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559432)</p></td>
<td align="left"><p>MINIPORT_RESET</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportRestart</em>](https://msdn.microsoft.com/library/windows/hardware/ff559435)</p></td>
<td align="left"><p>MINIPORT_RESTART</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportReturnNetBufferLists</em>](https://msdn.microsoft.com/library/windows/hardware/ff559437)</p></td>
<td align="left"><p>MINIPORT_RETURN_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportSendNetBufferLists</em>](https://msdn.microsoft.com/library/windows/hardware/ff559440)</p></td>
<td align="left"><p>MINIPORT_SEND_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportSetOptions</em>](https://msdn.microsoft.com/library/windows/hardware/ff559443)</p></td>
<td align="left"><p>MINIPORT_SET_OPTIONS</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportSharedMemoryAllocateComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff559446)</p></td>
<td align="left"><p>MINIPORT_ALLOCATE_SHARED_MEM_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportShutdownEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559449)</p></td>
<td align="left"><p>MINIPORT_SHUTDOWN</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportStartDevice</em>](https://msdn.microsoft.com/library/windows/hardware/ff559452)</p></td>
<td align="left"><p>MINIPORT_START_DEVICE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportSynchronizeInterrupt</em>](https://msdn.microsoft.com/library/windows/hardware/ff559454)</p></td>
<td align="left"><p>MINIPORT_SYNCHRONIZE_INTERRUPT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportSynchronizeMessageInterrupt</em>](https://msdn.microsoft.com/library/windows/hardware/ff559455)</p></td>
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
<p><em>Routine</em> is the callback routine that is specified in the second parameter to the [<strong>NdisQueueIoWorkItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563775) function.</p></td>
<td align="left"><p>NDIS_IO_WORKITEM_FUNCTION</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>NetTimerCallback</em>](https://msdn.microsoft.com/library/windows/hardware/ff568351)</p></td>
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
<td align="left"><p>[<em>FilterAttach</em>](https://msdn.microsoft.com/library/windows/hardware/ff549905)</p></td>
<td align="left"><p>FILTER_ATTACH</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>FilterCancelDirectOidRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff549908)</p></td>
<td align="left"><p>FILTER_CANCEL_DIRECT_OID_REQUEST</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>FilterCancelSendNetBufferLists</em>](https://msdn.microsoft.com/library/windows/hardware/ff549915)</p></td>
<td align="left"><p>FILTER_CANCEL_SEND_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>FilterCancelOidRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff549911)</p></td>
<td align="left"><p>FILTER_CANCEL_OID_REQUEST</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>FilterDetach</em>](https://msdn.microsoft.com/library/windows/hardware/ff549918)</p></td>
<td align="left"><p>FILTER_DETACH</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>FilterDevicePnPEventNotify</em>](https://msdn.microsoft.com/library/windows/hardware/ff549926)</p></td>
<td align="left"><p>FILTER_DEVICE_PNP_EVENT_NOTIFY</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>FilterDirectOidRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff549931)</p></td>
<td align="left"><p>FILTER_DIRECT_OID_REQUEST</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>FilterDirectOidRequestComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff549933)</p></td>
<td align="left"><p>FILTER_DIRECT_OID_REQUEST_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>FilterDriverUnload</em>](https://msdn.microsoft.com/library/windows/hardware/ff549936)</p></td>
<td align="left"><p>DRIVER_UNLOAD</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>FilterNetPnPEvent</em>](https://msdn.microsoft.com/library/windows/hardware/ff549952)</p></td>
<td align="left"><p>FILTER_NET_PNP_EVENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>FilterOidRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff549954)</p></td>
<td align="left"><p>FILTER_OID_REQUEST</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>FilterOidRequestComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff549956)</p></td>
<td align="left"><p>FILTER_OID_REQUEST_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>FilterPause</em>](https://msdn.microsoft.com/library/windows/hardware/ff549957)</p></td>
<td align="left"><p>FILTER_PAUSE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>FilterReceiveNetBufferLists</em>](https://msdn.microsoft.com/library/windows/hardware/ff549960)</p></td>
<td align="left"><p>FILTER_RECEIVE_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>FilterRestart</em>](https://msdn.microsoft.com/library/windows/hardware/ff549962)</p></td>
<td align="left"><p>FILTER_RESTART</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>FilterReturnNetBufferLists</em>](https://msdn.microsoft.com/library/windows/hardware/ff549964)</p></td>
<td align="left"><p>FILTER_RETURN_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>FilterSendNetBufferLists</em>](https://msdn.microsoft.com/library/windows/hardware/ff549966)</p></td>
<td align="left"><p>FILTER_SEND_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>FilterSendNetBufferListsComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff549967)</p></td>
<td align="left"><p>FILTER_SEND_NET_BUFFER_LISTS_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>FilterSetModuleOptions</em>](https://msdn.microsoft.com/library/windows/hardware/ff549970)</p></td>
<td align="left"><p>FILTER_SET_MODULE_OPTIONS</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>FilterSetOptions</em>](https://msdn.microsoft.com/library/windows/hardware/ff549972)</p></td>
<td align="left"><p>FILTER_SET_OPTIONS</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>FilterStatus</em>](https://msdn.microsoft.com/library/windows/hardware/ff549973)</p></td>
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
<td align="left"><p>[<em>MiniportCoActivateVc</em>](https://msdn.microsoft.com/library/windows/hardware/ff559351)</p></td>
<td align="left"><p>MINIPORT_CO_ACTIVATE_VC</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportCoCreateVc</em>](https://msdn.microsoft.com/library/windows/hardware/ff559354)</p></td>
<td align="left"><p>MINIPORT_CO_CREATE_VC</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportCoDeactivateVc</em>](https://msdn.microsoft.com/library/windows/hardware/ff559356)</p></td>
<td align="left"><p>MINIPORT_CO_DEACTIVATE_VC</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportCoDeleteVc</em>](https://msdn.microsoft.com/library/windows/hardware/ff559358)</p></td>
<td align="left"><p>MINIPORT_CO_DELETE_VC</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>MiniportCoOidRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff559362)</p></td>
<td align="left"><p>MINIPORT_CO_OID_REQUEST</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MiniportCoSendNetBufferLists</em>](https://msdn.microsoft.com/library/windows/hardware/ff559365)</p></td>
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
<td align="left"><p>[<em>ProtocolBindAdapterEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff570220)</p></td>
<td align="left"><p>PROTOCOL_BIND_ADAPTER_EX</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolCloseAdapterCompleteEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff570236)</p></td>
<td align="left"><p>PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolDirectOidRequestComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570259)</p></td>
<td align="left"><p>PROTOCOL_DIRECT_OID_REQUEST_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolNetPnPEvent</em>](https://msdn.microsoft.com/library/windows/hardware/ff570263)</p></td>
<td align="left"><p>PROTOCOL_NET_PNP_EVENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolOidRequestComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570264)</p></td>
<td align="left"><p>PROTOCOL_OID_REQUEST_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolOpenAdapterCompleteEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff570265)</p></td>
<td align="left"><p>PROTOCOL_OPEN_ADAPTER_COMPLETE_EX</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolReceiveNetBufferLists</em>](https://msdn.microsoft.com/library/windows/hardware/ff570267)</p></td>
<td align="left"><p>PROTOCOL_RECEIVE_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolSendNetBufferListsComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570268)</p></td>
<td align="left"><p>PROTOCOL_SEND_NET_BUFFER_LISTS_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolSetOptions</em>](https://msdn.microsoft.com/library/windows/hardware/ff570269)</p></td>
<td align="left"><p>PROTOCOL_SET_OPTIONS</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolStatusEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff570270)</p></td>
<td align="left"><p>PROTOCOL_STATUS_EX</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolUnbindAdapterEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff570278)</p></td>
<td align="left"><p>PROTOCOL_UNBIND_ADAPTER_EX</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolUninstall</em>](https://msdn.microsoft.com/library/windows/hardware/ff570279)</p></td>
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
<td align="left"><p>[<em>ProtocolClAddPartyComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570221)</p></td>
<td align="left"><p>PROTOCOL_CL_ADD_PARTY_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolClCallConnected</em>](https://msdn.microsoft.com/library/windows/hardware/ff570223)</p></td>
<td align="left"><p>PROTOCOL_CL_CALL_CONNECTED</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolClCloseAfComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570224)</p></td>
<td align="left"><p>PROTOCOL_CL_CLOSE_AF_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolClCloseCallComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570225)</p></td>
<td align="left"><p>PROTOCOL_CL_CLOSE_CALL_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolClDeregisterSapComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570226)</p></td>
<td align="left"><p>PROTOCOL_CL_DEREGISTER_SAP_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolClDropPartyComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570227)</p></td>
<td align="left"><p>PROTOCOL_CL_DROP_PARTY_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolClIncomingCall</em>](https://msdn.microsoft.com/library/windows/hardware/ff570228)</p></td>
<td align="left"><p>PROTOCOL_CL_INCOMING_CALL</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolClIncomingCallQoSChange</em>](https://msdn.microsoft.com/library/windows/hardware/ff570229)</p></td>
<td align="left"><p>PROTOCOL_CL_INCOMING_CALL_QOS_CHANGE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolClIncomingCloseCall</em>](https://msdn.microsoft.com/library/windows/hardware/ff570230)</p></td>
<td align="left"><p>PROTOCOL_CL_INCOMING_CLOSE_CALL</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolClIncomingDropParty</em>](https://msdn.microsoft.com/library/windows/hardware/ff570231)</p></td>
<td align="left"><p>PROTOCOL_CL_INCOMING_DROP_PARTY</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolClMakeCallComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570232)</p></td>
<td align="left"><p>PROTOCOL_CL_MAKE_CALL_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolClModifyCallQoSComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570233)</p></td>
<td align="left"><p>PROTOCOL_CL_MODIFY_CALL_QOS_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolClNotifyCloseAf</em>](https://msdn.microsoft.com/library/windows/hardware/ff570234)</p></td>
<td align="left"><p>PROTOCOL_CL_NOTIFY_CLOSE_AF</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolClOpenAfComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570235)</p></td>
<td align="left"><p>PROTOCOL_CL_OPEN_AF_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolClOpenAfCompleteEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff570235)</p></td>
<td align="left"><p>PROTOCOL_CL_OPEN_AF_COMPLETE_EX</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolClRegisterSapComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570237)</p></td>
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
<td align="left"><p>[<em>ProtocolCmActivateVcComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570238)</p></td>
<td align="left"><p>PROTOCOL_CM_ACTIVATE_VC_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolCmAddParty</em>](https://msdn.microsoft.com/library/windows/hardware/ff570239)</p></td>
<td align="left"><p>PROTOCOL_CM_ADD_PARTY</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolCmCloseAf</em>](https://msdn.microsoft.com/library/windows/hardware/ff570240)</p></td>
<td align="left"><p>PROTOCOL_CM_CLOSE_AF</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolCmCloseCall</em>](https://msdn.microsoft.com/library/windows/hardware/ff570241)</p></td>
<td align="left"><p>PROTOCOL_CM_CLOSE_CALL</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolCmDeactivateVcComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570242)</p></td>
<td align="left"><p>PROTOCOL_CM_DEACTIVATE_VC_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolCmDeregisterSap</em>](https://msdn.microsoft.com/library/windows/hardware/ff570243)</p></td>
<td align="left"><p>PROTOCOL_CM_DEREGISTER_SAP</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolCmDropParty</em>](https://msdn.microsoft.com/library/windows/hardware/ff570244)</p></td>
<td align="left"><p>PROTOCOL_CM_DROP_PARTY</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolCmIncomingCallComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570245)</p></td>
<td align="left"><p>PROTOCOL_CM_INCOMING_CALL_COMPLETE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolCmMakeCall</em>](https://msdn.microsoft.com/library/windows/hardware/ff570246)</p></td>
<td align="left"><p>PROTOCOL_CM_MAKE_CALL</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolCmModifyCallQoS</em>](https://msdn.microsoft.com/library/windows/hardware/ff570247)</p></td>
<td align="left"><p>PROTOCOL_CM_MODIFY_QOS_CALL</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolCmNotifyCloseAfComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570248)</p></td>
<td align="left"><p>PROTOCOL_CM_NOTIFY_CLOSE_AF_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolCmOpenAf</em>](https://msdn.microsoft.com/library/windows/hardware/ff570249)</p></td>
<td align="left"><p>PROTOCOL_CM_OPEN_AF</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolCmRegisterSap</em>](https://msdn.microsoft.com/library/windows/hardware/ff570250)</p></td>
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
<td align="left"><p>[<em>ProtocolCoAfRegisterNotify</em>](https://msdn.microsoft.com/library/windows/hardware/ff570251)</p></td>
<td align="left"><p>PROTCOL_CO_AF_REGISTER_NOTIFY</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolCoCreateVc</em>](https://msdn.microsoft.com/library/windows/hardware/ff570252)</p></td>
<td align="left"><p>PROTOCOL_CO_CREATE_VC</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolCoDeleteVc</em>](https://msdn.microsoft.com/library/windows/hardware/ff570253)</p></td>
<td align="left"><p>PROTOCOL_CO_DELETE_VC</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolCoOidRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff570255)</p></td>
<td align="left"><p>PROTOCOL_CO_OID_REQUEST</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolCoOidRequestComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570255)</p></td>
<td align="left"><p>PROTOCOL_CO_OID_REQUEST_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolCoReceiveNetBufferLists</em>](https://msdn.microsoft.com/library/windows/hardware/ff570256)</p></td>
<td align="left"><p>PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>ProtocolCoSendNetBufferListsComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff570257)</p></td>
<td align="left"><p>PROTOCOL_CO_SEND_NET_BUFFER_LISTS_COMPLETE</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>ProtocolCoStatusEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff570258)</p></td>
<td align="left"><p>PROTOCOL_CO_STATUS_EX</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Static%20Driver%20Verifier%20NDIS%20Function%20Declarations%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




