---
title: Spooler Notification
author: windows-driver-content
description: Spooler Notification
ms.assetid: b5d9b909-f2e4-4773-903e-1dd73b0ca567
keywords: ["spooler notification WDK print", "print spooler notification WDK", "notification WDK print spooler"]
---

# Spooler Notification


## <a href="" id="ddk-spooler-notification-gg"></a>


This feature is available in Windows Vista and later.

The spooler notification mechanism provides a two-way communication path between spooler-hosted components (such as printer drivers, print processors, and port monitors) and applications. The applications involved can run in different sessions and security contexts.

The spooler notification mechanism solves the problem that occurs when printing components that run in the spooler process need to display user interface elements in the session in which the print job was initiated. In Windows 2000 and earlier, any UI displayed by these printing components always appears in session zero, the session in which the spooler service runs. To help with this problem, two spooler functions were added for Windows XP, [**SplPromptUIInUsersSession**](https://msdn.microsoft.com/library/windows/hardware/ff562679) and [**SplIsSessionZero**](https://msdn.microsoft.com/library/windows/hardware/ff562677). The spooler notification mechanism provides more capabilities than do these functions, which are limited to presenting messages in dialog boxes.

[Overview of Spooler Notification](overview-of-spooler-notification.md)

[Spooler Notification Terminology](spooler-notification-terminology.md)

[Public Interfaces](public-interfaces.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Spooler%20Notification%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


