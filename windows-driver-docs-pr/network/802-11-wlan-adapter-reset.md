---
title: 802.11 WLAN Adapter Reset
description: 802.11 WLAN Adapter Reset
ms.assetid: 1f993977-b4a1-42ec-8de3-2f4855db93a7
keywords:
- adapters WDK 802.11 WLAN , resetting
- WLAN adapters WDK , resetting
- resetting WLAN adapters
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# 802.11 WLAN Adapter Reset


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The operating system calls [*Dot11ExtIhvAdapterReset*](https://msdn.microsoft.com/library/windows/hardware/ff547434) whenever it becomes necessary to restore the wireless LAN (WLAN) adapter to its initialized state. The operating system calls this function whenever one of the following events occurs.

-   The WLAN adapter performs a disconnection operation. For more information about this operation, see [Disconnection Operations](disconnection-operations.md).

-   The operating system resets the Native 802.11 miniport driver, which manages the adapter, through a set request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409).

When [*Dot11ExtIhvAdapterReset*](https://msdn.microsoft.com/library/windows/hardware/ff547434) is called, the IHV Extensions DLL must follow these guidelines.

-   The IHV Extensions DLL must restore its state to the same state it was in after the [*Dot11ExtIhvInitAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff547469) function was called. If the DLL configured proprietary settings on the WLAN adapter, it must restore these settings to the same state they were in after *Dot11ExtIhvInitAdapter* was called.

-   If the IHV Extensions DLL had a pending pre-association operation, which was initiated through a call to the [*Dot11ExtIhvPerformPreAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547499) IHV Handler function, the DLL must call [**Dot11ExtPreAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547538) to cancel the operation. In this situation, the DLL sets the *dwWin32Error* parameter of **Dot11ExtPreAssociateCompletion** to ERROR\_CANCELLED.

    For more information about the pre-association operation, see [Pre-Association Operations](pre-association-operations.md).

-   If the DLL had a pending post-association operation, which was initiated through a call to the [*Dot11ExtIhvPerformPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547492) IHV Handler function, the DLL must call [**Dot11ExtPostAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547530) to cancel the operation. In this situation, the DLL sets the *dwWin32Error* parameter of **Dot11ExtPostAssociateCompletion** to ERROR\_CANCELLED.

    For more information about the post-association operation, see [Post-Association Operations](post-association-operations.md).

 

 





