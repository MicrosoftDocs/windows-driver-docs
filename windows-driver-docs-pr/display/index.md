---
title: Display Devices Design Guide
description: Display Devices Design Guide
ms.assetid: 0cbd75a3-49c3-4805-8f97-ab3551d0c6ee
keywords:
- display drivers WDK
- miniport drivers WDK display
ms.date: 10/10/2019
ms.topic: article
---

# Display Devices Design Guide

Welcome to the Windows Display Driver Design Guide. This section includes:

- [Windows Display Driver Model (WDDM) Design Guide](windows-vista-display-driver-model-design-guide.md)

  WDDM is the display/graphics driver architecture available starting with Windows Vista. Drivers that adhere to WDDM run only on Windows Vista and later.

- [Windows 2000 Display Driver Model (XDDM) Design Guide](windows-2000-display-driver-model-design-guide.md)

  XDDM is the display/graphics driver architecture available for Windows 2000 through Windows Vista and Windows 7. XDDM and VGA drivers will not compile on Windows 8 and later versions. If display hardware is attached to a Windows 8 computer without a driver that is certified to support WDDM 1.2 or later, the system defaults to running the Microsoft Basic Display Driver.

- [Display Samples](display-samples.md)
