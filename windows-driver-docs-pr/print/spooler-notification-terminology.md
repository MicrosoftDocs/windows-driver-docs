---
title: Spooler Notification Terminology
description: Spooler Notification Terminology
ms.assetid: 7d4888b1-cb5f-4095-9e1b-c330c04e4971
keywords:
- spooler notification WDK print , terminology
- print spooler notification WDK , terminology
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Spooler Notification Terminology





The following terms are used in the discussion of asnychronous spooler notification.

<a href="" id="callback-interface"></a>callback interface  
When a listening client registers for notifications, it must provide a pointer to an [IPrintAsyncNotifyCallback](http://go.microsoft.com/fwlink/p/?linkid=124755) interface, as described later in this document. The methods of this interface are called back when notifications arrive or when the channel is closed.

<a href="" id="listening-clients-"></a>listening clients   
Refers to either applications or spooler internal components registered to receive print notifications. This is different from what was previously referred to as the clients of the spooler notification pipe. A client of the spooler notification pipe is whatever component defines a notification type and schema.

<a href="" id="notification"></a>notification  
is the data sent through the notification channel between the printing components and listening clients.

<a href="" id="notification-channel-"></a>notification channel   
a logical component. It is represented by an **IPrintAsyncNotifyCallback** interface pointer, as described later in this documentation.

The printing component creates the notification channel when it needs to send out notifications. The listening client uses the notification channel when it sends data back to the printing component.

<a href="" id="notification-registration-handle"></a>notification registration handle  
the handle created by the service when a listening clients registers for receiving notifications. The listening client can use this handle to unregister for notifications.

<a href="" id="printing-component"></a>printing component  
Refers to components loaded by Spoolsv.exe, such as print processors, drivers, and monitors.

<a href="" id="service"></a>service  
Refers to the functionality implemented by the spooler, either as part of the service itself (Spoolsv.exe) or as part of the client side (Winspool.drv).

 

 




