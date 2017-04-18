---
title: Root-Level-Only Attributes
author: windows-driver-content
description: Root-Level-Only Attributes
ms.assetid: 1b3d74b9-4cf4-4303-92ae-b93b3f9b7f7c
keywords: ["root-level-only attributes WDK Unidrv", "general printer attributes WDK Unidrv , root-level-only"]
---

# Root-Level-Only Attributes


## <a href="" id="ddk-root-level-only-attributes-gg"></a>


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
<td><p>*<strong>CodePage</strong></p></td>
<td><p>Numeric-valued Windows code page identifier, as described in the Microsoft Windows SDK documentation.</p></td>
<td><p>Optional. If not specified, Unicode is used. The code page is applied to all displayed strings.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>FontCartSlots</strong></p></td>
<td><p>Numeric value representing the number of font cartridge slots provided by the printer.</p></td>
<td><p>Optional. If not specified, the default value is zero.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>GPDFileName</strong></p></td>
<td><p>Quoted text string representing the GPD file name (without path).</p></td>
<td><p>Optional.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>GPDFileVersion</strong></p></td>
<td><p>Quoted text string representing the current GPD file version. Recommended format is <em>MajorVersion</em>.<em>MinorVersion</em>, such as &quot;1.0&quot;.</p></td>
<td><p>Optional. If specified, this string is displayed in Unidrv's About dialog box.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>GPDSpecVersion</strong></p></td>
<td><p>Quoted text string representing the current GPD specification version. Required format is <em>MajorVersion</em>.<em>MinorVersion</em>, such as &quot;1.0&quot;.</p></td>
<td><p>Required. Must be first entry in GPD file, before any comments.</p>
<p>This value must be &quot;1.0&quot; for Windows 2000.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>HelpFile</strong></p></td>
<td><p>Quoted string containing the name of a customized help file, with a .hlp extension.</p></td>
<td><p>Optional. If included, it can add topics or overwrite existing topics in Unidrv's help file. Help file indexes are specified by *HelpIndex attributes for features and options.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>Include</strong></p></td>
<td><p>Quoted string containing the name of an additional GPD file.</p></td>
<td><p>Obsolete. This entry has been redefined as a [preprocessor directive](preprocessor-directives.md).</p></td>
</tr>
<tr class="even">
<td><p>*<strong>InstalledOptionName</strong></p></td>
<td><p>Quoted string that is displayed to indicate an installable feature or option is installed. Typically, this string is &quot;Installed&quot;, but any appropriate string can be specified.</p></td>
<td><p>Required if *Installable? is <strong>TRUE</strong> for any features or options (see [Feature Attributes](feature-attributes.md)), and if *<strong>rcInstalledOptionNameID</strong> is not specified.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>MasterUnits</strong></p></td>
<td><p>PAIR representing the printer's [master units](master-units.md).</p></td>
<td><p>Required. To reduce potential round-off errors, use the same values for resolution units in font metrics data that you specify for *<strong>MasterUnits</strong>. (See Unidrv Font Metrics in [Customized Font Management](customized-font-management.md).)</p></td>
</tr>
<tr class="even">
<td><p>*<strong>MaxCopies</strong></p></td>
<td><p>Numeric value representing the maximum number of copies the printer can support.</p></td>
<td><p>Optional. If not specified, the default value is 1.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>ModelName</strong></p></td>
<td><p>Quoted text string representing the printer model name.</p></td>
<td><p>Required if *<strong>rcModelNameID</strong> is not specified. String must match name in setup.inf.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>NotInstalledOptionName</strong></p></td>
<td><p>Quoted string that is displayed to indicate an installable feature or option is not installed. Typically, this string is &quot;Not installed&quot;, but any appropriate string can be specified.</p></td>
<td><p>Required if *<strong>Installable?</strong> is <strong>TRUE</strong> for any features or options (see [Feature Attributes](feature-attributes.md)), and if *<strong>rcNotInstalledOptionNameID</strong> is not specified.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>Personality</strong></p></td>
<td><p>Quoted string representing the printer language used by the printer.</p></td>
<td><p>Optional. If specified, the string is displayed by Directory Services. Also see *rcPersonalityID.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>PrinterType</strong></p></td>
<td><p>PAGE, SERIAL, or TTY</p></td>
<td><p>Required.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>PrintRate</strong></p></td>
<td><p>Numeric value representing the monochrome print rate. Units are specified by *<strong>PrintRateUnit</strong>.</p></td>
<td><p>Optional. If not specified, the default value is 0.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>PrintRatePPM</strong></p></td>
<td><p>Numeric value representing the printing speed, in pages per minute.</p></td>
<td><p>Optional. If not specified, the default value is 0.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>PrintRateUnit</strong></p></td>
<td><p></p>
PPM - Pages/min.
CPS - Characters/sec.
LPM - Lines/min.
IPM - Inches/min. (IPM is for plotters)</td>
<td><p>Required if *<strong>PrintRate</strong> is specified. The specified unit should match the printer type. For example, PPM should be specified for page printers.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>rcInstalledOptionNameID</strong></p></td>
<td><p>Resource ID of a string resource that is displayed to indicate an installable feature or option is installed. Typically, this string is &quot;Installed&quot;, but any appropriate string can be specified.</p></td>
<td><p>Required if *Installable? is <strong>TRUE</strong> for any features or options (see [Feature Attributes](feature-attributes.md)), and if *<strong>InstalledOptionName</strong> is not specified.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>rcNotInstalledOptionNameID</strong></p></td>
<td><p>Resource ID of a string resource that is displayed to indicate an installable feature or option is not installed. Typically, this string is &quot;Not installed&quot;, but any appropriate string can be specified.</p></td>
<td><p>Required if *<strong>Installable?</strong> is <strong>TRUE</strong> for any features or options (see [Feature Attributes](feature-attributes.md)), and if *<strong>NotInstalledOptionName</strong> is not specified.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>rcPersonalityID</strong></p></td>
<td><p>Resource ID of a string resource representing the printer language used by the printer.</p></td>
<td><p>Optional. If specified, the string is displayed by Directory Services. Also see *Personality.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>rcPrinterIconID</strong></p></td>
<td><p>Resource ID of an RC_ICON resource representing an icon associated with the printer.</p></td>
<td><p>Optional. If not specified, a default printer icon is displayed. It is recommended that all RC_ICON resource IDs be numbered contiguously starting with 1.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>ResourceDLL</strong></p></td>
<td><p>Quoted string containing the name, without path information, of a resource DLL.</p></td>
<td><p>Optional. See [Using Resource DLLs in a Minidriver](using-resource-dlls-in-a-minidriver.md).</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

For information about new root-level-only attributes for Windows Vista, see [New Root-Level-Only GPD Attributes for Windows Vista](new-root-level-only-gpd-attributes-for-windows-vista.md) and [New Root-Level-Only PPD Attributes for Windows Vista](new-root-level-only-ppd-attributes-for-windows-vista.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Root-Level-Only%20Attributes%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


