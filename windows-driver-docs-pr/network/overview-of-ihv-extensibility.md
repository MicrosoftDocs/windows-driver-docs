---
title: Overview of IHV Extensibility
description: Overview of IHV Extensibility
ms.assetid: 446d91e9-3497-4b45-82a6-7f36dd136e08
keywords: ["IHV extensions WDK Native 802.11 , about IHV extensibility", "Native 802.11 IHV Extensions WDK , about IHV extensibility"]
---

# Overview of IHV Extensibility


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Native 802.11 framework provides support for an independent hardware vendor (IHV) to add functionality to the Native 802.11 framework.

For example, the IHV can provide support for any of the following:

-   Proprietary or non-standard authentication algorithms for port-based network access. For more information, see [Extending Support for 802.11 Authentication Algorithms](extending-support-for-802-11-authentication-algorithms.md).

-   Proprietary or non-standard cipher algorithms for data encryption. For more information, see [Extending Support for 802.11 Cipher Algorithms](extending-support-for-802-11-cipher-algorithms.md).

-   Proprietary PHY configurations. For more information, see [Extending Support for 802.11 PHY Configurations](extending-support-for-802-11-phy-configurations.md).

In order to extend the Native 802.11 functionality, the IHV must provide the following components:

-   A Native 802.11 miniport driver that supports the Extensible Station (ExtSTA) operation mode. For more information about this mode, see [Extensible Station Operation Mode](extensible-station-operation-mode.md). For more information about ways the ExtSTA operation mode can extend Native 802.11 functionality, see [Extending Native 802.11 Functionality](extending-native-802-11-functionality.md).

-   An IHV Extensions DLL, which processes the security packets exchanged through the proprietary authentication algorithms that the IHV supports. The IHV Extensions DLL is also responsible for cipher key derivation through these authentication algorithms, as well as the validation of user data that pertains to the security extensions supported by the IHV.

    For more information about the IHV Extensions DLL, see [Native 802.11 IHV Extensions DLL](https://msdn.microsoft.com/library/windows/hardware/ff560614).

-   An IHV User Interface (UI) Extensions DLL, which extends the Native 802.11 user interface to configure connectivity and security settings that are validated and processed by the IHV Extensions DLL.

    For more information about the IHV UI Extensions DLL, see [Native 802.11 IHV UI Extensions DLL](https://msdn.microsoft.com/library/windows/hardware/ff560635).

For more information about the modules provided by the IHV, see [Native 802.11 Software Architecture](native-802-11-software-architecture.md).

To provide a secure execution environment, the IHV should do the following:

1.  Do not log any sensitive information, such as encryption keys, in event or debug logs.

2.  Use [CryptProtectMemory](http://go.microsoft.com/fwlink/p/?linkid=64677) to protect sensitive encryption keys stored in memory, and [SecureZeroMemory](http://go.microsoft.com/fwlink/p/?linkid=64678) to clear memory when done with the keys.

3.  Treat the IHV extension portions of the [network profile](configuration-through-a-network-profile.md) as untrusted data that may have been manipulated by an attacker. IHV extension portions of profiles are opaque to the 802.11 Auto Configuration Module (ACM) and Media Specific Module (MSM) and will not be validated. (See [Native 802.11 Software Architecture](native-802-11-software-architecture.md) for descriptions of these modules and configuration control paths.) This IHV extension data should be appropriately parsed to prevent any buffer overflows or attacks that could lead to a local escalation of privileges.

 

 





