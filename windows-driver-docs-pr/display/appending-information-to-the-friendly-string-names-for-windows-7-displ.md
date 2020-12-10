---
title: Append Info to Windows 7 Display Driver Friendly Names
description: Describes the information you must append to the friendly string name for Windows 7 Display Drivers.
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# Appending Information to the Friendly String Names for Windows 7 Display Drivers


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

A graphics adapter's friendly name is a localizable string name that is required in the INF for every Windows 7 in-box display driver. The section on [Appending Information to the Friendly String Names of Graphics Adapters](appending-information-to-the-friendly-string-names-of-graphics-adapter.md) describes the information that you must append for the Windows Display Driver Model (WDDM) and the [Windows 2000 Display Driver Model](windows-2000-display-driver-model-design-guide.md). For the WDDM optimized for Windows 7, you must append "(Microsoft Corporation - WDDM v1.1)":

```cpp
New Driver Model Foo Device Name (Microsoft Corporation - WDDM v1.1)
```

The text appended to the graphics adapter's friendly name specifies the WDDM version that the driver uses.

 

 





