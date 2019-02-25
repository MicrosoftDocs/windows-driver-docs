---
title: InfVerif
description: InfVerif (InfVerif.exe) is a tool that you can use to test a driver INF file. In addition to reporting INF syntax problems, the tool reports if the INF file is universal.
ms.assetid: 6F565E1C-C6FC-4637-B476-FE4E4672CCC3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# InfVerif


InfVerif (InfVerif.exe) is a tool that you can use to test a driver INF file. In addition to reporting INF syntax problems, the tool reports if the INF file is universal.

> [!NOTE]
> InfVerif replaces the ChkINF tool.

When you build a driver in Microsoft Visual Studio 2017 with Windows Driver Kit (WDK) 10, the compiler runs the tool automatically as part of the build process. Alternatively, you can run the InfVerif.exe tool from the command line.

The verification tool is part of the WDK 10 installation, and can be found in the \\tools subdirectory of your WDK 10 installation, c:\\Program Files(x86)\\Windows Kits\\10\\tools\\.

The InfVerif tool reports the following types of errors/warnings:

-   **Errors/Warnings** (1200-1299): These issues do not prevent your driver package from being installed, but they do indicate that specific lines of your INF are not being executed when the driver is installed.

-   **Issues that make an INF non-universal.** (1300-1309)

-   **Warnings** (2000-2999): These issues are always reported as warnings.

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
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Installing a Universal Windows driver](https://msdn.microsoft.com/windows-drivers/develop/installing_a_universal_driver)

[Using a Universal INF File](https://msdn.microsoft.com/library/windows/hardware/dn941087)

 

 






