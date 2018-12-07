---
title: Interfaces Implemented at Both Ends of the Notification Channel
description: Interfaces Implemented at Both Ends of the Notification Channel
ms.assetid: cc6f1b06-c185-4915-a212-d0b3a2702d5d
keywords:
- spooler notification WDK print , channel
- print spooler notification WDK , channel
- notification channel WDK print spooler
- channel notification WDK print spooler
- data channels WDK spooler notification
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Interfaces Implemented at Both Ends of the Notification Channel





The following figure shows the COM interfaces that are used in spooler asynchronous notification.

![diagram illustrating the com interfaces that are used in spooler asynchronous notification](images/splnotarch.png)

The left side of the picture depicts the sender end of the notification channel, along with the interfaces that the spooler implements. The right side of the picture depicts the listener side of the notification channel, along with the interfaces that are implemented by the application or printing component, and those implemented by the server side of the spooler. The sender and listeners implement the interfaces shown above the dashed line. The spooler implements the interfaces and functions shown below the dashed line.

 

 




