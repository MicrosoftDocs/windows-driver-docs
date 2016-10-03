---
title: Stopping a Post-Association Operation
description: Stopping a Post-Association Operation
ms.assetid: 28400cad-1e77-4bcd-9b9a-103df5f06d10
keywords: ["post-association operations WDK Native 802.11 IHV Extensions DLL", "stopping post-association operations"]
---

# Stopping a Post-Association Operation


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The operating system terminates the post-association operation by calling the [*Dot11ExtIhvStopPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547521) IHV Handler function whenever one of the following occurs.

-   The wireless LAN (WLAN) adapter completes a disassociation operation with the AP. In this situation, the Native 802.11 station, which manages the adapter, makes a media-specific [NDIS\_STATUS\_DOT11\_DISASSOCIATION](https://msdn.microsoft.com/library/windows/hardware/ff567334) indication. For more information about the disassociation operation, see [Disassociation Operations](disassociation-operations.md).

-   The WLAN adapter is disabled or removed. In this situation, the operating system calls the [*Dot11ExtIhvStopPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547521) function before it calls the [*Dot11ExtIhvDeinitAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff547452) function.

The operating system calls the [*Dot11ExtIhvStopPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547521) function to notify the IHV Extensions DLL that the data port created for the association with an AP is down. The operating system calls this function regardless of whether the DLL has completed the post-association operation through a call to [**Dot11ExtPostAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547530).

When [*Dot11ExtIhvStopPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547521) is called, the IHV Extensions must release all of the resources allocated for the data port. If the post-association operation was not completed with a call to [**Dot11ExtPostAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547530), the IHV Extensions DLL must cancel the operation internally but must not call **Dot11ExtPostAssociateCompletion**.

 

 





