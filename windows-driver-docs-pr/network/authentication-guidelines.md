---
title: Authentication Guidelines
description: Authentication Guidelines
ms.assetid: 0ede519c-c06d-4711-9e36-84c9e43d7bd4
keywords:
- algorithms WDK Native 802.11 authentication
- authentication WDK Native 802.11 , guidelines
- Robust Security Network Association WDK Native 802.11
- RSNA WDK Native 802.11
- Wi-Fi Protected Access WDK Native 802.11
- WPA WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Authentication Guidelines


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Before authenticating to a basic service set (BSS) network, the 802.11 station must have followed the guidelines discussed in [Connection Operations](connection-operations.md) to select the BSS. In particular, the 802.11 station must have selected a BSS that best matches its enabled authentication and cipher algorithms.

The 802.11 station determines the authentication and cipher algorithms it uses for the authentication operation from the intersection of the following:

-   The authentication algorithms enabled on the 802.11 station.

-   The authentication algorithms advertised in the 802.11 Beacon or Probe Response frames sent by the access point (AP) or peer station.

The 802.11 station must select the most secure authentication and cipher algorithms from this intersection. The following list defines the authentication algorithms supported for infrastructure BSS networks sorted by security preferences. For more information about these authentication algorithms, see [**DOT11\_AUTH\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/ff547655).

-   **DOT11\_AUTH\_ALGO\_RSNA**(most secure)

-   **DOT11\_AUTH\_ALGO\_RSNA\_PSK**

-   **DOT11\_AUTH\_ALGO\_WPA**

-   **DOT11\_AUTH\_ALGO\_WPA\_PSK**

-   **DOT11\_AUTH\_ALGO\_80211\_OPEN**

-   **DOT11\_AUTH\_ALGO\_80211\_SHARED\_KEY**(least secure)

The following list, sorted by security preferences, defines the authentication algorithms supported for independent BSS (IBSS) networks.

-   **DOT11\_AUTH\_ALGO\_RSNA\_PSK**(most secure)

-   **DOT11\_AUTH\_ALGO\_80211\_OPEN**

-   **DOT11\_AUTH\_ALGO\_80211\_SHARED\_KEY**(least secure)

**Note**  The 802.11 station is required to support the **DOT11\_AUTH\_ALGO\_RSNA\_PSK** authentication algorithm and **DOT11\_CIPHER\_ALGO\_CCMP** cipher algorithm for IBSS networks. The operating system only enables **DOT11\_AUTH\_ALGO\_RSNA\_PSK** for an IBSS network if the **DOT11\_CIPHER\_ALGO\_CCMP** cipher algorithm is supported within the IBSS network.

 

The following list, sorted by security preferences, defines the cipher algorithms. For more information about these cipher algorithms, see [**DOT11\_CIPHER\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/ff547672).

-   **DOT11\_CIPHER\_ALGO\_CCMP**(most secure)

-   **DOT11\_CIPHER\_ALGO\_TKIP**

-   **DOT11\_CIPHER\_ALGO\_WEP**

-   **DOT11\_CIPHER\_ALGO\_WEP104**

-   **DOT11\_CIPHER\_ALGO\_WEP40**

-   **DOT11\_CIPHER\_ALGO\_NONE**(least secure)

**Note**  The operating system only enables **DOT11\_CIPHER\_ALGO\_WEP** if the **DOT11\_AUTH\_ALGO\_80211\_OPEN** or **DOT11\_AUTH\_ALGO\_80211\_SHARED\_KEY** authentication algorithms have been enabled. For more information about how cipher algorithms are enabled, see [Enabling Cipher Algorithms](enabling-cipher-algorithms.md).

 

**Note**  Beginning with Windows 7, an 802.11 miniport driver can report any combination of supported authentication and cipher algorithm pairs in the [**DOT11\_AUTH\_CIPHER\_PAIR\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff547662) structure. However, if the operating system starts Soft AP, it enables only the **DOT11\_AUTH\_ALGO\_RSNA\_PSK** authentication algorithm and the **DOT11\_CIPHER\_ALGO\_CCMP** cipher algorithm. To support Soft AP, the miniport driver must support this authentication/cipher pair.
If WPS is enabled on a NIC that is operating in Extensible AP mode, the miniport driver must allow peer stations to associate with the Extensible AP by using [Open System Authentication](open-system-authentication.md) or [Wired Equivalent Privacy (WEP)](wep.md) algorithms, regardless of the enabled authorization and cipher algorithms. For more information about WPS and Extensible AP, see [OID\_DOT11\_WPS\_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569436).

 

The independent hardware vendor (IHV) can rank its proprietary or non-standard authentication and cipher algorithms in any way it wants. For more information about this, see [Extending Support for 802.11 Authentication Algorithms](extending-support-for-802-11-authentication-algorithms.md) and [Extending Support for 802.11 Cipher Algorithms](extending-support-for-802-11-cipher-algorithms.md).

If the miniport driver's current packet filter enables NDIS\_PACKET\_TYPE\_802\_11\_DIRECTED\_MGMT, it must indicate all 802.11 management packets received during the authentication operation. For more information about this packet filter, see [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).

If the 802.11 station selects an authentication algorithm from either the Robust Security Network Association (RSNA) or Wi-Fi Protected Access (WPA) suite, it must follow these guidelines:

-   The 802.11 station starts the authentication operation without a cipher key defined for packet encryption or decryption. The 802.11 must initially transmit all packets unencrypted.

-   If the 802.11 station is operating in an infrastructure BSS network, the station must first authenticate with the AP using the Open System authentication algorithm. For more information about this algorithm, see [Open System Authentication](open-system-authentication.md).

-   If the 802.11 station is operating in an independent BSS (IBSS) network, the station must first authenticate with a peer station using either the 802.11 Open System algorithm or an algorithm defined by the independent hardware vendor (IHV).

-   If the authentication algorithm is RSNA or WPA, the 802.1X port-based authentication must complete in order for a pairwise master key (PMK) to be derived by the supplicant.

    If the authentication algorithm is RSNA-PSK or WPA-PSK, the supplicant uses the preshared key (PSK) as the PMK.

-   The supplicant and authenticator verify the PMK through the four-way handshake. For the WPA suite, the four-way handshake is described in Section 2.2.5.4.2 of the *WPA* specification. For the RSNA suite, the four-way handshake is described in Clause 8.5.3 of the IEEE 802.11i-2004 standard.

    After the four-way handshake completes successfully, the supplicant derives a pairwise key for cipher operations, and downloads the key to the 802.11 station through a set request of [OID\_DOT11\_CIPHER\_DEFAULT\_KEY](https://msdn.microsoft.com/library/windows/hardware/ff569119). Following the set request, the 802.11 station must encrypt all transmitted packets.

-   The supplicant and authenticator derive a group key through the group key handshake. This handshake can occur periodically while the 802.11 station is associated with the AP or peer station.

    For the WPA suite, the four-way handshake is described in Section 2.2.5.4.3 of the *WPA* specification. For the RSNA suite, the four-way handshake is described in Clause 8.5.4 of the IEEE 802.11i-2004 standard.

For more information about pairwise and group keys, see [AES-CCMP](aes-ccmp.md) or [TKIP](tkip.md). For more information about the supplicant and authenticator, see [WPA](wpa.md) or [RSNA](rsna.md).

After the authentication operation completes, the 802.11 station can complete the association operation that initiated the authentication operation. For more information about the association operation, see [Association Operations](association-operations.md).

 

 





