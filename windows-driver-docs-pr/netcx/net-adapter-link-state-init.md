---
title: NET\_ADAPTER\_LINK\_STATE\_INIT method
description: Initializes a NET\_ADAPTER\_LINK\_STATE structure.
ms.assetid: a49b5ab3-6bbf-491f-876d-a6ed5712895a
keywords: ["NET_ADAPTER_LINK_STATE_INIT method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_LINK_STATE_INIT
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_LINK\_STATE\_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes a [NET\_ADAPTER\_LINK\_STATE](net-adapter-link-state.md) structure.

Syntax
------

```ManagedCPlusPlus
FORCEINLINE VOID NET_ADAPTER_LINK_STATE_INIT(
  _Out_ PNET_ADAPTER_LINK_STATE            LinkState,
  _In_  ULONG64                            LinkSpeed,
  _In_  NET_IF_MEDIA_CONNECT_STATE         MediaConnectState,
  _In_  NET_IF_MEDIA_DUPLEX_STATE          MediaDuplexState,
  _In_  NET_ADAPTER_PAUSE_FUNCTIONS        SupportedPauseFunctions,
  _In_  NET_ADAPTER_AUTO_NEGOTIATION_FLAGS SupportedPauseFunctions
);
```

Parameters
----------

*LinkState* \[out\]  
A pointer to a driver-allocated [**NET\_ADAPTER\_LINK\_STATE**](net-adapter-link-state.md) structure.

*LinkSpeed* \[in\]  
The link speed of the adapter in bits per second.

*MediaConnectState* \[in\]  
The media connect state for the miniport adapter.

*MediaDuplexState* \[in\]  
The media duplex state for the miniport adapter.

*SupportedPauseFunctions* \[in\]  
Support for the IEEE 802.3 pause frames. For more info, see [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923).

*SupportedPauseFunctions* \[in\]  
The auto-negotiation settings for the miniport adapter. For more info, see [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923).

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


[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)

[**NetAdapterSetCurrentLinkState**](netadaptersetcurrentlinkstate.md)

[**NET\_ADAPTER\_LINK\_STATE\_INIT\_DISCONNECTED**](net-adapter-link-state-init-disconnected.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_ADAPTER_LINK_STATE_INIT%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





