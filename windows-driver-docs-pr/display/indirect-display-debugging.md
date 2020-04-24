---
title: Debugging Indirect Display Drivers
description: Describes debugging techniques for Indirect Displays
ms.assetid: a343812d-03d0-4a95-9c36-7e6b5a404088
ms.date: 04/22/2020
ms.localizationpriority: medium
---

# Debugging Indirect Displays

Indirect Displays drivers are UMDF drivers so the UMDF debugging documentation is a good starting point, [here](https://docs.microsoft.com/windows-hardware/drivers/wdf/determining-why-the-umdf-driver-fails-to-load-or-the-umdf-device-fails) is an example of a page in that section.  This page will provide Indirect Display specific debugging information.

## <span id="Registry_Control"></span><span id="registry_control"></span><span id="REGISTRY_CONTROL"></span>Registry Control

IddCx has some registry settings that can be used to aid debugging Indirect Display drivers.  All registry values are located under the **HKLM\System\CurrentControlSet\Control\GraphicsDrivers** registry key.


| Value Name               | Details |
|--------------------------|---------|
| TerminateIndirectOnStall | A zero value will disable the watchdog that terminates the driver if it does not process a frame within 10 seconds of the frame being available.  Any other value will leave the watchdog enabled. |
| IddCxDebugCtrl           | Bit-field that enabled different debug aspects of IddCx, see table below |

**NOTE** If the TerminateIndirectOnStall registry value is used to disable the watchdog HLK tests will fail.

### IddCxDebugCtrl values

| Bit in IddCxDebugCtrl | Meaning  |
|:---------------------:|----------|
| 0x0001 | Break into the debugger when IddCx detects an error |
| 0x0002 | Break into the debugger when IddCx is loaded |
| 0x0004 | Break into the debugger when IddCx is unloaded |
| 0x0008 | Break into the debugger when IddCx DriverEntry is called |
| 0x0010 | Break into the debugger when driver bind is called |
| 0x0020 | Break into the debugger when driver start is called |
| 0x0040 | Break into the debugger when driver unbind is called |
| 0x0080 | Disables the DDI watchdog which terminates driver is takes too long in DDI call |
| 0x0100 | Unused |
| 0x0200 | Enable debug overlay, see below |
| 0x0400 | Overlay colored alpha box over dirty rects in frame, requires 0x0200 to be set |
| 0x0800 | Overlay pref stats into frame, requires 0x0200 to be set |

**NOTE** For any of the overlay function to work the Direct3D device created by the driver and passed to IddCxSwapChainSetDevice() has to be created with the D3D11_CREATE_DEVICE_BGRA_SUPPORT flag.
