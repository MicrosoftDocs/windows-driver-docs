---
title: Static Driver Verifier
description: Static Driver Verifier
ms.assetid: 74feeb16-387c-4796-987a-aff3fb79b556
keywords:
- verifying drivers WDK , Static Driver Verifier
- driver verification WDK , Static Driver Verifier
- Static Driver Verifier WDK
- StaticDV WDK
- SDV WDK
- paths WDK SDV
- compile-time static verification tool WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Static Driver Verifier


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Purpose</strong></p>
<p>Static Driver Verifier (also known as &quot;StaticDV&quot; or &quot;SDV&quot;) is a static verification tool that systematically analyzes the source code of Windows kernel-mode drivers. SDV is a compile time tool that is capable of discovering defects and design issues in a driver. Based on a set of interface rules and a model of the operating system, SDV determines whether the driver correctly interacts with the Windows operating system kernel.</p>
<p></p>
 
</div>
<p><strong>Visual Studio Integration</strong></p>
<p>Static Driver Verifier is integrated into Visual Studio. You can run static analysis on your Visual Studio driver project. You can launch, configure, and control Static Driver Verifier from the <strong>Driver</strong> menu in Visual Studio.</p>
<p><strong>Static Driver Verifier Documentation</strong></p>
<a href="https://docs.microsoft.com/windows-hardware/drivers/develop/static-driver-verifier-known-issues">Static Driver Verifier Known Issues</a>
<p>Lists latest known issues for Static Driver Verifier</p>
<a href="using-static-driver-verifier-to-find-defects-in-drivers.md" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](using-static-driver-verifier-to-find-defects-in-drivers.md)">Using Static Driver Verifier to Find Defects in Drivers</a>
<p>Tells you what you need to get started analyzing your driver code in the Visual Studio environment.</p>
<a href="-static-driver-verifier-commands--msbuild-.md" data-raw-source="[Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md)">Static Driver Verifier commands (MSBuild)</a>
<p>Lists the MSBuild commands to use to run SDV in a Visual Studio Command Prompt window.</p>
<a href="introducing-static-driver-verifier.md" data-raw-source="[Introducing Static Driver Verifier](introducing-static-driver-verifier.md)">Introducing Static Driver Verifier</a>
<p>Provides an overview of the static analysis tool.</p>
<a href="using-static-driver-verifier.md" data-raw-source="[Using Static Driver Verifier](using-static-driver-verifier.md)">Using Static Driver Verifier</a>
<p>Provides the details about using and configuring the static analysis tool.</p>
<a href="static-driver-verifier-report.md" data-raw-source="[Static Driver Verifier Report](static-driver-verifier-report.md)">Static Driver Verifier Report</a>
<p>Describes the viewer that displays the detailed trace of the static code analysis.</p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552840" data-raw-source="[Static Driver Verifier Rules](https://msdn.microsoft.com/library/windows/hardware/ff552840)">Static Driver Verifier Rules</a>
<p>The rules define the requirements for proper interaction between a driver model and the kernel interface of the operating system.</p>
<a href="static-driver-verifier-reference.md" data-raw-source="[Static Driver Verifier Reference](static-driver-verifier-reference.md)">Static Driver Verifier Reference</a>
<p>Provides reference information about the function role types, SDV configuration files, error, and warning messages.</p></td>
<td align="left"><p><em>Static Analysis can reduce defects by up to a factor of six!</em></p>
<p>— Capers Jones, Software Productivity Group</p>
<p><strong>Finding Bugs in Windows Driver Code</strong></p>
<p>Microsoft uses SDV to test the kernel-mode drivers that are included with the Microsoft Windows operating system and to test the sample drivers in the WDK. Prior to the release of Windows 8, Microsoft used SDV to find and fix 127 potentially critical bugs.</p>
<p>By using the DDI compliance rules for specific driver models, SDV can verify correct driver behavior. For example, SDV can verify that the driver:</p>
<ul>
<li><p>Calls functions at the correct IRQL</p></li>
<li><p>Acquires and releases locks in the correct sequence</p></li>
<li><p>Correctly uses functions that handle I/O request packets (IRP)</p></li>
</ul>
<p>SDV examines all possible paths through the driver code. It is designed to find serious errors in obscure paths that are unlikely to be encountered even in thorough testing.</p>
<p><strong>Resources</strong></p>
<p>For specific information about the drivers that SDV can verify, see <a href="supported-drivers.md" data-raw-source="[Supported Drivers](supported-drivers.md)">Supported Drivers</a>.</p>
<p>For more information and tips about using Static Driver Verifier, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=154232" data-raw-source="[Static Driver Tools blog](http://go.microsoft.com/fwlink/p/?linkid=154232)">Static Driver Tools blog</a>.</p></td>
</tr>
</tbody>
</table>

 

 

 

