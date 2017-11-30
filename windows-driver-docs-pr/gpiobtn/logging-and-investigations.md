---
title: Logging and investigations
author: windows-driver-content
description: This topic describes logging and investigations for GPIO implementations.
ms.assetid: 27D6349D-5F92-450B-B9AA-90BA9C5D7E65
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Logging%20and%20investigations%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


