---
title: Setting the Driver Control Flags
description: Setting the Driver Control Flags
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Driver Control Flags


The **ExcludeFromSelect** directive is required for all drivers, except for [mirror drivers](mirror-drivers.md), that are written to the Windows Display Driver Model (WDDM).

The following example shows how to add the **ExcludeFromSelect** directive to a **ControlFlags** section of the INF file:

```inf
[ControlFlags]
ExcludeFromSelect=*
```

For more information on driver control flags, see [**INF ControlFlags Section**](../install/inf-controlflags-section.md).

 

