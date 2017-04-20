---
title: Native 802.11 IHV UI Extensions DLL Overview
description: Native 802.11 IHV UI Extensions DLL Overview
ms.assetid: 82276ffb-eec4-4a77-9feb-f8f2ca1d7b34
keywords:
- IHV UI Extensions DLL WDK Native 802.11 , about IHV UI Extensions DLL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 IHV UI Extensions DLL Overview


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

If the independent hardware vendor (IHV) provides a Native 802.11 IHV Extensions DLL, the IHV can optionally provide a Native 802.11 IHV UI Extensions DLL. Through this DLL, the IHV can do the following:

-   Extend the Microsoft Network Configuration user interface (UI) properties, which are used for wireless connection and security configuration settings. In this situation, the Native 802.11 IHV UI Extensions DLL can do the following:

    -   Add custom display elements to the standard Microsoft 802.11 properties. For example, the Native 802.11 IHV UI Extensions DLL can add items to a list to provide the end user with selections for proprietary security options.
    -   Launch a custom UI that you can use to configure proprietary connection and security settings.

    For more information about extending Microsoft 802.11 properties, see [Extending 801.11 Properties](extending-the-properties-for-wireless-network-profiles.md).

-   Launch a custom UI at the request of the Native 802.11 IHV Extensions DLL. Depending on the current state of the underlying Native 802.11 miniport driver, the operating system displays the UI as either of the following:

    -   A set of wizard pages within the flow of the operating system's 802.11 UI. For example, if the Native 802.11 IHV Extensions DLL requires user credentials during a wireless LAN (WLAN) connection operation, the operating system displays the custom UI pages provided by the Native 802.11 UI Extensions DLL as part of the standard UI flow.

        A stand-alone UI launched from a balloon notification. For example, if the Native 802.11 Extensions DLL determines that the connection or authentication state on the WLAN connection has changes, the DLL can request that the Native 802.11 UI Extensions DLL display a balloon notification to alert the end user.

    For more information about launching a UI that results from requests from the Native 802.11 Extensions DLL, see [Handling UI Requests from the Native 802.11 IHV Extensions DLL](handling-requests-for-the-display-of-a-custom-ui.md).

For more information about the Native 802.11 IHV Extensions DLL, see [Native 802.11 IHV Extensions DLL](https://msdn.microsoft.com/library/windows/hardware/ff560614).

For more information about the Microsoft Network Configuration UI and other Native 802.11 components, see [Native 802.11 Software Architecture](native-802-11-software-architecture.md).

 

 





