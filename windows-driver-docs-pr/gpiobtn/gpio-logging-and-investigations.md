---
title: GPIO logging and investigations
description: This topic describes logging and investigations for GPIO testing.
ms.assetid: 998BF6BC-D931-4555-A8BC-F860DFA9A18F
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GPIO logging and investigations


This topic describes logging and investigations for GPIO testing.

LogMan:

``` syntax
logman start -ets buttonTrace -p {5a81715a-84c0-4def-ae38-edde40df5b3a} 0xFFFFFFFF 4
<repro>

logman stop -ets buttonTrace
```

**Note**  
This is a WPP trace.

 

If a test fails, logging can help diagnose whether the appropriate injection was performed. For example, if a dock indicator change is expected, the following entry should be found in the log at the time that the notification is triggered.

``` syntax
--- start of log ---
10: Indicator_EvtDevicePrepareHardware - Received 0 resource descriptors, assuming indicator status will be injected via WriteFile
11: Indicator_EvtIoWrite - Indicator state change : DockMode_Indicator : old state : NotDocked
12: Indicator_UpdateRegistryValue - Indicator state update : DockMode_Indicator : new state : Docked
```

For additional guidance on how to implement the indicator injection, see the [GPIO buttons and indicators implementation guide for Windows 8.1](gpio-buttons-and-indicators-implementation-guide-for-windows-8-1.md).

 

 




