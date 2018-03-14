---
title: OID_DOT11_DESIRED_BSS_TYPE
author: windows-driver-content
description: OID_DOT11_DESIRED_BSS_TYPE
ms.assetid: 8e90f503-5aeb-49b9-b368-4fdc8f0cf496
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_DESIRED_BSS_TYPE Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_DESIRED\_BSS\_TYPE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_DESIRED\_BSS\_TYPE object identifier (OID) requests that the miniport driver set the value of the IEEE 802.11 **dot11DesiredBSSType** management information base (MIB) object to the specified value.

When queried, OID\_DOT11\_DESIRED\_BSS\_TYPE requests that the miniport driver return the value of the **dot11DesiredBSSType** MIB object.

The **dot11DesiredBSSType** MIB object specifies the type of basic service set (BSS) that the 802.11 station can join or start. The 802.11 station uses the desired BSS type to determine the type of 802.11 BSS to join or start in the following way:

-   If the desired BSS type is **dot11\_BSS\_type\_infrastructure**, the 802.11 station can only connect to infrastructure BSSs.

-   If the desired BSS type is **dot11\_BSS\_type\_independent**, the 802.11 station can only connect to an existing independent BSS (IBSS) or start a new IBSS network.

The miniport driver cannot set the **dot11DesiredBSSType** MIB object to **dot11\_BSS\_type\_any**. The miniport driver must fail a set request for this value by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

Regardless of whether the **dot11DesiredBSSType** MIB object changes when OID\_DOT11\_DESIRED\_BSS\_TYPE is set, the miniport driver must always reload the defaults values for the following:

-   The enabled authentication algorithms. For more information about the default values for authentication algorithms, see [OID\_DOT11\_ENABLED\_AUTHENTICATION\_ALGORITHM](oid-dot11-enabled-authentication-algorithm.md).

-   The enabled unicast cipher algorithms. For more information about the default values for unicast cipher algorithms, see [OID\_DOT11\_ENABLED\_UNICAST\_CIPHER\_ALGORITHM](oid-dot11-enabled-unicast-cipher-algorithm.md).

-   The enabled multicast cipher algorithms. For more information about the default values for multicast cipher algorithms, see [OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM](oid-dot11-enabled-multicast-cipher-algorithm.md).

The default for the **dot11DesiredBSSType** MIB object is **dot11\_BSS\_type\_infrastructure**. The miniport driver must set this MIB object to its default if any of the following occur:

-   The miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the MAC layer of the 802.11 station and the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure is **TRUE**.

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

 

 




