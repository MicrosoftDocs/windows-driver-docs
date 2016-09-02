---
title: Native 802.11 MiniportInitializeEx Requirements
description: Native 802.11 MiniportInitializeEx Requirements
ms.assetid: fb7988cf-b0d4-4c75-a987-a6e7f922bbf9
keywords: ["initializing Native 802.11 miniport drivers", "initializing miniport drivers", "MiniportInitializeEx"]
---

# Native 802.11 MiniportInitializeEx Requirements


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

A Native 802.11 miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function must do the following:

-   Set all 802.11 management information base (MIB) objects to their default values, as defined in [IEEE 802.11 MIB Objects](https://msdn.microsoft.com/library/windows/hardware/ff553782). For more information regarding the 802.11 MIB objects, refer to Annex D of the IEEE 802.11 standards listed in [Background Reading on 802.11](background-reading-on-802-11.md).

-   If the miniport driver supports the Extensible AP (ExtAP) operation mode, set all ExtAP MIB objects to their default values, as defined in [Extensible AP MIB Objects](https://msdn.microsoft.com/library/windows/hardware/ff549865).

-   If the miniport driver supports the Extensible Station (ExtSTA) operation mode, set all ExtSTA MIB objects to their default values, as defined in [Extensible Station MIB Objects](https://msdn.microsoft.com/library/windows/hardware/ff549882).

-   Initialize the power state of the radio based on the retained value of the **msDot11NICPowerState** MIB object. The value of the **msDot11NICPowerState** MIB object must persist across system shutdown and calls to [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) and [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432).

    For more information about the **msDot11NICPowerState** MIB object, see [OID\_DOT11\_NIC\_POWER\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569392).

    For more information about radio power states, see [Radio Power Management](radio-power-management.md).

-   The driver must clear all statistical counters returned through queries of [OID\_DOT11\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569420).

-   Clear the cached lists of BSS networks maintained during scan operations. The driver returns this cached list when queried through [OID\_DOT11\_ENUM\_BSS\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569360).

-   If the 802.11 station supports 802.11 pre-authentication through a pairwise master key identifier (PMKID), clear its PMKID cache. The driver's PMKID cache is set or queried through [OID\_DOT11\_PMKID\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569400).

-   Call the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function to provide NDIS with the general attributes of the miniport driver. In this situation, the *MiniportAttributes* parameter must be set to the address of a driver-allocated block of memory that is formatted as an [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure.

    The following table describes how the miniport driver sets the members of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure for the Native 802.11 interface.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES member</th>
    <th align="left">Value</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p><strong>MediaType</strong></p></td>
    <td align="left"><p><strong>NdisMediumNative802_11</strong></p></td>
    </tr>
    <tr class="even">
    <td align="left"><p><strong>PhysicalMediumType</strong></p></td>
    <td align="left"><p><strong>NdisPhysicalMediumNative802_11</strong></p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p><strong>MtuSize</strong></p></td>
    <td align="left"><p>2304</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p><strong>MediaConnectState</strong></p></td>
    <td align="left"><p><strong>MediaConnectStateConnected</strong></p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p><strong>MediaDuplexState</strong></p></td>
    <td align="left"><p><strong>MediaDuplexStateFull</strong></p></td>
    </tr>
    <tr class="even">
    <td align="left"><p><strong>SupportedPacketFilters</strong></p></td>
    <td align="left"><p>Flags that define the standard and Native 802.11 packet filters that are supported by the 802.11 station. For more information about the packet filters, see [OID_GEN_CURRENT_PACKET_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p><strong>MacAddressLength</strong></p></td>
    <td align="left"><p>6</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p><strong>PermanentMacAddress</strong></p></td>
    <td align="left"><p>The address of the 802.11 station as encoded in the NIC hardware</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p><strong>CurrentMacAddress</strong></p></td>
    <td align="left"><p>The address that the 802.11 station is currently using, which can either be the permanent MAC address or a locally-administered MAC address set through a configuration parameter.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p><strong>AccessType</strong></p></td>
    <td align="left"><p><strong>NET_IF_ACCESS_BROADCAST</strong></p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p><strong>DirectionType</strong></p></td>
    <td align="left"><p><strong>NET_IF_DIRECTION_SENDRECEIVE</strong></p></td>
    </tr>
    <tr class="even">
    <td align="left"><p><strong>ConnectionType</strong></p></td>
    <td align="left"><p><strong>NET_IF_CONNECTION_DEDICATED</strong></p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p><strong>IfType</strong></p></td>
    <td align="left"><p><strong>IF_TYPE_IEEE80211</strong></p></td>
    </tr>
    <tr class="even">
    <td align="left"><p><strong>IfConnectorPresent</strong></p></td>
    <td align="left"><p>TRUE</p></td>
    </tr>
    </tbody>
    </table>

     

-   After calling [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) to provide NDIS with the general attributes of the miniport driver, call **NdisMSetMiniportAttributes** to provide NDIS with the Native 802.11l attributes of the miniport driver. In this situation, the *MiniportAttributes* parameter must be set to the address of a driver-allocated block of memory that is formatted as an [**NDIS\_MINIPORT\_ADAPTER\_NATIVE\_802\_11\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565926) structure.

-   Report **MediaConnectStateConnected** in the **MediaConnectState** member of [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923).

A Native 802.11 miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function must not do the following:

-   Connect to any basic service set (BSS) network.

-   Maintain encryption keys in permanent storage (disk, registry, flash, or other storage). During initialization, the miniport driver must clear any cipher keys that are used by the 802.11 station.

-   Report a status of **MediaConnectStateDisconnected** when indicating [**NDIS\_STATUS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567391) on any NDIS port.

 

 





