---
title: NET_ADAPTER_WAKE_PATTERN_FLAGS enumeration
topic_type:
- apiref
api_name:
- NET_ADAPTER_WAKE_PATTERN_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_WAKE_PATTERN_FLAGS enumeration

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Specifies wake patterns that an adapter supports.

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_WAKE_PATTERN_FLAGS { 
  NET_ADAPTER_WAKE_BITMAP_PATTERN            = NDIS_PM_WOL_BITMAP_PATTERN_ENABLED,
  NET_ADAPTER_WAKE_MAGIC_PACKET              = NDIS_PM_WOL_MAGIC_PACKET_ENABLED,
  NET_ADAPTER_WAKE_IPV4_TCP_SYN              = NDIS_PM_WOL_IPV4_TCP_SYN_ENABLED,
  NET_ADAPTER_WAKE_IPV6_TCP_SYN              = NDIS_PM_WOL_IPV6_TCP_SYN_ENABLED,
  NET_ADAPTER_WAKE_IPV4_DEST_ADDR_WILDCARD   = NDIS_PM_WOL_IPV4_DEST_ADDR_WILDCARD_ENABLED,
  NET_ADAPTER_WAKE_IPV6_DEST_ADDR_WILDCARD   = NDIS_PM_WOL_IPV6_DEST_ADDR_WILDCARD_ENABLED,
  NET_ADAPTER_WAKE_EAPOL_REQUEST_ID_MESSAGE  = NDIS_PM_WOL_EAPOL_REQUEST_ID_MESSAGE_ENABLED
} NET_ADAPTER_WAKE_PATTERN_FLAGS;
```

Constants
---------

**NET_ADAPTER_WAKE_BITMAP_PATTERN**  
If this flag is set, the network adapter is enabled to generate a wake-up event when it receives a packet that matches a configured bitmap pattern.

**NET_ADAPTER_WAKE_MAGIC_PACKET**  
If this flag is set, the network adapter is enabled to generate a wake-up event when it receives a WOL magic packet. A *magic packet* contains within its payload a string of six bytes with a value of 0xFF, followed immediately by 16 contiguous copies of the receiving network adapter's media access control (MAC) address.

**NET_ADAPTER_WAKE_IPV4_TCP_SYN**  
If this flag is set, the network adapter is enabled to generate a wake-up event when it receives an IPv4 TCP SYN packet. Remote hosts send TCP SYN packets to initiate a TCP connection to the local computer.

**NET_ADAPTER_WAKE_IPV6_TCP_SYN**  
If this flag is set, the network adapter is enabled to generate a wake-up event when it receives an IPv6 TCP SYN packet.

**NET_ADAPTER_WAKE_IPV4_DEST_ADDR_WILDCARD**  
If this flag is set, the network adapter must treat as wildcard values any zero-filled, or unspecified, values for IPv4 addresses and TCP/UDP ports in a WOL pattern. In this way, the wildcard value matches any IPv4 address and any port value of the incoming packet in the location specified by the WOL pattern.

If this flag is set, the network adapter is enabled to generate a wake-up event if the following pattern-matching conditions are true:

* Any value from the incoming packet in the location specified by the WOL pattern is a match, if the WOL pattern for that location contains a wildcard value.
* A value from the incoming packet in the location specified by the WOL pattern is a match if the WOL pattern for that location contains a nonzero value that equals the packet's value.

> [!NOTE]
> Wildcard values that are enabled by this flag can include unspecified IPv4 source and destination addresses, as well as unspecified source and destination ports.

**NET_ADAPTER_WAKE_IPV6_DEST_ADDR_WILDCARD**  
If this flag is set, the network adapter must treat as wildcard values any zero-filled, or unspecified, values for IPv6 addresses and TCP/UDP ports in a WOL pattern. In this way, the wildcard value matches any IPv6 address and any port value of the incoming packet in the location specified by the WOL pattern.

If this flag is set, the network adapter is enabled to generate a wake-up event if the following pattern-matching conditions are true:

* Any value from the incoming packet in the location specified by the WOL pattern is a match, if the WOL pattern for that location contains a wildcard value.
* A value from the incoming packet in the location specified by the WOL pattern is a match if the WOL pattern for that location contains a nonzero value that equals the packet's value.

> [!NOTE]
> Wildcard values that are enabled by this flag can include unspecified IPv6 source and destination addresses, as well as unspecified source and destination ports.

**NET_ADAPTER_WAKE_EAPOL_REQUEST_ID_MESSAGE**  
If this flag is set, the network adapter is enabled to generate a wake-up event when it receives an EAPOL request identifier message.

Remarks
-----
The **NET_ADAPTER_WAKE_PATTERN_FLAGS** enumeration is used to specify supported statistics in the [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md) structure.

The client driver passes an initialized [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md) structure as an input parameter value to [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md).

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



