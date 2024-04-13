---
title: WDI_TLV_PLDR_SUPPORT
ms.topic: reference
description: WDI_TLV_PLDR_SUPPORT is a TLV that specifies if PLDR (Platform Level Reset) is supported.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_PLDR_SUPPORT Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PLDR\_SUPPORT

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


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

 

## Requirements

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


[PLDR](./wdi-pldr-and-fldr.md)

 

