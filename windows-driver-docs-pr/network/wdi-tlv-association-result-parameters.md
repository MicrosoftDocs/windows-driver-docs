---
title: WDI_TLV_ASSOCIATION_RESULT_PARAMETERS
description: WDI_TLV_ASSOCIATION_RESULT_PARAMETERS is a TLV that contains parameters for an association result.
ms.assetid: A6F29084-EF36-43C4-B646-E071E755E110
ms.date: 07/18/2017
keywords:
 - WDI_TLV_ASSOCIATION_RESULT_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ASSOCIATION\_RESULT\_PARAMETERS


WDI\_TLV\_ASSOCIATION\_RESULT\_PARAMETERS is a TLV that contains parameters for an association result.

## TLV Type


0x2D

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                        | Description                                                                                                                                                                                                                                         |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32                                                      | Specifies the completion status of the association attempt as defined in [**WDI\_ASSOC\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/dn897725).                                                                                                                       |
| UINT32                                                      | The 802.11 status code sent by the peer in response to an authentication or association request from this port.                                                                                                                                     |
| UINT8                                                       | Specifies whether the port sent an 802.11 association or an 802.11 reassociation request to the AP. This value should be set to 1 if a reassociation request was used.                                                                              |
| [**WDI\_AUTH\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/dn897792)     | The authentication algorithm that the port negotiated with the peer during association.                                                                                                                                                             |
| [**WDI\_CIPHER\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/dn897802) | The unicast cipher algorithm that the port negotiated with the peer during association.                                                                                                                                                             |
| [**WDI\_CIPHER\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/dn897802) | The multicast data cipher algorithm that the port negotiated with the peer during association.                                                                                                                                                      |
| [**WDI\_CIPHER\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/dn897802) | The multicast management cipher algorithm that the port negotiated with the peer during association.                                                                                                                                                |
| UINT8                                                       | Specifies if the port has associated with a peer that supports distribution system (DS) services for ISO Layer 2 bridging on any station in the BSS network, including mobile stations and APs. This value should be set to 1 if this is supported. |
| UINT8                                                       | Specifies whether the port has performed port authorization during the association operation.                                                                                                                                                       |
| UINT8                                                       | Specifies whether 802.11 WMM QoS protocol has been negotiated for this association. This value should be set to 1 if it has been negotiated.                                                                                                        |
| [**WDI\_DS\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn897813)                   | Specifies whether the port is connected to the same DS as its previous association.                                                                                                                                                                 |
| UINT32                                                      | When a (re)association fails with an 802.11 reason code of 30, this value indicates the value of the association comeback time requested by the peer.                                                                                               |
| WDI\_BAND\_ID (UINT32)                                      | The band ID on which the association is established.                                                                                                                                                                                                |
| UINT32                                                      | The IHV association status. If the association failed, this can contain an IHV-defined status code. This is only used for debugging purpose.                                                                                                        |

 

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

 

 




