---
title: Reporting Device Power Capabilities
author: windows-driver-content
description: Reporting Device Power Capabilities
MS-HAID:
- 'PwrMgmt\_d2fc0773-52ee-49ba-bd25-9a189a6dfd25.xml'
- 'kernel.reporting\_device\_power\_capabilities'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 67a504d0-2c41-4c74-a912-4f0771885f7d
keywords: ["reporting device power capabilities", "device power capabilities WDK kernel", "DEVICE_CAPABILITIES structure", "query-capabilities IRPs WDK power management", "IRPs WDK power management", "I/O request packets WDK power management"]
---

# Reporting Device Power Capabilities


## <a href="" id="ddk-reporting-device-power-capabilities-kg"></a>


During enumeration, drivers report device-specific information in response to a PnP [**IRP\_MN\_QUERY\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664) request. Along with other such information, drivers report a device's power management capabilities in the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure. Typically, the bus driver fills in this structure.

Higher-level drivers should set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine for the query-capabilities IRP so that they can make a local copy of the structure and ensure that it contains appropriate values. As a general rule, higher-level drivers should not change these values. However, if a change is necessary, a driver can further restrict device capabilities but cannot add to them. In other words, a driver can make the rules more restrictive but cannot loosen them.

After the IRP is complete and all drivers' completion routines have been run, the structure is cached and a driver cannot change its contents.

The following members of the **DEVICE\_CAPABILITIES** structure pertain to power management:

[DeviceD1 and DeviceD2](deviced1-and-deviced2.md)

[WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3](wakefromd0--wakefromd1--wakefromd2--and-wakefromd3.md)

[DeviceState](devicestate.md)

[SystemWake](systemwake.md)

[DeviceWake](devicewake.md)

[D1Latency, D2Latency, and D3Latency](d1latency--d2latency--and-d3latency.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Reporting%20Device%20Power%20Capabilities%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


