---
title: Printer Connected to an Infrared Port
description: Printer Connected to an Infrared Port
ms.assetid: 8545cf66-9b5c-41e8-82e0-e0edd75ad41b
keywords:
- infrared ports WDK printer
- IR ports WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer Connected to an Infrared Port





Printers connected over an infrared (IR) port do not support Plug and Play using the 1284 device string. For a computer with an IR port, a service constantly polls for devices. When an IR Plug and Play printer is brought within range, a PDO is created under Enum\\Root\\ with a [*device ID*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-id) of the form HWP*nnnn*. The [*hardware ID*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-id) of the [*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode) has a single entry of the form HWP*nnnn*.

The [**INF Manufacturer section**](https://msdn.microsoft.com/library/windows/hardware/ff547454) entries for a printer that supports Plug and Play over LPT and IR ports should appear similar to the following:

```cpp
 
"Model Name XYZ" = Install_Section_XYZ, LPTENUM\Company_NameModelNam1234, Company_NameModelNam1234, Model_Name_XYZ
"Model Name XYZ" = Install_Section_XYZ, HWP9876, Model_Name_XYZ
```

 

 




