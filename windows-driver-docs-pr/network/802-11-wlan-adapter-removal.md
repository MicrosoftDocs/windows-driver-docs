---
title: 802.11 WLAN Adapter Removal
description: 802.11 WLAN Adapter Removal
ms.assetid: 2181d284-7987-48db-b7a4-d1296d8313ed
keywords: ["adapters WDK 802.11 WLAN , removing", "WLAN adapters WDK , removing", "removing WLAN adapters"]
---

# 802.11 WLAN Adapter Removal


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When a wireless LAN (WLAN) adapter is removed or disabled, the operating system calls [*Dot11ExtIhvDeinitAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff547452) to notify the IHV Extensions DLL of the adapter's removal. The operating system also calls the *Dot11ExtIhvDeinitAdapter* function for every adapter managed by the IHV Extensions DLL before the operating system unloads the DLL.

When [*Dot11ExtIhvDeinitAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff547452) is called, the IHV Extensions DLL must follow these guidelines.

-   The IHV Extensions DLL must free any allocated resources for the WLAN adapter. In particular, all memory allocated through calls to [**Dot11ExtAllocateBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff547419) must be freed through calls to [**Dot11ExtFreeBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff547422).

-   The handle used by the operating system to reference the WLAN adapter is no longer valid when [*Dot11ExtIhvDeinitAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff547452) is called. The operating system passes its handle to the IHV Extensions DLL through the *hDot11SvcHandle* parameter when [*Dot11ExtIhvInitAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff547469) is called.

    Within the call to the *Dot11ExtIhvDeinitAdapter* function and after returning from the call, the DLL must not use the handle value when calling any IHV Extensibility function that declares an *hDot11SvcHandle* parameter, such as [**Dot11ExtSendPacket**](https://msdn.microsoft.com/library/windows/hardware/ff547563).

-   If the IHV Extensions DLL had a pending pre-association operation, which was initiated through a call to the [*Dot11ExtIhvPerformPreAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547499) IHV Handler function, the operating system regards the operation as canceled through the call to the [*Dot11ExtIhvDeinitAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff547452) function. Within the call, the DLL must cancel the pre-association operation internally but must not call [**Dot11ExtPreAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547538) to complete the pre-association operation.

    For more information about the pre-association operation, see [Pre-Association Operations](pre-association-operations.md).

-   If the IHV Extensions DLL had a pending post-association operation, which was initiated through a call to the [*Dot11ExtIhvPerformPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547492) IHV Handler function, the operating system cancels the operation by calling the [*Dot11ExtIhvStopPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547521) function before it calls [*Dot11ExtIhvDeinitAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff547452).

    For more information about the post-association operation, see [Post-Association Operations](post-association-operations.md).

-   The operating system calls the [*Dot11ExtIhvDeinitAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff547452) function for every adapter managed by the IHV Extensions DLL before the operating system unloads the DLL. In this situation, the operating system calls the [*Dot11ExtIhvDeinitService*](https://msdn.microsoft.com/library/windows/hardware/ff547457) IHV Handler function after the last WLAN adapter has been halted through a call to *Dot11ExtIhvDeinitAdapter*.

    For more information about this operation, see [DLL Stop Operations](dll-stop-operations.md).

 

 





