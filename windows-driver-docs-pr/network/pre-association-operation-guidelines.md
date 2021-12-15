---
title: Pre-Association Operation Guidelines
description: Pre-Association Operation Guidelines
keywords:
- pre-association operations WDK Native 802.11 IHV Extensions DLL
ms.date: 04/20/2017
---

# Pre-Association Operation Guidelines




 

The IHV Extensions DLL must follow these guidelines when performing the pre-association operation.

-   When the [*Dot11ExtIhvPerformPreAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_pre_associate) function is called, the IHV Extensions DLL must do the following:
    -   Verify the IHV extensions for the connectivity and security profile. If the profile parameters are invalid, the *Dot11ExtIhvPerformPreAssociate* function returns an appropriate error code as defined in Winerror.h.
    -   Create and begin a new thread for the completion of the pre-association operation. Because the pre-association operation must be completed asynchronously from the call to [*Dot11ExtIhvPerformPreAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_pre_associate), the IHV Extensions DLL must call [**Dot11ExtPreAssociateCompletion**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_pre_associate_completion) from this thread after the operation completes.
    -   Return ERROR\_SUCCESS from the function call. At this point, the operating system is notified that the network profile is valid and the pre-association operation is in progress.
-   The IHV Extensions DLL can call the [**Dot11ExtNicSpecificExtension**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_nic_specific_extension) function to configure the wireless LAN (WLAN) adapter. This function can be called either from within the call to [*Dot11ExtIhvPerformPreAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_pre_associate) or from the thread that handles the pre-association operation after *Dot11ExtIhvPerformPreAssociate* returns.

-   Calls to the [**Dot11ExtSetProfileCustomUserData**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_profile_custom_user_data), [**Dot11ExtGetProfileCustomUserData**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_get_profile_custom_user_data), and [**Dot11ExtSetCurrentProfile**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_current_profile) must not be made from within the call to [*Dot11ExtIhvPerformPreAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_pre_associate). These functions can only be called after *Dot11ExtIhvPerformPreAssociate* returns ERROR\_SUCCESS.

-   After the IHV Extensions DLL calls [**Dot11ExtPreAssociateCompletion**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_pre_associate_completion) to complete the pre-association operation, the handle for the connection session is no longer valid. The operating system passes this handle through the *hConnectSession* parameter of [*Dot11ExtIhvPerformPreAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_pre_associate). The DLL must not use this handle value when calling any IHV Extensibility functions that declare an *hConnectSession* parameter.

    For more information about the IHV Extensibility functions, see [Native 802.11 IHV Extensibility Functions](./native-802-11-ihv-extensibility-functions.md).

-   If the [*Dot11ExtIhvAdapterReset*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_adapter_reset) function is called, the IHV Extensions DLL must cancel the pre-association operation by calling [**Dot11ExtPreAssociateCompletion**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_pre_associate_completion). For more information about the reset operation, see [802.11 WLAN Adapter Reset](802-11-wlan-adapter-reset.md).

-   If the [*Dot11ExtIhvDeinitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_adapter) function is called, the IHV Extensions DLL must cancel the pre-association operation internally. However, it must not call any of the IHV Extensibility functions that can be called only after adapter initialization, including [**Dot11ExtPreAssociateCompletion**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_pre_associate_completion).

 

 
