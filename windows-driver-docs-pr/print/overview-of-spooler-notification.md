---
title: Overview of Spooler Notification
description: Overview of Spooler Notification
ms.assetid: 1d0c9130-eeb8-4a7b-8be4-5b434413c870
keywords: ["spooler notification WDK print , about spooler notification", "print spooler notification WDK , about spooler notification", "bidirectional channels WDK spooler notification", "unidirectional channels WDK spooler notification", "data channels WDK spooler notification"]
---

# Overview of Spooler Notification


## <a href="" id="ddk-overview-of-spooler-notification-gg"></a>


Spooler notification consists of a set of COM interfaces for spooler-hosted print components that enable them to open a bidirectional or unidirectional data channel with applications running in sessions other than the spooler's session.

This data channel is notification-based and is associated with either a printer name or a server name. Only printing components hosted by the spooler can open the notification channel, but notifications can be sent in both directions.

Spooler notification also includes a set of COM interfaces that print components and applications can use to register for print notifications. Applications can register for notifications, but they cannot open notification channels. Printing components loaded by the spooler can register for notifications.

For bidirectional channels, when a notification is received, the listener client is also informed which channel it can use to send data back to the printing component.

For unidirectional channels, the listener client receives only the notification, because it is not expected to respond to the notification.

An in-process spooler component can open a notification channel whether or not there are any listeners. After the channel is opened, the printing component can send notifications. If there are no listeners, the call will still succeed, but the value returned indicates that no one received the notification.

A printing component loaded by either the spooler or an application can register for notifications with a printer or with a server (local or remote), whether or not there are any open channels.

After a channel is opened and a notification is sent, the listener client receives the notification. The listener client also receives information about which channel was used for the notification (for bidirectional channels).

The notification mechanism is asynchronous. The order of notifications is guaranteed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Overview%20of%20Spooler%20Notification%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




