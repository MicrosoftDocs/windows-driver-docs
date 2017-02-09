---
title: NetAdapterSetLinkLayerCapabilities method
description: Sets the link capabilities of the network adapter.
ms.assetid: 79254942-2e9c-4b19-8c0f-ae6498600c2e
keywords: ["NetAdapterSetLinkLayerCapabilities method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetAdapterSetLinkLayerCapabilities
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NetAdapterSetLinkLayerCapabilities method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Sets the link capabilities of the network adapter.

Syntax
------

```ManagedCPlusPlus
VOID NetAdapterSetLinkLayerCapabilities(
  _In_ NETADAPTER                           Adapter,
  _In_ PNET_ADAPTER_LINK_LAYER_CAPABILITIES LinkCapabilities
);
```

Parameters
----------

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*LinkCapabilities* \[in\]  
A pointer to an allocated and initialized [**NET\_ADAPTER\_LINK\_LAYER\_CAPABILITIES**](net-adapter-link-layer-capabilities.md) structure.

Return value
------------

This method does not return a value.

Remarks
-------

The client driver calls this method from its [*EVT\_NET\_ADAPTER\_SET\_CAPABILITIES*](evt-net-adapter-set-capabilities.md) event callback routine.

This method along with a few other set capability methods (see below) is the replacement for the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) union that a (non-WDF) client of Ndis.sys sets by calling [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672).

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


[**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md)

[**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md)

 

 






