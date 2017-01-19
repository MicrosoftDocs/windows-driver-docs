---
title: NetTxQueueCreate method
description: Creates a net transmit queue object.
ms.assetid: 6b360b14-d104-4ffd-b0ef-e45cfa2b3ab2
keywords: ["NetTxQueueCreate method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetTxQueueCreate
api_location:
- nettxqueue.h
api_type:
- HeaderDef
---

# NetTxQueueCreate method


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Creates a net transmit queue object.

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetTxQueueCreate(
  _Inout_ PNETTXQUEUE_INIT       NetTxQueueInit,
  _In_    PWDF_OBJECT_ATTRIBUTES TxQueueAttributes,
  _In_    PNET_TXQUEUE_CONFIG    Configuration,
  _Out_   NETTXQUEUE             *TxQueue
);
```

Parameters
----------

*NetTxQueueInit* \[in, out\]  
A pointer to the **NETTXQUEUE\_INIT** structure that the client driver received in [*EVT\_NET\_ADAPTER\_CREATE\_TXQUEUE*](evt-net-adapter-create-txqueue.md).

*TxQueueAttributes* \[in\]  
A pointer to caller-allocated [**WDF\_OBJECT\_ATTRIBUTES**](wdf-wdf_object_attributes) structure. The structure’s **ParentObject** must be NULL. The parameter is optional and can be WDF\_NO\_OBJECT\_ATTRIBUTES.

*Configuration* \[in\]  
A pointer to a caller-allocated [**NET\_TXQUEUE\_CONFIG**](net-txqueue-config.md) structure.

*TxQueue* \[out\]  
A pointer to a location that receives a handle to the new net receive queue object.

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

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
<td align="left">[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
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
<td align="left">Nettxqueue.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetTxQueueCreate%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




