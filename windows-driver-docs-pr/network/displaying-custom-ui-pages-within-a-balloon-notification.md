---
title: Displaying Custom UI Pages within a Balloon Notification
description: Displaying Custom UI Pages within a Balloon Notification
ms.assetid: 5ed2ba59-88ae-4379-b729-1d741b30a7a0
keywords:
- custom UI WDK Native 802.11 IHV UI Extensions DLL , balloon notifications
- balloon notifications WDK
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Displaying Custom UI Pages within a Balloon Notification


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

If the Native 802.11 IHV Extensions DLL calls [**Dot11ExtSendUIRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547567) to display a custom user interface (UI), the operating system will display the UI through a clickable balloon notification if the wireless LAN (WLAN) adapter has connected to a wireless network. In this situation, the request for the custom UI is displayed as a balloon notification:

-   After the Native 802.11 IHV Extensions DLL calls [**Dot11ExtPostAssociateCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff547530) to successfully complete the post-association operation.

-   Before the operating system calls the DLL's [*Dot11ExtIhvAdapterReset*](https://msdn.microsoft.com/library/windows/hardware/ff547434) IHV Handler function to reset the WLAN connection.

For more information about how the Native 802.11 IHV Extensions DLL requests the display of a custom UI, see [Requesting the Display of a Custom UI](requesting-the-display-of-a-custom-ui.md).

When processing a custom UI request as a balloon notification, the operating system does the following.

1.  Calls the Native 802.11 IHV Extensions DLL's [*Dot11ExtIhvIsUIRequestPending*](https://msdn.microsoft.com/library/windows/hardware/ff547479) IHV Handler function to determine whether a UI request is still pending. The operating system specifies the UI request using the globally unique identifier (GUID) passed to [**Dot11ExtSendUIRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547567) by the Native 802.11 IHV Extensions DLL.

2.  If [*Dot11ExtIhvIsUIRequestPending*](https://msdn.microsoft.com/library/windows/hardware/ff547479) returns **TRUE** for the specified UI request, the operating system will call the Native 802.11 IHV UI Extensions DLL's [**IDot11ExtUI::GetDot11ExtUIBalloonText**](https://msdn.microsoft.com/library/windows/hardware/ff553771) method. Through this method, the DLL returns a string buffer that contains the localized text to be displayed within the balloon notification.

3.  Displays the balloon notification that contains the localized text.

4.  If the end user clicks the balloon notification, the operating system will launch the custom UI that is supported by the requested **IWizardExtension** COM interface. When it calls [**Dot11ExtSendUIRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547567), the Native 802.11 IHV Extensions DLL specifies the class identifier (CLSID) of the **IWizardExtension** implementation within the Native 802.11 IHV UI Extensions DLL.

    When the operating system calls the **IWizardExtension::AddPages** method, the Native 802.11 IHV UI Extensions DLL returns an array of handles for PROPSHEETPAGE structures representing the custom UI pages.

    For more information about the **IWizardExtension** COM interface, see [IWizardExtension COM Interface](http://go.microsoft.com/fwlink/p/?linkid=56607). For more information about the PROPSHEETPAGE structure, refer to the documentation in the Microsoft Windows SDK.

5.  Navigates through the UI pages as specified by the Native 802.11 IHV UI Extensions DLL through **IWizardSite** COM interface. For more information about this interface, see [IWizardSite COM Interface](http://go.microsoft.com/fwlink/p/?linkid=56608).

While the custom UI is displayed, the Native 802.11 IHV UI Extensions DLL can read or write context-specific data through the [IPropertyBag COM interface](http://go.microsoft.com/fwlink/p/?linkid=56610). For more information about this process, see [Accessing Profile and Context Data](accessing-profile-and-context-data.md). After the display of the custom UI has completed, the Native 802.11 IHV UI Extensions DLL can return the user-entered response data to the Native 802.11 IHV Extensions DLL by calling **WlanSendUIResponse** . The DLL passes in the GUID for the UI request as well as a pointer to a buffer that contains the response data.

After the Native 802.11 IHV UI Extensions DLLcalls **WlanSendUIResponse**, the operating system will call the Native 802.11 IHV Extension DLL's [*Dot11ExtIhvProcessUIResponse*](https://msdn.microsoft.com/library/windows/hardware/ff547504) IHV Handler function to forward the response data for the custom UI.

For more information about the **WlanSendUIResponse** API, refer to the documentation in the Windows SDK.

 

 





