---
title: Mofcomp task
description: The Windows Driver Kit (WDK) provides the Mofcomp task so that you can run the Mofcomp.exe tool when you build your driver using MSBuld.
ms.assetid: 94B70223-393F-49C9-B2C9-34FF64D26454
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mofcomp task


The Windows Driver Kit (WDK) provides the Mofcomp task so that you can run the Mofcomp.exe tool when you build your driver using MSBuld. For information about the tool, see [**mofcomp**](https://msdn.microsoft.com/library/aa392389).

MSBuild uses the Mofcomp item to send the parameters for the Mofcomp task to Mofcomp.exe. The item metadata for Mofcomp is accessed using the Mofcomp item in project files.

The following example shows how to edit metadata in the .vcxproj file.

```XML
<ItemGroup>
    <Mofcomp Include="b.mof">
      <WMISyntaxCheck>true</WMISyntaxCheck>
    </Mofcomp>
</ItemGroup>
```

The following example shows the command-line invocation:

```
mofcomp.exe -WMI b.mof
```

This example invokes mofcomp.exe on the file b.mof with the -WMI switch.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Mofcomp Task Parameter</th>
<th align="left">Item Metadata</th>
<th align="left">Tool Switch</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Sources</td>
<td align="left">@(Mofcomp)</td>
<td align="left"></td>
<td align="left">Required ITaskItem[] parameter. Specifies a list of source files.</td>
</tr>
<tr class="even">
<td align="left">Amendment</td>
<td align="left">%(Mofcomp.Amendment)</td>
<td align="left"><strong>-AMENDMENT:</strong><em>&lt;Locale&gt;</em></td>
<td align="left">Optional string parameter. Splits the MOF file into language-neutral and -specific versions.</td>
</tr>
<tr class="odd">
<td align="left">Authority</td>
<td align="left">%(Mofcomp.Authority)</td>
<td align="left"><strong>-A:</strong><em>&lt;Authority&gt;</em></td>
<td align="left">Optional string parameter. Specifies Authority as the authority (domain name) to use when logging on to WMI.</td>
</tr>
<tr class="even">
<td align="left">AutoRecover</td>
<td align="left">%(Mofcomp.AutoRecover)</td>
<td align="left"><strong>-autorecover</strong></td>
<td align="left">Optional Boolean parameter. Adds the named MOF file to the list of files compiled during repository recovery.</td>
</tr>
<tr class="odd">
<td align="left">CreateBinaryMOFFile</td>
<td align="left">%(Mofcomp.CreateBinaryMOFFile)</td>
<td align="left"><strong>-B:</strong><em>&lt;Filename&gt;</em></td>
<td align="left">Optional string parameter. Requests that the compiler create a binary version of the MOF file with the name Filename without making any modifications to the WMI repository.</td>
</tr>
<tr class="even">
<td align="left">LanguageNeutralOutput</td>
<td align="left">%(Mofcomp.LanguageNeutralOutput)</td>
<td align="left"><strong>-MOF:</strong><em>&lt;Path&gt;</em></td>
<td align="left">Optional string parameter. Name of the language neutral output.</td>
</tr>
<tr class="odd">
<td align="left">LanguageSpecificOutput</td>
<td align="left">%(Mofcomp.LanguageSpecificOutput)</td>
<td align="left"><strong>-MFL:</strong><em>&lt;Path&gt;</em></td>
<td align="left">Optional string parameter. Name of the language specific output.</td>
</tr>
<tr class="even">
<td align="left">MinimalRebuildFromTracking</td>
<td align="left">%(Mofcomp.MinimalRebuildFromTracking)</td>
<td align="left"></td>
<td align="left">Optional Boolean parameter. If true, a tracked incremental build is performed; otherwise, a rebuild is performed.</td>
</tr>
<tr class="odd">
<td align="left">MOFClass</td>
<td align="left">%(Mofcomp.MOFClass)</td>
<td align="left"><ul>
<li><strong>-class:</strong><em>createonly</em></li>
<li><strong>-class:</strong><em>forceupdate</em></li>
<li><strong>-class:</strong><em>safeupdate</em></li>
<li><strong>-class:</strong><em>updateonly</em></li>
</ul></td>
<td align="left">Optional string parameter. Allows or Disallows the creation or update of classes in MOF files. See the documentation on the -class family of switches for details.</td>
</tr>
<tr class="even">
<td align="left">MOFInstance</td>
<td align="left">%(Mofcomp.MOFInstance)</td>
<td align="left"><ul>
<li><strong>-instance:</strong><em>createonly</em></li>
<li><strong>-instance:</strong><em>updateonly</em></li>
</ul></td>
<td align="left">Optional string parameter. Allows the creation or update of instances in MOF files. See the documentation on the -instance family of switches for details.</td>
</tr>
<tr class="odd">
<td align="left">NamespacePath</td>
<td align="left">%(Mofcomp.NamespacePath)</td>
<td align="left"><strong>-N:</strong><em>&lt;namespacepath&gt;</em></td>
<td align="left">Optional string parameter. Requests that the compiler load the MOF file into the namespace specified as namespacepath.</td>
</tr>
<tr class="even">
<td align="left">Password</td>
<td align="left">%(Mofcomp.Password)</td>
<td align="left"><strong>-P:</strong><em>&lt;Password&gt;</em></td>
<td align="left">Optional string parameter. Specifies Password as the password for the computer user to enter when logging on.</td>
</tr>
<tr class="odd">
<td align="left">ResourceLocale</td>
<td align="left">%(Mofcomp.ResourceLocale)</td>
<td align="left"><strong>-L:</strong><em>&lt;ResourceLocale&gt;</em></td>
<td align="left">Optional string parameter. Extracts the localized MOF descriptions from the binary MOF when used with -ER switch.</td>
</tr>
<tr class="even">
<td align="left">ResourceName</td>
<td align="left">%(Mofcomp.ResourceName)</td>
<td align="left"><strong>-ER:</strong><em>&lt;ResourceName&gt;</em></td>
<td align="left">Optional string parameter. Extracts binary MOF from a named resource.</td>
</tr>
<tr class="odd">
<td align="left">SyntaxCheck</td>
<td align="left">%(Mofcomp.SyntaxCheck)</td>
<td align="left"><strong>-check</strong></td>
<td align="left">Optional Boolean parameter. Requests that the compiler perform a syntax check only and print appropriate error messages. No other switch can be used with this switch.</td>
</tr>
<tr class="even">
<td align="left">ToolPath</td>
<td align="left">$(MofcompToolPath)</td>
<td align="left"></td>
<td align="left">Optional string parameter. Allows you to specify the full path to the folder where the tool is located.</td>
</tr>
<tr class="odd">
<td align="left">TrackerLogDirectory</td>
<td align="left">%(Mofcomp.TrackerLogDirectory)</td>
<td align="left"></td>
<td align="left">Optional string parameter. Specifies the Log directory for tracker to write tlogs.</td>
</tr>
<tr class="even">
<td align="left">TrackFileAccess</td>
<td align="left">$(TrackFileAccess)</td>
<td align="left"></td>
<td align="left">Optional Boolean parameter. If true, tracks file access patterns for this task.</td>
</tr>
<tr class="odd">
<td align="left">UserName</td>
<td align="left">%(Mofcomp.UserName)</td>
<td align="left"><strong>-U:</strong><em>&lt;UserName&gt;</em></td>
<td align="left">Optional string parameter. Specifies UserName as the name of the user who is logging on.</td>
</tr>
<tr class="even">
<td align="left">WMISyntaxCheck</td>
<td align="left">%(Mofcomp.WMISyntaxCheck)</td>
<td align="left"><strong>-WMI</strong></td>
<td align="left">Optional Boolean parameter. Requests that the compiler perform a WMI syntax check. The -B: switch must be used with this switch.</td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[**mofcomp**](https://msdn.microsoft.com/library/aa392389)

 

 






