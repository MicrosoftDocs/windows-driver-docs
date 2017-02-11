---
title: NetRxQueueCreate method
topic_type:
- apiref
api_name:
- NetRxQueueCreate
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetRxQueueCreate method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Creates a net receive queue object.

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetRxQueueCreate(
  _Inout_ PNETRXQUEUE_INIT       NetRxQueueInit,
  _In_    PWDF_OBJECT_ATTRIBUTES RxQueueAttributes,
  _In_    PNET_RXQUEUE_CONFIG    Configuration,
  _Out_   NETRXQUEUE             *RxQueue
);
```

Parameters
----------

*NetRxQueueInit* \[in, out\]  
A pointer to the **NETRXQUEUE\_INIT** structure that the client driver received in [*EVT\_NET\_ADAPTER\_CREATE\_RXQUEUE*](evt-net-adapter-create-rxqueue.md).

*RxQueueAttributes* \[in\]  
A pointer to caller-allocated [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure. The structure’s **ParentObject** must be NULL. The parameter is optional and can be WDF\_NO\_OBJECT\_ATTRIBUTES.

*Configuration* \[in\]  
A pointer to a caller-allocated [**NET\_RXQUEUE\_CONFIG**](net-rxqueue-config.md) structure.

*RxQueue* \[out\]  
A pointer to a location that receives a handle to the new net receive queue object.

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------

The client typically calls **NetRxQueueCreate** from within its [*EVT\_NET\_ADAPTER\_CREATE\_RXQUEUE*](evt-net-adapter-create-rxqueue.md) event callback function. For info on assigning context space to the new object, see [Framework Object Context Space](https://msdn.microsoft.com/windows/hardware/drivers/wdf/framework-object-context-space).

The NETRXQUEUE object is a standard WDF object. The framework manages its deletion, which occurs when the parent WDFDEVICE is deleted.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Universal</td>
</tr>
<tr class="even">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">NetRxQueue.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">NetAdapterCxStub.lib</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





