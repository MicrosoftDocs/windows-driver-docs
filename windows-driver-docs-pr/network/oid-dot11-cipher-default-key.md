---
title: OID_DOT11_CIPHER_DEFAULT_KEY
author: windows-driver-content
description: OID_DOT11_CIPHER_DEFAULT_KEY
ms.assetid: 51b6c89f-4f9f-482a-a3fe-6622cbcfa04a
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_CIPHER_DEFAULT_KEY Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_CIPHER\_DEFAULT\_KEY


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_CIPHER\_DEFAULT\_KEY object identifier (OID) requests that the miniport driver add, modify, or delete an entry in its default key or per-station default key tables.

**Note**  Support for this OID is mandatory if the 802.11 station supports any cipher algorithms. The miniport driver returns a list of supported cipher algorithms when [OID\_DOT11\_SUPPORTED\_UNICAST\_ALGORITHM\_PAIR](oid-dot11-supported-unicast-algorithm-pair.md) or [OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR](oid-dot11-supported-multicast-algorithm-pair.md) are queried.

 

The data type for this OID is the [**DOT11\_CIPHER\_DEFAULT\_KEY\_VALUE**](https://msdn.microsoft.com/library/windows/hardware/ff547674) structure.

When the OID\_DOT11\_CIPHER\_DEFAULT\_KEY OID is set, the miniport driver must follow these guidelines:

-   If the 802.11 station does not support the cipher algorithm specified by the **AlgorithmId** member, fail the set request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the specified cipher algorithm does not support the key index specified by the **uKeyIndex** member, fail the set request by returning NDIS\_STATUS\_INVALID\_DATA from its *MiniportOidRequest* function.

-   If the **dot11DesiredBSSType** management information base (MIB) object is set to **dot11\_BSS\_type\_independent** and the **MacAddr** member is not set to 0x000000000000, the key defined by the [**DOT11\_CIPHER\_KEY\_MAPPING\_KEY\_VALUE**](https://msdn.microsoft.com/library/windows/hardware/ff547675) structure is a per-station cipher key. For more information about per-station default cipher keys, see [Per-Station Default Keys](https://msdn.microsoft.com/library/windows/hardware/ff570016).

    In this situation, the miniport driver must fail the set request if any of the following are true:

    -   The **dot11DesiredBSSType** management information base (MIB) object is not set to **dot11\_BSS\_type\_independent**. In this situation, the miniport driver returns NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. For more information about the **dot11DesiredBSSType** MIB object, see [OID\_DOT11\_DESIRED\_BSS\_TYPE](oid-dot11-desired-bss-type.md).
    -   **MacAddr** is not a valid unicast MAC address. In this situation, the miniport driver returns NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.
    -   A per-station default key table referenced by **MacAddr** does not exist and the 802.11 station does not have the resources to add a per-station default key table. In this situation, the driver returns NDIS\_STATUS\_INVALID\_LENGTH from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

        **Note**  The miniport driver returns the number of per-station default key tables supported by the 802.11 station when [OID\_DOT11\_EXTSTA\_CAPABILITY](oid-dot11-extsta-capability.md) is queried.

         

-   If the **bDelete** member is set to **TRUE**, delete the key material for the key referenced by the **uKeyIndex** member. If the driver had previously deleted the specified key, it must accept the set request by returning NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

When modifying TKIP keys, the miniport driver must synchronize the key update with the packet-processing path on the 802.11 station.

For example, the miniport driver must avoid situations in which the packet payload was decrypted using the old cipher key and verified using the new message integrity code (MIC) key.

The 802.11 station must clear its default keys in the following situations:

-   When the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

-   When a method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the MAC layer of the 802.11 station.

For more information about default keys and per-station default keys, see [802.11 Cipher Key Types](https://msdn.microsoft.com/library/windows/hardware/ff543625).

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

 

 




