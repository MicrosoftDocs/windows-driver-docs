---
title: NDIS_STATUS_WDI_INDICATION_FT_ASSOC_PARAMS_NEEDED
author: windows-driver-content
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_FT_ASSOC_PARAMS_NEEDED to request parameters for 802.11r roaming.ObjectPort .
ms.assetid: AB745908-AA7B-416A-9C97-B376293F3DEE
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_WDI_INDICATION_FT_ASSOC_PARAMS_NEEDED Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_FT\_ASSOC\_PARAMS\_NEEDED


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_FT\_ASSOC\_PARAMS\_NEEDED to request parameters for 802.11r roaming.

| Object |
|--------|
| Port   |

 

During [OID\_WDI\_TASK\_ROAM](oid-wdi-task-roam.md), WDI provides the parameters to send the 802.11 Authentication Request (PmkR0Name, R0KH-ID, SNonce, MDIE). Upon receiving the Authentication response, the LE requests additional needed parameters for the reassociation request, such as PMKR1Name and R1KH-ID. The LE also sends the parameters received in the Authentication Response (ANonce, SNonce, and R1KHID).

For a connection where Initial Mobility Domain is successfully done, the LE should only perform 11r roams (Fast roams). The LE can use the candidate list provided by the operating system, or use their own for the roams. If the LE uses its own candidate list, it must use the parameters (MDE, FTE, and PMKR0Name) provided in any one of the candidates suggested by the operating system to do a 11r roam. 11r is disabled whenever the connection is in FIPS mode. 11r fast roaming is currently only supported for FT over 1x authentication type.

## Payload data


| Type                                                                  | Multiple TLV instances allowed | Optional | Description                            |
|-----------------------------------------------------------------------|--------------------------------|----------|----------------------------------------|
| [**WDI\_TLV\_BSSID**](https://msdn.microsoft.com/library/windows/hardware/dn926153)                         |                                |          | The BSSID of the AP.                   |
| [**WDI\_TLV\_FT\_AUTH\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/mt269116)   |                                |          | The authentication request byte blob.  |
| [**WDI\_TLV\_FT\_AUTH\_RESPONSE**](https://msdn.microsoft.com/library/windows/hardware/mt269117) |                                |          | The authentication response byte blob. |

 

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


[OID\_WDI\_TASK\_ROAM](oid-wdi-task-roam.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WDI_INDICATION_FT_ASSOC_PARAMS_NEEDED%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


