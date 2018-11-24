---
title: WDI_TLV_IHV_TASK_REQUEST_PARAMETERS
description: WDI_TLV_IHV_TASK_REQUEST_PARAMETERS is a TLV that contains the requested priority for NDIS_STATUS_WDI_INDICATION_IHV_TASK_REQUEST.
ms.assetid: C33CF8FE-EDBC-41D1-A63C-E43650E9570E
ms.date: 07/18/2017
keywords:
 - WDI_TLV_IHV_TASK_REQUEST_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_IHV\_TASK\_REQUEST\_PARAMETERS


WDI\_TLV\_IHV\_TASK\_REQUEST\_PARAMETERS is a TLV that contains the requested priority for [NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/dn925637).

## TLV Type


0xDF

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                             |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | The IHV-requested priority for this task. See [**WDI\_IHV\_TASK\_PRIORITY**](https://msdn.microsoft.com/library/windows/hardware/dn926064) for valid priority values. |

 

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

 

 




