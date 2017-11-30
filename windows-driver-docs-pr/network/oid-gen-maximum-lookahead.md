---
title: OID_GEN_MAXIMUM_LOOKAHEAD
author: windows-driver-content
description: As a query, the OID_GEN_MAXIMUM_LOOKAHEAD OID specifies the maximum number of bytes that the NIC can provide as lookahead data.
ms.assetid: 086581f7-c0a5-4355-82fe-22f53201b540
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_MAXIMUM_LOOKAHEAD Network Drivers Starting with Windows Vista
---

# OID\_GEN\_MAXIMUM\_LOOKAHEAD


As a query, the OID\_GEN\_MAXIMUM\_LOOKAHEAD OID specifies the maximum number of bytes that the NIC can provide as lookahead data. This specification does not include a header.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

NDIS 6.0 and later miniport drivers do not receive this OID request. NDIS handles this OID with a cached value that miniport drivers supply during initialization.

Upper-layer drivers examine lookahead data to determine whether a packet that is associated with the lookahead data is intended for one or more of their clients.

If the underlying driver supports multipacket receive indications, bound protocol drivers are given full net packets on every indication. Consequently, this value is identical to that returned for [OID\_GEN\_RECEIVE\_BLOCK\_SIZE](oid-gen-receive-block-size.md).

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

## See also


[OID\_GEN\_RECEIVE\_BLOCK\_SIZE](oid-gen-receive-block-size.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_MAXIMUM_LOOKAHEAD%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


