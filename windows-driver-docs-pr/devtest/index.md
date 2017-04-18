---
title: Driver Development Tools
description: Driver Development Tools
ms.assetid: 1d384d73-d1d2-445f-8077-40eed1f99a8c
keywords: ["tools WDK", "driver development tools WDK", "WsdCodeGen tool WDK", "tools WDK , developing drivers", "Web Services for Devices WDK WIA , tools"]
---

# Driver Development Tools


## <span id="ddk_driver_development_tools_tools"></span><span id="DDK_DRIVER_DEVELOPMENT_TOOLS_TOOLS"></span>


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Purpose</strong></p>
<p>The Windows Driver Kit (WDK) provides a set of tools that you can use to develop, analyze, build, install, and test your driver. The WDK includes powerful verification tools that are designed to help you detect, analyze, and correct errors in driver code during the development process. Many of these tools can be used very early in the development process where they are most critical and can save you the most time and effort.</p>
<p><strong>Overview</strong></p>
<p>The Windows Driver Kit (WDK) is fully integrated with Microsoft Visual Studio 2015. The WDK uses the same compiler and build tools that you use to build Visual Studio projects. The code analysis and verification tools can now be easily configured and launched from the Visual Studio development environment, so that you can find and fix problems in your driver source early in the development cycle.</p>
<p>The WDK provides a sophisticated driver test framework and a set of device fundamental tests that you can use to automatically build, deploy, and test your driver on remote test systems. The WDK provides the tools to make testing and debugging drivers more convenient and effective than before.</p>
<p><strong>Driver Development Tools Documentation</strong></p>
<p>This section describes the tools and techniques that can help you during development:</p>
<p>[Tools for INF Files](tools-for-inf-files.md)</p>
<p>[Tools for Changing Boot Options for Driver Testing and Debugging](boot-options-for-driver-testing-and-debugging.md)</p>
<p>[Tools for Building Drivers](tools-for-building-drivers.md)</p>
<p>[Tools for Signing Drivers](tools-for-signing-drivers.md)</p>
<p>[Tools for Testing Drivers](tools-for-testing-drivers.md)</p>
<p>[Tools for Verifying Drivers](tools-for-verifying-drivers.md)</p>
<p>[Tools for Software Tracing](tools-for-software-tracing.md)</p>
<p>[Tools for Debugging Drivers](tools-for-debugging-drivers.md)</p>
<p>[Tools for Device Metadata Packages](tools-for-device-metadata-packages.md)</p></td>
<td align="left"><p><strong>Resources</strong></p>
<p>[Getting Started with Universal Windows Drivers](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers)</p>
<p>Universal Windows drivers allow developers to create a single driver that runs across multiple different device types, from embedded systems to tablets and desktop PCs. Hardware developers can use their existing components and device drivers across different form factors.</p>
<p>[Converting WDK 8.1 Projects to WDK 10](https://msdn.microsoft.com/windows-drivers/develop/converting_wdk_8_1_projects_to_wdk_10)</p>
<p>You can convert projects and solutions that you created with WDK 8 or Windows Driver Kit (WDK) 8.1 to work with Windows Driver Kit (WDK) 10 and Visual Studio 2015. Before you open the projects or solutions, run the ProjectUpgradeTool. The ProjectUpgradeTool converts the projects and solutions so that they can be built using WDK for Windows 10.</p>
<p></p>
<p>[Validating Universal Windows drivers](https://msdn.microsoft.com/windows-drivers/develop/validating_universal_drivers)</p>
<p>You can use the ApiValidator.exe tool to verify that the APIs that your driver calls are valid for a Universal Windows driver. The tool returns an error if your driver calls an API that is outside the set of valid APIs for Universal Windows drivers. This tool is part of the WDK for Windows 10.</p>
[WDK and Visual Studio build environment](wdk-and-visual-studio-build-environment.md)
<p>More information and tips for driver developers about using the WDK and the Visual Studio build environment.</p>
[Developing, Testing, and Deploying Drivers](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment)
<p>For specific information about building drivers, and using the verification tools and tests in the Visual Studio development environment.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Driver%20Development%20Tools%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




