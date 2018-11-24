---
title: WDI_TLV_SCAN_MODE
description: WDI_TLV_SCAN_MODE is a TLV that contains scan mode parameters.
ms.assetid: 9F954B66-4F1D-48F2-9316-BE623DF0CAE6
ms.date: 07/18/2017
keywords:
 - WDI_TLV_SCAN_MODE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_SCAN\_MODE


WDI\_TLV\_SCAN\_MODE is a TLV that contains scan mode parameters.

## TLV Type


0x6

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                | Description                                                                                                                                                                                                                       |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8                                               | The number of times the full scan procedure should be repeated. If this value is set to 0, the scan should be repeated until the task is aborted by the host.                                                                     |
| [**WDI\_SCAN\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn926115)       | Specifies the type of scan that should be performed. If WDI\_SCAN\_TYPE\_ACTIVE is set, the device must only scan active channels.                                                                                                |
| UINT8                                               | Specifies if live updates are needed and discovered entries must be reported when they are found, with the recommended throttling logic above. This value is always true when the Microsoft component manages the BSS list cache. |
| [**WDI\_SCAN\_TRIGGER**](https://msdn.microsoft.com/library/windows/hardware/dn926114) | Specifies the trigger for the scan.                                                                                                                                                                                               |

 

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

 

 




