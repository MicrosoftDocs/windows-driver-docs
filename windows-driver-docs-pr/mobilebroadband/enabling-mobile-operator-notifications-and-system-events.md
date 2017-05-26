---
title: Enabling mobile operator notifications and system events
description: Enabling mobile operator notifications and system events
ms.assetid: 988bafcc-ad8e-446d-9336-85c19cf05577
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enabling mobile operator notifications and system events


This topic provides information about the Mobile Operator Notification system event for Windows 8, Windows 8.1, and Windows 10. It provides guidelines for you to develop Windows Store mobile broadband apps that handle incoming SMS- or USSD-based mobile operator notifications and relevant mobile broadband system events.

## <span id="Introduction"></span><span id="introduction"></span><span id="INTRODUCTION"></span>Introduction


A customer’s primary experience of a mobile broadband network brand in Windows 8, Windows 8.1, and Windows 10 is the mobile broadband app. This app is not expected to provide primary connection management functions, but instead provides an account management experience and a service experience. To keep the user informed about their account status, the app must perform some activities even when the user is not interacting with it. These activities include the following:

-   Responding to operator SMS or network-initiated USSD messages

-   Notifying the user that they are approaching their data limit

-   Notifying the user that their data plan has expired

-   Notifying the user of their roaming status

-   Verifying whether tethering is supported on the user’s data plan

### <span id="Background_brokered_work_items"></span><span id="background_brokered_work_items"></span><span id="BACKGROUND_BROKERED_WORK_ITEMS"></span>Background brokered work items

Windows 8 introduced Windows Store mobile broadband apps that run on the full screen. Users are only expected to interact with the application that is in the foreground. The foreground app is assumed to be the most important to the user, so this app receives all the resources of the system. When an app is not in the foreground, it is suspended and cannot run any code. A suspended app remains suspended until the user resumes it by bringing the app back to the foreground. With this model of app behavior, the user experience is never affected by lags or delays caused by the execution of unimportant background apps. In addition, reducing unnecessary background activity optimizes battery life on a variety of form factors. The time taken to resume a suspended app is negligible and would appear to be almost unnoticeable to most users.

Windows 8, Windows 8.1, and Windows 10 provide Windows push notifications that can keep the app tile up-to-date even when the app is suspended. Push notifications are optimized for system performance and longer device battery life, so it’s best to use Windows push notifications whenever possible. If a suspended app must run its own code to do other kinds of work, you can create background tasks.

Although Windows Store apps cannot run any code if they are not running in the foreground, the System Event Broker lets you run code in response to events while an app is in the background. Apps can register work items with the System Event Broker to respond to specific background brokered events. Windows runs the app’s work item when background brokered events are triggered, regardless of the app’s current state (active or suspended).

In general, background events are intended as simple trigger points and are not intended to signal large amounts of processing. As such, quotas for each app are placed on the processing time that is allowed for background events. The background events offered by the Network Operator API, including the [MobileOperatorNotification](mobile-operator-notification-event-technical-details.md) event and [HotspotAuthentication](handling-the-hotspot-authentication-event.md) event, are treated by Windows as critical events. Compared to general background events in Windows 8, Windows 8.1, and Windows 10, background work items associated with MobileOperatorNotification and HotspotAuthentication events run for every instance of the event regardless of a processing time quota, although each instance of the background work item is subject to a processing time quota. You should limit processing in the background event handler and defer larger processing to the mobile broadband app.

## <span id="In_this_section"></span><span id="in_this_section"></span><span id="IN_THIS_SECTION"></span>In this section


-   [Develop an app to handle the MobileOperatorNotification event](develop-an-app-to-handle-the-mobileoperatornotification-event.md)

-   [Mobile operator notification event technical details](mobile-operator-notification-event-technical-details.md)

-   [Mobile operator notification scenarios](mobile-operator-notification-scenarios.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Enabling%20mobile%20operator%20notifications%20and%20system%20events%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




