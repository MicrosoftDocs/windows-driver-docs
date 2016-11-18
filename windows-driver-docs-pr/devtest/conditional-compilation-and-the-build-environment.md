---
title: Conditional Compilation and the Build Environment
description: Conditional Compilation and the Build Environment
ms.assetid: 7879b6c6-4985-4817-a8bc-b287397df721
keywords: ["DBG preprocessor constant", "debugging code WDK , conditional compilation", "debugging code WDK , build environment", "conditional compilation WDK debugging"]
---

# Conditional Compilation and the Build Environment


## <span id="ddk_conditional_compilation_and_the_build_environment_tools"></span><span id="DDK_CONDITIONAL_COMPILATION_AND_THE_BUILD_ENVIRONMENT_TOOLS"></span>


When you use Windows Driver Kit (WDK) 8 you can conditionally compile the debugging code in your driver by selecting the release (free) or debug (checked) configuration. The configuration you choose sets the **DBG** preprocessor constant.

The value of **DBG** depends on the build configuration you choose to build your driver:

-   If you create your driver using a debug (checked) configuration, **DBG** will equal 1.

-   If you create your driver by using a release (free) build configuration, **DBG** will equal 0 (or will be undefined if neither wdm.h nor ntddk.h is included).

The debugging routines [**ASSERT**](https://msdn.microsoft.com/library/windows/hardware/ff542107), [**ASSERTMSG**](https://msdn.microsoft.com/library/windows/hardware/ff542113), [**KdBreakPoint**](https://msdn.microsoft.com/library/windows/hardware/ff548063), [**KdBreakPointWithStatus**](https://msdn.microsoft.com/library/windows/hardware/ff548065), [**KdPrint**](https://msdn.microsoft.com/library/windows/hardware/ff548092), and [**KdPrintEx**](https://msdn.microsoft.com/library/windows/hardware/ff548100) are actually macros that are conditionally defined depending on the value of **DBG**. If it is 0, these macros are no-ops. Therefore, these macros are active only in the debug (checked) build of a driver.

**Note**   All debugging routines beginning with the letters "Kd" have no effect in a free build of a driver, except for **KdRefreshDebuggerNotPresent**.

 

For more information about using Visual Studio and MSBuild to create to release and debug versions of a driver, see [Building a Driver](https://msdn.microsoft.com/windows-drivers/develop/building_a_driver) and the [WDK and Visual Studio build environment](wdk-and-visual-studio-build-environment.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Conditional%20Compilation%20and%20the%20Build%20Environment%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




