---
title: Registering to Receive Notifications
description: Registering to Receive Notifications
ms.assetid: 2442c204-c9d8-49fa-93ae-02623d08119c
keywords:
- spooler notification WDK print , registering to receive
- print spooler notification WDK , registering to receive
- receiving spooler notifications
- registering for spooler notifications
- RegisterForPrintAsyncNotifications
- UnRegisterForPrintAsyncNotifications
- unregistering for spooler notifications
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering to Receive Notifications





Listening clients call the [RegisterForPrintAsyncNotifications](http://go.microsoft.com/fwlink/p/?linkid=124752) method to register for receiving notifications. The listening client can be an application or can run inside the spooler. Winspool.drv exposes this functionality regardless of where is it loaded.

Spoolss.lib exposes this functionality so that port monitors can register for notifications. Components that run inside the spooler and that link to Spoolss.lib can call **RegisterForPrintAsyncNotifications**. The following procedure details the information that must be passed in a call to this function. The first step of the procedure applies to the first parameter, the second step applies to the second parameter, and so on.

```cpp
HRESULT
 RegisterForPrintAsyncNotifications(
    IN LPCWSTR,
    IN PrintAsyncNotificationType*,
    IN PrintAsyncNotifyUserFilter,
    IN PrintAsyncNotifyConversationStyle,
    IN IPrintAsyncNotifyCallback*,
    OUT HANDLE*
    );
```

**To register for notifications, specify**

1.  A local/remote printer or server name.

2.  The type of notification that the listener is interested in.

3.  The user filter, which indicates the user from which the client is interested in receiving notifications, either the same user as the notification sender, or all users.

4.  The conversation style filter. The client can specify either unidirectional or bidirectional communication.

5.  The [IPrintAsyncNotifyCallback](http://go.microsoft.com/fwlink/p/?linkid=124755) interface to be called when a notification returns from the other end of the channel. This parameter cannot be **NULL**.

When this function returns, the sixth parameter (of type HANDLE\*) points to a registration handle. The registration handle is an opaque structure that the client receives. The registration is associated with the user identity of the thread making the registration call. The spooler filters listening clients based on the channel's session filter and the client's registration session, in addition to the client session's filter.

To notify the spooler that the listening client should no longer receive notifications, the client must use this handle when it calls [UnRegisterForPrintAsyncNotifications](http://go.microsoft.com/fwlink/p/?linkid=124754). For unidirectional communication, any pending notifications on the server side are dismissed. For bidirectional communication, if there are open bidirectional channels, communication continues until they are closed.

```cpp
HRESULT
 UnRegisterForPrintAsyncNotifications(
    IN HANDLE
    );
```








