---
title: Native 802.11 IHV Extensibility functions
description: This section describes Native 802.11 IHV Extensibility functions for the Native 802.11 IHV Extensions DLL
keywords: ["Native 802.11 IVH Extensibility functions", "Native 802.11 IHV Extensions DLL Extensibility Functions", "WDK Native 802.11 IVH Extensibility functions"]
ms.date: 04/27/2017
---

# Native 802.11 IHV Extensibility functions

> [!IMPORTANT]
> The [Native 802.11 Wireless LAN](/previous-versions/windows/hardware/wireless/native-802-11-wireless-lan4) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](./wdi-miniport-driver-design-guide.md).

The Native 802.11 IHV Extensibility functions are provided by the operating system and are called by the IHV Extensions DLL to do the following:

- Allocate and free buffers that are used within the Native 802.11 framework.
- Send packets, such as a packet defined by an authentication algorithm, through the IHV's wireless LAN (WLAN) adapter.
- Configure the IHV's WLAN adapter with various security settings for any authentication and cipher algorithms supported by the IHV Extensions DLL.
- Interface with the IHV UI Extensions DLL (if installed) to process event notifications. For example, the IHV Extensions DLL could notify the IHV UI Extensions DLL about the various stages involved in a basic service set (BSS) network connection. 

For more information about the IHV UI Extensions DLL, see [Native 802.11 IHV UI Extensions DLL](native-802-11-ihv-ui-extensions-dll2.md).

> [!NOTE]
> The IHV Extensions DLL calls each Native 802.11 IHV Extensibility function through a function pointer associated with a member of the [DOT11EXT_APIS](/windows-hardware/drivers/ddi/wlanihv/ns-wlanihv-_dot11ext_apis) structure. When the operating system calls the [Dot11ExtIhvInitService](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_service) IHV Handler function, it passes the list of pointers to the IHV Extensibility functions through the *pDot11ExtAPI* parameter.
 
The following table lists the Native 802.11 IHV Extensibility Functions that can be called by the IHV Extensions DLL. Each IHV Extensibility function can only be called under these conditions.


- **Called After Service Initialization**  
The IHV Extensibility function can only be called after the [Dot11ExtIhvInitService](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_service) IHV Handler function has been called to initialize the IHV Extensions DLL. Also, the Extensions DLL cannot call the IHV Extensibility function after the [Dot11ExtIhvDeinitService](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_service) IHV Handler function has been called.
- **Called after Adapter Initialization**  
The IHV Extensibility function can only be called after the [Dot11ExtIhvInitAdapter](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_adapter) IHV Handler function has been called to initialize the interface to the IHV's WLAN adapter.  
The IHV Extensibility function requires a handle, which identifies the WLAN adapter. When *Dot11ExtIhvInitAdapter* is called, the IHV Extensions DLL is passed this handle through the *hDot11SvcHandle* parameter.  
The Extensions DLL cannot call the IHV Extensibility function after the [Dot11ExtIhvDeinitAdapter](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_adapter) IHV Handler function has been called.
- **Called after Pre-Association**  
The IHV Extensibility function can only be called after the [Dot11ExtIhvPerformPreAssociate](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_pre_associate) IHV Handler function has been called to initiate a pre-association operation with a basic service set (BSS) network.  
The IHV Extensibility function requires a handle, which identifies the BSS network connection. When *Dot11ExtIhvPerformPreAssociate* is called, the IHV Extensions DLL is passed this handle through the *hConnection* parameter.  
The Extensions DLL cannot call the IHV Extensibility function after the [Dot11ExtIhvDeinitAdapter](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_adapter) or [Dot11ExtIhvAdapterReset](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_adapter_reset) IHV Handler functions have been called.
- **Called after Post-Association**  
The IHV Extensibility function can only be called after the [Dot11ExtIhvPerformPostAssociate](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_post_associate) IHV Handler function has been called to initiate a post-association operation with a basic service set (BSS) network.  
The IHV Extensibility function requires a handle, which identifies the security session with the BSS network connection. When *Dot11ExtIhvPerformPostAssociate* is called, the IHV Extensions DLL is passed this handle through the *hSecuritySessionID* parameter.  
The Extensions DLL cannot call the IHV Extensibility function after the [Dot11ExtIhvDeinitAdapter](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_adapter) or [Dot11ExtIhvAdapterReset](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_adapter_reset) IHV Handler functions have been called.

| Function | Called after service initialization | Called after adapter initialization | Called after pre-association | Called after post-association |
| --- | --- | --- | --- | --- |
| [Dot11ExtAllocateBuffer](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_allocate_buffer) | X |   |   |   |
| [Dot11ExtFreeBuffer](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_free_buffer) | X |   |   |   |
| [Dot11ExtGetProfileCustomUserData](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_get_profile_custom_user_data) |   |   | X |   | 
| [Dot11ExtNicSpecificExtension](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_nic_specific_extension) |   | X |   |   |
| [Dot11ExtStartOneX](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_onex_start) |   |   |   | X |
| [Dot11ExtStopOneX](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_onex_stop) |   |   |   | X |
| [Dot11ExtPostAssociateCompletion](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_post_associate_completion) |   |   |   | X |
| [Dot11ExtPreAssociateCompletion](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_pre_associate_completion) |   |   | X |   |
| [Dot11ExtProcessOneXPacket](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_process_onex_packet) |   |   |   | X |
| [Dot11ExtQueryVirtualStationProperties](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_query_virtual_station_properties) |   | X |   |   |
| [Dot11ExtReleaseVirtualStation](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_release_virtual_station) |   | X |   |   |
| [Dot11ExtRequestVirtualStation](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_request_virtual_station) |   | X |   |   |
| [Dot11ExtSendNotification](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_notification) |   | X |   |   |
| [Dot11ExtSendUIRequest](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_ui_request) |   | X |   |   |
| [Dot11ExtSetAuthAlgorithm](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_auth_algorithm) |   | X |   |   |
| [Dot11ExtSetCurrentProfile](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_current_profile) |   |   | X |   |
| [Dot11ExtSetDefaultKey](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_default_key) |   | X |   |   |
| [Dot11ExtSetDefaultKeyId](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_default_key_id)|   | X |   |   |
| [Dot11ExtSetEtherTypeHandling](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_ethertype_handling) |   | X |   |   |
| [Dot11ExtSetExcludeUnencrypted](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_exclude_unencrypted) |   | X |   |   |
| [Dot11ExtSetKeyMappingKey](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_key_mapping_key) |   | X |   |   |
| [Dot11ExtSetMulticastCipherAlgorithm](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_multicast_cipher_algorithm) |   | X |   |   |
| [Dot11ExtSetProfileCustomUserData](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_profile_custom_user_data) |   | X |   |   |
| [Dot11ExtSetUnicastCipherAlgorithm](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_unicast_cipher_algorithm) |   | X |   |   |
| [Dot11ExtSetVirtualStationAPProperties](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_virtual_station_ap_properties) |   |   | X |   | 

For more information about IHV Handler functions, see [Native 802.11 IHV Handler Functions](native-802-11-ihv-handler-functions.md).
