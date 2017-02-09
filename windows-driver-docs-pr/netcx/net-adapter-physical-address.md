---
title: NET_ADAPTER_PHYSICAL_ADDRESS structure
description: Call NET\_ADAPTER\_PHYSICAL\_ADDRESS\_INIT to initialize this structure.
ms.assetid: 19d6a263-9741-47ce-beeb-20c59b9d1f54
keywords: ["NET_ADAPTER_PHYSICAL_ADDRESS structure Network Drivers Starting with Windows Vista", "PNET_ADAPTER_PHYSICAL_ADDRESS structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_PHYSICAL_ADDRESS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_PHYSICAL\_ADDRESS structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Call [NET\_ADAPTER\_PHYSICAL\_ADDRESS\_INIT](net-adapter-physical-address-init.md) to initialize this structure.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_ADAPTER_PHYSICAL_ADDRESS {
  USHORT Length;
  UCHAR  PermanentAddress[NDIS_MAX_PHYS_ADDRESS_LENGTH];
  UCHAR  CurrentAddress[NDIS_MAX_PHYS_ADDRESS_LENGTH];
} NET_ADAPTER_PHYSICAL_ADDRESS, *PNET_ADAPTER_PHYSICAL_ADDRESS;
```

Members
-------

**Length**  
The MAC address length, in bytes. The MAC address length is specific to the type of media.

**PermanentAddress**  
The permanent MAC address. For example, the [**OID_802_3_PERMANENT_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff569074) OID specifies the permanent MAC address for IEEE 802.3 drivers.

**CurrentAddress**  
The current MAC address. For example, the [**OID_802_3_CURRENT_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff569069) OID specifies the current MAC address for IEEE 802.3 drivers.

Remarks
-----
The driver supplies a member of type [NET_ADAPTER_PHYSICAL_ADDRESS](net-adapter-physical-address.md) when it allocates a [NET_ADAPTER_LINK_LAYER_CAPABILITIES](net-adapter-link-layer-capabilities.md) structure to pass as an input parameter to [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md).

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

[**NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)
