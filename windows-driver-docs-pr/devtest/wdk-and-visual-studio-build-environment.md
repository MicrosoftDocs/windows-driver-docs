---
title: WDK and Visual Studio build environment
description: The Windows Driver Kit (WDK) 8.1 and WDK 8 introduced a major change to the environment that you use to build a driver.
ms.assetid: B964CF3F-ACDB-41ED-8962-B7DDB957D7D3
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="msbuild-primer-for-wdk-developers.md" data-raw-source="[MSBuild primer for WDK developers](msbuild-primer-for-wdk-developers.md)">MSBuild primer for WDK developers</a></p></td>
<td align="left"><p>This section introduces some basic MSBuild terminology to WDK developers, who are familiar with Build.exe and NMake.exe. This section shows the construction of simple MSBuild projects.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdk-and-msbuild-overview.md" data-raw-source="[WDK and MSBuild overview](wdk-and-msbuild-overview.md)">WDK and MSBuild overview</a></p></td>
<td align="left"><p>Visual Studio can manage multiple projects. This section describes the WDK build environment.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="platform-toolset.md" data-raw-source="[Platform Toolset](platform-toolset.md)">Platform Toolset</a></p></td>
<td align="left"><p>The Windows Driver Kit (WDK) takes advantage of the MSBuild platform toolset feature to provide tools and libraries that are specific to driver development. The MSBuild platform toolset feature is extensible. The specific version of the platform toolset that you want to use is controlled by an MSBuild property called <strong>PlatformToolset</strong>. Projects can switch between tools and libraries by setting the <strong>PlatformToolset</strong> property in the project file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="windows-driver-specific-property-files.md" data-raw-source="[Windows driver-specific property files](windows-driver-specific-property-files.md)">Windows driver-specific property files</a></p></td>
<td align="left"><p>The driver property sheets have default settings for all of the tools that MSBuild uses to build any driver project.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="windows-driver-targets.md" data-raw-source="[Windows driver targets](windows-driver-targets.md)">Windows driver targets</a></p></td>
<td align="left"><p>The WindowsDriver.Common.targets, WindowsDriver.masm.targets, and WindowsDriver.arm.targets files provide the targets that are necessary to build a driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdk-build-output.md" data-raw-source="[WDK build output](wdk-build-output.md)">WDK build output</a></p></td>
<td align="left"><p>By default, the WDK uses the intermediate directory <strong>$(IntDir)</strong> macro to specify the default build output directory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdk-tasks-for-msbuild.md" data-raw-source="[WDK tasks for MSBuild](wdk-tasks-for-msbuild.md)">WDK tasks for MSBuild</a></p></td>
<td align="left"><p>The Windows Driver Kit (WDK) includes tools that are often used in the build process but are not normally distributed with Visual Studio. These tools are used to sign drivers or driver packages, implement software tracing, or to process and compile resource or message files (stampinf.exe, mc.exe, tracewpp.exe, binplace.exe, etc.). These command-line tools need to be exposed to MSBuild as tasks (contained in targets) so that they can be run during the build process. The WDK provides the necessary components so that you can run these tools as MSBuild tasks when you build your driver.</p></td>
</tr>
</tbody>
</table>

 

 

 





