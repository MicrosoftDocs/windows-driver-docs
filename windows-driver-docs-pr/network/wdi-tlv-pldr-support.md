---
title: WDI_TLV_PLDR_SUPPORT
description: WDI_TLV_PLDR_SUPPORT is a TLV that specifies if PLDR (Platform Level Reset) is supported.
ms.assetid: BC1BE1A7-AA2D-4D11-A75A-EC0143343F33
ms.date: 07/18/2017
keywords:
 - WDI_TLV_PLDR_SUPPORT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_PLDR\_SUPPORT


WDI\_TLV\_PLDR\_SUPPORT is a TLV that specifies if PLDR (Platform Level Reset) is supported.

**Note**  This TLV was added in Windows 10, version 1511, WDI version 1.0.10.

 

## TLV Type


0x11A

## Length


The size (in bytes) of a UINT8.

## Values


| Type  | Description                                                                                                                                                                                                                       |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | Specifies if PLDR is supported. This value is set to 0 if the device or bus does not support reset functionality (usually by querying the ACPI or PCI methods). A non-zero value specifies that reset functionality is supported. |

 

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

## See also


[PLDR](https://msdn.microsoft.com/library/windows/hardware/mt269098)

 

 




