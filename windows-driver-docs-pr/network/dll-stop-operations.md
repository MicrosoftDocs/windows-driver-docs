---
title: DLL Stop Operations
description: DLL Stop Operations
ms.assetid: b49e9215-3781-4e19-8287-f484553ccb2e
keywords:
- IHV Extensions DLL WDK Native 802.11 , stop operations
- unloading IHV Extensions DLL
- stopping IHV Extensions DLL
- Native 802.11 IHV Extensions DLL WDK , stop operations
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DLL Stop Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The operating system stops and unloads the IHV Extensions DLL whenever.

-   The last wireless LAN (WLAN) adapter managed by the DLL is either removed or disabled.

-   The host computer is reset or shut down.

The operating system follows this sequence when stopping and unloading the IHV Extensions DLL.

1.  The operating system first calls the [*Dot11ExtIhvDeinitAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff547452) IHV Handler function for every WLAN adapter managed by the IHV Extensions DLL. For more information about this operation, see [802.11 WLAN Adapter Removal](802-11-wlan-adapter-removal.md).

    After the call to *Dot11ExtIhvDeinitAdapter*, the IHV Extensions DLL must not call any IHV Extensions function related to adapter-specific operations, such as [**Dot11ExtNicSpecificExtension**](https://msdn.microsoft.com/library/windows/hardware/ff547526).

2.  The operating system then calls the [*Dot11ExtIhvDeinitService*](https://msdn.microsoft.com/library/windows/hardware/ff547457) IHV Handler function. When this function is called, the IHV Extensions DLL must free all allocated resources and prepare itself for unloading.

    After the call to *Dot11ExtIhvDeinitService*, the IHV Extensions DLL must not call any IHV Extensions function.

3.  Finally, the operating system calls the *DllMain* function in the IHV Extensions DLL with the *fdwReason* parameter set to DLL\_PROCESS\_DETACH. For more information about *DllMain* and DLLs, refer to the topic "About Dynamic-Link Libraries" within the Microsoft Windows SDK documentation.

For more information about the IHV Extensibility functions, see [Native 802.11 IHV Extensibility Functions](https://msdn.microsoft.com/library/windows/hardware/ff560609).

 

 





