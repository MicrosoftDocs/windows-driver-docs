---
title: Ctrpp task
description: The Windows Driver Kit (WDK) provides the Ctrpp task so that you can run the ctrpp.exe tool when you build your driver using MSBuild.
ms.assetid: DB457500-5BFF-4488-95EB-EEB3F63947C1
---

# Ctrpp task


The Windows Driver Kit (WDK) provides the Ctrpp task so that you can run the ctrpp.exe tool when you build your driver using MSBuild. For information about using ctrpp.exe, see [**CTRPP**](https://msdn.microsoft.com/library/windows/desktop/aa372128).

MSBuild uses the Ctrpp Item to send the parameters for the Ctrpp task to ctrpp.exe. The Ctrpp item in the project files accesses the item metadata for ctrpp.exe.

The following example shows how to edit the metadata in the .vcxproj file.

```XML
<ItemGroup>
    <Ctrpp Include="a.manifest">
      <GenerateHeaderFileForCounter>true</GenerateHeaderFileForCounter>
      <HeaderFileNameForCounter>c:\test\abc.h</HeaderFileNameForCounter>
    </Ctrpp>
</ItemGroup>
```

The following example shows the command-line invocation:

``` syntax
ctrpp.exe –ch "c:\test\abc.h" a.manifest
```

In the example above, MSBuild invokes ctrpp.exe on the file a.manifest, with the **–ch** option because the metadata GenerateHeaderFileForCounter is set to true. Also, MSBuild uses the HeaderFileNameForCounter metadata to specify the argument for the **–ch** option

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Ctrpp Task Parameter</th>
<th align="left">Item Metadata</th>
<th align="left">Tool Switch</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Source</td>
<td align="left">@(Ctrpp)</td>
<td align="left"></td>
<td align="left">Required ITaskItem parameter. Specifies the counter manifest to be processed.</td>
</tr>
<tr class="even">
<td align="left">AddPrefix</td>
<td align="left">%(Ctrpp.AddPrefix)</td>
<td align="left"><strong>-prefix</strong><em>&lt;prefix&gt;</em></td>
<td align="left">Optional string parameter. Specifies the prefix to be added to functions and variables generated.</td>
</tr>
<tr class="odd">
<td align="left">BackwardCompatibility</td>
<td align="left">%(Ctrpp.BackwardCompatibility)</td>
<td align="left"><strong>-backcompat</strong></td>
<td align="left">Optional Boolean parameter. Generates code that is binary compatible with operating systems prior to Windows 7.</td>
</tr>
<tr class="even">
<td align="left">EnableLegacy</td>
<td align="left">%(Ctrpp.EnableLegacy)</td>
<td align="left"><strong>-Legacy</strong></td>
<td align="left">Optional Boolean parameter. Reverts to the previous ctrpp file. This switch causes ctrpp to generate four output files: two header files, a resource file, and a source code file. This mimics the behavior found in previous versions of ctrpp. The -o, -ch, -rc and -prefix options cannot be used in conjunction with -legacy.</td>
</tr>
<tr class="odd">
<td align="left">GeneratedCounterFilesPath</td>
<td align="left">%(Ctrpp.GeneratedCounterFilesPath)</td>
<td align="left"><strong>-sumPath</strong><em>&lt;path&gt;</em></td>
<td align="left">Optional string parameter. Specifies the path to generate binary counter files default.</td>
</tr>
<tr class="even">
<td align="left">GenerateHeaderFileForCounter</td>
<td align="left">%(Ctrpp.GenerateHeaderFileForCounter)</td>
<td align="left"></td>
<td align="left">If this is set to true, it enables the -ch switch.</td>
</tr>
<tr class="odd">
<td align="left">HeaderFileNameForCounter</td>
<td align="left">%(Ctrpp.HeaderFileNameForCounter)</td>
<td align="left"><strong>-ch</strong><em>&lt;filename&gt;</em></td>
<td align="left">Optional string parameter. Generates a header file that contains the counter names and ids.</td>
</tr>
<tr class="even">
<td align="left">GenerateHeaderFileForProvider</td>
<td align="left">%(Ctrpp.GenerateHeaderFileForProvider)</td>
<td align="left"></td>
<td align="left">If this is set to true, it enables the -o switch.</td>
</tr>
<tr class="odd">
<td align="left">HeaderFileNameForProvider</td>
<td align="left">%(Ctrpp.HeaderFileNameForProvider)</td>
<td align="left"><strong>-o</strong><em>&lt;filename&gt;</em></td>
<td align="left">Optional string parameter. Generates header file for provider.</td>
</tr>
<tr class="even">
<td align="left">GenerateMemoryRoutines</td>
<td align="left">%(Ctrpp.GenerateMemoryRoutines)</td>
<td align="left"><strong>-MemoryRoutines</strong></td>
<td align="left">Optional Boolean parameter. Generates memory allocation and free routine templates.</td>
</tr>
<tr class="odd">
<td align="left">GenerateNotificationCallback</td>
<td align="left">%(Ctrpp.GenerateNotificationCallback)</td>
<td align="left"><strong>-NotificationCallback</strong></td>
<td align="left">Optional Boolean parameter. Generates customized notification callback template. Similar to the &quot;callback&quot; attribute in the &lt;provider&gt; element.</td>
</tr>
<tr class="even">
<td align="left">GenerateResourceSourceFile</td>
<td align="left">%(Ctrpp.GenerateResourceSourceFile)</td>
<td align="left"></td>
<td align="left">If this is set to true, it enables the -rc switch.</td>
</tr>
<tr class="odd">
<td align="left">ResourceFileName</td>
<td align="left">%(Ctrpp.ResourceFileName)</td>
<td align="left"><strong>-rc</strong><em>&lt;filename&gt;</em></td>
<td align="left">Optional string parameter. Generates resource source file.</td>
</tr>
<tr class="even">
<td align="left">GenerateSummaryGlobalFile</td>
<td align="left">%(Ctrpp.GeneratedSummaryGlobalFile)</td>
<td align="left"><strong>-summary</strong><em>&lt;path&gt;</em></td>
<td align="left">Optional string parameter. Generates binary counter file per provider generate summary global file GenSumResource.BIN.</td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[**CTRPP**](https://msdn.microsoft.com/library/windows/desktop/aa372128)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Ctrpp%20task%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





