---
title: NET_PACKET_CHECKSUM structure
---

# NET_PACKET_CHECKSUM structure

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

A [**NET_PACKET**](net-packet.md) structure contains a member of type **NET_PACKET_CHECKSUM**.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_PACKET_CHECKSUM
{
    UINT8 Layer2 : 2;
    UINT8 Layer3 : 2;
    UINT8 Layer4 : 2;
    UINT8 Reserved : 2;
} NET_PACKET_CHECKSUM;
```

Members
-------

**Layer2**  
A bit field that specifies a flag from either **NET_PACKET_TX_CHECKSUM_ACTION** or **NET_PACKET_RX_CHECKSUM_EVALUATION**.

**Layer3**  
A bit field that specifies a flag from either **NET_PACKET_TX_CHECKSUM_ACTION** or **NET_PACKET_RX_CHECKSUM_EVALUATION**.

**Layer4**  
A bit field that specifies a flag from either **NET_PACKET_TX_CHECKSUM_ACTION** or **NET_PACKET_RX_CHECKSUM_EVALUATION**.

**Reserved**  
Reserved for system use.

Remarks
-----
See more info in the description of the **Checksum** member of [**NET_PACKET**](net-packet.md).

For a transmit queue, the client specifies flag values from the **NET_PACKET_TX_CHECKSUM_ACTION** enumeration:

```
typedef enum _NET_PACKET_TX_CHECKSUM_ACTION
{
    NET_PACKET_TX_CHECKSUM_PASSTHROUGH                  = 0,
    NET_PACKET_TX_CHECKSUM_REQUIRED                     = 2,
} NET_PACKET_TX_CHECKSUM_ACTION;
```

For a receive queue, the client specifies flag values from the **NET_PACKET_RX_CHECKSUM_EVALUATION** enumeration.

```
typedef enum _NET_PACKET_RX_CHECKSUM_EVALUATION
{
    NET_PACKET_RX_CHECKSUM_NOT_CHECKED                  = 0,
    NET_PACKET_RX_CHECKSUM_VALID                        = 1,
    NET_PACKET_RX_CHECKSUM_INVALID                      = 2,
} NET_PACKET_RX_CHECKSUM_EVALUATION;
```

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
