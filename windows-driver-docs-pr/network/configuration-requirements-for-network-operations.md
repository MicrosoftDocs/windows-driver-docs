---
title: Configuration Requirements for Network Operations
description: Configuration Requirements for Network Operations
ms.assetid: 6f3fd054-4a4c-40bd-8e0b-0329df78c95c
keywords: ["network operations WDK Native 802.11 , configuration requirements", "BSS networks WDK Native 802.11"]
---

# Configuration Requirements for Network Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The 802.11 station must have previously been configured for network operations within a basic service set (BSS) network. For more information about this process, see [Configuration through a Network Profile](configuration-through-a-network-profile.md).

At the very least, the 802.11 station must have the following configured before it can perform any network operations:

<a href="" id="desired-bss-type"></a>Desired BSS Type  
The desired BSS type specifies whether the 802.11 station will associate with an access point (AP) within an infrastructure BSS or peer stations within an independent BSS (IBSS) network. The desired BSS type is configured through a set request of [OID\_DOT11\_DESIRED\_BSS\_TYPE](https://msdn.microsoft.com/library/windows/hardware/ff569142).

**Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

 

<a href="" id="desired-service-set-identifier--ssid--list"></a>Desired Service Set Identifier (SSID) List  
The desired SSID list specifies zero or more BSS networks with which the 802.11 station will attempt to connect. This list is configured through a set request of [OID\_DOT11\_DESIRED\_SSID\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569145).

<a href="" id="desired-bss-identifier--bssid--list"></a>Desired BSS Identifier (BSSID) List  
The desired BSSID list specifies zero or more BSSIDs of APs or peer stations with which the 802.11 station can connect or roam. If the desired BSSID list contains zero entries, the 802.11 station cannot connect to any BSS network. This list is configured through a set request of [OID\_DOT11\_DESIRED\_BSSID\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569141).

**Note**  Depending upon the network profile, the operating system might leave the 802.11 station's desired BSSID list in its default setting. The default BSSID list contains only the wildcard BSSID of 0xFFFFFFFFFFFF.

 

<a href="" id="desired-country-or-region-string"></a>Desired Country or Region String  
The desired country or region string specifies the regulatory domain that the 802.11 uses when it starts a new independent BSS (IBSS) network.

**Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

 

After it starts the IBSS network, the 802.11 station advertises the regulatory domain by setting the IEEE 802.11d Country or Region information element (IE) within the 802.11 Beacon and Probe Response frames that it sends. The desired country or region string is configured through a set request of [OID\_DOT11\_DESIRED\_COUNTRY\_OR\_REGION\_STRING](https://msdn.microsoft.com/library/windows/hardware/ff569143).

**Note**  If the 802.11 station connects to an existing infrastructure or IBSS network, the station resolves the regulatory domain through the Country IE of the received Beacon or Probe Response frames. In this situation, the 802.11 station does not use the desired country or region string.

 

<a href="" id="desired-phy-list"></a>Desired PHY List  
The desired PHY list specifies the PHYs on the 802.11 station that can be used for operations within a BSS network. This list is configured through a set request of [OID\_DOT11\_DESIRED\_PHY\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569144).

<a href="" id="ibss-network-parameters"></a>IBSS Network Parameters  
If configured to operate within an IBSS network, additional parameters for IBSS network operations are specified through a set request of [OID\_DOT11\_IBSS\_PARAMS](https://msdn.microsoft.com/library/windows/hardware/ff569378).

**Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

 

<a href="" id="enabled-authentication-algorithms"></a>Enabled Authentication Algorithms  
When connecting to or roaming within a BSS network, the 802.11 station will associate with the AP or peer station only if there is a match between the 802.11 station's enabled authentication algorithms and the authentication algorithms supported by the AP or peer station. The AP or peer station specifies the authentication algorithms it supports within its 802.11 Beacon and Probe Response frames.

During the association operation, the 802.11 station authenticates with the AP or peer station using an authentication algorithm from the intersection of its enabled algorithms and the authentication algorithms supported by the AP or peer station.

Authentication algorithms are enabled on the 802.11 station through a set request of [OID\_DOT11\_ENABLED\_AUTHENTICATION\_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569356).

<a href="" id="enabled-cipher-algorithms"></a>Enabled Cipher Algorithms  
When connecting to or roaming within a BSS network, the 802.11 station will associate with the AP or peer station only if there is a match between the 802.11 station's enabled cipher algorithms and the cipher algorithms supported by the AP or peer station. The AP or peer station specifies the cipher algorithms it supports within its 802.11 Beacon and Probe Response frames.

Cipher algorithms are enabled on the 802.11 station through set requests of [OID\_DOT11\_ENABLED\_UNICAST\_CIPHER\_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569358) and [OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569357).

 

 





