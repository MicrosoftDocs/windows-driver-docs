---
title: OID\_DOT11\_START\_AP\_REQUEST
author: windows-driver-content
description: OID\_DOT11\_START\_AP\_REQUEST
ms.assetid: b37ce67b-e80e-4b34-a810-89d438ed848f
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_START_AP_REQUEST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_START\_AP\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_START\_AP\_REQUEST object identifier (OID) requests that the miniport driver configure the NIC to start the infrastructure network and to serve as an access point (AP). The NIC must switch from ExtAP INIT mode to ExtAP OP mode.

**Note**  Support for this OID is mandatory.

 

The NIC must be in ExtAP INIT mode in order to configure new AP profile settings. If the NIC is in ExtAP OP mode, the operating system will issue an OID\_DOT11\_RESET\_REQUEST before it configures a new AP profile.

Before the operating system issues an OID\_DOT11\_START\_AP\_REQUEST to start an 802.11 infrastructure network, it adds configuration parameters for the network by using set requests on one or more of the following OIDs:

-   [OID\_DOT11\_ADDITIONAL\_IE](oid-dot11-additional-ie.md)

-   [OID\_DOT11\_AUTO\_CONFIG\_ENABLED](oid-dot11-auto-config-enabled.md)

-   [OID\_DOT11\_BEACON\_PERIOD](oid-dot11-beacon-period.md)

-   [OID\_DOT11\_CIPHER\_DEFAULT\_KEY](oid-dot11-cipher-default-key.md)

-   [OID\_DOT11\_CIPHER\_DEFAULT\_KEY\_ID](oid-dot11-cipher-default-key-id.md)

-   [OID\_DOT11\_CIPHER\_KEY\_MAPPING\_KEY](oid-dot11-cipher-key-mapping-key.md)

-   [OID\_DOT11\_CURRENT\_CHANNEL](oid-dot11-current-channel.md)

-   [OID\_DOT11\_CURRENT\_FREQUENCY](oid-dot11-current-frequency.md)

-   [OID\_DOT11\_CURRENT\_OPERATION\_MODE](oid-dot11-current-operation-mode.md)

-   [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md)

-   [OID\_DOT11\_DESIRED\_PHY\_LIST](oid-dot11-desired-phy-list.md)

-   [OID\_DOT11\_DESIRED\_SSID\_LIST](oid-dot11-desired-ssid-list.md)

-   [OID\_DOT11\_DTIM\_PERIOD](oid-dot11-dtim-period.md)

-   [OID\_DOT11\_ENABLED\_AUTHENTICATION\_ALGORITHM](oid-dot11-enabled-authentication-algorithm.md)

-   [OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM](oid-dot11-enabled-multicast-cipher-algorithm.md)

-   [OID\_DOT11\_ENABLED\_UNICAST\_CIPHER\_ALGORITHM](oid-dot11-enabled-unicast-cipher-algorithm.md)

-   [OID\_DOT11\_EXCLUDE\_UNENCRYPTED](oid-dot11-exclude-unencrypted.md)

-   [OID\_DOT11\_FLUSH\_BSS\_LIST](oid-dot11-flush-bss-list.md)

-   [OID\_DOT11\_FRAGMENTATION\_THRESHOLD](oid-dot11-fragmentation-threshold.md)

-   [OID\_DOT11\_MULTICAST\_LIST](oid-dot11-multicast-list.md)

-   [OID\_DOT11\_NIC\_POWER\_STATE](oid-dot11-nic-power-state.md)

-   [OID\_DOT11\_OPERATIONAL\_RATE\_SET](oid-dot11-operational-rate-set.md)

-   [OID\_DOT11\_PRIVACY\_EXEMPTION\_LIST](oid-dot11-privacy-exemption-list.md)

-   [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md)

-   [OID\_DOT11\_SCAN\_REQUEST](oid-dot11-scan-request.md)

The following interaction sequence between miniport driver and operating system takes place:

1.  The operating system sets the network service set identifier (SSID) by setting [OID\_DOT11\_DESIRED\_SSID\_LIST](oid-dot11-desired-ssid-list.md).

2.  The miniport driver should set the basic service set identifier (BSSID) to be the NIC's MAC address.

3.  The miniport driver can optionally set [OID\_DOT11\_BEACON\_PERIOD](oid-dot11-beacon-period.md) to schedule the NIC's transmission of 802.11 Beacon frames.

4.  The operating system sets security-related OIDs in the following order:

    -   [OID\_DOT11\_ENABLED\_AUTHENTICATION\_ALGORITHM](oid-dot11-enabled-authentication-algorithm.md)
    -   [OID\_DOT11\_ENABLED\_UNICAST\_CIPHER\_ALGORITHM](oid-dot11-enabled-unicast-cipher-algorithm.md)
    -   [OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM](oid-dot11-enabled-multicast-cipher-algorithm.md)(optional). If this OID is not set, the NIC should use the unicast cipher algorithm.

    Any OIDs not listed here that can be set in ExtAP INIT mode can come to the miniport driver in any order.

    If the miniport driver receives an OID\_DOT11\_START\_AP\_REQUEST set request after it has indicated [NDIS\_STATUS\_DOT11\_STOP\_AP](ndis-status-dot11-stop-ap.md) but before it has indicated [NDIS\_STATUS\_DOT11\_CAN\_SUSTAIN\_AP](ndis-status-dot11-can-sustain-ap.md), the driver should fail the OID request with a failure code of NDIS\_STATUS\_INVALID\_STATE.

    The NIC should support 802.11 open authentication and shared-key authentication infrastructure security. The NIC can additionally support any of the following infrastructure security features:

    -   WPA
    -   WPA-PSK
    -   RSNA
    -   RSNA-PSK

5.  For each enabled 802.11a PHY, the miniport driver should set [OID\_DOT11\_CURRENT\_FREQUENCY](oid-dot11-current-frequency.md).

6.  For each enabled 802.11b or g PHY, the miniport driver should set [OID\_DOT11\_CURRENT\_CHANNEL](oid-dot11-current-channel.md).

7.  The operating system sets other Microsoft standard configuration parameters, such as a packet exemption list that exempts packets with certain Ethernet types from cipher operations.

For any optional settings that are not set by the operating system, the miniport driver should use the default values provided by the NIC manufacturer.

The miniport driver should use the first entry from the desired SSID list as the SSID for the NIC. The BSSID of the network must be the MAC address of the NIC. If the **msDot11DesiredPhyList** management information base (MIB) object is DOT11\_PHY\_ID\_ANY, the miniport driver can start the new BSS on any PHY. If **msDot11DesiredPhyList** contains a list of specific PHY identifiers, the miniport driver should start the new BSS by using the first specified PHY identifier.

The NIC should send out 802.11 beacon packets periodically as specified in the *IEEE 802.11 Standard*. When the NIC does this, it should attach the list of additional information elements (IEs) to the end of each beacon packet. The operating system will guarantee that it will not set WPA and WMM IEs in its list of IEs. For more information on how the miniport driver should handle additional IE data, see [OID\_DOT11\_ADDITIONAL\_IE](oid-dot11-additional-ie.md).

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


[NDIS\_STATUS\_DOT11\_CAN\_SUSTAIN\_AP](ndis-status-dot11-can-sustain-ap.md)

[NDIS\_STATUS\_DOT11\_STOP\_AP](ndis-status-dot11-stop-ap.md)

[OID\_DOT11\_ADDITIONAL\_IE](oid-dot11-additional-ie.md)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_START_AP_REQUEST%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


