---
title: NET_PACKET_LAYOUT structure
---

# NET_PACKET_LAYOUT structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

TBD

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_PACKET_LAYOUT
{
    /// One of the NET_PACKET_LAYER2_TYPE values
    UINT8 Layer2Type : 4;

    /// One of the NET_PACKET_LAYER3_TYPE values
    UINT8 Layer3Type : 4;

    /// One of the NET_PACKET_LAYER4_TYPE values
    UINT8 Layer4Type : 4;
    UINT8 Reserved   : 4;

    UINT16 Layer2HeaderLength : 7;
    UINT16 Layer3HeaderLength : 9;
    UINT8  Layer4HeaderLength : 8;

} NET_PACKET_LAYOUT;```

Members
-------

**Layer2Type**  

**Layer3Type**  

**Layer4Type**  

**Reserved**  

**Layer2HeaderLength**  

**Layer3HeaderLength**  

**Layer4HeaderLength**  

Remarks
-------
A [**NET_PACKET**](net-packet.md) structure contains a member of type **NET_PACKET_LAYOUT**.

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
