---
title: Building Drivers for Different Versions of Windows
description: If you are writing drivers for different versions of Windows, the following section provides some guidelines about how you should build those drivers using the Windows Driver Kit, Visual Studio, and MSBuild.
ms.date: 03/14/2022
---

# Building Drivers for Different Versions of Windows

If you are [writing drivers for different versions of Windows](../gettingstarted/platforms-and-driver-versions.md), the following section provides some guidelines about how you should build those drivers using the Windows Driver Kit (WDK), Visual Studio, and MSBuild.

## <span id="Guidelines_that_apply_to_building_both_user-mode_and_kernel-mode_drivers"></span><span id="guidelines_that_apply_to_building_both_user-mode_and_kernel-mode_drivers"></span><span id="GUIDELINES_THAT_APPLY_TO_BUILDING_BOTH_USER-MODE_AND_KERNEL-MODE_DRIVERS"></span>Guidelines that apply to building both user-mode and kernel-mode drivers


-   Build your drivers using the target configurations and platforms that the WDK provides. Always use the latest version of the WDK that supports the version of Windows that you want to target. For info about WDK and operating system version support, see [Installing preview versions of the Windows Driver Kit](/windows-hardware/drivers/installing-preview-versions-wdk) and [Download the Windows Driver Kit](/windows-hardware/drivers/download-the-wdk).
-   If your driver must run only on a single version of Windows, build the driver for the target configuration and platform that matches your target Windows version.
-   If you want your driver to run on multiple versions of Windows, but without features that are available only on newer versions, build the driver for the oldest version that you want the driver to support.

If you are targeting Windows 7, Windows 8, or Windows 8.1, set **TargetVersion** using the Configuration Manager or manually in the .vcxproj file, for example `<TargetVersion>Windows7</TargetVersion>`.

If you are targeting Windows 10 or Windows 11, set both **TargetVersion** and **_NT_TARGET_VERSION**, for example `<TargetVersion>Windows10</TargetVersion>
<_NT_TARGET_VERSION>0xA000006</_NT_TARGET_VERSION>`.

**_NT_TARGET_VERSION** values are listed in the Sdkddkver.h header file in the form `NTDDI_WIN10_*`, for example `#define NTDDI_WIN10_RS5 0x0A000006`.

## <span id="Guidelines_that_apply_to_building_kernel-mode_drivers"></span><span id="guidelines_that_apply_to_building_kernel-mode_drivers"></span><span id="GUIDELINES_THAT_APPLY_TO_BUILDING_KERNEL-MODE_DRIVERS"></span>Guidelines that apply to building kernel-mode drivers


-   If you want your kernel-mode driver to run on multiple versions of Windows and dynamically determine the features that are available to the driver, build the driver using the build configuration for the most recent version of the operating system. For example, if you want your driver to support all versions of Windows starting with Windows 8.1, but to use certain features that were first available in Windows 10 when your driver is running on Windows 10 or later versions of the operating system, specify Windows 10 (**Win10**) as the target configuration.

