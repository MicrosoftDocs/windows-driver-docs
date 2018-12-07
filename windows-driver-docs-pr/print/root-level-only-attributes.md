---
title: Root-Level-Only Attributes
description: Root-Level-Only Attributes
ms.assetid: 1b3d74b9-4cf4-4303-92ae-b93b3f9b7f7c
keywords:
- root-level-only attributes WDK Unidrv
- general printer attributes WDK Unidrv , root-level-only
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Root-Level-Only Attributes





Root-level-only attributes are [general attributes](general-attributes.md) that describe such driver-specific characteristics as the names of resource files, help files, or additional included GPD files, along with specifications for the driver's master units, version number, and character code page.

Additional root-level-only attributes specify such device-specific characteristics as the printer's name, type, maximum copy capacity, and number of font cartridge slots.

These attributes are called root-level-only attributes because they must always be placed in a GPD file at root level (that is, not inside braces).

The following table lists the root-level-only attributes.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute Name</th>
<th>AttributeParameter</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em><strong>CodePage</strong></p></td>
<td><p>Numeric-valued Windows code page identifier, as described in the Microsoft Windows SDK documentation.</p></td>
<td><p>Optional. If not specified, Unicode is used. The code page is applied to all displayed strings.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>FontCartSlots</strong></p></td>
<td><p>Numeric value representing the number of font cartridge slots provided by the printer.</p></td>
<td><p>Optional. If not specified, the default value is zero.</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>GPDFileName</strong></p></td>
<td><p>Quoted text string representing the GPD file name (without path).</p></td>
<td><p>Optional.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>GPDFileVersion</strong></p></td>
<td><p>Quoted text string representing the current GPD file version. Recommended format is <em>MajorVersion</em>.<em>MinorVersion</em>, such as &quot;1.0&quot;.</p></td>
<td><p>Optional. If specified, this string is displayed in Unidrv&#39;s About dialog box.</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>GPDSpecVersion</strong></p></td>
<td><p>Quoted text string representing the current GPD specification version. Required format is <em>MajorVersion</em>.<em>MinorVersion</em>, such as &quot;1.0&quot;.</p></td>
<td><p>Required. Must be first entry in GPD file, before any comments.</p>
<p>This value must be &quot;1.0&quot; for Windows 2000.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>HelpFile</strong></p></td>
<td><p>Quoted string containing the name of a customized help file, with a .hlp extension.</p></td>
<td><p>Optional. If included, it can add topics or overwrite existing topics in Unidrv&#39;s help file. Help file indexes are specified by <em>HelpIndex attributes for features and options.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>Include</strong></p></td>
<td><p>Quoted string containing the name of an additional GPD file.</p></td>
<td><p>Obsolete. This entry has been redefined as a <a href="preprocessor-directives.md" data-raw-source="[preprocessor directive](preprocessor-directives.md)">preprocessor directive</a>.</p></td>
</tr>
<tr class="even">
<td><p><em><strong>InstalledOptionName</strong></p></td>
<td><p>Quoted string that is displayed to indicate an installable feature or option is installed. Typically, this string is &quot;Installed&quot;, but any appropriate string can be specified.</p></td>
<td><p>Required if <em>Installable? is <strong>TRUE</strong> for any features or options (see <a href="feature-attributes.md" data-raw-source="[Feature Attributes](feature-attributes.md)">Feature Attributes</a>), and if *<strong>rcInstalledOptionNameID</strong> is not specified.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>MasterUnits</strong></p></td>
<td><p>PAIR representing the printer&#39;s <a href="master-units.md" data-raw-source="[master units](master-units.md)">master units</a>.</p></td>
<td><p>Required. To reduce potential round-off errors, use the same values for resolution units in font metrics data that you specify for <em><strong>MasterUnits</strong>. (See Unidrv Font Metrics in <a href="customized-font-management.md" data-raw-source="[Customized Font Management](customized-font-management.md)">Customized Font Management</a>.)</p></td>
</tr>
<tr class="even">
<td><p></em><strong>MaxCopies</strong></p></td>
<td><p>Numeric value representing the maximum number of copies the printer can support.</p></td>
<td><p>Optional. If not specified, the default value is 1.</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>ModelName</strong></p></td>
<td><p>Quoted text string representing the printer model name.</p></td>
<td><p>Required if *<strong>rcModelNameID</strong> is not specified. String must match name in setup.inf.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>NotInstalledOptionName</strong></p></td>
<td><p>Quoted string that is displayed to indicate an installable feature or option is not installed. Typically, this string is &quot;Not installed&quot;, but any appropriate string can be specified.</p></td>
<td><p>Required if <em><strong>Installable?</strong> is <strong>TRUE</strong> for any features or options (see <a href="feature-attributes.md" data-raw-source="[Feature Attributes](feature-attributes.md)">Feature Attributes</a>), and if *<strong>rcNotInstalledOptionNameID</strong> is not specified.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>Personality</strong></p></td>
<td><p>Quoted string representing the printer language used by the printer.</p></td>
<td><p>Optional. If specified, the string is displayed by Directory Services. Also see <em>rcPersonalityID.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>PrinterType</strong></p></td>
<td><p>PAGE, SERIAL, or TTY</p></td>
<td><p>Required.</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>PrintRate</strong></p></td>
<td><p>Numeric value representing the monochrome print rate. Units are specified by *<strong>PrintRateUnit</strong>.</p></td>
<td><p>Optional. If not specified, the default value is 0.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>PrintRatePPM</strong></p></td>
<td><p>Numeric value representing the printing speed, in pages per minute.</p></td>
<td><p>Optional. If not specified, the default value is 0.</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>PrintRateUnit</strong></p></td>
<td><p></p>
PPM - Pages/min.
CPS - Characters/sec.
LPM - Lines/min.
IPM - Inches/min. (IPM is for plotters)</td>
<td><p>Required if *<strong>PrintRate</strong> is specified. The specified unit should match the printer type. For example, PPM should be specified for page printers.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>rcInstalledOptionNameID</strong></p></td>
<td><p>Resource ID of a string resource that is displayed to indicate an installable feature or option is installed. Typically, this string is &quot;Installed&quot;, but any appropriate string can be specified.</p></td>
<td><p>Required if <em>Installable? is <strong>TRUE</strong> for any features or options (see <a href="feature-attributes.md" data-raw-source="[Feature Attributes](feature-attributes.md)">Feature Attributes</a>), and if *<strong>InstalledOptionName</strong> is not specified.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>rcNotInstalledOptionNameID</strong></p></td>
<td><p>Resource ID of a string resource that is displayed to indicate an installable feature or option is not installed. Typically, this string is &quot;Not installed&quot;, but any appropriate string can be specified.</p></td>
<td><p>Required if <em><strong>Installable?</strong> is <strong>TRUE</strong> for any features or options (see <a href="feature-attributes.md" data-raw-source="[Feature Attributes](feature-attributes.md)">Feature Attributes</a>), and if *<strong>NotInstalledOptionName</strong> is not specified.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>rcPersonalityID</strong></p></td>
<td><p>Resource ID of a string resource representing the printer language used by the printer.</p></td>
<td><p>Optional. If specified, the string is displayed by Directory Services. Also see <em>Personality.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>rcPrinterIconID</strong></p></td>
<td><p>Resource ID of an RC_ICON resource representing an icon associated with the printer.</p></td>
<td><p>Optional. If not specified, a default printer icon is displayed. It is recommended that all RC_ICON resource IDs be numbered contiguously starting with 1.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>ResourceDLL</strong></p></td>
<td><p>Quoted string containing the name, without path information, of a resource DLL.</p></td>
<td><p>Optional. See <a href="using-resource-dlls-in-a-minidriver.md" data-raw-source="[Using Resource DLLs in a Minidriver](using-resource-dlls-in-a-minidriver.md)">Using Resource DLLs in a Minidriver</a>.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

For information about new root-level-only attributes for Windows Vista, see [New Root-Level-Only GPD Attributes for Windows Vista](new-root-level-only-gpd-attributes-for-windows-vista.md) and [New Root-Level-Only PPD Attributes for Windows Vista](new-root-level-only-ppd-attributes-for-windows-vista.md).

 

 




