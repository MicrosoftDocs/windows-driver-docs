---
title: InfVerif
description: InfVerif (InfVerif.exe) is a tool that you can use to test a driver INF file. In addition to reporting INF syntax problems, the tool reports if the INF file is universal.
ms.assetid: 6F565E1C-C6FC-4637-B476-FE4E4672CCC3
---

# InfVerif


InfVerif (InfVerif.exe) is a tool that you can use to test a driver INF file. In addition to reporting INF syntax problems, the tool reports if the INF file is universal.

When you build a driver in Microsoft Visual Studio 2015 with Windows Driver Kit (WDK) 10, the compiler runs the tool automatically as part of the build process. Alternatively, you can run the InfVerif.exe tool from the command line.

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
<td align="left"><p>[Running InfVerif from the command line](running-infverif-from-the-command-line.md)</p></td>
<td align="left"><p>This topic lists the options that are available when you run InfVerif.exe from the command line.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[INF Validation Errors and Warnings](inf-validation-errors-and-warnings.md)</p></td>
<td align="left"><p>This topic describes driver installation errors and warnings that can appear as a result of the automatic INF verification that Visual Studio performs, or when you run the InfVerif tool.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Installing a Universal Windows driver](https://msdn.microsoft.com/windows-drivers/develop/installing_a_universal_driver)

[Using a Universal INF File](https://msdn.microsoft.com/library/windows/hardware/dn941087)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20InfVerif%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





