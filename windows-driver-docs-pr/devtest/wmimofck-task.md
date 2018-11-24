---
title: Wmimofck task
description: The Windows Driver Kit (WDK) provides the Wmimofck task so you can run the wmimofck.exe tool when you build a driver using MSBuild.
ms.assetid: 33C5C079-510F-4BD3-AEF1-F152E88E45C2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Wmimofck task


The Windows Driver Kit (WDK) provides the Wmimofck task so you can run the wmimofck.exe tool when you build a driver using MSBuild.

For information about using the Wmimofck tool, see [Using Wmimofck.exe](https://msdn.microsoft.com/library/windows/hardware/ff565588).

MSBuild uses the Wmimofck item to send the parameters for the Wmimofck task. The item metadata for wmimofck is accessed using the Wmimofck item in project files.

The following example shows how to edit metadata in the .vcxproj file.

```XML
<ItemGroup>
    <Wmimofck Include="a.bmf">
      <GenerateStructureDefinitionsForDatablocks>true</GenerateStructureDefinitionsForDatablocks>
    </Wmimofck>
    <Wmimofck Include="b.bmf">
      <HeaderOuputFile>b.h</HeaderOuputFile>
    </Wmimofck>
</ItemGroup>
```

The following example shows how you run Wmimofck.exe in a Command Prompt window:

```
Wmimofck.exe -u a.bmf
Wmimofck.exe –h"b.h" b.bmf
```

The example above invokes wmimofck.exe on both a.bmf and b.bmf, but with different sets of parameters and with different metadata. Therefore, the switches will also be different for these inputs. In other words, you can call each input with its own set of metadata.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Wmimofck Task Parameter</th>
<th align="left">Item Metadata</th>
<th align="left">Tool Switch</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>Source</strong>
<p>Required ITaskItem parameter. Specifies the input source file.</p></td>
<td align="left">@(Wmimofck)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>GenerateStructureDefinitionsForDatablocks</strong>
<p>Optional Boolean parameter. Wmimofck generates member definitions for every property that has a fixed size, including optional properties that specify a MaxLen qualifier.</p></td>
<td align="left">%(Wmimofck.GenerateStructureDefinitionsForDatablocks)</td>
<td align="left"><strong>-u</strong></td>
</tr>
<tr class="odd">
<td align="left"><strong>GenerateStructureDefinitionsForMethodParameters</strong>
<p>Optional Boolean parameter. The header file includes structure definitions for the input and output of each WMI method.</p></td>
<td align="left">%(Wmimofck.GenerateStructureDefinitionsForMethodParameters)</td>
<td align="left"><strong>-m</strong></td>
</tr>
<tr class="even">
<td align="left"><strong>HeaderOuputFile</strong>
<p>Optional string parameter. Generates a C language header file (.h file) that can then be used to keep the header file in sync with MOF definitions.</p></td>
<td align="left">%(Wmimofck.HeaderOuputFile)</td>
<td align="left"><strong>-h</strong><em>Filename</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>HexdumpOutputFile</strong>
<p>Optional string parameter. Generates a Hex version of .bmf data that can be included in the driver source for supplying dynamic MOF data at run time.</p></td>
<td align="left">%(Wmimofck.HexdumpOutputFile)</td>
<td align="left"><strong>-x</strong><em>Filename</em></td>
</tr>
<tr class="even">
<td align="left"><strong>HTMLUIOutputDirectory</strong>
<p>If this is set to true, it generates the -w switch.</p></td>
<td align="left">%(Wmimofck.HTMLUIOutputDirectory)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>HTMLOutputDirectory</strong>
<p>Optional string parameter. Specifies the directory for the HTML files that Wmimofck generates.</p></td>
<td align="left">%(Wmimofck.HTMLOutputDirectory)</td>
<td align="left"><strong>-w</strong><em>Directory</em></td>
</tr>
<tr class="even">
<td align="left"><strong>MFLFile</strong>
<p>Optional string parameter. Specifies a file containing amended classes.</p></td>
<td align="left">%(Wmimofck.MFLFile)</td>
<td align="left"><strong>-z</strong><em>MFLFile</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>MinimalRebuildFromTracking</strong>
<p>Optional Boolean parameter. If true, a tracked incremental build is performed; if false, a rebuild is performed.</p></td>
<td align="left">%(Wmimofck.MinimalRebuildFromTracking)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>MOFFile</strong>
<p>Optional string parameter. Specifies a file containing language-independent WMI class declarations.</p></td>
<td align="left">%(Wmimofck.MOFFile)</td>
<td align="left"><strong>-y</strong><em>MOFFile</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>SourceOutputFile</strong>
<p>Optional string parameter. Generates a C language source file which contains stubs for WMI driver code.</p></td>
<td align="left">%(Wmimofck.SourceOutputFile)</td>
<td align="left"><strong>-c</strong><em>Filename</em></td>
</tr>
<tr class="even">
<td align="left"><strong>TLogReadFiles</strong>
<p>Optional string parameter.</p></td>
<td align="left">@(WmimofckTLogReadFiles)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>TLogWriteFiles</strong>
<p>Optional string parameter.</p></td>
<td align="left">@(WmimofckTLogWriteFiles)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>ToolExe</strong>
<p>Optional string parameter.</p></td>
<td align="left">$(WmimofckToolExe)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>ToolPath</strong>
<p>Optional string parameter. Specifies the full path to the folder where the tool is located.</p></td>
<td align="left">$(WmimofckToolPath)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>TrackerLogDirectory</strong>
<p>Optional string parameter. Specifies the Log directory for tracker to write tlogs.</p></td>
<td align="left">%(Wmimofck.TrackerLogDirectory)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>TrackFileAccess</strong>
<p>Optional Boolean parameter. If true, tracks file access patterns for this task.</p></td>
<td align="left">$(TrackFileAccess)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>ToolArchitecture</strong>
<p>Optional string parameter.</p></td>
<td align="left">$(WmimofckToolArchitecture)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>TrackerFrameworkPath</strong>
<p>Optional string parameter.</p></td>
<td align="left">$(WmimofckTrackerFrameworkPath)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>TrackerSdkPath</strong>
<p>Optional string parameter.</p></td>
<td align="left">$(WmimofckTrackerSdkPath)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>VBScriptTestOutputFile</strong>
<p>Optional string parameter. A VBScript program is created that will query all data blocks and properties specified in the MOF file.</p></td>
<td align="left">%(Wmimofck.VBScriptTestOutputFile)</td>
<td align="left"><strong>-t</strong><em>Filename</em></td>
</tr>
<tr class="even">
<td align="left"><strong>AdditionalOptions</strong>
<p>Optional string parameter.</p></td>
<td align="left">%(Wmimofck.AdditionalOptions)</td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Using Wmimofck.exe](https://msdn.microsoft.com/library/windows/hardware/ff565588)

 

 






