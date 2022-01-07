---
title: 802.11 WLAN Adapter Arrival
description: 802.11 WLAN Adapter Arrival
keywords:
- adapters WDK 802.11 WLAN , arrivals
- WLAN adapters WDK , arrivals
ms.date: 04/20/2017
---

# 802.11 WLAN Adapter Arrival




 

When the operating system detects a wireless LAN (WLAN) adapter for which an IHV Extensions DLL has been installed, the operating system calls the [*Dot11ExtIhvInitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_adapter) IHV Handler function. The operating system calls this function whenever a WLAN adapter becomes available and enabled for use, such as when a PCMCIA adapter is inserted.

When the [*Dot11ExtIhvInitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_adapter) function is called, the IHV Extensions DLL does the following:

-   Allocates an array for the WLAN adapter context data, as well as any resources the DLL needs for the WLAN adapter.

-   Registers a list of IEEE EtherTypes for the security packets received and consumed by the IHV Extensions DLL.

-   Configures the adapter with any proprietary settings defined by the IHV.

The IHV Extensions DLL must follow these guidelines when [*Dot11ExtIhvInitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_adapter) is called.

-   The *hDot11SvcHandle* parameter contains a unique handle value assigned by the operating system for the WLAN adapter. The IHV Extensions DLL must save this handle value and pass it to the *hDot11SvcHandle* parameter of the IHV Extensibility functions related to the adapter-specific processing, such as [**Dot11ExtSetKeyMappingKey**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_key_mapping_key).

    Typically, the DLL saves this handle value within a member of its WLAN adapter context array.

-   The IHV Extensions DLL must return a unique handle value for the WLAN adapter through the *phIhvExtAdapter* parameter. The operating system passes the handle value to the *hIhvExtAdapter* parameter of the IHV Handler functions related to the adapter-specific processing, such as [*Dot11ExtIhvReceiveIndication*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_receive_indication).

    Typically, the DLL returns the address of the WLAN adapter context array as the handle value.

-   The IHV Extensions DLL calls [**Dot11ExtSetEtherTypeHandling**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_ethertype_handling) to register a list of the IEEE EtherTypes for the security packets that the DLL will receive. The IHV Extensions DLL can also specify a list of EtherTypes that will be excluded from payload decryption. For more information about registering EtherTypes, see [IEEE EtherType Handling](ieee-ethertype-handling.md).

    After EtherTypes are registered, the operating system calls the [*Dot11ExtIhvReceivePacket*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_receive_packet) IHV Handler function for every packet whose EtherType matches an entry in the list.

-   The operating system configures the adapter with standard 802.11 parameters through set requests of the Native 802.11 object identifiers (OIDs). For more information about these OIDs, see [Native 802.11 Wireless LAN OIDs](/previous-versions/windows/hardware/wireless/native-802-11-oids).

    However, the DLL can configure the adapter with proprietary parameters through calls to the [**Dot11ExtNicSpecificExtension**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_nic_specific_extension) function. Through this function call, the DLL can communicate directly with the Native 802.11 miniport driver that manages the WLAN adapter and issue query or set requests to the driver based on a proprietary format defined by the IHV.

    For more information about the interface through which the DLL and WLAN adapter communicate, see [802.11 WLAN Adapter Communication Channel](802-11-wlan-adapter-communication-channel.md).

 

 
