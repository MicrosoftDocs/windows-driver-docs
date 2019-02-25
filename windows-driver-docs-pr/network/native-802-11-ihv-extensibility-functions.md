---
title: Native 802.11 IHV Extensibility functions
description: This section describes Native 802.11 IHV Extensibility functions for the Native 802.11 IHV Extensions DLL
keywords: ["Native 802.11 IVH Extensibility functions", "Native 802.11 IHV Extensions DLL Extensibility Functions", "WDK Native 802.11 IVH Extensibility functions"]
ms.assetid: 0E7CC153-5434-459D-9773-8CCAFBACD016
ms.date: 04/27/2017
ms.localizationpriority: medium
---

# Native 802.11 IHV Extensibility functions

> [!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-miniport-driver-design-guide).

The Native 802.11 IHV Extensibility functions are provided by the operating system and are called by the IHV Extensions DLL to do the following:

- Allocate and free buffers that are used within the Native 802.11 framework.
- Send packets, such as a packet defined by an authentication algorithm, through the IHV's wireless LAN (WLAN) adapter.
- Configure the IHV's WLAN adapter with various security settings for any authentication and cipher algorithms supported by the IHV Extensions DLL.
- Interface with the IHV UI Extensions DLL (if installed) to process event notifications. For example, the IHV Extensions DLL could notify the IHV UI Extensions DLL about the various stages involved in a basic service set (BSS) network connection. 

For more information about the IHV UI Extensions DLL, see [Native 802.11 IHV UI Extensions DLL](native-802-11-ihv-ui-extensions-dll2.md).

