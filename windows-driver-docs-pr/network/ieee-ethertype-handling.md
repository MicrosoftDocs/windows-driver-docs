---
title: IEEE EtherType Handling
description: IEEE EtherType Handling
keywords:
- send operations WDK Native 802.11 IHV Extensions DLL
- receive operations WDK Native 802.11 IHV Extensions DLL
- IEEE EtherType handling WDK Native 802.11 IHV Extensions DLL
- EtherType handling WDK Native 802.11 IHV Extensions DLL
- privacy exceptions WDK Native 802.11 IHV Extensions DLL
- decryption WDK Native 802.11 IHV Extensions DLL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IEEE EtherType Handling




 

The IHV Extensions DLL can specify a list of IEEE EtherTypes for special handling of packets received by the wireless LAN (WLAN) adapter. The following types of EtherType handling can be specified.

<a href="" id="privacy-exemptions"></a>**Privacy Exemptions**  
The IHV Extensions DLL can specify packet decryption exemptions for received packets. For example, the DLL can specify that a packet with a specified EtherType is allowed to be received unencrypted even if a matching cipher key is configured on the WLAN adapter.

<a href="" id="ethertype-registration"></a>**EtherType Registration**  
The IHV Extensions DLL can register the EtherTypes that it will process and consume. The operating system forwards packets that match a registered EtherType to the DLL through calls to the [*Dot11ExtIhvReceivePacket*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_receive_packet) function.

The IHV Extensions DLL specifies EtherType handling through a call to the [**Dot11ExtSetEtherTypeHandling**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_ethertype_handling) function. When calling this function, the IHV Extensions DLL must follow these guidelines.

-   The IHV Extensions DLL can only call [**Dot11ExtSetEtherTypeHandling**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_ethertype_handling) any time prior to completing a pre-association operation. For more information about this operation, see [Pre-Association Operations](pre-association-operations.md).

-   The IHV Extensions DLL specifies its list of privacy exemptions through an array of zero or more [**DOT11\_PRIVACY\_EXEMPTION**](/windows-hardware/drivers/ddi/windot11/ns-windot11-dot11_privacy_exemption) structures. If the IHV Extensions DLL does not call [**Dot11ExtSetEtherTypeHandling**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_ethertype_handling), the operating system defaults to an empty list of privacy exemptions for any 802.11 association with an access point (AP).
    **Note**  For Windows Vista, the IHV Extensions DLL supports only infrastructure basic service set (BSS) networks.

     

-   The IHV Extensions DLL registers a list of zero or more EtherTypes that it will receive. Typically, the DLL registers the EtherTypes for the security packets it processes during the post-association operation. For more information about this operation, see [Post-Association Operations](post-association-operations.md).

    If the IHV Extensions DLL does not call [**Dot11ExtSetEtherTypeHandling**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_ethertype_handling), the operating system defaults to an empty list of registered EtherTypes for any 802.11 association with an AP.

-   After the IHV Extensions DLL completes the pre-association operation by calling [**Dot11ExtPreAssociateCompletion**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_pre_associate_completion), the list of privacy exemptions and EtherType registrations specified through a call to [**Dot11ExtSetEtherTypeHandling**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_ethertype_handling) is applied to every 802.11 association made by the WLAN adapter while connected to the basic service set (BSS) network.

-   The operating system clears the list of privacy exemptions and EtherType registrations before it calls [*Dot11ExtIhvAdapterReset*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_adapter_reset).

 

 
