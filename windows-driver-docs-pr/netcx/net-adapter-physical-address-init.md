---
title: NET_ADAPTER_PHYSICAL_ADDRESS_INIT method
topic_type:
- apiref
api_name:
- NET_ADAPTER_PHYSICAL_ADDRESS_INIT
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_PHYSICAL_ADDRESS_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

> [!WARNING]
> This method is no longer supported in NetAdapterCx version 1.1 and later. Link layer addresses are now initialized with the [NET_ADAPTER_LINK_LAYER_ADDRESS_INIT](net-adapter-link-layer-address-init.md) method and set with the [NetAdapterSetCurrentLinkLayerAddress](netadaptersetcurrentlinklayeraddress.md) method or the [NetAdapterSetPermanentLinkLayerAddress](netadaptersetpermanentlinklayeraddress.md), depending on the type of address.

Initializes the [**NET_ADAPTER_PHYSICAL_ADDRESS**](net-adapter-physical-address.md) structure.

Syntax
------

```cpp
VOID NET_ADAPTER_PHYSICAL_ADDRESS_INIT(
  _Out_ PNET_ADAPTER_PHYSICAL_ADDRESS PhysicalAddress,
  _In_  USHORT                        Length,
  _In_  PCUCHAR                       PermanentAddressBuffer,
  _In_  PCUCHAR                       CurrentAddressBuffer
);
```

Parameters
----------

*PhysicalAddress* [out]  
A pointer to the driver-allocated [**NET_ADAPTER_PHYSICAL_ADDRESS**](net-adapter-physical-address.md) structure.

*Length* [in]  
The number of bytes to copy from each address buffer parameter into the corresponding fields of the structure pointed to by *PhysicalAddress*.  If this value is greater than NDIS_MAX_PHYS_ADDRESS_LENGTH, that value is used instead.

*PermanentAddressBuffer* [in]  
The permanent physical address. For example, the [**OID_802_3_PERMANENT_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff569074) OID specifies the permanent physical address for IEEE 802.3 drivers.

*CurrentAddressBuffer* [in]  
The current physical address. For example, the [**OID_802_3_CURRENT_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff569069) OID specifies the current physical address for IEEE 802.3 drivers.

Return value
------------

This method does not return a value.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also

[NET_ADAPTER_LINK_LAYER_CAPABILITIES](net-adapter-link-layer-capabilities.md)

[**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md)

[NET_ADAPTER_PHYSICAL_ADDRESS](net-adapter-physical-address.md)

 





