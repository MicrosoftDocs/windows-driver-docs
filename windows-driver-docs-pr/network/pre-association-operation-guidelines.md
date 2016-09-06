---
title: Pre-Association Operation Guidelines
description: Pre-Association Operation Guidelines
ms.assetid: 35e9b701-6d5d-4c76-80fc-bb146be1ddb1
keywords: ["pre-association operations WDK Native 802.11 IHV Extensions DLL"]
---

# Pre-Association Operation Guidelines


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The IHV Extensions DLL must follow these guidelines when performing the pre-association operation.

-   When the [*Dot11ExtIhvPerformPreAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547499) function is called, the IHV Extensions DLL must do the following:
    -   Verify the IHV extensions for the connectivity and security profile. If the profile parameters are invalid, the *Dot11ExtIhvPerformPreAssociate* function returns an appropriate error code as defined in Winerror.h.
    -   Create and begin a new thread for the completion of the pre-association operation. Because the pre-association operation must be completed asynchronously from the call to [*Dot11ExtIhvPerformPreAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547499), the IHV Extensions DLL must call [**Dot11ExtPreAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547538) from this thread after the operation completes.
    -   Return ERROR\_SUCCESS from the function call. At this point, the operating system is notified that the network profile is valid and the pre-association operation is in progress.
-   The IHV Extensions DLL can call the [**Dot11ExtNicSpecificExtension**](https://msdn.microsoft.com/library/windows/hardware/ff547526) function to configure the wireless LAN (WLAN) adapter. This function can be called either from within the call to [*Dot11ExtIhvPerformPreAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547499) or from the thread that handles the pre-association operation after *Dot11ExtIhvPerformPreAssociate* returns.

-   Calls to the [**Dot11ExtSetProfileCustomUserData**](https://msdn.microsoft.com/library/windows/hardware/ff547603), [**Dot11ExtGetProfileCustomUserData**](https://msdn.microsoft.com/library/windows/hardware/ff547430), and [**Dot11ExtSetCurrentProfile**](https://msdn.microsoft.com/library/windows/hardware/ff547574) must not be made from within the call to [*Dot11ExtIhvPerformPreAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547499). These functions can only be called after *Dot11ExtIhvPerformPreAssociate* returns ERROR\_SUCCESS.

-   After the IHV Extensions DLL calls [**Dot11ExtPreAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547538) to complete the pre-association operation, the handle for the connection session is no longer valid. The operating system passes this handle through the *hConnectSession* parameter of [*Dot11ExtIhvPerformPreAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547499). The DLL must not use this handle value when calling any IHV Extensibility functions that declare an *hConnectSession* parameter.

    For more information about the IHV Extensibility functions, see [Native 802.11 IHV Extensibility Functions](https://msdn.microsoft.com/library/windows/hardware/ff560609).

-   If the [*Dot11ExtIhvAdapterReset*](https://msdn.microsoft.com/library/windows/hardware/ff547434) function is called, the IHV Extensions DLL must cancel the pre-association operation by calling [**Dot11ExtPreAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547538). For more information about the reset operation, see [802.11 WLAN Adapter Reset](802-11-wlan-adapter-reset.md).

-   If the [*Dot11ExtIhvDeinitAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff547452) function is called, the IHV Extensions DLL must cancel the pre-association operation internally. However, it must not call any of the IHV Extensibility functions that can be called only after adapter initialization, including [**Dot11ExtPreAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547538).

 

 





