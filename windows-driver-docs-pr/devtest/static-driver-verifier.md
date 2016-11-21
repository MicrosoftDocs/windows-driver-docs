---
title: Static Driver Verifier
description: Static Driver Verifier
ms.assetid: 74feeb16-387c-4796-987a-aff3fb79b556
keywords: ["verifying drivers WDK , Static Driver Verifier", "driver verification WDK , Static Driver Verifier", "Static Driver Verifier WDK", "StaticDV WDK", "SDV WDK", "paths WDK SDV", "compile-time static verification tool WDK"]
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
<div class="alert">
<strong>Note</strong>  
<p>Windows 10 WDK Version 1511</p>
<p>A critical issue has been found when using Static Driver Verifier (SDV) when used with Visual Studio 2015 Update 1. Static Driver Verifier fails to complete a scan once started and the status will display &quot;Building...&quot; indefinitely.</p>
<p>The following work around can be used.</p>
<p>1. Edit the following file as administrator.</p>
<p><strong>C:\Program Files (x86)\Windows Kits\10\build\WindowsDriver.Sdv.targets</strong></p>
<p>2. Replace the following line:</p>
<p><strong>&lt;Exec Command=&quot;staticdv.exe $(Inputs)&quot;</strong></p>
<p>With this text:</p>
<p><strong>&lt;Exec Command=&quot;chcp 437 &amp;&amp; staticdv.exe $(Inputs)&quot;</strong></p>
<p>Information on the root cause of this issue is available here: [https://github.com/Microsoft/msbuild/issues/397](https://github.com/Microsoft/msbuild/issues/397)</p>
</div>
<div>
 
</div>
<p><strong>Visual Studio Integration</strong></p>
<p>Static Driver Verifier is integrated into Visual Studio. You can run static analysis on your Visual Studio driver project. You can launch, configure, and control Static Driver Verifier from the <strong>Driver</strong> menu in Visual Studio.</p>
<p><strong>Static Driver Verifier Documentation</strong></p>
[Using Static Driver Verifier to Find Defects in Drivers](using-static-driver-verifier-to-find-defects-in-drivers.md)
<p>Tells you what you need to get started analyzing your driver code in the Visual Studio environment.</p>
[Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md)
<p>Lists the MSBuild commands to use to run SDV in a Visual Studio Command Prompt window.</p>
[Introducing Static Driver Verifier](introducing-static-driver-verifier.md)
<p>Provides an overview of the static analysis tool.</p>
[Using Static Driver Verifier](using-static-driver-verifier.md)
<p>Provides the details about using and configuring the static analysis tool.</p>
[Static Driver Verifier Report](static-driver-verifier-report.md)
<p>Describes the viewer that displays the detailed trace of the static code analysis.</p>
[Static Driver Verifier Rules](https://msdn.microsoft.com/library/windows/hardware/ff552840)
<p>The rules define the requirements for proper interaction between a driver model and the kernel interface of the operating system.</p>
[Static Driver Verifier Reference](static-driver-verifier-reference.md)
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
<p>For specific information about the drivers that SDV can verify, see [Supported Drivers](supported-drivers.md).</p>
<p>For more information and tips about using Static Driver Verifier, see the [Static Driver Tools blog](http://go.microsoft.com/fwlink/p/?linkid=154232).</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Static%20Driver%20Verifier%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




