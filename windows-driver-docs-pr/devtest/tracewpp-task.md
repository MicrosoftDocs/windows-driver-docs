---
title: TraceWPP task
description: The Windows Driver Kit (WDK) provides the TraceWPP task so that you can run the tracewpp.exe tool when you build your driver using MSBuild.
ms.assetid: 74CE1912-8D1D-417E-8B29-36B2AB0253EE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TraceWPP task


The Windows Driver Kit (WDK) provides the TraceWPP task so that you can run the tracewpp.exe tool when you build your driver using MSBuild. The tracewpp.exe tool is used to implement [WPP Software Tracing](wpp-software-tracing.md).

WppEnabled is a new metadata for the ClCompile item that enables tracing for source files. The Wpp task runs through the entire ClCompile Item Collections and invokes tracewpp.exe for each Item for which the WppEnabled metadata is set to **TRUE**.

The WppEnabled metadata was added to the ClCompile Item because the WPP task runs on the same type of input files as the CL task, in this case .c, .cpp, and .h files.

**Note**  You access the Item metadata for tracewpp by using the ClCompile item in project files. MSBuild uses the TraceWpp item internally inside the target to pass it to the task.

 

The following example shows how to edit the metadata in the .vcxproj file.

```XML
<ItemGroup>
    <ClCompile Include="a.c" />
      <WppEnabled>false</WppEnabled>
    <ClCompile Include="b.c">
        <WppEnabled>true</WppEnabled>
        <WppKernelMode>true</WppKernelMode>
        <WppAdditionalIncludeDirectories>c:\test\</WppAdditionalIncludeDirectories>
    </ClCompile>
    <ClCompile Include="test1.c" />
    <ClCompile Include="test2.c">
        <WppEnabled>true</WppEnabled>
        <WppDllMacro>true</WppDllMacro>
    </ClCompile>
</ItemGroup>
```

The command-line invocation would be:

```
tracewpp.exe  km /Ic:\test\b.c
tracewpp.exe  dll test2.c
```

