---
title: Validating Network Profile Extensions
description: Validating Network Profile Extensions
ms.assetid: d29805a3-7ecb-4587-99c5-b1f8ad9f1503
keywords: ["network profiles WDK Native 802.11 IHV Extensions DLL , validating extensions", "validating network profile extensions WDK Native 802.11 IHV Extensions DLL"]
---

# Validating Network Profile Extensions


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The operating system calls IHV Handler functions to validate IHV-defined connectivity and security settings under the following conditions.

-   The user creates a new network profile that contains settings for the IHV-defined connectivity and/or security profile extensions. In this situation, the operating system calls the [*Dot11ExtIhvValidateProfile*](https://msdn.microsoft.com/library/windows/hardware/ff547523) IHV Handler function to validate the user settings.

-   The WLAN adapter completes a scan operation and returns its results to the operating system. The operating system calls the [*Dot11ExtIhvPerformCapabilityMatch*](https://msdn.microsoft.com/library/windows/hardware/ff547488) IHV Handler function to determine whether a detected basic service set (BSS) network matches the IHV-defined connectivity and security settings from a network profile.

    The operating system passes a list of the 802.11 Beacon and Probe Response frames from the BSS network to the *pConnectableBssid* parameter of the **Dot1ExtIhvPerformCapabilityMatch** function. The operating system also passes the connectivity and security profile extensions to the *pIhvConnProfile* and *pIhvSecProfile* parameters, respectively.

    If all of the entries in the list of 802.11 Beacon and Probe Response frames advertise the connectivity and security attributes defined in the profile fragments, the [*Dot11ExtIhvPerformCapabilityMatch*](https://msdn.microsoft.com/library/windows/hardware/ff547488) function returns ERROR\_SUCCESS.

-   The operating system initiates a pre-association operation by calling the [*Dot11ExtIhvPerformPreAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547499) function. In this situation, the IHV Extensions DLL must verify that the connectivity and security settings are valid. If the settings are valid, the function returns ERROR\_SUCCESS and the DLL proceeds with the pre-association operation. Otherwise, the function returns an appropriate error code as defined in Winerror.h.

    For more information about the pre-association operation, see [Pre-Association Operations](pre-association-operations.md).

For more information about the IHV Handler functions, see [Native 802.11 IHV Handler Functions](https://msdn.microsoft.com/library/windows/hardware/ff560627).

 

 





