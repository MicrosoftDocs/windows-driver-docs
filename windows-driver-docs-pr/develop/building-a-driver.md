---
ms.assetid: f5676c9c-b582-47d0-9b7c-02b6443103ad
title: Building a Driver with the WDK
description: This topic describes how to build a driver with the Windows Driver Kit (WDK).
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Building a Driver with Visual Studio and the WDK

This topic describes how you can build a driver with the Windows Driver Kit (WDK). WDK 10 is fully integrated with Microsoft Visual Studio. You can build a driver using the Visual Studio development environment, or you can build a driver directly from the command line by using the Microsoft Build Engine ([MSBuild](http://go.microsoft.com/fwlink/p/?linkid=262804)).

You can use any edition of Microsoft Visual Studio 2015, including Microsoft Visual Studio Community 2015, to build drivers for:

-   Windows 10
-   Windows 8.1
-   Windows 7

**Important**  Starting in Windows Driver Kit (WDK) 8, MSBuild replaced the Windows Build Utility (Build.exe). The WDK now uses the same compiler and build tools that you use to build Visual Studio projects. Driver projects that were built with previous versions of the WDK must be converted to work in the Visual Studio environment. You can run a conversion utility from the command line, or you can convert an existing driver by creating new Visual Studio project from existing sources. For more info, see [Creating a Driver From Existing Source Files](creating-a-driver-from-existing-source-files.md) and [WDK and the Visual Studio build environment](https://msdn.microsoft.com/library/windows/hardware/hh454286).

 

## <span id="building_a_driver_using_visual_studio"></span><span id="BUILDING_A_DRIVER_USING_VISUAL_STUDIO"></span>Building a Driver Using Visual Studio


You build a driver the same way you build any project or solution in Visual Studio. When you create a new driver project using a Windows driver template, the template defines a default (active) project configuration and a default (active) solution build configuration.

**Note**  You can convert projects and solutions that you created with WDK 8 or Windows Driver Kit (WDK) 8.1 to work with Windows Driver Kit (WDK) 10 and Visual Studio 2015. Before you open the projects or solutions, run the [ProjectUpgradeTool](https://msdn.microsoft.com/Library/Windows/Hardware/Dn265174). The ProjectUpgradeTool converts the projects and solutions so that they can be built using WDK 10.

 

For information about managing and editing build configurations, see [Building in Visual Studio](http://go.microsoft.com/fwlink/p/?linkid=227872).

The default Solution build configuration is **Debug** and **Win32**. In versions of the WDK prior to Windows 8, this build configuration would correspond to building a driver using an **x86 Checked Build Environment**.

**To select a configuration and build a driver**

1.  Ensure that you have the same version of SDK and WDK installed on your computer.
2.  Open the driver project or solution in Visual Studio.
3.  Right-click the solution in the **Solutions Explorer** and select **Configuration Manager**.
4.  From the **Configuration Manager**, select the **Active solution configuration** (for example, **Debug** or **Release**) and the **Active solution platform** (for example, **Win32**) that correspond to the type of build you are interested in.
5.  Right click the Avshws project and select **Properties**.  Navigate to **Driver Settings > General**, and set **Target OS Version** and **Target Platform**.
6.  Configure the project properties for your driver or driver package. You can set properties for deployment, driver signing, or other tasks. For more information, see [Configuring project properties for your driver and driver package](#configure_project_props).
7.  From the **Build** menu, click **Build Solution** (**Ctrl+Shift+B**).

## <span id="building_a_driver_using_the_command_line__msbuild_"></span><span id="BUILDING_A_DRIVER_USING_THE_COMMAND_LINE__MSBUILD_"></span>Building a Driver Using the Command Line (MSBuild)


You can build a driver from the command line using the **Visual Studio Command Prompt** window and the Microsoft Build Engine ([MSBuild](http://go.microsoft.com/fwlink/p/?linkid=262804))

**To build a driver using the Visual Studio Command Prompt window**

1.  Open a **Developer Command Prompt for VS2015** window.

    From this window you can use MSBuild.exe to build any Visual Studio project by specifying the project (.VcxProj) or solutions (.Sln) file.

2.  Navigate to the project directory and enter the **MSbuild** command for your target.

    For example, to perform a clean build of a Visual Studio driver project called MyDriver.vcxproj using the default Platform and Configuration, navigate to the project directory and enter the following MSBuild command:

    ```cpp
    msbuild /t:clean /t:build .\MyDriver.vcxproj
    ```

    **Syntax** - To specify a specific configuration and platform, use the following command syntax:

    ```cpp
    msbuild /t:clean /t:build ProjectFile /p:Configuration=<Debug|Release> /p:Platform=architecture /p:TargetPlatformVersion=a.b.c.d /p:TargetVersion=OS    
    ```

    For example, the following command builds a Universal Windows driver for the "Debug" configuration, "Win32" platform, and for Windows 10.

    ```cpp
    msbuild /t:clean /t:build .\MyDriver.vcxproj /p:Configuration="Debug" /p:Platform=Win32 /p:TargetVersion=”Windows10” /p:TargetPlatformVersion=”10.0.10010.0”
    ```

    The **TargetPlatformVersion** setting is optional and allows you to specify the kit version to build with. The default is to use the latest kit.

## <span id="configure_project_props"></span><span id="CONFIGURE_PROJECT_PROPS"></span>Configuring project properties for your driver and driver package


You use **property pages** to configure and set options for your driver and driver package. You can choose to configure your driver so that it is automatically signed when you build your solution, or automatically deployed to a remote test computer.

The WDK provides a number of command-line tools, such as [Stampinf](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786) and [WPP Preprocessor (WPP Tracing)](https://msdn.microsoft.com/Library/Windows/Hardware/Ff556201), that are commonly included in the build process. These tools are not distributed with Visual Studio. To combine these tools with the Visual Studio build environment they are wrapped as [WDK tasks for MSBuild](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454288). If you use one of the driver templates or have an existing driver that you have converted, these property pages might already exist for your project. If not, the property pages are automatically added to your project as you add the related file types to the project or solution (for example, .mc or .man files for the message compiler). For more information, see [WDK and the Visual Studio build environment](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454286)

You can set properties for an individual driver or for an entire driver package. The following table shows some of the available properties that you can configure specifically for drivers and driver packages.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Driver Project Properties</th>
<th align="left">Driver Package Properties</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Signing properties for individual driver files (see <a href="signing-a-driver.md" data-raw-source="[Signing a Driver](signing-a-driver.md)">Signing a Driver</a>)</p></td>
<td align="left"><p>Signing properties for driver packages (see <a href="signing-a-driver.md" data-raw-source="[Signing a Driver](signing-a-driver.md)">Signing a Driver</a>)</p></td>
</tr>
<tr class="even">
<td align="left"><a href="counters-manifest-preprocessor-properties-for-driver-projects.md" data-raw-source="[Counters Manifest Preprocessor Properties for Driver Projects](counters-manifest-preprocessor-properties-for-driver-projects.md)">Counters Manifest Preprocessor Properties for Driver Projects</a> (for <a href="https://msdn.microsoft.com/library/windows/desktop/aa372128" data-raw-source="[CTRPP](https://msdn.microsoft.com/library/windows/desktop/aa372128)">CTRPP</a>)</td>
<td align="left"><p><a href="deployment-properties-for-driver-projects.md" data-raw-source="[Deployment Properties for Driver Package Projects](deployment-properties-for-driver-projects.md)">Deployment Properties for Driver Package Projects</a> (see <a href="deploying-a-driver-to-a-test-computer.md" data-raw-source="[Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md)">Deploying a Driver to a Test Computer</a>)</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="driver-model-settings-properties-for-driver-projects.md" data-raw-source="[Driver Model Settings Properties for Driver Projects](driver-model-settings-properties-for-driver-projects.md)">Driver Model Settings Properties for Driver Projects</a></td>
<td align="left"><p><a href="driver-verifier-properties-for--driver-projects.md" data-raw-source="[Driver Verifier Properties for Driver Package Projects](driver-verifier-properties-for--driver-projects.md)">Driver Verifier Properties for Driver Package Projects</a></p></td>
</tr>
<tr class="even">
<td align="left"><a href="message-compiler-properties-for-driver-projects.md" data-raw-source="[Message Compiler Properties for Driver Projects](message-compiler-properties-for-driver-projects.md)">Message Compiler Properties for Driver Projects</a></td>
<td align="left"><p><a href="kmdf-verifier-properties-for-driver-package-projects.md" data-raw-source="[KMDF Verifier Properties for Driver Package Projects](kmdf-verifier-properties-for-driver-package-projects.md)">KMDF Verifier Properties for Driver Package Projects</a></p></td>
</tr>
<tr class="odd">
<td align="left"><a href="stampinf-properties-for-driver-projects.md" data-raw-source="[Stampinf Properties for Driver Projects](stampinf-properties-for-driver-projects.md)">Stampinf Properties for Driver Projects</a></td>
<td align="left"><p><a href="umdf-verifier-properties-for-driver-package-projects.md" data-raw-source="[UMDF Verifier Properties for Driver Package Projects](umdf-verifier-properties-for-driver-package-projects.md)">UMDF Verifier Properties for Driver Package Projects</a></p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff556201" data-raw-source="[WPP Preprocessor (WPP Tracing)](https://msdn.microsoft.com/Library/Windows/Hardware/Ff556201)">WPP Preprocessor (WPP Tracing)</a></td>
<td align="left"><p><a href="inf2cat-properties-for-driver-package-projects.md" data-raw-source="[Inf2Cat Properties for Driver Package Projects](inf2cat-properties-for-driver-package-projects.md)">Inf2Cat Properties for Driver Package Projects</a> (see the <a href="../devtest/inf2cat.md" data-raw-source="[&lt;strong&gt;Inf2Cat&lt;/strong&gt;](../devtest/inf2cat.md)"><strong>Inf2Cat</strong></a> tool)</p></td>
</tr>
</tbody>
</table>

 

## <span id="troubleshooting"></span><span id="TROUBLESHOOTING"></span>Troubleshooting tip for building a driver


The following tip can help you troubleshoot problems when you use the WDK and Visual Studio to build drivers.

**To increase the verbosity of the build output using the options in Visual Studio**

1.  Click **Tools**&gt; **Options**.
2.  Click the **Project and Solutions** folder and click **Build and Run**.
3.  Change the options for the **MSBuild project build output verbosity** and **MSBuild project build log file verbosity**. By default, these are set to Minimal.

## <span id="related_topics"></span>Related topics


* [Building in Visual Studio](http://go.microsoft.com/fwlink/p/?linkid=227872)
* [Building Drivers for Different Versions of Windows](building-drivers-for-different-versions-of-windows.md)
* [Using the Microsoft C Runtime with User-Mode Drivers and Desktop Apps](using-the-microsoft-c-runtime-with-user-mode-drivers-and-apps.md)
* [ProjectUpgradeTool](https://msdn.microsoft.com/Library/Windows/Hardware/Dn265174)
* [MSBuild](http://go.microsoft.com/fwlink/p/?linkid=262804)
* [Creating a Driver From Existing Source Files](creating-a-driver-from-existing-source-files.md)
* [WDK and the Visual Studio build environment](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454286)
* [Signing a Driver](signing-a-driver.md)
* [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md)







