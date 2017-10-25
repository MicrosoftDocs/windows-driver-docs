---
title: NET_ADAPTER_PHYSICAL_ADDRESS structure
topic_type:
- apiref
api_name:
- NET_ADAPTER_PHYSICAL_ADDRESS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_PHYSICAL_ADDRESS structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

> [!WARNING]
> This structure is no longer supported in NetAdapterCx version 1.1 and later. Link layer addresses are now initialized with the [NET_ADAPTER_LINK_LAYER_ADDRESS_INIT](net-adapter-link-layer-address-init.md) method and set with the [NetAdapterSetCurrentLinkLayerAddress](netadaptersetcurrentlinklayeraddress.md) method or the [NetAdapterSetPermanentLinkLayerAddress](netadaptersetpermanentlinklayeraddress.md), depending on the type of address.

Call [NET_ADAPTER_PHYSICAL_ADDRESS_INIT](net-adapter-physical-address-init.md) to initialize this structure.

Syntax
------

```cpp
typedef struct _NET_ADAPTER_PHYSICAL_ADDRESS {
  USHORT Length;
  UCHAR  PermanentAddress[NDIS_MAX_PHYS_ADDRESS_LENGTH];
  UCHAR  CurrentAddress[NDIS_MAX_PHYS_ADDRESS_LENGTH];
} NET_ADAPTER_PHYSICAL_ADDRESS, *PNET_ADAPTER_PHYSICAL_ADDRESS;
```

Members
-------

**Length**  
The physical address length, in bytes. The physical address length is specific to the type of media.

**PermanentAddress**  
The permanent physical address. For example, the [**OID_802_3_PERMANENT_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff569074) OID specifies the permanent physical address for IEEE 802.3 drivers.

**CurrentAddress**  
The current physical address. For example, the [**OID_802_3_CURRENT_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff569069) OID specifies the current physical address for IEEE 802.3 drivers.

Remarks
-----
The driver supplies a member of type [NET_ADAPTER_PHYSICAL_ADDRESS](net-adapter-physical-address.md) when it initializes a [NET_ADAPTER_LINK_LAYER_CAPABILITIES](net-adapter-link-layer-capabilities.md) structure to pass as an input parameter to [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md).

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
