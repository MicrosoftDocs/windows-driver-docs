---
title: Extending Support for 802.11 PHY Configurations
description: Extending Support for 802.11 PHY Configurations
ms.assetid: 91c216e9-c6eb-4a4e-801e-dc805d37eb0b
keywords:
- extending functionality WDK Native 802.11
- Extensible Station PHY configuration WDK Native 802.11
- ExtSTA PHY configuration WDK Native 802.11
- PHY configuration WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Extending Support for 802.11 PHY Configurations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

An independent hardware vendor (IHV) can use the Extensible Station (ExtSTA) operation mode to extend the support for 802.11 PHY types to include proprietary or non-standard PHY types provided by the IHV.

The IHV can also use the ExtSTA operation mode to support 802.11 network interface cards (NICs) that have two or more PHYs. These PHYs can be the same or different PHY types.

Windows Vista and later operating systems support the following PHY types:

-   Frequency-hopping spread-spectrum (FHSS) PHY.

-   Direct sequence spread spectrum (DSSS) PHY.

-   Infrared (IR) baseband PHY.

-   Orthogonal frequency division multiplexing (OFDM) PHY.

-   High-rate DSSS (HRDSSS) PHY.

-   Extended rate PHY (ERP).

To extend this list with proprietary PHY types, the miniport driver must do the following:

-   Assign a unique value to each proprietary PHY type that is supported by the 802.11 NIC. The value must be within the range of **dot11\_phy\_type\_IHV\_start** through dot11\_phy\_type\_IHV\_end.

    **Note**  The value assigned to a proprietary PHY type is not a globally unique identifier (GUID). Therefore, the same value can be used in miniport drivers for different classes of 802.11 NICs that are supported by the IHV.

     

-   When [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](https://msdn.microsoft.com/library/windows/hardware/ff569426) is queried, return a DOT11\_SUPPORTED\_PHY\_TYPES structure that specifies the list of PHY types on the 802.11 NIC. The **dot11PhyType** member defines this list, which includes both standard and proprietary 802.11 PHY types.

    If the NIC has more than one PHY of the same type, the miniport driver must add a PHY type value to the **dot11PhyType** member for each instance of the PHY on the NIC.

    **Note**  The driver must return the PHY types in the same order within the **dot11PhyType** member on each query of [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](https://msdn.microsoft.com/library/windows/hardware/ff569426).

     

After the miniport driver returns its list of PHY types through a query of [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](https://msdn.microsoft.com/library/windows/hardware/ff569426), the operating system and the driver use a PHY identifier (ID) to specify a PHY type on the NIC. The PHY ID is the index of a PHY type value within the returned **dot11PhyType** member. A PHY ID of 0xFFFFFFFFF is a wildcard value that is used to specify any PHY type on the 802.11 NIC.

The operating system will set or query the configuration of a single PHY on the 802.11 NIC. This PHY is referenced through the ExtSTA **msDot11CurrentPhyId** management information base (MIB) object. For example, PHY attributes that are configured through Native 802.11 MIB objects, such as [OID\_DOT11\_CURRENT\_FREQUENCY](https://msdn.microsoft.com/library/windows/hardware/ff569130) or [OID\_DOT11\_CURRENT\_CHANNEL](https://msdn.microsoft.com/library/windows/hardware/ff569127), are issued to the PHY with the PHY ID specified by this MIB object. The **msDot11CurrentPhyId** MIB object is set or queried through [OID\_DOT11\_CURRENT\_PHY\_ID](https://msdn.microsoft.com/library/windows/hardware/ff569135).

The operating system uses a list of one or more PHY IDs when requesting:

-   A scan operation through an OID set request of [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413).

    When this OID is set, the 802.11 station performs the scan operation using the list of PHY IDs specified in the [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure that accompanies the set request.

    When [OID\_DOT11\_ENUM\_BSS\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569360) is queried, the miniport driver returns the list of BSS networks that the 802.11 station detected during the most recent scan operation. The miniport driver specifies each BSS network through a DOT11\_BSS\_ENTRY structure, which includes the PHY ID that the 802.11 station used to detect the basic service set (BSS) network.

    For more information about scan operations, see [Native 802.11 Scan Operations](native-802-11-scan-operations.md).

-   A connection operation through an OID set request of [OID\_DOT11\_CONNECT\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569122).

    Prior to the set request of this OID, the operating system will specify the PHY types used in the connection attempt through a set of [OID\_DOT11\_DESIRED\_PHY\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569144).

    When the connection operation completes, the list of PHY types that the 802.11 station uses on the BSS network is referenced through the ExtSTA **msDot11ActivePhyList** MIB object. The miniport driver returns this MIB object when [OID\_DOT11\_ACTIVE\_PHY\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569102) is queried.

    For more information about connection operations, see [Connection Operations](connection-operations.md).

 

 





