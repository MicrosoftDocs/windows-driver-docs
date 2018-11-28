---
title: WDI_TLV_SET_CIPHER_KEY_INFO
description: WDI_TLV_SET_CIPHER_KEY_INFO is a TLV that contains cipher key mapping key information for OID_WDI_SET_ADD_CIPHER_KEYS.
ms.assetid: 6352284A-73CD-4B15-A057-80D0C8518CD5
ms.date: 07/18/2017
keywords:
 - WDI_TLV_SET_CIPHER_KEY_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_SET\_CIPHER\_KEY\_INFO


WDI\_TLV\_SET\_CIPHER\_KEY\_INFO is a TLV that contains cipher key mapping key information for [OID\_WDI\_SET\_ADD\_CIPHER\_KEYS](https://msdn.microsoft.com/library/windows/hardware/dn925855).

## TLV Type


0x52

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                 | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_PEER\_MAC\_ADDRESS**](wdi-tlv-peer-mac-address.md)                                     |                                | X        | Specifies the MAC address of the peer that this key is associated with. If not present, assume this is a default key. At least one of peer MAC Address or cipher key ID must be present. This field must be present when key type is set to WDI\_CIPHER\_KEY\_TYPE\_PAIRWISE\_KEY, and may be present when key type is set to WDI\_CIPHER\_KEY\_TYPE\_GROUP\_KEY. |
| [**WDI\_TLV\_CIPHER\_KEY\_ID**](wdi-tlv-cipher-key-id.md)                                           |                                | X        | Specifies the ID for this cipher key. At least one of peer MAC address or cipher key ID must be present. This field is not required for pairwise keys.                                                                                                                                                                                                            |
| [**WDI\_TLV\_CIPHER\_KEY\_TYPE\_INFO**](wdi-tlv-cipher-key-type-info.md)                            |                                |          | Specifies the cipher key type information.                                                                                                                                                                                                                                                                                                                        |
| [**WDI\_TLV\_CIPHER\_KEY\_RECEIVE\_SEQUENCE\_COUNT**](wdi-tlv-cipher-key-receive-sequence-count.md) |                                | X        | Specifies the initial 48-bit value of Packet Number (PN), which is used for replay protection. This is optional if the cipher algorithm is WDI\_CIPHER\_ALGO\_WEP40, WDI\_CIPHER\_ALGO\_WEP104, or WDI\_CIPHER\_ALGO\_WEP.                                                                                                                                        |
| [**WDI\_TLV\_CIPHER\_KEY\_CCMP\_KEY**](wdi-tlv-cipher-key-ccmp-key.md)                              |                                | X        | Specifies the CCMP cipher algorithm key data. This is only present if the cipher algorithm is WDI\_CIPHER\_ALGO\_CCMP.                                                                                                                                                                                                                                            |
| [**WDI\_TLV\_CIPHER\_KEY\_TKIP\_INFO**](wdi-tlv-cipher-key-tkip-info.md)                            |                                | X        | Specifies the TKIP information. This is only present if the cipher algorithm is WDI\_CIPHER\_ALGO\_TKIP.                                                                                                                                                                                                                                                          |
| [**WDI\_TLV\_CIPHER\_KEY\_BIP\_KEY**](wdi-tlv-cipher-key-bip-key.md)                                |                                | X        | Specifies the BIP key. This is only present if the cipher algorithm is WDI\_CIPHER\_ALGO\_BIP.                                                                                                                                                                                                                                                                    |
| [**WDI\_TLV\_CIPHER\_KEY\_WEP\_KEY**](wdi-tlv-cipher-key-wep-key.md)                                |                                | X        | Specifies the WEP key. This is only present if the cipher algorithm is WDI\_CIPHER\_ALGO\_WEP40, WDI\_CIPHER\_ALGO\_WEP104, or WDI\_CIPHER\_ALGO\_WEP.                                                                                                                                                                                                            |
| [**WDI\_TLV\_CIPHER\_KEY\_IHV\_KEY**](wdi-tlv-cipher-key-ihv-key.md)                                |                                | X        | Specifies the IHV cipher key. This is only present if [**WDI\_TLV\_CIPHER\_KEY\_TYPE\_INFO**](wdi-tlv-cipher-key-type-info.md) is in the range WDI\_CIPHER\_ALGO\_IHV\_START to WDI\_CIPHER\_ALGO\_IHV\_END.                                                                                                                                                     |

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 




