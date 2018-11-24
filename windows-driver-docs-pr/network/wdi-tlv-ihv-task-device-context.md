---
title: WDI_TLV_IHV_TASK_DEVICE_CONTEXT
description: WDI_TLV_IHV_TASK_DEVICE_CONTEXT is a TLV that contains IHV-provided device context for NDIS_STATUS_WDI_INDICATION_IHV_TASK_REQUEST.
ms.assetid: FBFE8931-DF29-4605-A14D-12CEC0433086
ms.date: 07/18/2017
keywords:
 - WDI_TLV_IHV_TASK_DEVICE_CONTEXT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_IHV\_TASK\_DEVICE\_CONTEXT


WDI\_TLV\_IHV\_TASK\_DEVICE\_CONTEXT is a TLV that contains IHV-provided device context for [NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/dn925637).

## TLV Type


0xE0

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                    |
|-----------|--------------------------------------------------------------------------------|
| UINT8\[\] | The IHV-provided device context information that is forwarded to the IHV task. |

 

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

 

 




