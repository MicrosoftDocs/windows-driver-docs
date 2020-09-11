---
title: WDI_TLV_OWE_DH_IE
description: WDI_TLV_OWE_DH_IE is a TLV that must be included in the association request sent by the station when the auth type is OWE. 
ms.assetid:
ms.date: 09/10/2020
keywords:
 - WDI_TLV_OWE_DH_IENetwork Drivers Starting with Windows 10, Version 2004
ms.localizationpriority: medium
---

# WDI\_TLV\_OWE\_DH\_IE

WDI\_TLV\_OWE\_DH\_IE is a Diffie-Hellman Extension IE blob that must be included in the association request sent by the station when auth type is OWE. This is applicable to any BSSID that the device would associate with and should be included in addition to the other associated req vendor IEs.

## TLV Type

0x16A

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |                                                         |
| --- | --- |
| UINT8\[\] | An array of UINT8 elements that contains the IEs that must be included in association requests sent by the port. These are applicable to any BSSID that the device associates with. They should be used in addition to the common and BSSID specific IEs. |

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
<td><p>Windows 10, Version 2004</p></td>
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
