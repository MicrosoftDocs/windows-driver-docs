---
title: OID_GEN_RNDIS_CONFIG_PARAMETER
author: windows-driver-content
description: As a set, the OID_GEN_RNDIS_CONFIG_PARAMETER is used to set device-specific parameters.
ms.assetid: 79e74e8b-7811-46a5-8ede-f6cca92967b0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

Remarks
-------

The OID\_GEN\_RNDIS\_CONFIG\_PARAMETER is used with RNDIS devices. The host uses it to set device-specific parameters. It is not used by miniport drivers. For more information about this OID, see [Setting Device-Specific Parameters](https://msdn.microsoft.com/library/windows/hardware/ff570784).

Requirements
------------

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_RNDIS_CONFIG_PARAMETER%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


