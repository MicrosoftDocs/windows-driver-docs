---
title: WDI_TLV_ETHERTYPE_ENCAP_TABLE
description: WDI_TLV_ETHERTYPE_ENCAP_TABLE is a TLV that contains the Ethertype encapsulations for the association.
ms.assetid: BAAC7E5B-F13F-4AC8-A3F9-76197F92C7E3
ms.date: 07/18/2017
keywords:
 - WDI_TLV_ETHERTYPE_ENCAP_TABLE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ETHERTYPE\_ENCAP\_TABLE


WDI\_TLV\_ETHERTYPE\_ENCAP\_TABLE is a TLV that contains the Ethertype encapsulations for the association.

## TLV Type


0x31

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                                       | Description                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_ETHERTYPE\_ENCAPSULATION\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn897818)\[\] | An array of [**WDI\_ETHERTYPE\_ENCAPSULATION\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn897818) elements that specifies the Ethertype encapsulations for the association. |

 

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

 

 




