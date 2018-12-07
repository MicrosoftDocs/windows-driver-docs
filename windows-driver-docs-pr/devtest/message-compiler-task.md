---
title: Message compiler task
description: The Windows Driver Kit (WDK) provides the MessageCompiler task so that you can run the MC.exe tool when you build your driver using MSBuild. For information about using MC.exe, see Message Compiler (MC.exe).
ms.assetid: 77B2DBF4-64EB-4396-BAA5-80F23C9899CC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Message compiler task


The Windows Driver Kit (WDK) provides the MessageCompiler task so that you can run the MC.exe tool when you build your driver using MSBuild. For information about using MC.exe, see [**Message Compiler (MC.exe)**](https://msdn.microsoft.com/library/windows/desktop/aa385638).

MSBuild uses the MessageCompile Item to send the parameters for the MessageCompiler task. The MessageCompile item accesses the item metadata for mc.exe in project files.

The following example shows how to edit the metadata in the .vcxproj file.

```XML
<ItemGroup>
    <MessageCompile Include="a.mc">
      <GenerateBaselineResource>true</GenerateBaselineResource>
      <BaselineResourcePath>c:\test\</BaselineResourcePath>
    </MessageCompile>
</ItemGroup>
```

The following example shows the command-line invocation:

```
mc.exe –s "c:\test\" a.mc
```

In the example above, MSBuild invokes mc.exe on the file a.mc, with the –s switch because the metadata GenerateBaselineResource is set to true. Also, MSBuild uses the BaselineResourcePath metadata to specify the argument for –s switch.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">MessageCompiler Task Parameter</th>
<th align="left">Item Metadata</th>
<th align="left">Tool Switch</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>Sources</strong>
<p>Optional string parameter. Specifies the name of the manifest file to compile. Specifies the name of a message file to compile.</p></td>
<td align="left">@(MessageCompile)</td>
<td align="left"><p><strong>&lt;filename.man&gt;</strong></p>
<p><strong>&lt;filename.mc&gt;</strong></p></td>
</tr>
<tr class="even">
<td align="left"><strong>ANSIInputFile</strong>
<p>Specifies that the Input file is ANSI (default).</p></td>
<td align="left">%(MessageCompile.ANSIInputFile)</td>
<td align="left"><strong>-a</strong></td>
</tr>
<tr class="odd">
<td align="left"><strong>ANSIMessageInBinFile</strong>
<p>Specifies that the messages in the .BIN file should be ANSI.</p></td>
<td align="left">%(MessageCompile.ANSIMessageInBinFile)</td>
<td align="left"><strong>-A</strong></td>
</tr>
<tr class="even">
<td align="left"><strong>EnableDebugOutputPath</strong>
<p>If this is set to true, it enables the –x switch.</p></td>
<td align="left">%(MessageCompile.EnableDebugOutputPath)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>DebugOutputPath</strong>
<p>Specifies the folder into which the compiler places the .dbg C include file. The .dbg file maps message IDs to their symbolic names.</p></td>
<td align="left">%(MessageCompile.DebugOutputPath)</td>
<td align="left"><strong>-x</strong><em>&lt;path&gt;</em></td>
</tr>
<tr class="even">
<td align="left"><strong>EnableCallOutMacro</strong>
<p>Adds callout macro to invoke user code during logging. This switch is not valid for C# and is ignored.</p></td>
<td align="left">%(MessageCompile.EnableCallOutMacro)</td>
<td align="left"><strong>-co</strong></td>
</tr>
<tr class="odd">
<td align="left"><strong>EventmanPath</strong>
<p>Specifies the path to eventman.xsd file.</p></td>
<td align="left">%(MessageCompile.EventmanPath)</td>
<td align="left"><strong>-w</strong><em>&lt;file&gt;</em></td>
</tr>
<tr class="even">
<td align="left"><strong>GenerateBaselineResource</strong>
<p>If this is set to true, it enables -s switch.</p></td>
<td align="left">%(MessageCompile.GenerateBaselineResource)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>BaselineResourcePath</strong>
<p>Generates binary resource per provider. Generates summary global resource MCGenResource.BIN.</p></td>
<td align="left">%(MessageCompile.BaselineResourcePath)</td>
<td align="left"><strong>-s</strong><em>&lt;path&gt;</em></td>
</tr>
<tr class="even">
<td align="left"><strong>GenerateC#LoggingClass</strong>
<p>Generates C# (managed) logging class based on FX3.5 Eventing class.</p></td>
<td align="left">%(MessageCompile.GenerateC#LoggingClass)</td>
<td align="left"><strong>-cs</strong><em>&lt;namespace&gt;</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>GenerateC#StaticLoggingClass</strong>
<p>Generates static C# (managed) logging class based on FX3.5 Eventing class.</p></td>
<td align="left">%(MessageCompile.GenerateC#StaticLoggingClass)</td>
<td align="left"><strong>-css</strong><em>&lt;namespace&gt;</em></td>
</tr>
<tr class="even">
<td align="left"><strong>GeneratedFilesBaseName</strong>
<p>Specifies the base name of the generated files. The default is the basename of input file.</p></td>
<td align="left">%(MessageCompile.GeneratedFilesBaseName)</td>
<td align="left"><strong>-z</strong><em>&lt;basename&gt;</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>GeneratedHeaderPath</strong>
<p>If this is set to true, it enables -h switch.</p></td>
<td align="left">%(MessageCompile.GeneratedHeaderPath)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>HeaderFilePath</strong>
<p>Specifies the path of where to create the C include file. The default is ..</p></td>
<td align="left">%(MessageCompile.HeaderFilePath)</td>
<td align="left"><strong>-h</strong><em>&lt;path&gt;</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>GeneratedRcAndMessagesPath</strong>
<p>If this is set to true, it enables the -r switch.</p></td>
<td align="left">%(MessageCompile.GeneratedRcAndMessagesPath)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>RCFilePath</strong>
<p>Specifies the path of the RC includes file and the binary message resource files that it includes. The default is ..</p></td>
<td align="left">%(MessageCompile.RCFilePath)</td>
<td align="left"><strong>-r</strong><em>&lt;path&gt;</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>GenerateKernelModeLoggingMacros</strong>
<p>Generates Kernel Mode logging macros.</p></td>
<td align="left">%(MessageCompile.GenerateKernelModeLoggingMacros)</td>
<td align="left"><strong>-km</strong></td>
</tr>
<tr class="even">
<td align="left"><strong>GenerateMOFFile</strong>
<p>Generates down-level support for all functions and macros that are generated. The MOF file is generated from the manifest. The MOF file is placed in the location specified by the &quot;-h&quot; switch.</p></td>
<td align="left">%(MessageCompile.GenerateMOFFile)</td>
<td align="left"><strong>-mof</strong></td>
</tr>
<tr class="odd">
<td align="left"><strong>GenerateOLE2Header</strong>
<p>Generates the OLE2 header file. Uses the HRESULT definition instead of the status code definition.</p></td>
<td align="left">%(MessageCompile.GenerateOLE2Header)</td>
<td align="left"><strong>-o</strong></td>
</tr>
<tr class="even">
<td align="left"><strong>GenerateUserModeLoggingMacros</strong>
<p>Generates User Mode logging macros.</p></td>
<td align="left">%(MessageCompile.GenerateUserModeLoggingMacros)</td>
<td align="left"><strong>-um</strong></td>
</tr>
<tr class="odd">
<td align="left"><strong>HeaderExtension</strong>
<p>Specifies the extension for the header file (1-3 chars).</p></td>
<td align="left">%(MessageCompile.HeaderExtension)</td>
<td align="left"><strong>-e</strong><em>&lt;extension&gt;</em></td>
</tr>
<tr class="even">
<td align="left"><strong>MaximumMessageLength</strong>
<p>Generates a warning if the size of any message exceeds &lt;length&gt; characters.</p></td>
<td align="left">%(MessageCompile.MaximumMessageLength)</td>
<td align="left"><strong>-m</strong><em>&lt;length&gt;</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>PrefixMacroName</strong>
<p>Defines the macro name prefix that is applied to each generated logging macro. The default is &quot;EventWrite&quot;.</p></td>
<td align="left">%(MessageCompile PrefixMacroName)</td>
<td align="left"><strong>-p</strong><em>&lt;prefix&gt;</em></td>
</tr>
<tr class="even">
<td align="left"><strong>RemoveCharsFromSymbolName</strong>
<p>Defines the text at the start of each event symbol name to remove before forming the macro names. The default is NULL.</p></td>
<td align="left">%(RemoveCharsFromSymbolName)</td>
<td align="left"><strong>-P</strong><em>&lt;prefix&gt;</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>SetCustomerbit</strong>
<p>Sets the Customer bit in the entire message Ids.</p></td>
<td align="left">%(MessageCompile.SetCustomerbit)</td>
<td align="left"><strong>-c</strong></td>
</tr>
<tr class="even">
<td align="left"><strong>TerminateMessageWithNull</strong>
<p>Terminates all strings with null characters in the message tables.</p></td>
<td align="left">%(MessageCompile.TerminateMessageWithNull)</td>
<td align="left"><strong>-n</strong></td>
</tr>
<tr class="odd">
<td align="left"><strong>UnicodeInputFile</strong>
<p>Input file is Unicode.</p></td>
<td align="left">%(MessageCompile.UnicodeInputFile)</td>
<td align="left"><strong>-u</strong></td>
</tr>
<tr class="even">
<td align="left"><strong>UnicodeMessageInBinFile</strong>
<p>Messages in .BIN file should be Unicode (default).</p></td>
<td align="left">%(MessageCompile.UnicodeMessageInBinFile)</td>
<td align="left"><strong>-U</strong></td>
</tr>
<tr class="odd">
<td align="left"><strong>UseBaseNameOfInput</strong>
<p>Specifies that the .BIN filename should have .mc filename included for uniqueness.</p></td>
<td align="left">%(MessageCompile. UseBaseNameOfInput)</td>
<td align="left"><strong>-b</strong></td>
</tr>
<tr class="even">
<td align="left"><strong>UseDecimalValues</strong>
<p>Specifies the FACILTY and SEVERITY values in header file in decimal. Sets message values in header to decimal initially.</p></td>
<td align="left">%(MessageCompile.UseDecimalValues)</td>
<td align="left"><strong>-d</strong></td>
</tr>
<tr class="odd">
<td align="left"><strong>ValdateAgainstBaselineResource</strong>
<p>If this is set to true, then it generates the -t switch.</p></td>
<td align="left">%(MessageCompile.ValdateAgainstBaselineResource)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>BaselinePath</strong>
<p>Validates against the baseline resource.</p></td>
<td align="left">%(MessageCompile.BaselinePath)</td>
<td align="left"><strong>-t</strong><em>&lt;path&gt;</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>Verbose</strong>
<p>Specifies verbose output.</p></td>
<td align="left">%(MessageCompile.Verbose)</td>
<td align="left"><strong>-v</strong></td>
</tr>
<tr class="even">
<td align="left"><strong>WinmetaPath</strong>
<p>Specifies the path to the winmeta.xml file.</p></td>
<td align="left">%(MessageCompile.WinmetaPath)</td>
<td align="left"><strong>-W</strong><em>&lt;file&gt;</em></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[**Message Compiler (MC.exe)**](https://msdn.microsoft.com/library/windows/desktop/aa385638)

 

 






