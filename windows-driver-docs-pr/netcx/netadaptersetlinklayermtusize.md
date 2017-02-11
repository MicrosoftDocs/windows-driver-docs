---
title: NetAdapterSetLinkLayerMtuSize method
topic_type:
- apiref
api_name:
- NetAdapterSetLinkLayerMtuSize
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetAdapterSetLinkLayerMtuSize method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Overrides the maximum transfer unit (MTU) size that the client driver provided to [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md).

Syntax
------

```ManagedCPlusPlus
void NetAdapterSetLinkLayerMtuSize(
  _In_ NETADAPTER Adapter,
  _In_ ULONG      MtuSize
);
```

Parameters
----------

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*MtuSize* \[in\]  
The new size of the adapter's MTU, in bytes.

Return value
------------

This method does not return a value.

Remarks
-------

The client driver first sets MTU size by calling [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md) from its [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md) implementation.

The client driver can change MTU size after returning from [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md) by calling **NetAdapterSetLinkLayerMtuSize**. Doing so causes all of the adapter's Tx and Rx queues to be recreated.

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
<td align="left">Netadapter.h (include Netadaptercx.h)</td>
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

## See also


[**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md)

 

 






