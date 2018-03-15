---
title: Native 802.11 IHV Handler functions
description: This section describes Native 802.11 IHV Handler functions for the Native 802.11 IHV Extensions DLL
keywords: ["Native 802.11 IVH Handler functions", "Native 802.11 IHV Extensions DLL Handler Functions", "WDK Native 802.11 IVH Handler functions"]
ms.assetid: BF0DC1C7-48E1-487E-8F64-146BBA322F40
ms.author: windowsdriverdev
ms.date: 04/27/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 IHV Handler functions

>[!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

The Native 802.11 IHV Handler functions are provided by the IHV Extensions DLL and are called by the operating system to do the following:

- Allocate and free buffers that are used within the Native 802.11 framework.
- Send packets, such as a packet defined by an authentication algorithm, through the IHV's wireless LAN (WLAN) adapter.
- Receive packets based on a specified list of IEEE EtherType values and privacy exemption rules.
- Configure the IHV's WLAN adapter with various security settings for any proprietary authentication and cipher algorithms.
- Interface with the IHV UI Extensions DLL (if installed) to process event notifications. For example, the IHV Extensions DLL could notify the UI Extensions DLL about the various stages involved in a basic service set (BSS) network connection. 

For more information about the IHV UI Extensions DLL, see [Native 802.11 IHV UI Extensions DLL](native-802-11-ihv-ui-extensions-dll2.md).

> [!NOTE]
> With the exception of [Dot11ExtIhvGetVersionInfo](https://msdn.microsoft.com/library/windows/hardware/ff547464) and [Dot11ExtIhvInitService](https://msdn.microsoft.com/library/windows/hardware/ff547470), the operating system calls the IHV Handler functions through a function pointer associated with a member of the [DOT11EXT_IHV_HANDLERS](https://msdn.microsoft.com/library/windows/hardware/ff547625) structure. When the operating system calls the *Dot11ExtIhvInitService* IHV Handler function, the IHV Extensions DLL returns the list of pointers to the IHV Handler functions through the *pDot11IHVHandlers* parameter.

This section describes the following Native 802.11 IHV Handler functions.

- [Dot11ExtIhvAdapterReset](https://msdn.microsoft.com/library/windows/hardware/ff547434)
- [Dot11ExtIhvControl](https://msdn.microsoft.com/library/windows/hardware/ff547438)
- [Dot11ExtIhvCreateDiscoveryProfiles](https://msdn.microsoft.com/library/windows/hardware/ff547445)
- [Dot11ExtIhvDeinitAdapter](https://msdn.microsoft.com/library/windows/hardware/ff547452)
- [Dot11ExtIhvDeinitService](https://msdn.microsoft.com/library/windows/hardware/ff547457)
- [Dot11ExtIhvGetVersionInfo](https://msdn.microsoft.com/library/windows/hardware/ff547464)
- [Dot11ExtIhvInitAdapter](https://msdn.microsoft.com/library/windows/hardware/ff547469)
- [Dot11ExtIhvInitService](https://msdn.microsoft.com/library/windows/hardware/ff547470)
- [Dot11ExtIhvInitVirtualStation](https://msdn.microsoft.com/library/windows/hardware/ff547475)
- [Dot11ExtIhvIsUIRequestPending](https://msdn.microsoft.com/library/windows/hardware/ff547479)
- [Dot11ExtIhvOneXIndicateResult](https://msdn.microsoft.com/library/windows/hardware/ff547482)
- [Dot11ExtIhvPerformCapabilityMatch](https://msdn.microsoft.com/library/windows/hardware/ff547488)
- [Dot11ExtIhvPerformPostAssociate](https://msdn.microsoft.com/library/windows/hardware/ff547492)
- [Dot11ExtIhvPerformPreAssociate](https://msdn.microsoft.com/library/windows/hardware/ff547499)
- [Dot11ExtIhvProcessSessionChange](https://msdn.microsoft.com/library/windows/hardware/ff547501)
- [Dot11ExtIhvProcessUIResponse](https://msdn.microsoft.com/library/windows/hardware/ff547504)
- [Dot11ExtIhvQueryUIRequest](https://msdn.microsoft.com/library/windows/hardware/ff547507)
- [Dot11ExtIhvReceiveIndication](https://msdn.microsoft.com/library/windows/hardware/ff547512)
- [Dot11ExtIhvReceivePacket](https://msdn.microsoft.com/library/windows/hardware/ff547513)
- [Dot11ExtIhvSendPacketCompletion](https://msdn.microsoft.com/library/windows/hardware/ff547516)
- [Dot11ExtIhvStopPostAssociate](https://msdn.microsoft.com/library/windows/hardware/ff547521)
- [Dot11ExtIhvValidateProfile](https://msdn.microsoft.com/library/windows/hardware/ff547523)

