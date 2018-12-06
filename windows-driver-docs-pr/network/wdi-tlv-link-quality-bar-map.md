---
title: WDI_TLV_LINK_QUALITY_BAR_MAP
description: WDI_TLV_LINK_QUALITY_BAR_MAP is a TLV that contains the mapping of signal quality to Wi-Fi signal strength bars.
ms.assetid: 35E073F4-D372-466A-98FF-0AAB1695284E
ms.date: 07/18/2017
keywords:
 - WDI_TLV_LINK_QUALITY_BAR_MAP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_LINK\_QUALITY\_BAR\_MAP


WDI\_TLV\_LINK\_QUALITY\_BAR\_MAP is a TLV that contains the mapping of signal quality to Wi-Fi signal strength bars.

## TLV Type


0xD8

## Length


The size (in bytes) of the array of WDI\_LINK\_QUALITY\_BAR\_MAP\_PARAMETERS elements. The array must contain 1 or more elements.

**Note**  WDI\_LINK\_QUALITY\_BAR\_MAP\_PARAMETERS is not a WDI structure. It is defined in the WDI TLV parser generator, and is used for documentation purposes only.

 

## Values


| Type                                         | Description                                         |
|----------------------------------------------|-----------------------------------------------------|
| WDI\_LINK\_QUALITY\_BAR\_MAP\_PARAMETERS\[\] | An array of signal strength bar mapping parameters. |

 

WDI\_LINK\_QUALITY\_BAR\_MAP\_PARAMETERS consists of the following elements.

| Type  | Description                                                                  |
|-------|------------------------------------------------------------------------------|
| UINT8 | The lower limit link quality (0-100) for the current signal strength bar.    |
| UINT8 | The upper limit of link quality (0-100) for the current signal strength bar. |
| UINT8 | The signal strength bar number.                                              |

 

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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 




