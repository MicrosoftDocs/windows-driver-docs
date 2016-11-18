---
title: WDK tasks for MSBuild
description: The Windows Driver Kit (WDK) includes tools that are often used in the build process but are not normally distributed with Visual Studio.
ms.assetid: 53A5AAC2-A608-4153-9482-D8EF3D05EF04
---

# WDK tasks for MSBuild


The Windows Driver Kit (WDK) includes tools that are often used in the build process but are not normally distributed with Visual Studio. These tools are used to sign drivers or driver packages, implement software tracing, or to process and compile resource or message files (stampinf.exe, mc.exe, tracewpp.exe, binplace.exe, etc.). These command-line tools need to be exposed to MSBuild as tasks (contained in targets) so that they can be run during the build process. The WDK provides the necessary components so that you can run these tools as MSBuild tasks when you build your driver.

**Note**  The WDK tools listed here are typically used in the build process and have MSBuild tasks, for a complete list of the tools included in the WDK and tools that are useful for driver development, see the [Index of Windows Driver Kit Tools](index-of-windows-driver-kit-tools.md).

 

The WDK command-line tools support a large number of options. Each option is exposed as a task parameter. When the tasks run, they can also receive inputs from the project file. MSBuild sets these properties immediately before executing the task. Each of the individual WDK task-wrapper classes create .NET properties that are available as input and output parameters for these tasks in the project file.

## <span id="Tools_that__have_WDK_Tasks"></span><span id="tools_that__have_wdk_tasks"></span><span id="TOOLS_THAT__HAVE_WDK_TASKS"></span>Tools that have WDK Tasks


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
<td align="left"><p>[TraceWPP task](tracewpp-task.md)</p></td>
<td align="left"><p>The WDK provides the TraceWPP task so that you can run the tracewpp.exe tool when you build your driver using MSBuild. The tracewpp.exe tool is used to implement [WPP Software Tracing](wpp-software-tracing.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Stampinf task](stampinf-task.md)</p></td>
<td align="left"><p>The WDK provides the StampInf task so that you can run the stampinf.exe tool when you build your driver using MSBuild. For information about the stampinf.exe tool, see [Stampinf](stampinf.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Wmimofck task](wmimofck-task.md)</p></td>
<td align="left"><p>The WDK provides the Wmimofck task so you can run the wmimofck.exe tool when you build a driver using MSBuild.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Mofcomp task](mofcomp-task.md)</p></td>
<td align="left"><p>The WDK provides the Mofcomp task so that you can run the Mofcomp.exe tool when you build your driver using MSBuld.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Message compiler task](message-compiler-task.md)</p></td>
<td align="left"><p>The WDK provides the MessageCompiler task so that you can run the MC.exe tool when you build your driver using MSBuild. For information about using MC.exe, see [<strong>Message Compiler (MC.exe)</strong>](https://msdn.microsoft.com/library/windows/desktop/aa385638).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Ctrpp task](ctrpp-task.md)</p></td>
<td align="left"><p>The WDK provides the Ctrpp task so that you can run the ctrpp.exe tool when you build your driver using MSBuild.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[**CTRPP**](https://msdn.microsoft.com/library/windows/desktop/aa372128)

[Using Wmimofck.exe](https://msdn.microsoft.com/library/windows/hardware/ff565588)

[**Message Compiler (MC.exe)**](https://msdn.microsoft.com/library/windows/desktop/aa385638)

[**mofcomp**](https://msdn.microsoft.com/library/aa392389)

[Stampinf](stampinf.md)

[WPP Preprocessor](wpp-preprocessor.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20WDK%20tasks%20for%20MSBuild%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





