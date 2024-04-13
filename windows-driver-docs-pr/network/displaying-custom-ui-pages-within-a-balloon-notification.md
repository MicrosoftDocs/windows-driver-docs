---
title: Displaying Custom UI Pages within a Balloon Notification
description: Displaying Custom UI Pages within a Balloon Notification
keywords:
- custom UI WDK Native 802.11 IHV UI Extensions DLL , balloon notifications
- balloon notifications WDK
ms.date: 04/20/2017
---

# Displaying Custom UI Pages within a Balloon Notification




 

If the Native 802.11 IHV Extensions DLL calls [**Dot11ExtSendUIRequest**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_ui_request) to display a custom user interface (UI), the operating system will display the UI through a clickable balloon notification if the wireless LAN (WLAN) adapter has connected to a wireless network. In this situation, the request for the custom UI is displayed as a balloon notification:

-   After the Native 802.11 IHV Extensions DLL calls [**Dot11ExtPostAssociateCompletion**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_post_associate_completion) to successfully complete the post-association operation.

-   Before the operating system calls the DLL's [*Dot11ExtIhvAdapterReset*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_adapter_reset) IHV Handler function to reset the WLAN connection.

For more information about how the Native 802.11 IHV Extensions DLL requests the display of a custom UI, see [Requesting the Display of a Custom UI](requesting-the-display-of-a-custom-ui.md).

When processing a custom UI request as a balloon notification, the operating system does the following.

1.  Calls the Native 802.11 IHV Extensions DLL's [*Dot11ExtIhvIsUIRequestPending*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_is_ui_request_pending) IHV Handler function to determine whether a UI request is still pending. The operating system specifies the UI request using the globally unique identifier (GUID) passed to [**Dot11ExtSendUIRequest**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_ui_request) by the Native 802.11 IHV Extensions DLL.

2.  If [*Dot11ExtIhvIsUIRequestPending*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_is_ui_request_pending) returns **TRUE** for the specified UI request, the operating system will call the Native 802.11 IHV UI Extensions DLL's [**IDot11ExtUI::GetDot11ExtUIBalloonText**](/previous-versions/windows/hardware/wireless/ff553771(v=vs.85)) method. Through this method, the DLL returns a string buffer that contains the localized text to be displayed within the balloon notification.

3.  Displays the balloon notification that contains the localized text.

4.  If the end user clicks the balloon notification, the operating system will launch the custom UI that is supported by the requested **IWizardExtension** COM interface. When it calls [**Dot11ExtSendUIRequest**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_ui_request), the Native 802.11 IHV Extensions DLL specifies the class identifier (CLSID) of the **IWizardExtension** implementation within the Native 802.11 IHV UI Extensions DLL.

    When the operating system calls the **IWizardExtension::AddPages** method, the Native 802.11 IHV UI Extensions DLL returns an array of handles for PROPSHEETPAGE structures representing the custom UI pages.

    For more information about the **IWizardExtension** COM interface, see [IWizardExtension COM Interface](/windows/win32/api/shobjidl/nn-shobjidl-iwizardextension). For more information about the PROPSHEETPAGE structure, refer to the documentation in the Microsoft Windows SDK.

5.  Navigates through the UI pages as specified by the Native 802.11 IHV UI Extensions DLL through **IWizardSite** COM interface. For more information about this interface, see [IWizardSite COM Interface](/windows/win32/api/shobjidl/nn-shobjidl-iwizardsite).

While the custom UI is displayed, the Native 802.11 IHV UI Extensions DLL can read or write context-specific data through the [IPropertyBag COM interface](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768196(v=vs.85)). For more information about this process, see [Accessing Profile and Context Data](accessing-profile-and-context-data.md). After the display of the custom UI has completed, the Native 802.11 IHV UI Extensions DLL can return the user-entered response data to the Native 802.11 IHV Extensions DLL by calling **WlanSendUIResponse** . The DLL passes in the GUID for the UI request as well as a pointer to a buffer that contains the response data.

After the Native 802.11 IHV UI Extensions DLLcalls **WlanSendUIResponse**, the operating system will call the Native 802.11 IHV Extension DLL's [*Dot11ExtIhvProcessUIResponse*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_process_ui_response) IHV Handler function to forward the response data for the custom UI.

For more information about the **WlanSendUIResponse** API, refer to the documentation in the Windows SDK.

 

 
