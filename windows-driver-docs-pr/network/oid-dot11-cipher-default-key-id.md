---
title: OID\_DOT11\_CIPHER\_DEFAULT\_KEY\_ID
author: windows-driver-content
description: OID\_DOT11\_CIPHER\_DEFAULT\_KEY\_ID
ms.assetid: 2ff0ec23-a957-452e-9762-bf1d83e293e8
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_CIPHER_DEFAULT_KEY_ID Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_CIPHER\_DEFAULT\_KEY\_ID


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_CIPHER\_DEFAULT\_KEY\_ID object identifier (OID) requests that the miniport driver set the value of the Extensible Station (ExtSTA) **dot11DefaultKeyID** management information base (MIB) object to the specified value.

When queried, this OID requests that the miniport driver return the value of the **dot11DefaultKeyID** MIB object.

The **dot11DefaultKeyID** MIB object specifies the index of a cipher key in the 802.11 station's default key table that the station uses for data encryption. The 802.11 station uses the cipher key referenced by the **dot11DefaultKeyID** MIB object as the default encryption key for transmitted packets unless a key-mapping key exists for the destination media access control (MAC) address.

For more information about the default keys, per-station default keys, and key-mapping keys, see [802.11 Cipher Key Types](https://msdn.microsoft.com/library/windows/hardware/ff543625).

**Note**  Support for this OID is mandatory if the 802.11 station supports any cipher algorithms. The miniport driver returns a list of supported cipher algorithms when [OID\_DOT11\_SUPPORTED\_UNICAST\_ALGORITHM\_PAIR](oid-dot11-supported-unicast-algorithm-pair.md) or [OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR](oid-dot11-supported-multicast-algorithm-pair.md) are queried.

 

The data type for this OID is a ULONG value. For standard 802.11 cipher algorithms, the default key ID must be from 0 through 3. For a cipher algorithm developed by an IHV, the default key ID can be any value within the range defined by the IHV.

The IEEE 802.11-2012 standard defines key index values from 1 through 4. The value *x* specified by this OID maps to the 802.11 key index (*x* + 1).

When transmitting 802.11 data, the 802.11 station will encrypt the MAC service data unit (MSDU) payload data using the cipher key referenced by the **dot11DefaultKeyID** MIB object if the following are true:

-   The basic service set (BSS) network has enabled encryption.

-   A key mapping key does not exist for the destination MAC address. For more information about key-mapping keys, see [OID\_DOT11\_CIPHER\_KEY\_MAPPING\_KEY](oid-dot11-cipher-key-mapping-key.md).

When OID\_DOT11\_CIPHER\_DEFAULT\_KEY\_ID is set, the 802.11 station must synchronize the change to the default key ID with its packet-processing path. When the default key ID is changed, the 802.11 station must use it to encrypt the next MAC protocol data unit (MPDU) data frame that it transmits.

The default value of the **dot11DefaultKeyID** MIB object is zero. The miniport driver must set this MIB object to its default if any of the following occur:

-   The miniport driver's [*MiniportInitializeEx*](miniportinitializeex.md) function is called.

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_CIPHER_DEFAULT_KEY_ID%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


