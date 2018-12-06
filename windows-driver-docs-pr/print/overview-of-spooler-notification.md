---
title: Overview of Spooler Notification
description: Overview of Spooler Notification
ms.assetid: 1d0c9130-eeb8-4a7b-8be4-5b434413c870
keywords:
- spooler notification WDK print , about spooler notification
- print spooler notification WDK , about spooler notification
- bidirectional channels WDK spooler notification
- unidirectional channels WDK spooler notification
- data channels WDK spooler notification
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Spooler Notification





Spooler notification consists of a set of COM interfaces for spooler-hosted print components that enable them to open a bidirectional or unidirectional data channel with applications running in sessions other than the spooler's session.

This data channel is notification-based and is associated with either a printer name or a server name. Only printing components hosted by the spooler can open the notification channel, but notifications can be sent in both directions.

Spooler notification also includes a set of COM interfaces that print components and applications can use to register for print notifications. Applications can register for notifications, but they cannot open notification channels. Printing components loaded by the spooler can register for notifications.

For bidirectional channels, when a notification is received, the listener client is also informed which channel it can use to send data back to the printing component.

For unidirectional channels, the listener client receives only the notification, because it is not expected to respond to the notification.

An in-process spooler component can open a notification channel whether or not there are any listeners. After the channel is opened, the printing component can send notifications. If there are no listeners, the call will still succeed, but the value returned indicates that no one received the notification.

A printing component loaded by either the spooler or an application can register for notifications with a printer or with a server (local or remote), whether or not there are any open channels.

After a channel is opened and a notification is sent, the listener client receives the notification. The listener client also receives information about which channel was used for the notification (for bidirectional channels).

The notification mechanism is asynchronous. The order of notifications is guaranteed.

 

 




