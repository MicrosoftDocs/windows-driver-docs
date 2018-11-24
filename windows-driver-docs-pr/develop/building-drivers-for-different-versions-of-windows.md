---
ms.assetid: 176A3794-E9E9-46C3-B242-422843436D2A
title: Building Drivers for Different Versions of Windows
description: If you are writing drivers for different versions of Windows, the following section provides some guidelines about how you should build those drivers using the Windows Driver Kit (WDK) 8.1 or WDK 8, Visual Studio, and MSBuild.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Building Drivers for Different Versions of Windows

If you are [writing drivers for different versions of Windows](https://msdn.microsoft.com/Library/Windows/Hardware/Ff554887), the following section provides some guidelines about how you should build those drivers using the Windows Driver Kit (WDK) 8.1 or WDK 8, Visual Studio, and MSBuild.

## <span id="Guidelines_that_apply_to_building_both_user-mode_and_kernel-mode_drivers"></span><span id="guidelines_that_apply_to_building_both_user-mode_and_kernel-mode_drivers"></span><span id="GUIDELINES_THAT_APPLY_TO_BUILDING_BOTH_USER-MODE_AND_KERNEL-MODE_DRIVERS"></span>Guidelines that apply to building both user-mode and kernel-mode drivers


-   Build your drivers using the target configurations and platforms that the WDK provides. Always use the latest version of the WDK that supports the version of Windows that you want to target. For example, to build drivers for Windows XP, you must use the Windows 7 WDK. But if you are building a driver for Windows 8.1, Windows 8, Windows 7, use the WDK 8.1 and Visual Studio.
-   If your driver must run only on a single version of Windows, build the driver for the target configuration and platform that matches your target Windows version. For example, if you are building a driver that will run only on WDK 8.1, specify **Win8.1** in the Configuration Manager.
-   If you want your driver to run on multiple versions of Windows, but without features that are available only on newer versions, build the driver for the oldest version that you want the driver to support. For example, if your driver will run on all Windows versions starting with Windows Vista and it will use only features that are provided on Windows Vista, specify **Vista** for the project configuration.

## <span id="Guidelines_that_apply_to_building_kernel-mode_drivers"></span><span id="guidelines_that_apply_to_building_kernel-mode_drivers"></span><span id="GUIDELINES_THAT_APPLY_TO_BUILDING_KERNEL-MODE_DRIVERS"></span>Guidelines that apply to building kernel-mode drivers


-   If you want your kernel-mode driver to run on multiple versions of Windows and dynamically determine the features that are available to the driver, build the driver using the build configuration for the most recent version of the operating system. For example, if you want your driver to support all versions of Windows starting with Windows 7, but to use certain features that were first available in Windows 8.1 when your driver is running on Windows 8.1 or later versions of the operating system, specify Windows 8.1 (**Win8.1**) as the target configuration.

-   Use the [**RtlIsNtDdiVersionAvailable**](https://msdn.microsoft.com/Library/Windows/Hardware/Ff561954) and [**RtlIsServicePackVersionInstalled**](https://msdn.microsoft.com/Library/Windows/Hardware/Ff561956) functions to determine the version of Windows that is available to your driver at run time. For more information, see [Writing drivers for different versions of Windows](https://msdn.microsoft.com/Library/Windows/Hardware/Ff554887).
-   Create prototypes for pointers to functions that your driver must call conditionally.
-   If you have a WDM driver, or a non-KMDF kernel-mode driver, and you are targeting Windows 8.1 or Windows 8 but also want to run on earlier versions of Windows, you need to override the linker **$(KernelBufferOverflowLib)** option. When you select Windows 8 or Windows 8.1 configurations, the driver is linked with BufferOverflowFastFailK.lib, which is not available in earlier Windows versions. For Windows 7 and Vista, you must link with BufferOverflowK.lib instead.

    There are two ways to override the **$(KernelBufferOverflowLib)** linker option, using either MSBuild or Visual Studio.

    **Using MSBuild:**

    ```cpp
    msbuild /p:KernelBufferOverflowLib="C:\Program Files (x86)\Windows Kits\8.1\Lib\win8\km\x64\BufferOverflowK.lib" /p:platform=x64 /p:Configuration="Win8 Release" myDriver.sln
    ```

    **Using Visual Studio:**

    Using Notepad, or another text editor, open the driver project file (\*.vcxproj). In the project file, locate the **&lt;PropertyGroup&gt;** for the configurations your driver supports, and add the following line to override the default linker option:

    <span codelanguage="XML"></span>
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

    <span codelanguage="XML"></span>
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
    <td align="left"><pre><code>  &lt;PropertyGroup Condition=&quot;&#39;$(Configuration)|$(Platform)&#39;==&#39;Win8.1 Debug|Win32&#39;&quot; Label=&quot;Configuration&quot;&gt;
        &lt;TargetVersion&gt;WindowsV6.3&lt;/TargetVersion&gt;
        &lt;UseDebugLibraries&gt;true&lt;/UseDebugLibraries&gt;
        &lt;KernelBufferOverflowLib&gt;$(DDK_LIB_PATH)\BufferOverflowK.lib&lt;/KernelBufferOverflowLib&gt;
        &lt;PlatformToolset&gt;WindowsKernelModeDriver8.1&lt;/PlatformToolset&gt;
        &lt;ConfigurationType&gt;Driver&lt;/ConfigurationType&gt;
        &lt;DriverType&gt;KMDF&lt;/DriverType&gt;
      &lt;/PropertyGroup&gt;
      &lt;PropertyGroup Condition=&quot;&#39;$(Configuration)|$(Platform)&#39;==&#39;Win8.1 Release|Win32&#39;&quot; Label=&quot;Configuration&quot;&gt;
        &lt;TargetVersion&gt;WindowsV6.3&lt;/TargetVersion&gt;
        &lt;UseDebugLibraries&gt;false&lt;/UseDebugLibraries&gt;
        &lt;KernelBufferOverflowLib&gt;$(DDK_LIB_PATH)\BufferOverflowK.lib&lt;/KernelBufferOverflowLib&gt;
        &lt;PlatformToolset&gt;WindowsKernelModeDriver8.1&lt;/PlatformToolset&gt;
        &lt;ConfigurationType&gt;Driver&lt;/ConfigurationType&gt;
        &lt;DriverType&gt;KMDF&lt;/DriverType&gt;
      &lt;/PropertyGroup&gt;
      &lt;PropertyGroup Condition=&quot;&#39;$(Configuration)|$(Platform)&#39;==&#39;Win8 Debug|Win32&#39;&quot; Label=&quot;Configuration&quot;&gt;
        &lt;TargetVersion&gt;Windows8&lt;/TargetVersion&gt;
        &lt;UseDebugLibraries&gt;true&lt;/UseDebugLibraries&gt;
        &lt;KernelBufferOverflowLib&gt;$(DDK_LIB_PATH)\BufferOverflowK.lib&lt;/KernelBufferOverflowLib&gt;
        &lt;PlatformToolset&gt;WindowsKernelModeDriver8.1&lt;/PlatformToolset&gt;
        &lt;ConfigurationType&gt;Driver&lt;/ConfigurationType&gt;
        &lt;DriverType&gt;KMDF&lt;/DriverType&gt;
      &lt;/PropertyGroup&gt;
      &lt;PropertyGroup Condition=&quot;&#39;$(Configuration)|$(Platform)&#39;==&#39;Win8 Release|Win32&#39;&quot; Label=&quot;Configuration&quot;&gt;
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


* [Writing drivers for different versions of Windows](https://msdn.microsoft.com/Library/Windows/Hardware/Ff554887)
* [Building a Driver](building-a-driver.md)
 

 






