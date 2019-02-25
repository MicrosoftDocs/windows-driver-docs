---
title: Security
description: Use the topics in this section to learn more about security in Windows 10 Mobile.
ms.assetid: 15783e59-f37b-4373-8604-d35c57eedfcc
ms.date: 08/31/2018
ms.localizationpriority: medium
---

# Security

Learn more about security in Windows 10.

## OS security tasks

To create a secure device, the OEM should complete the following tasks.

<table>
  <thead>
    <th>Task</th>
    <th>Description</th>
  </thead>
  <tbody>
    <tr>
      <td>Learn how to sign different types of executable code and other code assets</td>
      <td>All Windows 10 Mobile binaries need digital signatures to load and execute on a retail phone. For more info, see: <a href="https://docs.microsoft.com/windows-hardware/drivers/dashboard/get-a-code-signing-certificate">Get a code signing certificate</a>.</td>
</tr>
<tr class="even">
<td>Understand image validation and encryption</td>
<td>Windows 10 Mobile includes <a href="https://docs.microsoft.com/windows-hardware/drivers/bringup/secure-boot">secure boot</a>, a process that validates firmware images before they are allowed to execute. Windows 10 Mobile also provides <a href="https://docs.microsoft.com/windows-hardware/drivers/bringup/secure-boot-and-device-encryption-overview">device encryption</a>, a feature that encrypts all user data stored on internal data partitions. OEMs must perform a series of tasks during manufacturing to enable these features.</td>
</tr>
<tr>
<td>Understand the Security Development Lifecycle (SDL)</td>
<td><a href="https://www.microsoft.com/sdl">Security Development Lifecycle (SDL)</a> best practices and associated tools can be used by OEMs to improve the security of their products.</td>
</tr>
</tbody>
</table>

## SDL recommendations for OEMs

The Microsoft Security Development Lifecycle (SDL) is a set of best practices and associated tools that OEMs can use to improve the security of their products. SDL practices are organized by the phases of the traditional software development life cycle in which they are most effective. For example, threat modeling is most effective during software design.

Many of these security activities would provide some degree of security benefit if implemented on a standalone basis. However, practical experience at Microsoft has shown that security activities executed in chronological order during the right phase of the software development life cycle and as part of a repeatable process can result in greater security gains than those resulting from ad-hoc implementation. For more info about the SDL, see [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl).

The following table describes a subset of the SDL practices that are most useful for the OEM to adopt. Some of these practices are more helpful for driver code, while others are more helpful for application code. Some of the SDL practices are useful for both. Drivers tend to run with higher privileges, so it is important to consider these best practices when developing driver code.

|Tool|Information|Suggested area|
|----|----|----|
|[Microsoft SDL Threat Modeling Tool](https://www.microsoft.com/download/details.aspx?id=49168)|The SDL Threat Modeling Tool enables architects and developers to create threat models for their system and then analyze the threat models for potential security issues in the design of their systems. Threat modeling is most effective during design, before design is finalized. For more info, see [SDL practice #7: use threat modeling](https://www.microsoft.com/sdl/process/design.aspx).|Driver|
|[FxCop](https://www.microsoft.com/SDL/adopt/tools.aspx)|FxCop is a static analyzer. It analyzes managed-code assemblies and reports information about the assemblies such as possible design, localization, performance, and security improvements.|Partner apps|
|[Migrate from FxCop code analysis to .NET compiler platform analyzers](https://docs.microsoft.com/visualstudio/code-quality/fxcop-analyzers)|Visual Studio 2017 includes a built-in set of .NET Compiler Platform analyzers that analyze your C# or Visual Basic code as you type. You can install additional analyzers as a Visual Studio extension, or on a per-project basis as a NuGet package. Analyzers look at code style, code quality and maintainability, code design, and other issues.|Partner apps in managed code|
|[BinSkim](https://www.microsoft.com/SDL/adopt/tools.aspx)|BinSkim is a binary static analysis tool that scans Windows Portable Executable (PE) files for security and correctness.  Among the verifications performed by BinSkim are validations that the PE file has opted into all of the binary mitigations offered by the Windows Platform. ([User Guide](https://github.com/Microsoft/binskim/blob/develop/docs/BinSkimUserGuide.docx))|Drivers and partner apps|
|[Code Analysis for C/C++](https://docs.microsoft.com/visualstudio/code-quality/code-analysis-for-c-cpp-overview)|Code Analysis for C/C++ is a static analyzer that is provided with the installation of Visual Studio Team System Development Edition or Visual Studio Team Suite and helps to detect and correct code defects. It plows through source code one function at a time, and looks for C/C++ coding patterns and incorrect code usage that may indicate a programming error.|Drivers and partner apps|
