---
title: Native 802.11 IHV Handler functions
description: This section describes Native 802.11 IHV Handler functions for the Native 802.11 IHV Extensions DLL
keywords: ["Native 802.11 IVH Handler functions", "Native 802.11 IHV Extensions DLL Handler Functions", "WDK Native 802.11 IVH Handler functions"]
ms.assetid: BF0DC1C7-48E1-487E-8F64-146BBA322F40
ms.date: 04/27/2017
ms.localizationpriority: medium
---

# Native 802.11 IHV Handler functions

>[!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-miniport-driver-design-guide).

The Native 802.11 IHV Handler functions are provided by the IHV Extensions DLL and are called by the operating system to do the following:

- Allocate and free buffers that are used within the Native 802.11 framework.
- Send packets, such as a packet defined by an authentication algorithm, through the IHV's wireless LAN (WLAN) adapter.
- Receive packets based on a specified list of IEEE EtherType values and privacy exemption rules.
- Configure the IHV's WLAN adapter with various security settings for any proprietary authentication and cipher algorithms.
- Interface with the IHV UI Extensions DLL (if installed) to process event notifications. For example, the IHV Extensions DLL could notify the UI Extensions DLL about the various stages involved in a basic service set (BSS) network connection. 

For more information about the IHV UI Extensions DLL, see [Native 802.11 IHV UI Extensions DLL](native-802-11-ihv-ui-extensions-dll2.md).

> [!NOTE]
> With the exception of [Dot11ExtIhvGetVersionInfo](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_get_version_info) and [Dot11ExtIhvInitService](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_init_service), the operating system calls the IHV Handler functions through a function pointer associated with a member of the [DOT11EXT_IHV_HANDLERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/ns-wlanihv-_dot11ext_ihv_handlers) structure. When the operating system calls the *Dot11ExtIhvInitService* IHV Handler function, the IHV Extensions DLL returns the list of pointers to the IHV Handler functions through the *pDot11IHVHandlers* parameter.

This section describes the following Native 802.11 IHV Handler functions.

- [Dot11ExtIhvAdapterReset](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_adapter_reset)
- [Dot11ExtIhvControl](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_control)
- [Dot11ExtIhvCreateDiscoveryProfiles](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_create_discovery_profiles)
- [Dot11ExtIhvDeinitAdapter](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_deinit_adapter)
- [Dot11ExtIhvDeinitService](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_deinit_service)
- [Dot11ExtIhvGetVersionInfo](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_get_version_info)
- [Dot11ExtIhvInitAdapter](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_init_adapter)
- [Dot11ExtIhvInitService](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_init_service)
- [Dot11ExtIhvInitVirtualStation](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_init_virtual_station)
- [Dot11ExtIhvIsUIRequestPending](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_is_ui_request_pending)
- [Dot11ExtIhvOneXIndicateResult](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_onex_indicate_result)
- [Dot11ExtIhvPerformCapabilityMatch](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_perform_capability_match)
- [Dot11ExtIhvPerformPostAssociate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_perform_post_associate)
- [Dot11ExtIhvPerformPreAssociate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_perform_pre_associate)
- [Dot11ExtIhvProcessSessionChange](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_process_session_change)
- [Dot11ExtIhvProcessUIResponse](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_process_ui_response)
- [Dot11ExtIhvQueryUIRequest](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_query_ui_request)
- [Dot11ExtIhvReceiveIndication](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_receive_indication)
- [Dot11ExtIhvReceivePacket](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_receive_packet)
- [Dot11ExtIhvSendPacketCompletion](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_send_packet_completion)
- [Dot11ExtIhvStopPostAssociate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_stop_post_associate)
- [Dot11ExtIhvValidateProfile](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_validate_profile)

