---
title: WDK and Visual Studio build environment
description: The Windows Driver Kit (WDK) 8.1 and WDK 8 introduced a major change to the environment that you use to build a driver.
ms.assetid: B964CF3F-ACDB-41ED-8962-B7DDB957D7D3
---

# WDK and Visual Studio build environment


The Windows Driver Kit (WDK) 8.1 and WDK 8 introduced a major change to the environment that you use to build a driver. The WDK no longer uses Build.exe. The WDK build environment for drivers uses MSBuild.exe and is fully integrated with the Visual Studio development environment. This means that source files, makefile.inc, makefile.new and other related build files present in the previous version of the WDK are no longer used. The WDK now enables you to create, edit, build, test, and deploy a driver through Visual Studio. The purpose of this document is to provide information to help users familiar with previous WDKs in getting started with the WDK 8.1 and WDK 8.

**Note**  Projects and solutions created with the WDK 8 must be upgraded to work with the WDK 8.1 and Microsoft Visual Studio 2013. Before you open the projects or solutions, run the [ProjectUpgradeTool](projectupgradetool.md). The ProjectUpgradeTool converts the projects and solutions so that they can be built using WDK 8.1.

 

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[MSBuild primer for WDK developers](msbuild-primer-for-wdk-developers.md)</p></td>
<td align="left"><p>This section introduces some basic MSBuild terminology to WDK developers, who are familiar with Build.exe and NMake.exe. This section shows the construction of simple MSBuild projects.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[WDK and MSBuild overview](wdk-and-msbuild-overview.md)</p></td>
<td align="left"><p>Visual Studio can manage multiple projects. This section describes the WDK build environment.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Platform Toolset](platform-toolset.md)</p></td>
<td align="left"><p>The Windows Driver Kit (WDK) takes advantage of the MSBuild platform toolset feature to provide tools and libraries that are specific to driver development. The MSBuild platform toolset feature is extensible. The specific version of the platform toolset that you want to use is controlled by an MSBuild property called <strong>PlatformToolset</strong>. Projects can switch between tools and libraries by setting the <strong>PlatformToolset</strong> property in the project file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Windows driver-specific property files](windows-driver-specific-property-files.md)</p></td>
<td align="left"><p>The driver property sheets have default settings for all of the tools that MSBuild uses to build any driver project.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Windows driver targets](windows-driver-targets.md)</p></td>
<td align="left"><p>The WindowsDriver.Common.targets, WindowsDriver.masm.targets, and WindowsDriver.arm.targets files provide the targets that are necessary to build a driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[WDK build output](wdk-build-output.md)</p></td>
<td align="left"><p>By default, the WDK uses the intermediate directory <strong>$(IntDir)</strong> macro to specify the default build output directory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[WDK tasks for MSBuild](wdk-tasks-for-msbuild.md)</p></td>
<td align="left"><p>The Windows Driver Kit (WDK) includes tools that are often used in the build process but are not normally distributed with Visual Studio. These tools are used to sign drivers or driver packages, implement software tracing, or to process and compile resource or message files (stampinf.exe, mc.exe, tracewpp.exe, binplace.exe, etc.). These command-line tools need to be exposed to MSBuild as tasks (contained in targets) so that they can be run during the build process. The WDK provides the necessary components so that you can run these tools as MSBuild tasks when you build your driver.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20WDK%20and%20Visual%20Studio%20build%20environment%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




