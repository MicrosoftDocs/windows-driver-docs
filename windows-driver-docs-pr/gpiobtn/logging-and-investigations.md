---
title: Logging and investigations
description: This topic describes logging and investigations for GPIO implementations.
ms.assetid: 27D6349D-5F92-450B-B9AA-90BA9C5D7E65
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Logging and investigations


This topic describes logging and investigations for GPIO implementations.

## <span id="Live_debug_prints_from_the_kernel_debugger"></span><span id="live_debug_prints_from_the_kernel_debugger"></span><span id="LIVE_DEBUG_PRINTS_FROM_THE_KERNEL_DEBUGGER"></span>Live debug prints from the kernel debugger


``` syntax
!wmitrace.start buttonTrace -kd ; !wmitrace.enable buttonTrace {5a81715a-84c0-4def-ae38-edde40df5b3a} -level 4 -flag 0xFFFFFFFF
<repro>
!wmitrace.stop buttonTrace
```

## <span id="Logs_and_investigations"></span><span id="logs_and_investigations"></span><span id="LOGS_AND_INVESTIGATIONS"></span>Logs and investigations


IFR log from KD:

``` syntax
!rcdrkd msgpiowin32 
```

LogMan:

``` syntax
 
logman start -ets buttonTrace -p {5a81715a-84c0-4def-ae38-edde40df5b3a} 0xFFFFFFFF 4
<repro>
logman stop -ets buttonTrace
```

### <span id="Validations"></span><span id="validations"></span><span id="VALIDATIONS"></span>Validations

You can use IFR log or Logman to validate that the state is correctly toggled.

For example, if a dock indicator change is expected, the following entry should be found in the log at the time that the notification is triggered.

``` syntax
--- start of log ---
10: Indicator_EvtDevicePrepareHardware - Received 0 resource descriptors, assuming indicator status will be injected via WriteFile
11: Indicator_EvtIoWrite - Indicator state change : DockMode_Indicator : old state : NotDocked
12: Indicator_UpdateRegistryValue - Indicator state update : DockMode_Indicator : new state : Docked
```

 

 