The example above shows that MSBuild invokes **tracewpp.exe** only on b.c and test2.c because the **WppEnabled** metadata is set to **TRUE** for these inputs. Also note that the metadata for these two inputs are different. Therefore, the switches will also be different for these inputs. In other words, you can call each input with its own set of metadata.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">WPP Task Parameter</th>
<th align="left">Item Metadata</th>
<th align="left">Tool Switch</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>Sources</strong>
<p>Required ITaskItem[] parameter. Specifies a list of source files.</p></td>
<td align="left">@(TraceWpp)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>AddAlternateNameToMessageGUID</strong>
<p>Optional string parameter. Specifies an alternate friendly name for the message GUID for messages that come from this trace provider.</p></td>
<td align="left">%(TraceWpp.WppAddAlternateNameToMessageGUID)</td>
<td align="left"><strong>-o:</strong><em>String</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>AdditionalConfigurationFile</strong>
<p>Optional string parameter. Specifies an additional configuration file. WPP uses the specified file in addition to the default file, defaultwpp.ini.</p></td>
<td align="left">%(TraceWpp.WppAdditionalConfigurationFile)</td>
<td align="left"><strong>-ini:</strong><em>Path</em></td>
</tr>
<tr class="even">
<td align="left"><strong>AdditionalIncludeDirectories</strong>
<p>Optional string[] parameter. Adds a directory to the list of directories that WPP searches for include files.</p></td>
<td align="left">%(TraceWpp.WppAdditionalIncludeDirectories)</td>
<td align="left"><strong>-I</strong></td>
</tr>
<tr class="odd">
<td align="left"><strong>AlternateConfigurationFile</strong>
<p>Optional string parameter. Specifies an alternative configuration file. WPP uses this file instead of the defaultwpp.ini file.</p></td>
<td align="left">%(TraceWpp.WppAlternateConfigurationFile)</td>
<td align="left"><strong>-defwpp:</strong><em>Path</em></td>
</tr>
<tr class="even">
<td align="left"><strong>GenerateUsingTemplateFile</strong>
<p>Optional string parameter. For every source file that WPP processes with the name specified between the braces {}, WPP creates another file with the specified file name extension.</p></td>
<td align="left">%(TraceWpp.WppGenerateUsingTemplateFile)</td>
<td align="left"><strong>-gen{</strong><em>File.tpl</em><strong>}*.ext</strong></td>
</tr>
<tr class="odd">
<td align="left"><strong>MinimalRebuildFromTracking</strong>
<p>Optional Boolean parameter. If the value is <strong>TRUE</strong>, WPP performs a tracked incremental build. Otherwise, WPP performs a rebuild.</p></td>
<td align="left">%(TraceWpp.WppMinimalRebuildFromTracking)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>NumericBaseForFormatStrings</strong>
<p>Optional int parameter. Establishes a numeric base for the numbering of format strings.</p></td>
<td align="left">%(TraceWpp.WppNumericBaseForFormatStrings)</td>
<td align="left"><strong>-argbase:</strong><em>Number</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>AddControlGUID</strong>
<p>Optional string parameter. Defines a WPP_CONTROL_GUIDS macro with the specified control GUID and WPP_DEFINE_BIT entries named &#39;Error&#39;, &#39;Unusual&#39;, and &#39;Noise&#39;.</p></td>
<td align="left">%(TraceWpp.WppAddControlGUID)</td>
<td align="left"><strong>-ctl:</strong><em>GUID</em></td>
</tr>
<tr class="even">
<td align="left"><strong>AdditionalOptions</strong>
<p>Optional string parameter. A list of command-line options.</p></td>
<td align="left">%(TraceWpp.WppAdditionalOptions)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>ConfigurationDirectories</strong>
<p>Optional string[] parameter. Specifies the location of configuration and template files.</p></td>
<td align="left">%(TraceWpp.WppConfigurationDirectories)</td>
<td align="left"><strong>-cfgdir:</strong><em>[Path]</em></td>
</tr>
<tr class="even">
<td align="left"><strong>DllMacro</strong>
<p>Optional Boolean parameter. Defines the WPP_DLL macro.</p></td>
<td align="left">%(TraceWpp.WppDllMacro)</td>
<td align="left"><strong>-dll</strong></td>
</tr>
<tr class="odd">
<td align="left"><strong>FileExtensions</strong>
<p>Optional string[] parameter. Specifies the file types that WPP recognizes as source files. WPP ignores files with a different file name extension.</p></td>
<td align="left">%(TraceWpp.WppFileExtensions)</td>
<td align="left"><strong>-ext:</strong><em>.ext1 [.ext2]</em></td>
</tr>
<tr class="even">
<td align="left"><strong>IgnoreExclamationmarks</strong>
<p>Optional Boolean parameter. Directs WPP to ignore exclamation marks, also known as &#39;shrieks,&#39; used in complex formatting, such as %!timestamp!%.</p></td>
<td align="left">%(TraceWpp.WppIgnoreExclamationmarks)</td>
<td align="left"><strong>-noshrieks</strong></td>
</tr>
<tr class="odd">
<td align="left"><strong>KernelMode</strong>
<p>Optional Boolean parameter. Defines the WPP_KERNEL_MODE macro, which traces kernel-mode components. By default, only user-mode components are traced.</p></td>
<td align="left">%(TraceWpp.WppKernelMode)</td>
<td align="left"><strong>-km</strong></td>
</tr>
<tr class="even">
<td align="left"><strong>OutputDirectory</strong>
<p>Optional string parameter. Specifies the directory for the output files that WPP creates.</p></td>
<td align="left">%(TraceWpp.WppOutputDirectory)</td>
<td align="left"><strong>-odir:</strong><em>Path</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>PreprocessorDefinitions</strong>
<p>Optional string[] parameter. Defines a preprocessing symbol for your source file.</p></td>
<td align="left">%(TraceWpp.WppPreprocessorDefinitions)</td>
<td align="left"><strong>/D</strong></td>
</tr>
<tr class="even">
<td align="left"><strong>PreserveExtensions</strong>
<p>Optional string[] parameter. Preserves the specified file name extensions when creating TMH files.</p></td>
<td align="left">%(TraceWpp.WppPreserveExtensions)</td>
<td align="left"><strong>-preserveext:</strong><em>ext1[,ext2]</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>ScanConfigurationData</strong>
<p>Optional string parameter. Searches for configuration data, such as custom data types, in a file that is not a configuration file, as well as in defaultwpp.ini.</p></td>
<td align="left">%(TraceWpp.WppScanConfigurationData)</td>
<td align="left"><strong>-scan:</strong><em>File</em></td>
</tr>
<tr class="even">
<td align="left"><strong>SearchString</strong>
<p>Optional string parameter. Directs WPP to search the source files for the specified string to initiate tracing.</p></td>
<td align="left">%(TraceWpp.WppSearchString)</td>
<td align="left"><strong>-lookfor:</strong><em>String</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>ToolPath</strong>
<p>Optional string parameter. Allows you to specify the full path to the folder where the tool is located.</p></td>
<td align="left">$(WPPToolPath)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>TraceFunction</strong>
<p>Optional string[] parameter. Specifies functions that can then be used to generate trace messages.</p></td>
<td align="left">%(TraceWpp.WppTraceFunction)</td>
<td align="left"><strong>-func:</strong><em>FunctionDescription</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>TrackerLogDirectory</strong>
<p>Optional string parameter. Log directory for tracker to write tlogs.</p></td>
<td align="left">%(TraceWpp.WppTrackerLogDirectory)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>TrackFileAccess</strong>
<p>Optional Boolean parameter. If true, tracks file access patterns for this task.</p></td>
<td align="left">$(TrackFileAccess)</td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[WPP Preprocessor](wpp-preprocessor.md)

[WPP Software Tracing](wpp-software-tracing.md)

 

 






