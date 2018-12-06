---
Description: This topic provides a brief overview about using ETW to examine USB selective suspend state and identifying system energy efficiency problems by using the Windows PowerCfg utility.
title: USB ETW and Power Management
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB ETW and Power Management


This topic provides a brief overview about using ETW to examine USB selective suspend state and identifying system energy efficiency problems by using the Windows PowerCfg utility.

If a USB device driver supports [USB Selective Suspend](usb-selective-suspend.md), it can turn off the USB device when the device is idle. When the device is no longer idle, the system wakes the device and resumes normal operation. When the system is idle and all USB devices are suspended, no processor activity is required and therefore the processor enters a low-power state. Properly implementing selective suspend can result in significant power savings and increased battery life for mobile systems.

You can use USB ETW to examine USB devices and their drivers to validate whether they successfully go into selective suspend. Whether you are a system manufacturer, an IT professional, or a hardware developer, we encourage you to inspect your USB devices and drivers to ensure that they properly support selective suspend before you provide the devices to end users.

To help you identify system energy efficiency problems, we enhanced the Windows PowerCfg utility in Windows 7. PowerCfg is a command-line utility that is included with Windows that enables power policy enumeration and configuration. The enhancements to PowerCfg for determining energy efficiency problems are exercised by using the **-ENERGY** parameter. These enhancements enable PowerCfg to inspect the system for common energy efficiency problems and generate an HTML report that contains any issues that it found.

PowerCfg detects various energy efficiency problems, including ineffective use of selective suspend by USB devices, excessive processor utilization, increased timer resolution, inefficient power policy settings, and battery capacity degradation. PowerCfg identifies different levels of problems, including server problems (errors) and minor problems (warnings).

For more about Windows power management and the PowerCfg tool, see [Powercfg Command-Line Options](http://technet.microsoft.com/library/cc748940(WS.10).aspx) and [Using PowerCfg to Evaluate System Energy Efficiency](https://msdn.microsoft.com/library/windows/hardware/gg463250.aspx).

## Related topics
[USB Event Tracing for Windows](usb-event-tracing-for-windows.md)  



