---
title: Stampinf task
description: The Windows Driver Kit (WDK) provides the StampInf task so that you can run the stampinf.exe tool when you build your driver using MSBuild. For information about the stampinf.exe tool, see Stampinf.
ms.assetid: 4BD937D3-97C7-408D-9372-F01CBB7B0B62
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stampinf task


The Windows Driver Kit (WDK) provides the StampInf task so that you can run the stampinf.exe tool when you build your driver using MSBuild. For information about the stampinf.exe tool, see [Stampinf](stampinf.md).

The Inf Item sends the parameters for the StampInf task. The item metadata for stampinf is accessed by using the Inf item in project files.

The following example shows how the edit metadata in the .vcxproj file.

```XML
<ItemGroup>
    <Inf Include="a.inf">
      <SpecifyArchitecture>true</SpecifyArchitecture>
      <Architecture>x86</Architecture>
    </Inf>
    <Inf Include="b.inf">
      <SpecifyArchitecture>false</SpecifyArchitecture>
      <Architecture>amd64</Architecture>
    </Inf>
</ItemGroup>
```

The following example shows the command-line invocation:

```
stampinf.exe –a "x86" a.inf
stampinf.exe b.inf
```

In the example above, MSBuild invokes stampinf.exe on both a.inf and b.inf, but with different sets of parameters. In the case of b.inf, even though the **Architecture** metadata is specified, the **SpecifyArchitecture** metadata is set to false. Therefore, the **–a** switch is not enabled on the command line. If you set this metadata to **TRUE**, then it will enable **–a amd64** on the command line. In this way, you can just toggle this metadata and not have to edit the architecture metadata itself.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">StampInf Task Parameter</th>
<th align="left">Item Metadata</th>
<th align="left">Tool Switch</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>Source</strong>
<p>Required ITaskItem parameter. Specifies a list of source files.</p></td>
<td align="left">%(Inf.OutputPath)%(Inf.FileName).inf</td>
<td align="left"><strong>-f</strong><em>[source]</em></td>
</tr>
<tr class="even">
<td align="left"><strong>SpecifyArchitecture</strong>
<p>This will enable the -a switch if set to true.</p></td>
<td align="left">%(Inf.SpecifyArchitecture)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>Architecture</strong>
<p>Optional string parameter. Specifies the target platform architecture.</p></td>
<td align="left">%(Inf.Architecture)</td>
<td align="left"><strong>-a</strong><em>[architecture]</em></td>
</tr>
<tr class="even">
<td align="left"><strong>CatalogFile</strong>
<p>Optional string parameter. Specifies the catalog file directive in the INF version section.</p></td>
<td align="left">%(Inf.CatalogFileName)</td>
<td align="left"><strong>-c</strong><em>&lt;catalogFile&gt;</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>SpecifyDriverVerDirectiveDate</strong>
<p>This will enable the –d switch if set to true.</p></td>
<td align="left">%(Inf.SpecifyDriverVerDirectiveDate)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>DriverVerDirectiveDate</strong>
<p>Optional string</p></td>
<td align="left">%(Inf.DateStamp)</td>
<td align="left"><strong>-d</strong><em>[date|<em>]</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>DriverVerDirectiveSection</strong>
<p>Optional string parameter. Specifies the INF section in which the INF DriverVer directive should be placed.</p></td>
<td align="left">%(Inf.DriverVersionSectionName)</td>
<td align="left"><strong>-s</strong></td>
</tr>
<tr class="even">
<td align="left"><strong>SpecifyDriverVerDirectiveVersion</strong>
<p>This will enable the –v switch if set to true.</p></td>
<td align="left">%(Inf.SpecifyDriverDirectiveVersion)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>DriverVerDirectiveVersion</strong>
<p>Optional string parameter. Specifies the version number in the driver directive.</p></td>
<td align="left">%(Inf.TimeStamp)</td>
<td align="left"><strong>-v</strong><em>[time|</em>]</em></td>
</tr>
<tr class="even">
<td align="left"><strong>KmdfVersion</strong>
<p>Optional string parameter. Specifies the version of KMDF that this driver depends on.</p></td>
<td align="left">%(Inf.KmdfVersionNumber)</td>
<td align="left"><strong>-k</strong><em>&lt;version&gt;</em></td>
</tr>
<tr class="odd">
<td align="left"><strong>MinimalRebuildFromTracking</strong>
<p>Optional Boolean parameter. If true, a tracked incremental build is performed. Otherwise, a rebuild is performed.</p></td>
<td align="left">%(Inf.MinimalRebuildFromTracking)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>ToolPath</strong>
<p>Optional string parameter. Allows you to specify the full path to the folder where the tool is located.</p></td>
<td align="left">$(StampInfToolPath)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>TrackerLogDirectory</strong>
<p>Optional string parameter. Specifies a log directory for tracker to write tlogs.</p></td>
<td align="left">%(Inf.StampInfTrackerLogDirectory)</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>TrackFileAccess</strong>
<p>Optional Boolean parameter. If true, tracks file access patterns for this task.</p></td>
<td align="left">$(TrackFileAccess)</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>UmdfVersion</strong>
<p>Optional string parameter. Specifies the version of UMDF that this driver depends on.</p></td>
<td align="left">%(Inf.UmdfVersionNumber)</td>
<td align="left"><strong>-u</strong><em>&lt;version&gt;</em></td>
</tr>
<tr class="even">
<td align="left"><strong>Verbosity</strong>
<p>Optional Boolean parameter. Enables the verbosity of Stampinf output.</p></td>
<td align="left">%(Inf.EnableVerbose)</td>
<td align="left"><strong>-n</strong></td>
</tr>
</tbody>
</table>

 

 

 





