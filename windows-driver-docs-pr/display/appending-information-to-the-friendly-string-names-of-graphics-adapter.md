---
title: Append Info to Graphics Adapter Friendly String Names
description: You must append information to the string names of graphics adapters.
keywords:
- INF files WDK display , friendly string names
- friendly string names WDK display
- graphics adapters string names WDK display
- appending to graphics adapters string names WDK display
ms.date: 12/06/2018
---

# Appending Information to the Friendly String Names of Graphics Adapters


You must append information to the string names of graphics adapters. This information depends on the display driver model that the adapters' drivers are written to:

For the Windows 2000 Display Driver Model, you must append "(Microsoft Corporation)":

```cpp
XDDM Foo Device Name (Microsoft Corporation)
```

For the Windows Display Driver Model (WDDM), you must append "(Microsoft Corporation - WDDM)":

```cpp
New Driver Model Foo Device Name (Microsoft Corporation - WDDM)
```

For more information about the *Strings* section and the *%strkey%* tokens that are specified elsewhere in the INF, see [**INF Strings Section**](../install/inf-strings-section.md).

 
