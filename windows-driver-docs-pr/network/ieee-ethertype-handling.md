---
title: IEEE EtherType Handling
description: IEEE EtherType Handling
ms.assetid: ddd7244b-05a0-4ee8-b9aa-300015fbe3bd
keywords: ["send operations WDK Native 802.11 IHV Extensions DLL", "receive operations WDK Native 802.11 IHV Extensions DLL", "IEEE EtherType handling WDK Native 802.11 IHV Extensions DLL", "EtherType handling WDK Native 802.11 IHV Extensions DLL", "privacy exceptions WDK Native 802.11 IHV Extensions DLL", "decryption WDK Native 802.11 IHV Extensions DLL"]
---

# IEEE EtherType Handling


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The IHV Extensions DLL can specify a list of IEEE EtherTypes for special handling of packets received by the wireless LAN (WLAN) adapter. The following types of EtherType handling can be specified.

<a href="" id="privacy-exemptions"></a>**Privacy Exemptions**  
The IHV Extensions DLL can specify packet decryption exemptions for received packets. For example, the DLL can specify that a packet with a specified EtherType is allowed to be received unencrypted even if a matching cipher key is configured on the WLAN adapter.

<a href="" id="ethertype-registration"></a>**EtherType Registration**  
The IHV Extensions DLL can register the EtherTypes that it will process and consume. The operating system forwards packets that match a registered EtherType to the DLL through calls to the [*Dot11ExtIhvReceivePacket*](https://msdn.microsoft.com/library/windows/hardware/ff547513) function.

The IHV Extensions DLL specifies EtherType handling through a call to the [**Dot11ExtSetEtherTypeHandling**](https://msdn.microsoft.com/library/windows/hardware/ff547587) function. When calling this function, the IHV Extensions DLL must follow these guidelines.

-   The IHV Extensions DLL can only call [**Dot11ExtSetEtherTypeHandling**](https://msdn.microsoft.com/library/windows/hardware/ff547587) any time prior to completing a pre-association operation. For more information about this operation, see [Pre-Association Operations](pre-association-operations.md).

-   The IHV Extensions DLL specifies its list of privacy exemptions through an array of zero or more [**DOT11\_PRIVACY\_EXEMPTION**](https://msdn.microsoft.com/library/windows/hardware/ff548756) structures. If the IHV Extensions DLL does not call [**Dot11ExtSetEtherTypeHandling**](https://msdn.microsoft.com/library/windows/hardware/ff547587), the operating system defaults to an empty list of privacy exemptions for any 802.11 association with an access point (AP).
    **Note**  For Windows Vista, the IHV Extensions DLL supports only infrastructure basic service set (BSS) networks.

     

-   The IHV Extensions DLL registers a list of zero or more EtherTypes that it will receive. Typically, the DLL registers the EtherTypes for the security packets it processes during the post-association operation. For more information about this operation, see [Post-Association Operations](post-association-operations.md).

    If the IHV Extensions DLL does not call [**Dot11ExtSetEtherTypeHandling**](https://msdn.microsoft.com/library/windows/hardware/ff547587), the operating system defaults to an empty list of registered EtherTypes for any 802.11 association with an AP.

-   After the IHV Extensions DLL completes the pre-association operation by calling [**Dot11ExtPreAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547538), the list of privacy exemptions and EtherType registrations specified through a call to [**Dot11ExtSetEtherTypeHandling**](https://msdn.microsoft.com/library/windows/hardware/ff547587) is applied to every 802.11 association made by the WLAN adapter while connected to the basic service set (BSS) network.

-   The operating system clears the list of privacy exemptions and EtherType registrations before it calls [*Dot11ExtIhvAdapterReset*](https://msdn.microsoft.com/library/windows/hardware/ff547434).

 

 





