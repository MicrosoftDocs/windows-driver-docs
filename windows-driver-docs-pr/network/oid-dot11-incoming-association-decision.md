---
title: OID\_DOT11\_INCOMING\_ASSOCIATION\_DECISION
author: windows-driver-content
description: OID\_DOT11\_INCOMING\_ASSOCIATION\_DECISION
ms.assetid: dd9601c7-ff89-4629-affc-02a401b9ca83
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_INCOMING_ASSOCIATION_DECISION Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_INCOMING\_ASSOCIATION\_DECISION


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_INCOMING\_ASSOCIATION\_DECISION object identifier (OID) requests that the miniport driver notify the NIC whether it has accepted an incoming request from an 802.11 peer station to perform an association procedure.

**Note**  Support for this OID is mandatory. NDIS supports this OID with the direct OID request interface. For more information about the direct OID request interface, see [NDIS 6.1 Direct OID Request Interface](https://msdn.microsoft.com/library/windows/hardware/ff564736).

 

The data type for this OID is the [**DOT11\_INCOMING\_ASSOC\_DECISION**](https://msdn.microsoft.com/library/windows/hardware/ff548654) structure.

When this OID is set, the NIC must behave as follows:

-   If the Extensible AP is in the INIT state, the NIC must fail the request and return a status indication of NDIS\_STATUS\_INVALID\_STATE.

-   If the Extensible AP is in the OP state, the NIC must complete the request.

**Note**  Miniports must handle this OID synchronously. They must not process requests as pending.

 

For more information about the association procedure, see [Association Operation Guidelines for Extensible Access Point (ExtAP) Mode](https://msdn.microsoft.com/library/windows/hardware/ff543791).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**DOT11\_INCOMING\_ASSOC\_DECISION**](https://msdn.microsoft.com/library/windows/hardware/ff548654)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_INCOMING_ASSOCIATION_DECISION%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


