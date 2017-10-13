---
title: OID_GEN_PROTOCOL_OPTIONS
author: windows-driver-content
description: As a set, the OID\_GEN\_PROTOCOL\_OPTIONS OID specifies a bitmask that defines optional properties of the protocol driver.
ms.assetid: 48c3468b-2d8b-48cb-9a25-19470923f582
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_PROTOCOL_OPTIONS Network Drivers Starting with Windows Vista
---

# OID\_GEN\_PROTOCOL\_OPTIONS


As a set, the OID\_GEN\_PROTOCOL\_OPTIONS OID specifies a bitmask that defines optional properties of the protocol driver.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. This OID is for protocol drivers.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

A protocol informs NDIS of its properties, which can optionally take advantage of them. If the protocol driver does not set its flags on a binding, NDIS assumes they are all clear.

The following flags are currently defined:

<a href="" id="ndis-prot-option-estimated-length"></a>NDIS\_PROT\_OPTION\_ESTIMATED\_LENGTH  
Specifies that packets can be indicated at the worst-case estimate of packet size, instead of an exact value, to this protocol.

<a href="" id="ndis-prot-option-no-loopback"></a>NDIS\_PROT\_OPTION\_NO\_LOOPBACK  
Specifies that the protocol does not require loopback support on the binding.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_PROTOCOL_OPTIONS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


