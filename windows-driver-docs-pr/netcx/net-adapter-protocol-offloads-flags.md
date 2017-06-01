---
title: NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS enumeration
topic_type:
- apiref
api_name:
- NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS enumeration

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Specifies the low power protocol offload capabilities of a network adapter.

Syntax
------

```cpp
typedef enum _NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS { 
  NET_ADAPTER_PROTOCOL_OFFLOAD_ARP              = NDIS_PM_PROTOCOL_OFFLOAD_ARP_ENABLED,
  NET_ADAPTER_PROTOCOL_OFFLOAD_NS               = NDIS_PM_PROTOCOL_OFFLOAD_NS_ENABLED,
  NET_ADAPTER_PROTOCOL_OFFLOAD_80211_RSN_REKEY  = NDIS_PM_PROTOCOL_OFFLOAD_80211_RSN_REKEY_ENABLED
} NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS;
```

Constants
---------

**NET_ADAPTER_PROTOCOL_OFFLOAD_ARP**  
If this bit is set, the overlying driver will request the network adapter to enable the ARP protocol offload capability. As soon as this protocol offload has been configured by a set request of [OID_PM_ADD_PROTOCOL_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569763), the driver should enable the network adapter to respond to IPv4 ARP packets while it is in a low-power state.

**NET_ADAPTER_PROTOCOL_OFFLOAD_NS**  
If this bit is set, the overlying driver will request the network adapter to enable the IPv6 Neighbor Solicitation (NS) protocol offload capability. As soon as this protocol offload has been configured by a set request of [OID_PM_ADD_PROTOCOL_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569763), the driver should enable the network adapter to respond to NS packets while it is in a low-power state.

**NET_ADAPTER_PROTOCOL_OFFLOAD_80211_RSN_REKEY**  
If this bit is set, the overlying driver will request the network adapter to enable the IEEE 802.11i Robust Security Network (RSN) protocol offload capability. As soon as this protocol offload has been configured by a set request of [OID_PM_ADD_PROTOCOL_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569763), the driver should enable the network adapter to respond to RSN re-key requests packets while it is in a low power state.

Remarks
---
The **NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS** enumeration is used to specify protocol offload capabilities in the [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md) structure.

The client driver passes an initialized **NET_ADAPTER_POWER_CAPABILITIES** structure as an input parameter value to [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h</td>
</tr>
</tbody>
</table>

See Also
-----
[**NDIS_PM_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759)


 





