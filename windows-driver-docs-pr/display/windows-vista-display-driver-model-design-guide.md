---
title: Windows Display Driver Model (WDDM) Design Guide
description: The Windows Display Driver Model (WDDM) is available starting with Windows Vista and is required starting with Windows 8. This section discusses requirements, specifications, and behavior for WDDM drivers.
keywords:
- WDDM Design Guide WDK
- display driver model WDK Windows Vista
- Windows Vista display driver model WDK
- display devices WDK
- display drivers WDK , Windows Vista
- display driver model WDK Windows Vista , about display driver model
- Windows Vista display driver model WDK , about display driver model
- miniport drivers WDK display
- display miniport drivers WDK See miniport drivers WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows Display Driver Model (WDDM) Design Guide

The Windows Display Driver Model (WDDM) is required starting with Windows 8. This guide discusses WDDM requirements, specifications, and behavior for WDDM drivers.

> [!NOTE]
>
> The [Windows 2000 Display Driver Model (XDDM)](windows-2000-display-driver-model-design-guide.md) and VGA drivers will not compile on Windows 8 and later versions. If display hardware is attached to a Windows 8 computer without a driver that is certified to support WDDM 1.2 or later, the system defaults to running the Microsoft Basic Display Driver.
>
> WDDM drivers do not directly use services of the Windows Graphics Device Interface (GDI) engine; therefore, the [GDI](gdi.md) section is not relevant to writing display drivers for the WDDM driver model.