> [!NOTE]
> The IHV Extensions DLL calls each Native 802.11 IHV Extensibility function through a function pointer associated with a member of the [DOT11EXT_APIS](https://msdn.microsoft.com/library/windows/hardware/ff547617) structure. When the operating system calls the [Dot11ExtIhvInitService](https://msdn.microsoft.com/library/windows/hardware/ff547470) IHV Handler function, it passes the list of pointers to the IHV Extensibility functions through the *pDot11ExtAPI* parameter.
 
The following table lists the Native 802.11 IHV Extensibility Functions that can be called by the IHV Extensions DLL. Each IHV Extensibility function can only be called under these conditions.


- **Called After Service Initialization**  
The IHV Extensibility function can only be called after the [Dot11ExtIhvInitService](https://msdn.microsoft.com/library/windows/hardware/ff547470) IHV Handler function has been called to initialize the IHV Extensions DLL. Also, the Extensions DLL cannot call the IHV Extensibility function after the [Dot11ExtIhvDeinitService](https://msdn.microsoft.com/library/windows/hardware/ff547457) IHV Handler function has been called.
- **Called after Adapter Initialization**  
The IHV Extensibility function can only be called after the [Dot11ExtIhvInitAdapter](https://msdn.microsoft.com/library/windows/hardware/ff547469) IHV Handler function has been called to initialize the interface to the IHV's WLAN adapter.  
The IHV Extensibility function requires a handle, which identifies the WLAN adapter. When *Dot11ExtIhvInitAdapter* is called, the IHV Extensions DLL is passed this handle through the *hDot11SvcHandle* parameter.  
The Extensions DLL cannot call the IHV Extensibility function after the [Dot11ExtIhvDeinitAdapter](https://msdn.microsoft.com/library/windows/hardware/ff547452) IHV Handler function has been called.
- **Called after Pre-Association**  
The IHV Extensibility function can only be called after the [Dot11ExtIhvPerformPreAssociate](https://msdn.microsoft.com/library/windows/hardware/ff547499) IHV Handler function has been called to initiate a pre-association operation with a basic service set (BSS) network.  
The IHV Extensibility function requires a handle, which identifies the BSS network connection. When *Dot11ExtIhvPerformPreAssociate* is called, the IHV Extensions DLL is passed this handle through the *hConnection* parameter.  
The Extensions DLL cannot call the IHV Extensibility function after the [Dot11ExtIhvDeinitAdapter](https://msdn.microsoft.com/library/windows/hardware/ff547452) or [Dot11ExtIhvAdapterReset](https://msdn.microsoft.com/library/windows/hardware/ff547434) IHV Handler functions have been called.
- **Called after Post-Association**  
The IHV Extensibility function can only be called after the [Dot11ExtIhvPerformPostAssociate](https://msdn.microsoft.com/library/windows/hardware/ff547492) IHV Handler function has been called to initiate a post-association operation with a basic service set (BSS) network.  
The IHV Extensibility function requires a handle, which identifies the security session with the BSS network connection. When *Dot11ExtIhvPerformPostAssociate* is called, the IHV Extensions DLL is passed this handle through the *hSecuritySessionID* parameter.  
The Extensions DLL cannot call the IHV Extensibility function after the [Dot11ExtIhvDeinitAdapter](https://msdn.microsoft.com/library/windows/hardware/ff547452) or [Dot11ExtIhvAdapterReset](https://msdn.microsoft.com/library/windows/hardware/ff547434) IHV Handler functions have been called.

| Function | Called after service initialization | Called after adapter initialization | Called after pre-association | Called after post-association |
| --- | --- | --- | --- | --- |
| [Dot11ExtAllocateBuffer](https://msdn.microsoft.com/library/windows/hardware/ff547419) | X |   |   |   |
| [Dot11ExtFreeBuffer](https://msdn.microsoft.com/library/windows/hardware/ff547422) | X |   |   |   |
| [Dot11ExtGetProfileCustomUserData](https://msdn.microsoft.com/library/windows/hardware/ff547430) |   |   | X |   | 
| [Dot11ExtNicSpecificExtension](https://msdn.microsoft.com/library/windows/hardware/ff547526) |   | X |   |   |
| [Dot11ExtStartOneX](https://msdn.microsoft.com/library/windows/hardware/ff547610) |   |   |   | X |
| [Dot11ExtStopOneX](https://msdn.microsoft.com/library/windows/hardware/ff547614) |   |   |   | X |
| [Dot11ExtPostAssociateCompletion](https://msdn.microsoft.com/library/windows/hardware/ff547530) |   |   |   | X |
| [Dot11ExtPreAssociateCompletion](https://msdn.microsoft.com/library/windows/hardware/ff547538) |   |   | X |   |
| [Dot11ExtProcessOneXPacket](https://msdn.microsoft.com/library/windows/hardware/ff547541) |   |   |   | X |
| [Dot11ExtQueryVirtualStationProperties](https://msdn.microsoft.com/library/windows/hardware/ff547544) |   | X |   |   |
| [Dot11ExtReleaseVirtualStation](https://msdn.microsoft.com/library/windows/hardware/ff547549) |   | X |   |   |
| [Dot11ExtRequestVirtualStation](https://msdn.microsoft.com/library/windows/hardware/ff547556) |   | X |   |   |
| [Dot11ExtSendNotification](https://msdn.microsoft.com/library/windows/hardware/ff547560) |   | X |   |   |
| [Dot11ExtSendUIRequest](https://msdn.microsoft.com/library/windows/hardware/ff547567) |   | X |   |   |
| [Dot11ExtSetAuthAlgorithm](https://msdn.microsoft.com/library/windows/hardware/ff547571) |   | X |   |   |
| [Dot11ExtSetCurrentProfile](https://msdn.microsoft.com/library/windows/hardware/ff547574) |   |   | X |   |
| [Dot11ExtSetDefaultKey](https://msdn.microsoft.com/library/windows/hardware/ff547578) |   | X |   |   |
| [Dot11ExtSetDefaultKeyId](https://msdn.microsoft.com/library/windows/hardware/ff547584)|   | X |   |   |
| [Dot11ExtSetEtherTypeHandling](https://msdn.microsoft.com/library/windows/hardware/ff547587) |   | X |   |   |
| [Dot11ExtSetExcludeUnencrypted](https://msdn.microsoft.com/library/windows/hardware/ff547589) |   | X |   |   |
| [Dot11ExtSetKeyMappingKey](https://msdn.microsoft.com/library/windows/hardware/ff547597) |   | X |   |   |
| [Dot11ExtSetMulticastCipherAlgorithm](https://msdn.microsoft.com/library/windows/hardware/ff547599) |   | X |   |   |
| [Dot11ExtSetProfileCustomUserData](https://msdn.microsoft.com/library/windows/hardware/ff547603) |   | X |   |   |
| [Dot11ExtSetUnicastCipherAlgorithm](https://msdn.microsoft.com/library/windows/hardware/ff547606) |   | X |   |   |
| [Dot11ExtSetVirtualStationAPProperties](https://msdn.microsoft.com/library/windows/hardware/ff547609) |   |   | X |   | 

For more information about IHV Handler functions, see [Native 802.11 IHV Handler Functions](native-802-11-ihv-handler-functions.md).


