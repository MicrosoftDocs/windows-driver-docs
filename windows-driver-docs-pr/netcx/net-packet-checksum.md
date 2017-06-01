---
title: NET_PACKET_CHECKSUM structure
---

# NET_PACKET_CHECKSUM structure

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

A [**NET_PACKET**](net-packet.md) structure contains a member of type **NET_PACKET_CHECKSUM**.

Syntax
------

```cpp
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
A bit field that specifies a flag from either **NET_PACKET_TX_CHECKSUM_ACTION** or **NET_PACKET_RX_CHECKSUM_EVALUATION**.  Targets the checksum field in the packet's layer 2 header.

**Layer3**  
A bit field that specifies a flag from either **NET_PACKET_TX_CHECKSUM_ACTION** or **NET_PACKET_RX_CHECKSUM_EVALUATION**.  Targets the checksum field in the packet's layer 3 header.

**Layer4**  
A bit field that specifies a flag from either **NET_PACKET_TX_CHECKSUM_ACTION** or **NET_PACKET_RX_CHECKSUM_EVALUATION**.  Targets the checksum field in the packet's layer 4 header.

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

In a transmit queue, the client cross-references the **Checksum** member with the [**Layout**](net-packet-layout.md) member of [**NET_PACKET**](net-packet.md) in order to determine which hardware transmit checksum offloads need to be enabled.  A **NET_PACKET_TX_CHECKSUM_ACTION** value of **NET_PACKET_TX_CHECKSUM_REQUIRED** means that the client should perform the checksum calculation for this layer.

In a receive queue, the client converts its hardware packet descriptors' receive checksum offload fields into **NET_PACKET_RX_CHECKSUM_EVALUATION** values for each layer.  **NET_PACKET_RX_CHECKSUM_VALID** indicates that the hardware determined that the checksum value is correct, while **NET_PACKET_RX_CHECKSUM_INVALID** means that it is incorrect. The default value is **NET_PACKET_RX_CHECKSUM_NOT_CHECKED**, which means that the checksum will be validated in software further up in the networking stack.  The client should also fill out the [**Layout**](net-packet-layout.md) member of the [**NET_PACKET**](net-packet.md) structure.

The client driver must use NDIS functionality to enable checksum offloads.  For more information, see [**NDIS_TCP_IP_CHECKSUM_OFFLOAD**](https://msdn.microsoft.com/en-us/library/windows/hardware/ff567878).

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
