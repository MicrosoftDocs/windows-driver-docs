---
title: InfVerif
description: Learn about the InfVerif (InfVerif.exe) tool. You can use this tool to test a driver INF file or find out if the INF file is universal.
ms.date: 06/20/2024
---

# InfVerif


InfVerif (InfVerif.exe) is a tool that you can use to test a driver INF file. InfVerif works by passing your INF through the same INF parser that the OS uses, with logging and error checking turned up to maximum.

> [!NOTE]
> InfVerif replaces the ChkINF tool.

When you build a driver in Microsoft Visual Studio 2015 with Windows Driver Kit (WDK) 10 and later versions, the compiler runs the tool automatically as part of the build process. Alternatively, you can run the InfVerif.exe tool from the command line.

The verification tool is part of the WDK 10 installation, and can be found in the `\tools` subdirectory of your WDK 10 installation, `C:\Program Files (x86)\Windows Kits\10\Tools\`.

InfVerif reports errors and warnings based on the mode and rules supplied by the parameters. Errors should be considered "must fix". Warnings can be ignored if they are fully understood, but they are often symptoms of another problem. For instance, a warning about a section being unused could be a symptom of an INF directive being invoked incorrectly.

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
<td align="left"><p><a href="running-infverif-from-the-command-line.md" data-raw-source="[Running InfVerif from the command line](running-infverif-from-the-command-line.md)">Running InfVerif from the command line</a></p></td>
<td align="left"><p>This topic lists the options that are available when you run InfVerif.exe from the command line.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="inf-validation-errors-and-warnings.md" data-raw-source="[INF Validation Errors and Warnings](inf-validation-errors-and-warnings.md)">INF Validation Errors and Warnings</a></p></td>
<td align="left"><p>This topic describes driver installation errors and warnings that can appear as a result of the automatic INF verification that Visual Studio performs, or when you run the InfVerif tool.</p></td>
<tr class="odd">
<td align="left"><p><a href="infverif_h.md" data-raw-source="[InfVerif /h](infverif_h.md)">InfVerif /h</a></p></td>
<td align="left"><p>This topic lists details about the InfVerif mode required for a WHQL signature from Hardware Dev Center.</p></td>
</tr>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Get started developing Windows drivers](../develop/get-started-developing-windows-drivers.md)

[Using a Universal INF File](../install/using-a-universal-inf-file.md)

[Driver Package Isolation](../develop/driver-isolation.md) 

