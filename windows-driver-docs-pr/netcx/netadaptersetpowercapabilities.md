---
title: NetAdapterSetPowerCapabilities method
topic_type:
- apiref
api_name:
- NetAdapterSetPowerCapabilities
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NetAdapterSetPowerCapabilities method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Sets the power capabilities of the network adapter.

Syntax
------

```cpp
void NetAdapterSetPowerCapabilities(
  _In_ NETADAPTER                      Adapter,
  _In_ PNET_ADAPTER_POWER_CAPABILITIES PowerCapabilities
);
```

Parameters
----------

*Adapter* [in]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*PowerCapabilities* [in]  
A pointer to an allocated and initialized [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md) structure.

Return value
------------

This method does not return a value.

Remarks
-------

The client driver sets capabilities by calling the following methods from its [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md) event callback routine.

-   [**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md)
-   [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md)
-   **NetAdapterSetPowerCapabilities**

Alternatively, the client can call **NetAdapterSetPowerCapabilities** from a callback that NetAdapterCx calls after [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md). If it does, it must not change the [*EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN*](evt-net-adapter-preview-wake-pattern.md) event callback function.

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


[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)

[**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672)

[**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md)

[**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md)
 

 






