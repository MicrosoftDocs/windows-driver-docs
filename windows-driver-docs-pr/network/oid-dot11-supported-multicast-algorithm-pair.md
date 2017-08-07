---
title: OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR
author: windows-driver-content
description: OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR
ms.assetid: 93927df1-acaa-4c42-b8e1-48f651b9ef96
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_SUPPORTED_MULTICAST_ALGORITHM_PAIR Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR object identifier (OID) requests that the miniport driver return a list of the authentication and cipher algorithms that the 802.11 station supports for multicast and broadcast packets.

The data type for this OID is the [**DOT11\_AUTH\_CIPHER\_PAIR\_LIST**](dot11-auth-cipher-pair-list.md) structure.

When OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR is queried, the miniport driver only returns 802.11 authentication and cipher algorithms that the 802.11 station supports for the current value of the IEEE **dot11DesiredBSSType** management information base (MIB) object. For more information about this MIB object, see [OID\_DOT11\_DESIRED\_BSS\_TYPE](oid-dot11-desired-bss-type.md).

**Note**  For each value of the **dot11DesiredBSSType** MIB object, the miniport driver must not change the list of the 802.11 authentication and cipher algorithms after the OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR is queried.

 

There must be at least one cipher algorithm defined for each supported authentication algorithm. If the miniport driver does not support any multicast cipher algorithms for a particular authentication algorithm, it must still create a list entry for the authentication algorithm and use **DOT11\_CIPHER\_ALGO\_NONE** for the related cipher algorithm.

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
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_SUPPORTED_MULTICAST_ALGORITHM_PAIR%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


