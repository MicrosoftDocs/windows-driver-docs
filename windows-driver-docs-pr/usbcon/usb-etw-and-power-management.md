---
Description: 'This topic provides a brief overview about using ETW to examine USB selective suspend state and identifying system energy efficiency problems by using the Windows PowerCfg utility.'
MS-HAID: 'buses.usb\_etw\_and\_power\_management'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: USB ETW and Power Management
---

# USB ETW and Power Management


This topic provides a brief overview about using ETW to examine USB selective suspend state and identifying system energy efficiency problems by using the Windows PowerCfg utility.

If a USB device driver supports [USB Selective Suspend](usb-selective-suspend.md), it can turn off the USB device when the device is idle. When the device is no longer idle, the system wakes the device and resumes normal operation. When the system is idle and all USB devices are suspended, no processor activity is required and therefore the processor enters a low-power state. Properly implementing selective suspend can result in significant power savings and increased battery life for mobile systems.

You can use USB ETW to examine USB devices and their drivers to validate whether they successfully go into selective suspend. Whether you are a system manufacturer, an IT professional, or a hardware developer, we encourage you to inspect your USB devices and drivers to ensure that they properly support selective suspend before you provide the devices to end users.

To help you identify system energy efficiency problems, we enhanced the Windows PowerCfg utility in Windows 7. PowerCfg is a command-line utility that is included with Windows that enables power policy enumeration and configuration. The enhancements to PowerCfg for determining energy efficiency problems are exercised by using the **-ENERGY** parameter. These enhancements enable PowerCfg to inspect the system for common energy efficiency problems and generate an HTML report that contains any issues that it found.

PowerCfg detects various energy efficiency problems, including ineffective use of selective suspend by USB devices, excessive processor utilization, increased timer resolution, inefficient power policy settings, and battery capacity degradation. PowerCfg identifies different levels of problems, including server problems (errors) and minor problems (warnings).

For more about Windows power management and the PowerCfg tool, see [Powercfg Command-Line Options](http://technet.microsoft.com/library/cc748940(WS.10).aspx) and [Using PowerCfg to Evaluate System Energy Efficiency](http://msdn.microsoft.com/library/windows/hardware/gg463250.aspx).

## Related topics


[USB Event Tracing for Windows](usb-event-tracing-for-windows.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20ETW%20and%20Power%20Management%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




