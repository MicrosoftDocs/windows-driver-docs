---
title: PnP-X for mobile broadband apps
description: PnP-X for mobile broadband apps
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f8f4756e-00b6-4778-9d67-73653865cf54
---

# PnP-X for mobile broadband apps


## <span id="App_installation"></span><span id="app_installation"></span><span id="APP_INSTALLATION"></span>App installation


A mobile broadband adapter offers users the opportunity to have the appropriate mobile broadband app automatically installed when the adapter is connected. Personal hotspots cannot benefit from the same SIM-based carrier detection. However, personal hotspots that implement the PnP-X protocol can select an app to install. The app is automatically installed when the computer pairs with the PnP-X device.

This can be the same app that is auto-installed for mobile broadband users, or a branded app that the device manufacturer and the operator author together. The app should include many of the same functions as a standard mobile broadband app. See [Designing the user experience of a mobile broadband app](designing-the-user-experience-of-a-mobile-broadband-app.md) for suggestions on standard experiences in a mobile broadband app.

Certain classes of network devices are automatically paired; for more information, see [Windows Store device apps for internal devices](https://msdn.microsoft.com/library/windows/hardware/dn265152). Other device classes do not automatically install the app until the user pairs with the device by using the computer settings.

## <span id="App_privileges"></span><span id="app_privileges"></span><span id="APP_PRIVILEGES"></span>App privileges


Although the app does not have access to the same privileged APIs as a mobile broadband app, it can talk to the device over the network to retrieve equivalent information if the device exposes this information.

## <span id="related_topics"></span>Related topics


[Communication channels](communication-channels.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20PnP-X%20for%20mobile%20broadband%20apps%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





