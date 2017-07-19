---
title: NDIS\_STATUS\_WDI\_INDICATION\_TASK\_OFFLOAD\_CURRENT\_CONFIG
author: windows-driver-content
description: Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_TASK\_OFFLOAD\_CURRENT\_CONFIG to indicate when there is a change in the TCP offload capabilities of the hardware.
ms.assetid: 4E73F09A-965F-4F32-AFF7-FDF1E3B2853C
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_WDI_INDICATION_TASK_OFFLOAD_CURRENT_CONFIG Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WDI_INDICATION_TASK_OFFLOAD_CURRENT_CONFIG%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


