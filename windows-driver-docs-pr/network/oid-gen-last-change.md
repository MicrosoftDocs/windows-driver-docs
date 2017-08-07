---
title: OID\_GEN\_LAST\_CHANGE
author: windows-driver-content
description: As a query, use the OID\_GEN\_LAST\_CHANGE OID to determine the time of the last operational state change of a network interface (ifLastChange from RFC 2863).
ms.assetid: bd96d1ec-2fd0-491f-acb4-c1594ce6a084
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_GEN_LAST_CHANGE Network Drivers Starting with Windows Vista
---

# OID\_GEN\_LAST\_CHANGE


As a query, use the OID\_GEN\_LAST\_CHANGE OID to determine the time of the last operational state change of a network interface (*ifLastChange* from [RFC 2863](http://go.microsoft.com/fwlink/p/?linkid=84054)).

**Version Information**

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

Remarks
-------

Only [NDIS network interface](https://msdn.microsoft.com/library/windows/hardware/ff566527) providers, and therefore not miniport drivers or filter drivers, must support this OID as an OID request.

This OID returns the time, starting from the last computer restart, when the interface entered its current operational state. For more information about the operational state, see [**NDIS\_STATUS\_OPER\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff567406) and [OID\_GEN\_OPERATIONAL\_STATUS](oid-gen-operational-status.md). To get the current time, an interface provider can call the [**NdisGetSystemUpTimeEx**](ndisgetsystemuptimeex.md) function.

If the current operational state was entered before the last reinitialization of the interface, this value should be zero. . If the interface provider does not track operational state change time, the value should be zero.

If the interface provider returns NDIS\_STATUS\_SUCCESS, the result of the query is a ULONG64 value that specifies the state change time, in milliseconds, since the last computer restart.

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


[OID\_GEN\_OPERATIONAL\_STATUS](oid-gen-operational-status.md)

[**NDIS\_STATUS\_OPER\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff567406)

[**NdisGetSystemUpTimeEx**](ndisgetsystemuptimeex.md)

[NDIS Network Interface OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566545)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_LAST_CHANGE%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


