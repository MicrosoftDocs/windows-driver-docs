---
title: WPA
description: WPA
ms.assetid: 21d44181-3a95-40bc-b132-ef92bbc468ec
keywords: ["Wi-Fi Protected Access WDK Native 802.11", "WPA WDK Native 802.11", "authentication WDK Native 802.11 , WPA"]
---

# WPA


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Wi-Fi Protected Access (WPA) authentication algorithm is defined in Section 2 of the *WPA* specification.

If the 802.11 station supports WPA, it must support the [TKIP](tkip.md) cipher algorithm. Support for the [WEP](wep.md) and [AES-CCMP](aes-ccmp.md) cipher algorithms are optional for WPA.

TKIP or AES-CCMP cipher keys are derived through a mutual pairwise master key (PMK) that can be statically defined (preshared) on the 802.11 station or dynamically defined through a port-based authentication algorithm, such as IEEE 802.1X. The PMK is verified between the 802.11 station and the access point (AP) or peer station during the association operation.

WPA authentication consists of the following components:

<a href="" id="supplicant"></a>**Supplicant**  
802.1X defines the supplicant as "an entity at one end of a point-to-point LAN segment that is being authenticated by an authenticator attached to the other end of that link."

For WPA, the supplicant is a service that is executing on the 802.11 station.

<a href="" id="authenticator"></a>**Authenticator**  
802.1X defines the authenticator as "an entity at one end of a point-to-point LAN segment that facilitates authentication of the entity attached to the other end of that link."

For WPA, the authenticator is a service that is executing on the AP or peer station.

<a href="" id="authentication-server-------"></a>**Authentication Server**   
802.1X defines the authentication server as "an entity that provides the authenticator with an authentication service that determines, from the credentials provided by the supplicant, whether the supplicant is authorized to access the services provided by the authenticator."

For WPA, the authentication server is typically a Remote Access Dial-In User Service (RADIUS) server that authenticates through the Extensible Authentication Protocol (EAP) suite of algorithms.

For more information about the supplicant, authenticator, and authenticator server, refer to the IEEE 802.1X-2001 standard.

WPA consists of the following authentication algorithms:

<a href="" id="wpa"></a>WPA  
When the WPA algorithm is enabled, the 802.11 station associates only with an access point (AP) or peer station whose 802.11 Beacon or Probe Response frames contain the authentication suite of type 1 (802.1X) within the WPA information element (IE). For more information about the WPA IE, refer to Section 2.1 of the *WPA* specification.

Authentication of the 802.11 station is performed between the supplicant, authenticator, and authentication server through the IEEE 802.1X port-based authentication protocol. The PMK is dynamically derived through the authentication process and verified through a four-way handshake between the supplicant and authenticator.

<a href="" id="wpa-with-preshared-keys--wpa-psk-"></a>WPA with Preshared Keys (WPA-PSK)  
When the WPA PSK algorithm is enabled, the 802.11 station associates only with an AP or peer station whose 802.11 Beacon or Probe Response frames contain the authentication suite of type 2 (preshared key) within the WPA IE.

Authentication of the 802.11 station is performed between the supplicant and authenticator. The PMK is defined through a mutual PSK configured on the supplicant and authenticator, and is verified through a four-way handshake between the supplicant and authenticator.

When authenticating using the WPA suite of algorithms, the 802.11 station must do the following:

-   If the 802.11 station is operating in an infrastructure basic service set (BSS) network, first authenticate with the AP using the 802.11 Open System algorithm. For more information about this algorithm, see [Open System Authentication](open-system-authentication.md).

-   If the 802.11 station is operating in an independent BSS (IBSS) network, the station must first authenticate with a peer station using either the 802.11 Open System algorithm or an algorithm defined by the independent hardware vendor (IHV).

The following points apply to a miniport driver operating in Extensible Station (ExtSTA) mode:

-   If port-based authentication is managed by the operating system, the 802.11 station supports the WPA and WPA-PSK authentication algorithms only for infrastructure basic service set (BSS) networks.

-   If port-based authentication is managed by a service developed by the independent hardware vendor (IHV), the 802.11 station can support WPA and WPA-PSK as authentication algorithm extensions for any type of BSS network type, including independent BSS (IBSS) networks. For more information about authentication algorithm extensions, see [Extending Support for 802.11 Authentication Algorithms](extending-support-for-802-11-authentication-algorithms.md).

 

 





