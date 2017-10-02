---
title: OID_DOT11_EXCLUDE_UNENCRYPTED
author: windows-driver-content
description: OID\_DOT11\_EXCLUDE\_UNENCRYPTED
ms.assetid: 51a6563d-9e9d-4156-9f7a-b2892f4b7c25
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_EXCLUDE_UNENCRYPTED Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_EXCLUDE\_UNENCRYPTED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_EXCLUDE\_UNENCRYPTED OID requests that the miniport driver set the IEEE 802.11 **dot11ExcludeUnencrypted** management information base (MIB) object.

When queried, this OID requests that the miniport driver return the setting of the **dot11ExcludeUnencrypted** MIB object.

The **dot11ExcludeUnencrypted** MIB object specifies how the 802.11 station handles received packets with unencrypted payload data.

**Note**  Support for OID\_DOT11\_EXCLUDE\_UNENCRYPTED is mandatory if the 802.11 station supports any cipher algorithms. The miniport driver returns a list of supported cipher algorithms when [OID\_DOT11\_SUPPORTED\_UNICAST\_ALGORITHM\_PAIR](oid-dot11-supported-unicast-algorithm-pair.md) or [OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR](oid-dot11-supported-multicast-algorithm-pair.md) are queried.

 

The data type for this OID is a BOOLEAN value.

The **dot11ExcludeUnencrypted** MIB object defines the following actions:

-   If **dot11ExcludeUnencrypted** is **TRUE**, then the 802.11 station must discard any received unicast packets in which the Protected Frame subfield of the Frame Control field in the 802.11 MAC header is set to zero.

-   If **dot11ExcludeUnencrypted** is **FALSE**, then the 802.11 station can accept these packets and indicate them to the operating system.

When **dot11ExcludeUnencrypted** is **FALSE**, the miniport driver must connect to an access point (AP) with a Wired Equivalent Privacy (WEP) profile, even if the AP does not set the privacy field in the relevant management frames.

The actions defined by the **dot11ExcludeUnencrypted** MIB object do not apply to received packets that match an entry in the 802.11 station's current EtherType exemption list. For more information about the EtherType exemption list, see [OID\_DOT11\_PRIVACY\_EXEMPTION\_LIST](oid-dot11-privacy-exemption-list.md).

The default setting for the **dot11ExcludeUnencrypted** MIB object is **FALSE**. The miniport driver must set the MIB object to this default through its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function or when reset through [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md).

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_EXCLUDE_UNENCRYPTED%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


