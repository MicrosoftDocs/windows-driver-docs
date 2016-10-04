---
title: Extending Support for 802.11 Authentication Algorithms
description: Extending Support for 802.11 Authentication Algorithms
ms.assetid: f9ea385d-26ae-4c14-870d-1ac23f89267b
keywords: ["extending functionality WDK Native 802.11", "Extensible Station authentication algorithms WDK Native 802.11", "ExtSTA authentication algorithms WDK Native 802.11", "algorithms WDK Native 802.11 authentication", "authentication WDK Native 802.11 , extending support", "authentication WDK Native 802.11 , algorithms"]
---

# Extending Support for 802.11 Authentication Algorithms


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The independent hardware vendor (IHV) can use the Extensible Station (ExtSTA) operation mode to extend the types of 802.11 authentication algorithms that are supported by the operating system. Through these extensions, the IHV can do the following:

-   Add support for proprietary or non-standard algorithms that are not supported by the operating system.

-   Replace support for standard algorithms that are supported by the operating system with algorithms that are developed by the IHV.

Windows Vista and later operating systems support the following 802.11 authentication algorithms:

-   IEEE 802.11 Open System algorithm.

-   IEEE 802.11 Shared Key algorithm.

-   Wi-Fi Protected Access (WPA) algorithm. This algorithm is supported only for infrastructure basic service set (BSS) networks.

-   WPA algorithm that uses preshared keys (PSK). This algorithm is supported only for infrastructure BSS networks.

-   IEEE 802.11i Robust Security Network Association (RSNA) algorithm. This algorithm is supported only for infrastructure BSS networks.

-   IEEE 802.11i RSNA algorithm that uses PSK. This algorithm is supported for infrastructure BSS networks. This algorithm is also supported for independent BSS (IBSS) networks when used in conjunction with the AES-CCMP cipher algorithm.

To extend this list for the support of proprietary or non-standard 802.11 authentication algorithms, the miniport driver must assign a unique value within the range of **DOT11\_AUTH\_ALGO\_IHV\_START** through **DOT11\_AUTH\_ALGO\_IHV\_END** for each proprietary authentication algorithm that is supported by the 802.11 station.

**Note**  The value assigned to a proprietary authentication algorithm is not a globally unique identifier (GUID). The same value can be used by different Native 802.11 miniport drivers that are developed by the IHV.

 

The miniport driver returns a list of supported authentication algorithms, including the supported proprietary algorithms, whenever the following Native 802.11 object identifiers (OIDs) are queried:

<a href="" id="--------oid-dot11-supported-unicast-algorithm-pair"></a>[OID\_DOT11\_SUPPORTED\_UNICAST\_ALGORITHM\_PAIR](https://msdn.microsoft.com/library/windows/hardware/ff569430)  
When this OID is queried, the driver returns the list of 802.11 authentication and cipher algorithms that the 802.11 station supports for unicast packets.

<a href="" id="--------oid-dot11-supported-multicast-algorithm-pair"></a>[OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR](https://msdn.microsoft.com/library/windows/hardware/ff569424)  
When this OID is queried, the driver returns the list of 802.11 authentication and cipher algorithms that the 802.11 station supports for multicast and broadcast packets.

<a href="" id="--------oid-dot11-enabled-authentication-algorithm"></a>[OID\_DOT11\_ENABLED\_AUTHENTICATION\_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569356)  
When this OID is queried, the driver returns the list of 802.11 authentication algorithms that are enabled on the 802.11 station when connecting to a basic service set (BSS) network.

For more information about 802.11 authentication by Native 802.11 miniport drivers, see [Native 802.11 Authentication Operations](native-802-11-authentication-operations.md).

 

 





