---
title: NetAdapterSetDataPathCapabilities method
topic_type:
- apiref
api_name:
- NetAdapterSetDataPathCapabilities
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NetAdapterSetDataPathCapabilities method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Sets the data path capabilities of the network adapter.

Syntax
------

```cpp
VOID NetAdapterSetDataPathCapabilities(
  _In_ NETADAPTER                         Adapter,
  _In_ PNET_ADAPTER_DATAPATH_CAPABILITIES DataPathCapabilities
);
```

Parameters
----------

*Adapter* [in]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*DataPathCapabilities* [in]  
A pointer to an allocated and initialized [**NET_ADAPTER_DATAPATH_CAPABILITIES**](net-adapter-datapath-capabilities.md) structure.

Return value
------------

This method does not return a value.

Remarks
-------

The client driver must call this method from its [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md) event callback routine.

This method along with a few other set capability methods (see below) is the replacement for the [**NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) union that a (non-WDF) client of Ndis.sys sets by calling [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672).

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
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md)

[**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md)

 

 






