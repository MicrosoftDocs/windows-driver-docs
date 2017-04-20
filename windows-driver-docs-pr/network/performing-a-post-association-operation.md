---
title: Performing a Post-Association Operation
description: Performing a Post-Association Operation
ms.assetid: b029d499-a23d-4f2f-aa28-2e8bfb2a00e5
keywords:
- post-association operations WDK Native 802.11 IHV Extensions DLL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Performing a Post-Association Operation


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When the wireless LAN (WLAN) adapter successfully completes an 802.11 association operation with an access point (AP), the Native 802.11 miniport driver notifies the operating system by making an [NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION](https://msdn.microsoft.com/library/windows/hardware/ff567319) indication. For more information about the association operation, see [Association Operations](association-operations.md).

**Note**  For Windows Vista, the IHV Extensions DLL supports only infrastructure basic service set (BSS) networks.

 

After the operating system receives the NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION indication, it calls the [*Dot11ExtIhvPerformPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547492) function to notify the IHV Extensions DLL of the following:

-   The creation of a new data port for the association with the AP. The IHV Extensions DLL is passed the current state of the data port through the *pPortState* parameter of the [*Dot11ExtIhvPerformPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547492) function. For more information about the port state parameter, see [**DOT11\_PORT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff548753).

-   The parameters of the association between the wireless LAN (WLAN) adapter and the AP. The IHV Extensions DLL is passed the association parameters through the *pDot11AssocParams* parameter of the [*Dot11ExtIhvPerformPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547492) function. For more information about the association parameters, see [**DOT11\_ASSOCIATION\_COMPLETION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff547647).

When [*Dot11ExtIhvPerformPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547492) is called, the IHV Extensions DLL initiates a post-association operation with the AP to authenticate the data port. Through this operation, the IHV Extensions DLL can do the following:

-   Allocate any resources needed for the new data port.

-   Perform proprietary security processing on the data port for the association. The IHV Extensions DLL can determine the current state of the data port from *pPortState* parameter of the [*Dot11ExtIhvPerformPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547492) function.

-   Call the [**Dot11ExtSendUIRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547567) function to request the IHV UI Extensions DLL to prompt the user for security parameters, such as the user's credentials.

-   Authenticate with the AP using the authentication algorithm enabled through [**Dot11ExtSetAuthAlgorithm**](https://msdn.microsoft.com/library/windows/hardware/ff547571). The IHV Extensions DLL calls **Dot11ExtSetAuthAlgorithm** during the pre-association operation. For more information about this operation, see [Pre-Association Operations](pre-association-operations.md).

-   Send security packets to the AP through calls to the [**Dot11ExtSendPacket**](https://msdn.microsoft.com/library/windows/hardware/ff547563) function.

    When the security packet has been sent, the operating notifies the IHV Extensions DLL through a call to the [*Dot11ExtIhvSendPacketCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff547516) function.

    For more information about sending security packets, see [Send Operations](send-operations.md).

-   Receive security packets from the AP. The operating system calls the [*Dot11ExtIhvReceivePacket*](https://msdn.microsoft.com/library/windows/hardware/ff547513) function for each security packet received by the WLAN adapter.

    Each received security packet is serialized and indicated in the order they were received from the WLAN adapter. The operating system only calls the [*Dot11ExtIhvReceivePacket*](https://msdn.microsoft.com/library/windows/hardware/ff547513) function to indicate received security packets that match an entry in the list of IEEE EtherTypes, which were specified by the IHV Extensions DLL through a call to the [**Dot11ExtSetEtherTypeHandling**](https://msdn.microsoft.com/library/windows/hardware/ff547587) function.

    For more information about receiving security packets, see [Receive Operations](receive-operations.md).

-   Configure the WLAN adapter with the cipher keys that are derived through the authentication algorithm. The following IHV Extensibility functions can be called to download the cipher keys to the WLAN adapter.
    -   [**Dot11ExtSetDefaultKey**](https://msdn.microsoft.com/library/windows/hardware/ff547578)
    -   [**Dot11ExtSetDefaultKeyId**](https://msdn.microsoft.com/library/windows/hardware/ff547584)
    -   [**Dot11ExtSetKeyMappingKey**](https://msdn.microsoft.com/library/windows/hardware/ff547597)
-   Configure the WLAN adapter to exclude unencrypted packets through a call to the [**Dot11ExtSetExcludeUnencrypted**](https://msdn.microsoft.com/library/windows/hardware/ff547589) IHV Extensibility function.

After the data port has been authenticated, the IHV Extensions DLL must call [**Dot11ExtPostAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547530) to complete the post-association operation.

The following figure shows the steps involved during the post-association operation.

![diagram illustrating the steps involved during the post-association operation](images/ihv-ext-postassoc.png)

The IHV Extensions DLL must follow these guidelines when performing the post-association operation.

-   The IHV Extensions DLL must call [**Dot11ExtPostAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547530) asynchronously from the call to [*Dot11ExtIhvPerformPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547492).

-   After completing the post-association operation, the IHV Extensions DLL can call [**Dot11ExtPostAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547530) whenever the authentication status of the data port changes.

-   If the [*Dot11ExtIhvAdapterReset*](https://msdn.microsoft.com/library/windows/hardware/ff547434) function is called, the IHV Extensions DLL must cancel all pending post-association operations by calling [**Dot11ExtPostAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547530). For more information about the reset operation, see [802.11 WLAN Adapter Reset](802-11-wlan-adapter-reset.md).

-   If the [*Dot11ExtIhvDeinitAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff547452) function is called, the IHV Extensions DLL must cancel all pending post-association operations internally. However, it must not call any of the IHV Extensibility functions that can be called only after adapter initialization, including [**Dot11ExtPostAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547530). For more information about the IHV Extensibility functions, see [Native 802.11 IHV Extensibility Functions](https://msdn.microsoft.com/library/windows/hardware/ff560609).

 

 





