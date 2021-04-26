---
title: Fast User Switching
description: Fast User Switching
keywords:
- display driver model WDK Windows 2000 , Fast User Switching
- Windows 2000 display driver model WDK , Fast User Switching
- video miniport drivers WDK Windows 2000 , Fast User Switching
- Fast User Switching WDK Windows 2000 display
- multiple virtual display drivers WDK Windows 2000 display
- virtual display drivers WDK Windows 2000 display
- display drivers WDK Windows 2000 , Fast User Switching
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Fast User Switching

Fast User Switching enables multiple users to be logged onto the same machine. A particular user's desktop and any running applications persist from that user's logon session to their next session.

Fast User Switching works by allowing multiple virtual display drivers to run at the same time, where each virtual display driver is associated with a particular PDEV. The video miniport driver, however, exists as a single instance. When one of the virtual display drivers calls a video miniport driver callback, serious problems ensue if the miniport driver attempts to access a passed-in memory address in the context of the display driver when that display driver instance is no longer the active kernel thread. A tenet of the display driver/video miniport driver architecture is that information should flow in one direction only: from the display driver to the video miniport driver.
