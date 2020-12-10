---
title: Spooler Notification Terminology
description: Spooler Notification Terminology
keywords:
- spooler notification WDK print , terminology
- print spooler notification WDK , terminology
ms.date: 06/12/2020
ms.localizationpriority: medium
---

# Spooler notification terminology

The following terms are used in the discussion of asynchronous spooler notification:

| Term | Description |
|--|--|
| **callback interface** | When a listening client registers for notifications, it must provide a pointer to an [IPrintAsyncNotifyCallback](/windows/win32/api/prnasnot/nn-prnasnot-iprintasyncnotifycallback) interface. The methods of this interface are called back when notifications arrive or when the channel is closed. |
| **listening clients** | Either applications or spooler internal components registered to receive print notifications. This is different from what was previously referred to as the clients of the spooler notification pipe. A client of the spooler notification pipe is whatever component defines a notification type and schema. |
| **notification** | Data sent through the notification channel between the printing components and listening clients. |
| **notification channel** | A logical component. It is represented by an **IPrintAsyncNotifyCallback** interface pointer. The printing component creates the notification channel when it needs to send out notifications. The listening client uses the notification channel when it sends data back to the printing component. |
| **notification registration handle** | The handle created by the service when a listening clients registers for receiving notifications. The listening client can use this handle to unregister for notifications. |
| **printing component** | Components loaded by Spoolsv.exe, such as print processors, drivers, and monitors. |
| **service** | Functionality implemented by the spooler, either as part of the service itself (Spoolsv.exe) or as part of the client side (Winspool.drv). |
