---
title: RSNA Overview
description: RSNA Overview
ms.assetid: c14abe5c-d8fd-4f02-9ff4-2291f419230c
keywords:
- Robust Security Network Association WDK Native 802.11
- RSNA WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# RSNA Overview


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Robust Security Network Association (RSNA) authentication algorithm is defined in Clause 8.4 of the IEEE 802.11i-2004 standard.

If the 802.11 station supports RSNA, it must support the [AES-CCMP](aes-ccmp.md) cipher algorithm. Support for the [WEP](wep.md) and [TKIP](tkip.md) cipher algorithms are optional for RSNA.

TKIP or AES-CCMP cipher keys are derived through a mutual pairwise master key (PMK) that can be statically defined (preshared) on the 802.11 station or dynamically defined through the 802.1X port-based authentication algorithm. The PMK is verified between the 802.11 station and the access point (AP) or peer station during the association operation.

RSNA authentication consists of the following components:

<a href="" id="supplicant"></a>**Supplicant**  
802.1X defines the supplicant as "an entity at one end of a point-to-point LAN segment that is being authenticated by an authenticator attached to the other end of that link."

For RSNA, the supplicant is a service that is executing on the 802.11 station.

<a href="" id="authenticator"></a>**Authenticator**  
802.1X defines the authenticator as "an entity at one end of a point-to-point LAN segment that facilitates authentication of the entity attached to the other end of that link."

For RSNA, the authenticator is a service that is executing on the AP or peer station.

<a href="" id="authentication-server"></a>**Authentication Server**  
802.1X defines the authentication server as "an entity that provides the authenticator with an authentication service that determines, from the credentials provided by the supplicant, whether the supplicant is authorized to access the services provided by the authenticator."

For RSNA, the authentication server is typically a Remote Authentication Dial-In User Service (RADIUS) server that authenticates through the Extensible Authentication Protocol (EAP) suite of authentication algorithms.

For more information about the supplicant, authenticator, and authentication server, refer to the IEEE 802.1X-2001 standard.

RSNA consists of the following authentication algorithms:

<a href="" id="rsna"></a>RSNA  
When the RSNA algorithm is enabled, the 802.11 station associates only with an access point (AP) or peer station whose 802.11 Beacon or Probe Response frames contain the authentication suite of type 1 (802.1X) within the Robust Secure Network (RSN) information element (IE). For more information about the RSN IE, refer to Clause 7.3.2.25 of the IEEE 802.11i-2004 standard.

Authentication of the 802.11 station is performed between the supplicant, authenticator, and authentication server through the IEEE 802.1X port-based authentication protocol. The PMK is dynamically derived through the authentication process and verified through a four-way handshake between the supplicant and authenticator.

<a href="" id="rsna-with-preshared-keys--rsna-psk-"></a>RSNA with Preshared Keys (RSNA-PSK)  
When the RSNA PSK algorithm is enabled, the 802.11 station will associate only with an AP or peer station whose 802.11 Beacon or Probe Response frames contain the authentication suite of type 2 (preshared key) within the RSN IE.

Authentication of the 802.11 station is performed between the supplicant and authenticator. The PMK is defined through a mutual PSK configured on the supplicant and authenticator, and is verified through a four-way handshake between the supplicant and authenticator.

When authenticating using the RSNA suite of algorithms, the 802.11 station must do the following:

-   If the 802.11 station is operating in an infrastructure basic service set (BSS) network, first authenticate with the AP using the 802.11 Open System algorithm. For more information about this algorithm, see [Open System Authentication](open-system-authentication.md).

-   If the 802.11 station is operating in an independent BSS (IBSS) network, first authenticate with a peer station using either the 802.11 Open System algorithm or an algorithm defined by the independent hardware vendor (IHV).

The following points apply to a miniport driver operating in Extensible Station (ExtSTA) mode:

-   If port-based authentication is managed by the operating system, the 802.11 station must support the RSNA-PSK authentication algorithm for infrastructure networks.

    It is recommended that the 802.11 station support RSNA-PSK authentication for independent BSS (IBSS) networks. The operating system will only enable RSNA-PSK for IBSS networks if the [AES-CCMP](aes-ccmp.md) cipher suite is enabled.

-   If port-based authentication is managed by a service developed by the independent hardware vendor (IHV), the 802.11 station can support RSNA and RSNA-PSK as authentication algorithm extensions for any type of BSS network type, including independent BSS (IBSS) networks. For more information about authentication algorithm extensions, see [Extending Support for 802.11 Authentication Algorithms](extending-support-for-802-11-authentication-algorithms.md).

-   If the 802.11 station supports the RSNA authentication algorithm, it can support RSNA preauthentication through PMK identifiers (PMKIDs). In this situation, the 802.11 station maintains a PMKID cache large enough to store a minimum of three entries. The miniport driver reports the size of the PMKID cache when [OID\_DOT11\_EXTSTA\_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569366) is queried.

    For more information about RSNA preauthentication, see [RSNA Preauthentication](rsna-preauthentication.md).

 

 





