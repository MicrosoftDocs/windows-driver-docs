---
title: Breaking into a Debugger from KMDF Drivers
description: Breaking into a Debugger from KMDF Drivers
ms.assetid: b18e210c-cc9b-436c-b762-6346b946357c
keywords:
- debugging drivers WDK KMDF , breaking into the debugger
- breaking into the debugger WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





