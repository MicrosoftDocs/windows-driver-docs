---
title: PnP-X for mobile broadband apps
description: PnP-X for mobile broadband apps
ms.assetid: f8f4756e-00b6-4778-9d67-73653865cf54
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PnP-X for mobile broadband apps


## <span id="App_installation"></span><span id="app_installation"></span><span id="APP_INSTALLATION"></span>App installation


A mobile broadband adapter offers users the opportunity to have the appropriate mobile broadband app automatically installed when the adapter is connected. Personal hotspots cannot benefit from the same SIM-based carrier detection. However, personal hotspots that implement the PnP-X protocol can select an app to install. The app is automatically installed when the computer pairs with the PnP-X device.

This can be the same app that is auto-installed for mobile broadband users, or a branded app that the device manufacturer and the operator author together. The app should include many of the same functions as a standard mobile broadband app. See [Designing the user experience of a mobile broadband app](designing-the-user-experience-of-a-mobile-broadband-app.md) for suggestions on standard experiences in a mobile broadband app.

Certain classes of network devices are automatically paired; for more information, see [UWP device apps for internal devices](https://msdn.microsoft.com/library/windows/hardware/dn265152). Other device classes do not automatically install the app until the user pairs with the device by using the computer settings.

## <span id="App_privileges"></span><span id="app_privileges"></span><span id="APP_PRIVILEGES"></span>App privileges


Although the app does not have access to the same privileged APIs as a mobile broadband app, it can talk to the device over the network to retrieve equivalent information if the device exposes this information.

## <span id="related_topics"></span>Related topics


[Communication channels](communication-channels.md)

 

 






