---
title: Conditional Compilation and the Build Environment
description: Conditional Compilation and the Build Environment
keywords:
- DBG preprocessor constant
- debugging code WDK , conditional compilation
- debugging code WDK , build environment
- conditional compilation WDK debugging
ms.date: 04/20/2017
---

# Conditional Compilation and the Build Environment


## <span id="ddk_conditional_compilation_and_the_build_environment_tools"></span><span id="DDK_CONDITIONAL_COMPILATION_AND_THE_BUILD_ENVIRONMENT_TOOLS"></span>


When you use Windows Driver Kit (WDK) 8 you can conditionally compile the debugging code in your driver by selecting the release (free) or debug (checked) configuration. The configuration you choose sets the **DBG** preprocessor constant.

The value of **DBG** depends on the build configuration you choose to build your driver:

-   If you create your driver using a debug (checked) configuration, **DBG** will equal 1.

-   If you create your driver by using a release (free) build configuration, **DBG** will equal 0 (or will be undefined if neither wdm.h nor ntddk.h is included).

The debugging routines [**ASSERT**](/previous-versions/windows/hardware/previsioning-framework/ff542107(v=vs.85)), [**ASSERTMSG**](/windows-hardware/drivers/ddi/wdm/nf-wdm-assertmsg), [**KdBreakPoint**](/previous-versions/windows/hardware/previsioning-framework/ff548063(v=vs.85)), [**KdBreakPointWithStatus**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kdbreakpointwithstatus), [**KdPrint**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kdprint), and [**KdPrintEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kdprintex) are actually macros that are conditionally defined depending on the value of **DBG**. If it is 0, these macros are no-ops. Therefore, these macros are active only in the debug (checked) build of a driver.

**Note**   All debugging routines beginning with the letters "Kd" have no effect in a free build of a driver, except for **KdRefreshDebuggerNotPresent**.

 

For more information about using Visual Studio and MSBuild to create to release and debug versions of a driver, see [Building a Driver](../develop/building-a-driver.md) and the [WDK and Visual Studio build environment](wdk-and-visual-studio-build-environment.md).

 

