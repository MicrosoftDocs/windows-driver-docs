---
title: Security
author: windows-driver-content
description: Use the topics in this section to learn more about security in Windows 10 Mobile.
ms.assetid: 15783e59-f37b-4373-8604-d35c57eedfcc
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Security


Use the topics in this section to learn more about security in Windows 10 Mobile.

## OS security tasks


To create a secure device, the OEM should complete the following tasks.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Learn how to sign different types of executable code and other code assets</p></td>
<td><p>All Windows 10 Mobile binaries need digital signatures to load and execute on a retail phone.</p>
<p>[Code signing](https://msdn.microsoft.com/library/windows/hardware/dn756634)</p>
<p>[Submit binaries to be retail signed](https://msdn.microsoft.com/library/windows/hardware/dn789223)</p></td>
</tr>
<tr class="even">
<td><p>Understand image validation and encryption</p></td>
<td><p>Windows 10 Mobile includes secure boot, a process that validates firmware images before they are allowed to execute. Windows 10 Mobile also provides device encryption, a feature that encrypts all user data stored on internal data partitions. OEMs must perform a series of tasks during manufacturing to enable these features.</p></td>
</tr>
<tr class="odd">
<td><p>Understand the Security Development Lifecycle (SDL)</p></td>
<td><p>Security Development Lifecycle (SDL) best practices and associated tools can be used by OEMs to improve the security of their products.</p>
<p>[SDL recommendations for OEMs](#sdl)</p></td>
</tr>
</tbody>
</table>

 

## <a href="" id="sdl"></a>SDL recommendations for OEMs


The Microsoft Security Development Lifecycle (SDL) is a set of best practices and associated tools that OEMs can use to improve the security of their products. SDL practices are organized by the phases of the traditional software development life cycle in which they are most effective. For example, threat modeling is most effective during software design.

Many of these security activities would provide some degree of security benefit if implemented on a standalone basis. However, practical experience at Microsoft has shown that security activities executed in chronological order during the right phase of the software development life cycle and as part of a repeatable process can result in greater security gains than those resulting from ad-hoc implementation. For more info about the SDL, see [Microsoft Security Development Lifecycle](http://go.microsoft.com/fwlink/p/?LinkId=190289).

The following table describes a subset of the SDL practices that are most useful for the OEM to adopt. Some of these practices are more helpful for driver code, while others are more helpful for application code. Some of the SDL practices are useful for both. Drivers tend to run with higher privileges, so it is important to consider these best practices when developing driver code.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Tool</th>
<th>Information</th>
<th>Suggested area</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Microsoft SDL Threat Modeling Tool](http://go.microsoft.com/fwlink/p/?LinkId=190288)</p></td>
<td><p>The SDL Threat Modeling Tool enables architects and developers to create threat models for their system and then analyze the threat models for potential security issues in the design of their systems. Threat modeling is most effective during design, before design is finalized.</p></td>
<td><p>Driver</p></td>
</tr>
<tr class="even">
<td><p>[FxCop](http://go.microsoft.com/fwlink/p/?LinkId=190283)</p></td>
<td><p>FxCop is a static analyzer. It analyzes managed-code assemblies and reports information about the assemblies such as possible design, localization, performance, and security improvements.</p></td>
<td><p>Partner apps</p></td>
</tr>
<tr class="odd">
<td><p>[BinScope](http://go.microsoft.com/fwlink/p/?LinkId=190284)</p></td>
<td><p>The BinScope Binary Analyzer is a verification tool that analyzes binaries to ensure that they have been built in compliance with the SDL requirements and recommendations. BinScope checks that SDL-required compiler/linker flags are being set, strong-named assemblies are in use, up-to-date build tools are in place, and the latest good ATL headers are being used. BinScope also reports on dangerous constructs that are prohibited by SDL.</p></td>
<td><p>Drivers and partner applications</p></td>
</tr>
<tr class="even">
<td><p>[MiniFuzz](http://go.microsoft.com/fwlink/p/?LinkId=190286)</p></td>
<td><p>The MiniFuzz File Fuzzer is a basic testing tool designed to help detect issues that may expose security vulnerabilities in file-handling code. This tool could be helpful for developers that parse files in their apps.</p></td>
<td><p>Drivers and partner applications</p></td>
</tr>
<tr class="odd">
<td><p>[Banned.h](http://go.microsoft.com/fwlink/p/?LinkId=190287)</p></td>
<td><p>The banned.h header file is a sanitizing resource that supports the SDL requirement to remove banned functions from code. It lists all banned APIs and allows any developer to locate them in code.</p></td>
<td><p>Drivers and partner applications</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------


