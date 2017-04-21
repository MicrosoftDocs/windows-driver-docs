---
title: NET_PACKET_LAYOUT structure
---

# NET_PACKET_LAYOUT structure

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

A **NET_PACKET_LAYOUT** structure describes the start of each protocol header in a packet.

Syntax
------

```cpp
typedef struct _NET_PACKET_LAYOUT
{
    UINT8 Layer2Type : 4;
    UINT8 Layer3Type : 4;
    UINT8 Layer4Type : 4;
    UINT8 Reserved   : 4;
    UINT16 Layer2HeaderLength : 7;
    UINT16 Layer3HeaderLength : 9;
    UINT8  Layer4HeaderLength : 8;

} NET_PACKET_LAYOUT;
```

Members
-------

**Layer2Type**  
An enum that specifies a flag from **NET_PACKET_LAYER2_TYPE**.

```cpp
typedef enum _NET_PACKET_LAYER2_TYPE
{
    NET_PACKET_LAYER2_TYPE_UNSPECIFIED                  = 0,
    NET_PACKET_LAYER2_TYPE_NULL                         = 1,
    NET_PACKET_LAYER2_TYPE_ETHERNET                     = 2,
} NET_PACKET_LAYER2_TYPE;
```

**Layer3Type**  
An enum that specifies a flag from **NET_PACKET_LAYER3_TYPE**.

```cpp
typedef enum _NET_PACKET_LAYER3_TYPE
{
    NET_PACKET_LAYER3_TYPE_UNSPECIFIED                  = 0,
    NET_PACKET_LAYER3_TYPE_IPV4_UNSPECIFIED_OPTIONS     = 1,
    NET_PACKET_LAYER3_TYPE_IPV4_WITH_OPTIONS            = 2,
    NET_PACKET_LAYER3_TYPE_IPV4_NO_OPTIONS              = 3,
    NET_PACKET_LAYER3_TYPE_IPV6_UNSPECIFIED_EXTENSIONS  = 4,
    NET_PACKET_LAYER3_TYPE_IPV6_WITH_EXTENSIONS         = 5,
    NET_PACKET_LAYER3_TYPE_IPV6_NO_EXTENSIONS           = 6,
} NET_PACKET_LAYER3_TYPE;
```

**Layer4Type**  
An enum that specifies a flag from **NET_PACKET_LAYER4_TYPE**.

```cpp
typedef enum _NET_PACKET_LAYER4_TYPE
{
    NET_PACKET_LAYER4_TYPE_UNSPECIFIED                  = 0,
    NET_PACKET_LAYER4_TYPE_TCP                          = 1,
    NET_PACKET_LAYER4_TYPE_UDP                          = 2,
    NET_PACKET_LAYER4_TYPE_IP_NOT_FRAGMENTED            = 3,
    NET_PACKET_LAYER4_TYPE_IP_FRAGMENT                  = 4,
} NET_PACKET_LAYER4_TYPE;
```

**Reserved**  
Reserved for system use.

**Layer2HeaderLength**  
The length in bytes of the Layer 2 header, or zero if the Layer 2 length is unknown.

**Layer3HeaderLength**  
The length in bytes of the Layer 3 header, or zero if the Layer 3 length is unknown.

**Layer4HeaderLength**  
The length of the Layer 4 header, or zero if the Layer 4 length is unknown.

Remarks
-------
See more info in the description of the **Layout** member of [**NET_PACKET**](net-packet.md).

The client specifies flag values for this structure using the following enumerations:



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
