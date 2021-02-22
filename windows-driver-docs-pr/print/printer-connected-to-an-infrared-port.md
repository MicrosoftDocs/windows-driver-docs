---
title: Printer Connected to an Infrared Port
description: Printer Connected to an Infrared Port
keywords:
- infrared ports WDK printer
- IR ports WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer Connected to an Infrared Port





Printers connected over an infrared (IR) port do not support Plug and Play using the 1284 device string. For a computer with an IR port, a service constantly polls for devices. When an IR Plug and Play printer is brought within range, a PDO is created under Enum\\Root\\ with a *device ID* of the form HWP*nnnn*. The *hardware ID* of the *devnode* has a single entry of the form HWP*nnnn*.

The [**INF Manufacturer section**](../install/inf-manufacturer-section.md) entries for a printer that supports Plug and Play over LPT and IR ports should appear similar to the following:

```cpp
 
"Model Name XYZ" = Install_Section_XYZ, LPTENUM\Company_NameModelNam1234, Company_NameModelNam1234, Model_Name_XYZ
"Model Name XYZ" = Install_Section_XYZ, HWP9876, Model_Name_XYZ
```

 

