---
title: Testing Device Functionality
author: windows-driver-content
description: Testing Device Functionality
ms.assetid: 51b3e55d-b071-4dbe-b687-5e3ed25aed20
keywords:
- testing device functionality WDK printer
- device functionality testing WDK printer
- functionality testing WDK printer
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Testing Device Functionality


After you have completed all tests of device installation and Plug and Play functionality, verify that the device performs all functions as expected. Print test pages with as many applications and document types as possible.

You should also perform the following additional functionality tests.

1.  **User Access:** Verify that users with different levels of system access can print to the device, including users who are logged into the system remotely using the Remote Desktop Connection application.

2.  **Special Functionality:** Verify any special functionality that your device supports. For example, if a printer enables bidirectional (bidi) communication, verify that bidi requests from the printer work as expected, such as canceling print jobs from the device and duplex printing.

3.  **Job Control:** Verify that print jobs can be paused, canceled, resumed, and restarted. Also verify that multiple print jobs can be started, printed, canceled, and restarted at the same time.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Testing%20Device%20Functionality%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