-   Use the [**RtlIsNtDdiVersionAvailable**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlisntddiversionavailable) and [**RtlIsServicePackVersionInstalled**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlisservicepackversioninstalled) functions to determine the version of Windows that is available to your driver at run time. For more information, see [Writing drivers for different versions of Windows](../gettingstarted/platforms-and-driver-versions.md).
-   Create prototypes for pointers to functions that your driver must call conditionally.
-   If you have a WDM driver, or a non-KMDF kernel-mode driver, and you are targeting Windows 8.1 or Windows 8 but also want to run on earlier versions of Windows, you need to override the linker **$(KernelBufferOverflowLib)** option. When you select Windows 8 or Windows 8.1 configurations, the driver is linked with BufferOverflowFastFailK.lib, which is not available in earlier Windows versions. For Windows 7 and Vista, you must link with BufferOverflowK.lib instead.

    There are two ways to override the **$(KernelBufferOverflowLib)** linker option, using either MSBuild or Visual Studio.

    **Using MSBuild:**

    ```cpp
    msbuild /p:KernelBufferOverflowLib="C:\Program Files (x86)\Windows Kits\8.1\Lib\win8\km\x64\BufferOverflowK.lib" /p:platform=x64 /p:Configuration="Win8 Release" myDriver.sln
    ```

    **Using Visual Studio:**

    Using Notepad, or another text editor, open the driver project file (\*.vcxproj). In the project file, locate the **&lt;PropertyGroup&gt;** for the configurations your driver supports, and add the following line to override the default linker option:

    <span></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">XML</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code> 
       &lt;KernelBufferOverflowLib&gt;$(DDK_LIB_PATH)\BufferOverflowK.lib&lt;/KernelBufferOverflowLib&gt;
    </code></pre></td>
    </tr>
    </tbody>
    </table>

    For example, if your driver supports Windows 8.1 and Windows 8 debug and release builds, those configuration sections would look like the following:

    <span></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">XML</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>  &lt;PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Win8.1 Debug|Win32'" Label="Configuration"&gt;
        &lt;TargetVersion&gt;WindowsV6.3&lt;/TargetVersion&gt;
        &lt;UseDebugLibraries&gt;true&lt;/UseDebugLibraries&gt;
        &lt;KernelBufferOverflowLib&gt;$(DDK_LIB_PATH)\BufferOverflowK.lib&lt;/KernelBufferOverflowLib&gt;
        &lt;PlatformToolset&gt;WindowsKernelModeDriver8.1&lt;/PlatformToolset&gt;
        &lt;ConfigurationType&gt;Driver&lt;/ConfigurationType&gt;
        &lt;DriverType&gt;KMDF&lt;/DriverType&gt;
      &lt;/PropertyGroup&gt;
      &lt;PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Win8.1 Release|Win32'" Label="Configuration"&gt;
        &lt;TargetVersion&gt;WindowsV6.3&lt;/TargetVersion&gt;
        &lt;UseDebugLibraries&gt;false&lt;/UseDebugLibraries&gt;
        &lt;KernelBufferOverflowLib&gt;$(DDK_LIB_PATH)\BufferOverflowK.lib&lt;/KernelBufferOverflowLib&gt;
        &lt;PlatformToolset&gt;WindowsKernelModeDriver8.1&lt;/PlatformToolset&gt;
        &lt;ConfigurationType&gt;Driver&lt;/ConfigurationType&gt;
        &lt;DriverType&gt;KMDF&lt;/DriverType&gt;
      &lt;/PropertyGroup&gt;
      &lt;PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Win8 Debug|Win32'" Label="Configuration"&gt;
        &lt;TargetVersion&gt;Windows8&lt;/TargetVersion&gt;
        &lt;UseDebugLibraries&gt;true&lt;/UseDebugLibraries&gt;
        &lt;KernelBufferOverflowLib&gt;$(DDK_LIB_PATH)\BufferOverflowK.lib&lt;/KernelBufferOverflowLib&gt;
        &lt;PlatformToolset&gt;WindowsKernelModeDriver8.1&lt;/PlatformToolset&gt;
        &lt;ConfigurationType&gt;Driver&lt;/ConfigurationType&gt;
        &lt;DriverType&gt;KMDF&lt;/DriverType&gt;
      &lt;/PropertyGroup&gt;
      &lt;PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Win8 Release|Win32'" Label="Configuration"&gt;
        &lt;TargetVersion&gt;Windows8&lt;/TargetVersion&gt;
        &lt;UseDebugLibraries&gt;false&lt;/UseDebugLibraries&gt;
        &lt;KernelBufferOverflowLib&gt;$(DDK_LIB_PATH)\BufferOverflowK.lib&lt;/KernelBufferOverflowLib&gt;
        &lt;PlatformToolset&gt;WindowsKernelModeDriver8.1&lt;/PlatformToolset&gt;
        &lt;ConfigurationType&gt;Driver&lt;/ConfigurationType&gt;
        &lt;DriverType&gt;KMDF&lt;/DriverType&gt;
      &lt;/PropertyGroup&gt;</code></pre></td>
    </tr>
    </tbody>
    </table>

    The **&lt;KernelBufferOverflowLib&gt;** elements must appear in the driver project file before the element that imports Microsoft.Cpp.props, which imports the tool set.

    After you modify and save the driver project file, you can open the project file in Visual Studio and build the driver.

## <span id="how_to_customize_target_configuration"></span><span id="HOW_TO_CUSTOMIZE_TARGET_CONFIGURATION"></span>


## <span id="related_topics"></span>Related topics


* [Writing drivers for different versions of Windows](../gettingstarted/platforms-and-driver-versions.md)
* [Building a Driver](building-a-driver.md)
 

