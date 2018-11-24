---
ms.assetid: 47AC8BD7-7098-43C3-A198-3622D465B142
title: Avoiding Floating Point Errors in Custom Build Environments
description: This information is intended for developers and build engineers who compile kernel-mode drivers for Windows.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Avoiding Floating Point Errors in Custom Build Environments

This information is intended for developers and build engineers who compile kernel-mode drivers for Windows. In Microsoft Visual Studio Professional 2012, the default architecture for the Visual C++ (VC++) compiler changed from IA32 to the Streaming SIMD Extensions 2 (SSE2) instruction set. As a result of this change, SSE2 floating point (FP) instructions injected into the binary at compile time can generate floating-point errors if not accounted for. The issue can be encountered by those who use the Microsoft VC++ compiler, or a custom build environment to develop Windows drivers. However, the issue does not affect developers who use the Microsoft Visual Studio development environment, or who use the MSbuild utility to build drivers with an unmodified toolset.

## <span id="Floating_point_errors_can_cause_data_corruption_or_computer_crashes_"></span><span id="floating_point_errors_can_cause_data_corruption_or_computer_crashes_"></span><span id="FLOATING_POINT_ERRORS_CAN_CAUSE_DATA_CORRUPTION_OR_COMPUTER_CRASHES_"></span>Floating point errors can cause data corruption or computer crashes


If you compile a driver *without* using the WDK, Visual Studio, and the recommended platform toolset for Windows drivers (**WindowsKernelModeDriver8.0**), the driver might not manage floating point operations correctly, even if the driver compiles without errors.

The Visual Studio Professional 2012 VC++ compiler emits code that uses the SSE2 instruction set by setting the **/arch:sse2** compiler option. Starting with Visual Studio Professional 2012, this is the default option for x86 VC++ compiler code generation. Specifically, the default value changes from **/arch:ia32** to **/arch:sse2**.

For applications this change generates code that performs better and uses less processor time during execution. However, for kernel-mode drivers this change will not manage the floating point (FP) state properly. This is due to the VC++ compiler introducing FP instruction sequences in places where the context has not been saved. Any binary floating-point system can represent only a finite number of floating-point values in exact form, with the rest being approximations. The floating-point control state, such as, rounding mode or precision, is what keeps FP operations in sync with each other. When the state is undefined, this leads to FP calculation errors. These calculation errors are hard to detect because in most cases application state corruption is the only sign of this issue. This corruption can manifest itself in many ways, ranging from random crashes to data corruption.

## <span id="Solution"></span><span id="solution"></span><span id="SOLUTION"></span>Solution


To avoid these problem with floating-point calculations, add the **/kernel** flag to the C++ compiler and linker command lines to prevent generating SSE2 instructions. The **/kernel** flag changes the default **/arch:sse2** value back to **/arch:ia32**.

In addition, if you build a driver using the WDK and the Visual Studio Professional 2012 development environment, or use MSBuild, in a Visual Studio Command prompt window, the Microsoft provided platform toolset (**WindowsKernelModeDriver8.0**) sets the **/kernel** flag. As a result, floating-point generation errors are avoided.

```cpp
msbuild myProject.vcxproj /p:PlatformToolset=WindowsKernelModeDriver8.0
```

## <span id="Recommendations"></span><span id="recommendations"></span><span id="RECOMMENDATIONS"></span>Recommendations


Here are the recommended solutions based on the type of development environment you use:

-   **Microsoft tool set (MSBuild)** - No work required. Use **WindowsKernelModeDriver8.0** as the platform toolset the **/kernel** is automatically added where appropriate.
-   **Microsoft VC++ Compiler** - Add the **/kernel** flag to prevent compiler from emitting SSE2.
-   **Custom Tooling/Non-Microsoft Compiler** - You must manually account for the assembly instructions used in the resulting binary.

 

 





