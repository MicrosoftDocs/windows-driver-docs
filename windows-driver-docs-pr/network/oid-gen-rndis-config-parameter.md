---
title: OID_GEN_RNDIS_CONFIG_PARAMETER
ms.topic: reference
description: As a set, the OID_GEN_RNDIS_CONFIG_PARAMETER is used to set device-specific parameters.
ms.date: 03/02/2023
keywords: 
 -OID_GEN_RNDIS_CONFIG_PARAMETER Network Drivers Starting with Windows Vista
---

# OID\_GEN\_RNDIS\_CONFIG\_PARAMETER


As a set, the OID\_GEN\_RNDIS\_CONFIG\_PARAMETER is used to set device-specific parameters. The host uses it with RNDIS devices only.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For RNDIS devices only.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Optional.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Optional.

## Remarks

The OID\_GEN\_RNDIS\_CONFIG\_PARAMETER is used with RNDIS devices. The host uses it to set device-specific parameters. It is not used by miniport drivers. For more information about this OID, see [Setting Device-Specific Parameters](./setting-device-specific-parameters.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

