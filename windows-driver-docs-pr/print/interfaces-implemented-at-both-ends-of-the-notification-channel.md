---
title: Interfaces Implemented at Both Ends of the Notification Channel
author: windows-driver-content
description: Interfaces Implemented at Both Ends of the Notification Channel
ms.assetid: cc6f1b06-c185-4915-a212-d0b3a2702d5d
keywords:
- spooler notification WDK print , channel
- print spooler notification WDK , channel
- notification channel WDK print spooler
- channel notification WDK print spooler
- data channels WDK spooler notification
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Interfaces Implemented at Both Ends of the Notification Channel


## <a href="" id="ddk-interfaces-implemented-at-both-ends-of-the-notification-channel-gg"></a>


The following figure shows the COM interfaces that are used in spooler asynchronous notification.

![diagram illustrating the com interfaces that are used in spooler asynchronous notification](images/splnotarch.png)

The left side of the picture depicts the sender end of the notification channel, along with the interfaces that the spooler implements. The right side of the picture depicts the listener side of the notification channel, along with the interfaces that are implemented by the application or printing component, and those implemented by the server side of the spooler. The sender and listeners implement the interfaces shown above the dashed line. The spooler implements the interfaces and functions shown below the dashed line.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Interfaces%20Implemented%20at%20Both%20Ends%20of%20the%20Notification%20Channel%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


