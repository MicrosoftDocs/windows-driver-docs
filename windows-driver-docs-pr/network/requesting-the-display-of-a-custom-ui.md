---
title: Requesting the Display of a Custom UI
description: Requesting the Display of a Custom UI
ms.assetid: 4b7366d9-e55a-4b24-b75f-a5f133b80ca7
keywords:
- custom UI WDK Native 802.11 IHV UI Extensions DLL , requesting display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Requesting the Display of a Custom UI


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Native 802.11 IHV Extensions DLL can request the display of a custom user interface (UI) through the Native 802.11 IHV UI Extensions DLL. For example, the IHV Extensions DLL could request that a custom UI be displayed to:

-   Notify the end user at various stages during the wireless LAN (WLAN) association operation.

-   Notify the end user when the WLAN adapter has disassociated for the WLAN network.

-   Notify the end user with the results of the authentication to the WLAN network.

To launch a custom UI or display a notification, the Native 802.11 IHV Extensions DLL calls [**Dot11ExtSendUIRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547567) and passes a pointer to a [**DOT11EXT\_IHV\_UI\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff547637) structure through the *pIhvUIRequest* parameter of this function.

Through the [**DOT11EXT\_IHV\_UI\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff547637) structure, the Native 802.11 IHV Extensions DLL specifies the custom UI through the following data:

-   The user session identifier (ID), which is used to identify a specific user context.

-   A globally unique ID (GUID), which identifies the specific UI request.

-   The class ID (CLSID) of **IWizardExtension** COM interface implemented within the Native 802.11 IHV UI Extensions DLL. The CLSID is used to request a specific custom UI supported by the DLL.

    For more information about the **IWizardExtension** COM interface, see [IWizardExtension COM Interface](http://go.microsoft.com/fwlink/p/?linkid=56607).

-   A buffer containing data in a proprietary format that is defined by the independent hardware vendor (IHV) and processed by the specified **IWizardExtension** COM interface. For example, the buffer could contain the default values that are displayed within the custom UI.

Depending upon the WLAN connection state for the user session ID, the custom UI request will be displayed as one of the following:

-   If the adapter has connected to a WLAN network, the request will be displayed as a standalone UI launched through a clickable balloon notification. For more information about this process, see [Displaying a Balloon Notification](displaying-custom-ui-pages-within-a-balloon-notification.md).

-   If the adapter is in the process of connecting to a WLAN network, the request will be displayed as a set of wizard pages within the standard Network Connection UI. For more information about this process, see [Displaying Custom UI Pages within the Network Connection Wizard](displaying-custom-ui-pages-within-the-network-connection-wizard.md).

 

 





