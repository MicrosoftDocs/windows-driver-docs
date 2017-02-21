---
title: NET_PACKET_CHECKSUM structure
---

# NET_PACKET_CHECKSUM structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

TBD

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_PACKET_CHECKSUM
{
    // One of NET_PACKET_TX_CHECKSUM_ACTION or NET_PACKET_RX_CHECKSUM_EVALUATION
    UINT8 Layer2 : 2;

    // One of NET_PACKET_TX_CHECKSUM_ACTION or NET_PACKET_RX_CHECKSUM_EVALUATION
    UINT8 Layer3 : 2;

    // One of NET_PACKET_TX_CHECKSUM_ACTION or NET_PACKET_RX_CHECKSUM_EVALUATION
    UINT8 Layer4 : 2;

    UINT8 Reserved : 2;

} NET_PACKET_CHECKSUM;
```

Members
-------

**Layer2**  

**Layer3**  

**Layer4**  

**Reserved**  


Remarks
-------
A [**NET_PACKET**](net-packet.md) structure contains a member of type **NET_PACKET_CHECKSUM**.


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
<td align="left">Netpacket.h</td>
</tr>
</tbody>
</table>
