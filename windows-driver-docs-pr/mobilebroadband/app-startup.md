---
title: App startup
description: App startup
ms.assetid: 0aca0d3c-9865-4a11-a9c5-e77cc735ba21
---

# App startup


When the mobile broadband app is started, it should check whether Internet access is available. The app can use an API to discover the various states of Internet connectivity. The app can then determine whether it can access back-end data when the Internet connection is in a “walled garden” state. If there is no Internet connection, the app should show an appropriate message or offline experience to the user.

If multiple operators’ subscriber identity modules (SIMs) are attached to the PC, the app can determine this. The app must present a user interface that works for multiple connected operator devices or accounts.

For example, the app can read the IMSI and IMEI information from the mobile broadband device. This information can be used as part of the authentication scheme, in addition or in place of a logon screen that sends user-name and password information to the back-end. Windows provides an API to securely store user-name and password information that the app can subsequently use for authentication after the first logon attempt. All user-name and password information must be exchanged with the operator back-end over Secure HTTP (HTTPS).

## <span id="related_topics"></span>Related topics


[Mobile broadband app scenarios](mobile-broadband-app-scenarios.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20App%20startup%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





