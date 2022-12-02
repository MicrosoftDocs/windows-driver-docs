---
description: This article provides a brief overview about using Event Tracing for Windows (ETW) to examine USB selective suspend state and identifying system energy efficiency problems by using the Windows PowerCfg utility.
title: USB ETW and Power Management
ms.date: 12/02/2022
---

# USB ETW and power management

This article provides a brief overview about using Event Tracing for Windows (ETW) to examine USB selective suspend state and identifying system energy efficiency problems by using the Windows PowerCfg utility.

If a USB device driver supports [USB Selective Suspend](usb-selective-suspend.md), it can turn off the USB device when the device is idle. When the device is no longer idle, the system wakes the device and resumes normal operation. When the system is idle and all USB devices are suspended, no processor activity is required and therefore the processor enters a low-power state. Properly implementing selective suspend can result in significant power savings and increased battery life for mobile systems.

You can use USB ETW to examine USB devices and their drivers to validate whether they successfully go into selective suspend. Whether you are a system manufacturer, an IT professional, or a hardware developer, we encourage you to inspect your USB devices and drivers to ensure that they properly support selective suspend before you provide the devices to end users.

To help you identify system energy efficiency problems, we enhanced the Windows PowerCfg utility in Windows 7. PowerCfg is a command-line utility that is included with Windows that enables power policy enumeration and configuration. The enhancements to PowerCfg for determining energy efficiency problems are exercised by using the **[/energy](windows-hardware/design/device-experiences/powercfg-command-line-options#energy)** option. These enhancements enable PowerCfg to inspect the system for common energy efficiency problems and generate an HTML report that contains any issues that it found.

PowerCfg detects various energy efficiency problems, including ineffective use of selective suspend by USB devices, excessive processor utilization, increased timer resolution, inefficient power policy settings, and battery capacity degradation. PowerCfg identifies different levels of problems, including server problems (errors) and minor problems (warnings).

To generate a power efficiency diagnostics report using the PowerCfg utility, run the following command from an elevated command prompt:

```console
powercfg /energy
```

For more details, see [Guided Help: Get a detailed Power Efficiency Diagnostics Report](https://support.microsoft.com/topic/guided-help-get-a-detailed-power-efficiency-diagnostics-report-for-your-computer-in-windows-7-3f6ce138-fc04-7648-089a-854bcf332810).

For more about Windows power management and the PowerCfg tool, including the **[/energy](windows-hardware/design/device-experiences/powercfg-command-line-options#energy)** option, see [Powercfg Command-Line Options](/windows-hardware/design/device-experiences/powercfg-command-line-options).

## Related articles

- [USB Event Tracing for Windows](usb-event-tracing-for-windows.md)
- [Guided Help: Get a detailed Power Efficiency Diagnostics Report](https://support.microsoft.com/topic/guided-help-get-a-detailed-power-efficiency-diagnostics-report-for-your-computer-in-windows-7-3f6ce138-fc04-7648-089a-854bcf332810)
- [Powercfg Command-Line Options](/windows-hardware/design/device-experiences/powercfg-command-line-options)
