---
title: Displaying Custom UI Pages within the Network Connection Wizard
description: Displaying Custom UI Pages within the Network Connection Wizard
keywords:
- custom UI WDK Native 802.11 IHV UI Extensions DLL , Network Connection Wizard
- Network Connection Wizard WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Displaying Custom UI Pages within the Network Connection Wizard




 

A custom user interface (UI) supported by the Native 802.11 IHV UI Extensions DLL can be displayed within the operating system's Network Connection Wizard when the request for UI is made through either:

-   A call to [**Dot11ExtSendUIRequest**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_ui_request), made by the Native 802.11 IHV Extensions DLL. For more information about this process, see [Requesting the Display of a Custom UI](requesting-the-display-of-a-custom-ui.md).

-   A call to the Native 802.11 IHV Extensions DLL's **Dot11ExtQueryUIRequest** IHV Handler function, made by the operating system. For more information about this process, see [Querying for the Display of a Custom UI](querying-for-the-display-of-a-custom-ui.md).

The operating system displays the custom UI within the Network Connection Wizard if the wireless LAN (WLAN) adapter is attempting to connect to a wireless network. In this situation, the request for the custom UI will be displayed as a balloon notification within the period:

-   After the operating system calls the Native 802.11 IHV Extensions DLL's [*Dot11ExtIhvPerformPreAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_pre_associate) IHV Handler function to initiate a pre-association operation with the wireless network.

-   Before the Native 802.11 IHV Extensions DLL calls [**Dot11ExtPostAssociateCompletion**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_post_associate_completion) to successfully complete the post-association operation.

When inserting the custom UI request within the Network Connection Wizard, the operating system does the following:

1.  Calls the Native 802.11 IHV Extensions DLL's [*Dot11ExtIhvIsUIRequestPending*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_is_ui_request_pending) IHV Handler function to determine whether a UI request is still pending. The operating system specifies the UI request using the globally unique identifier (GUID) that is passed to [**Dot11ExtSendUIRequest**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_ui_request) by the Native 802.11 IHV Extensions DLL.

2.  If [*Dot11ExtIhvIsUIRequestPending*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_is_ui_request_pending) returns **TRUE** for the specified UI request, the operating system will instantiate the requested **IWizardExtension** COM interface and bind it into the current UI flow of the Network Connection Wizard. When it calls [**Dot11ExtSendUIRequest**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_ui_request), the Native 802.11 IHV Extensions DLL specifies the class identifier (CLSID) of the **IWizardExtension** implementation within the Native 802.11 IHV UI Extensions DLL.

    The operating system also calls the **IWizardExtension::AddPages** method, through which the Native 802.11 IHV UI Extensions DLL returns an array of handles for PROPSHEETPAGE structures representing the custom UI pages.

    For more information about the **IWizardExtension** COM interface, see [IWizardExtension COM Interface](/windows/win32/api/shobjidl/nn-shobjidl-iwizardextension).

3.  Navigates through the UI pages as controlled by the Native 802.11 IHV UI Extensions DLL through the **IWizardSite** COM interface. For more information about this interface, see [IWizardSite COM Interface](/windows/win32/api/shobjidl/nn-shobjidl-iwizardsite).

While the custom UI is displayed, the Native 802.11 IHV UI Extensions DLL can read or write context-specific data through the [IPropertyBag COM interface](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768196(v=vs.85)). For more information about this process, see [Accessing Profile and Context Data](accessing-profile-and-context-data.md).

After the custom UI is displayed, the Native 802.11 IHV UI Extensions DLL can return the user-entered response data to the Native 802.11 IHV Extensions DLL by calling **WlanSendUIResponse**. The DLL passes in the GUID for the UI request as well as a pointer to a buffer containing the response data.

After the Native 802.11 IHV UI Extensions DLL calls **WlanSendUIResponse**, the operating system calls the Native 802.11 IHV Extension DLL's [*Dot11ExtIhvProcessUIResponse*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_process_ui_response) IHV Handler function to forward the response data for the custom UI.

For more information about the **WlanSendUIResponse** API, refer to the documentation in the Microsoft Windows SDK.

 

 
