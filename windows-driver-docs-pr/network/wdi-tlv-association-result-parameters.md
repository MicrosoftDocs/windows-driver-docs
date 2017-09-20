---
title: WDI_TLV_ASSOCIATION_RESULT_PARAMETERS
author: windows-driver-content
description: WDI_TLV_ASSOCIATION_RESULT_PARAMETERS is a TLV that contains parameters for an association result.
ms.assetid: A6F29084-EF36-43C4-B646-E071E755E110
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_ASSOCIATION_RESULT_PARAMETERS Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_ASSOCIATION_RESULT_PARAMETERS%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


