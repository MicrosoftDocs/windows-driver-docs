---
title: NDIS_STATUS_WDI_INDICATION_TASK_OFFLOAD_CURRENT_CONFIG
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_TASK_OFFLOAD_CURRENT_CONFIG to indicate when there is a change in the TCP offload capabilities of the hardware.
ms.assetid: 4E73F09A-965F-4F32-AFF7-FDF1E3B2853C
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_TASK_OFFLOAD_CURRENT_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_TASK\_OFFLOAD\_CURRENT\_CONFIG


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_TASK\_OFFLOAD\_CURRENT\_CONFIG to indicate when there is a change in the TCP offload capabilities of the hardware.

| Object |
|--------|
| Port   |

 

When there is a change in the TCP offload capabilities of the hardware, the LE sends this unsolicited indication to the UE, with the new TCP checksum/LSO capabilities. Use the values **NDIS\_OFFLOAD\_SET\_OFF** and **NDIS\_OFFLOAD\_SET\_ON** for members in [**WDI\_TLV\_TCP\_OFFLOAD\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/dn898069) for indicating changes in offload capabilities. When the UE sends down a [OID\_WDI\_SET\_TCP\_OFFLOAD\_PARAMETERS](oid-wdi-set-tcp-offload-parameters.md), the LE should update the offload capabilities and then send this indication so that the OS is updated with the latest offload capabilities information.

## Payload data


| Type                                                                                  | Multiple TLV instances allowed | Optional | Description                                              |
|---------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------|
| [**WDI\_TLV\_TCP\_OFFLOAD\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/dn898069) |                                | X        | The TCP/IP checksum and Large Send Offload capabilities. |

 

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

## See also


[OID\_WDI\_SET\_TCP\_OFFLOAD\_PARAMETERS](oid-wdi-set-tcp-offload-parameters.md)

 

 




