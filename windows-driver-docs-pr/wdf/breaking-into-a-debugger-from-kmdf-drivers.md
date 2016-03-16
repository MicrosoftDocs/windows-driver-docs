---
title: Breaking into a Debugger from KMDF Drivers
description: Breaking into a Debugger from KMDF Drivers
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: b18e210c-cc9b-436c-b762-6346b946357c
keywords: ["debugging drivers WDK KMDF breaking into the debugger", "breaking into the debugger WDK KMDF"]
---

# Breaking into a Debugger from KMDF Drivers


If you want your framework-based driver to break into a kernel-mode debugger, you can use the following:

-   The [**WdfVerifierDbgBreakPoint**](https://msdn.microsoft.com/library/windows/hardware/ff551164) function breaks into the debugger if the [DbgBreakOnError](registry-values-for-debugging-kmdf-drivers.md) value is set in the registry.

-   The [**WDFVERIFY**](https://msdn.microsoft.com/library/windows/hardware/ff551167) macro tests a logical expression and breaks into the kernel debugger if the expression evaluates to **FALSE** and if the [VerifyOn](registry-values-for-debugging-kmdf-drivers.md) value is set in the registry.

-   The [**VERIFY\_IS\_IRQL\_PASSIVE\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff545588) macro breaks into the kernel debugger if the driver is not executing at IRQL = PASSIVE\_LEVEL and if the **VerifyOn** value is set in the registry.

-   The [**ASSERT**](https://msdn.microsoft.com/library/windows/hardware/ff542107) macro tests a logical expression and breaks into the kernel debugger if the expression evaluates to **FALSE**.

-   The [**ASSERTMSG**](https://msdn.microsoft.com/library/windows/hardware/ff542113) macro tests an expression and, if the expression evaluates to **FALSE**, breaks into the kernel debugger and supplies a displayable text message to the debugger.

-   The [**DbgPrintEx**](https://msdn.microsoft.com/library/windows/hardware/ff543634) and [**KdPrintEx**](https://msdn.microsoft.com/library/windows/hardware/ff548100) functions supply a displayable text message to the debugger.

The code for the WDFVERIFY and VERIFY\_IS\_IRQL\_PASSIVE\_LEVEL macros is included in your driver when you build your driver in a release or debug configuration (referred to as a free build environment or a checked build environment in Windows 7 and earlier). The code for the ASSERT and ASSERTMSG macros is included in your driver only when you build your driver in a debug configuration.

For more information about project configurations, see [Building a Driver](https://msdn.microsoft.com/windows-drivers/develop/building_a_driver).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Breaking%20into%20a%20Debugger%20from%20KMDF%20Drivers%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




