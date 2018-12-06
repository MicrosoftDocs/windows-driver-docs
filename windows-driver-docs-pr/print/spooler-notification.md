---
title: Spooler Notification
description: Spooler Notification
ms.assetid: b5d9b909-f2e4-4773-903e-1dd73b0ca567
keywords:
- spooler notification WDK print
- print spooler notification WDK
- notification WDK print spooler
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Spooler Notification





This feature is available in Windows Vista and later.

The spooler notification mechanism provides a two-way communication path between spooler-hosted components (such as printer drivers, print processors, and port monitors) and applications. The applications involved can run in different sessions and security contexts.

The spooler notification mechanism solves the problem that occurs when printing components that run in the spooler process need to display user interface elements in the session in which the print job was initiated. In Windows 2000 and earlier, any UI displayed by these printing components always appears in session zero, the session in which the spooler service runs. To help with this problem, two spooler functions were added for Windows XP, [**SplPromptUIInUsersSession**](https://msdn.microsoft.com/library/windows/hardware/ff562679) and [**SplIsSessionZero**](https://msdn.microsoft.com/library/windows/hardware/ff562677). The spooler notification mechanism provides more capabilities than do these functions, which are limited to presenting messages in dialog boxes.

[Overview of Spooler Notification](overview-of-spooler-notification.md)

[Spooler Notification Terminology](spooler-notification-terminology.md)

[Public Interfaces](public-interfaces.md)

 

 




