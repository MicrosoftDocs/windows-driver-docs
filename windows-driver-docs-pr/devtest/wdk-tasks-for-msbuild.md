---
title: WDK tasks for MSBuild
description: The Windows Driver Kit (WDK) includes tools that are often used in the build process but are not normally distributed with Visual Studio.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDK tasks for MSBuild

The [Windows Driver Kit (WDK)](../download-the-wdk.md) includes tools that are often used in the build process but are not normally distributed with Visual Studio. These tools are used to sign drivers or driver packages, implement software tracing, or to process and compile resource or message files (stampinf.exe, mc.exe, tracewpp.exe, binplace.exe, etc.). These command-line tools need to be exposed to MSBuild as tasks (contained in targets) so that they can be run during the build process. The WDK provides the necessary components so that you can run these tools as MSBuild tasks when you build your driver.

>[!NOTE]
>The WDK tools listed here are typically used in the build process and have MSBuild tasks, for a complete list of the tools included in the WDK and tools that are useful for driver development, see the [Index of Windows Driver Kit Tools](index-of-windows-driver-kit-tools.md).

The WDK command-line tools support a large number of options. Each option is exposed as a task parameter. When the tasks run, they can also receive inputs from the project file. MSBuild sets these properties immediately before executing the task. Each of the individual WDK task-wrapper classes create .NET properties that are available as input and output parameters for these tasks in the project file.

## Tools that have WDK Tasks

The following table lists the tools and their corresponding task, target, and item names.

| Tool Name    | Task Name | Target Name    | Item Name      |
|--------------|-----------|----------------|----------------|
| Tracewpp.exe | Wpp       | RunWpp         | ClCompile      |
| StampInf.exe | StampInf  | StampInf       | Inf            |
| Mofcomp.exe  | Mofcomp   | Mofcomp        | Mofcomp        |
| Wmimofck.exe | Wmimofck  | Wmimofck       | Wmimofck       |
| mc.exe       | Mc        | MessageCompile | MessageCompile |
| Ctrpp.exe    | Ctrpp     | Ctrpp          | Ctrpp          |

The following example shows how to invoke the tools.

```XML
<ItemGroup>
    <ClCompile Include="a.c" />
    <ClCompile Include="b.c">
        <WppEnabled>true</WppEnabled>
    </ClCompile>
</ItemGroup>
```

The example above invokes **tracewpp.exe** on the file **b.c** as if you issued the command **tracewpp.exe b.c**.

## In this section

|Topic|Description|
|----|----|
|[TraceWPP task](tracewpp-task.md)|The WDK provides the TraceWPP task so that you can run the tracewpp.exe tool when you build your driver using MSBuild. The tracewpp.exe tool is used to implement [WPP Software Tracing](wpp-software-tracing.md)|
|[Stampinf task](stampinf-task.md)|The WDK provides the StampInf task so that you can run the stampinf.exe tool when you build your driver using MSBuild. For information about the stampinf.exe tool, see [Stampinf](stampinf.md)|
|[Wmimofck task](wmimofck-task.md)|The WDK provides the Wmimofck task so you can run the wmimofck.exe tool when you build a driver using MSBuild.|
|[Mofcomp task](mofcomp-task.md)|The WDK provides the Mofcomp task so that you can run the Mofcomp.exe tool when you build your driver using MSBuld.|
|[Message compiler task](message-compiler-task.md)|The WDK provides the MessageCompiler task so that you can run the MC.exe tool when you build your driver using MSBuild. For information about using MC.exe, see [Message Compiler (MC.exe)](/windows/desktop/WES/message-compiler--mc-exe-)|
|[Ctrpp task](ctrpp-task.md)|The WDK provides the Ctrpp task so that you can run the ctrpp.exe tool when you build your driver using MSBuild.|

## Related topics

[CTRPP](/windows/desktop/PerfCtrs/ctrpp)

[Using Wmimofck.exe](../kernel/using-wmimofck-exe.md)

[Message Compiler (MC.exe)](/windows/desktop/WES/message-compiler--mc-exe-)

[mofcomp](/windows/desktop/WmiSdk/mofcomp)

[Stampinf](stampinf.md)

[WPP Preprocessor](wpp-preprocessor.md)
