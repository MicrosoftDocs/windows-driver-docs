---
title: Validating Network Profile Extensions
description: Validating Network Profile Extensions
keywords:
- network profiles WDK Native 802.11 IHV Extensions DLL , validating extensions
- validating network profile extensions WDK Native 802.11 IHV Extensions DLL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Validating Network Profile Extensions




 

The operating system calls IHV Handler functions to validate IHV-defined connectivity and security settings under the following conditions.

-   The user creates a new network profile that contains settings for the IHV-defined connectivity and/or security profile extensions. In this situation, the operating system calls the [*Dot11ExtIhvValidateProfile*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_validate_profile) IHV Handler function to validate the user settings.

-   The WLAN adapter completes a scan operation and returns its results to the operating system. The operating system calls the [*Dot11ExtIhvPerformCapabilityMatch*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_capability_match) IHV Handler function to determine whether a detected basic service set (BSS) network matches the IHV-defined connectivity and security settings from a network profile.

    The operating system passes a list of the 802.11 Beacon and Probe Response frames from the BSS network to the *pConnectableBssid* parameter of the **Dot1ExtIhvPerformCapabilityMatch** function. The operating system also passes the connectivity and security profile extensions to the *pIhvConnProfile* and *pIhvSecProfile* parameters, respectively.

    If all of the entries in the list of 802.11 Beacon and Probe Response frames advertise the connectivity and security attributes defined in the profile fragments, the [*Dot11ExtIhvPerformCapabilityMatch*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_capability_match) function returns ERROR\_SUCCESS.

-   The operating system initiates a pre-association operation by calling the [*Dot11ExtIhvPerformPreAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_pre_associate) function. In this situation, the IHV Extensions DLL must verify that the connectivity and security settings are valid. If the settings are valid, the function returns ERROR\_SUCCESS and the DLL proceeds with the pre-association operation. Otherwise, the function returns an appropriate error code as defined in Winerror.h.

    For more information about the pre-association operation, see [Pre-Association Operations](pre-association-operations.md).

For more information about the IHV Handler functions, see [Native 802.11 IHV Handler Functions](./native-802-11-ihv-handler-functions.md).

 

 
