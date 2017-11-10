---
title: Option Attributes for All Features
author: windows-driver-content
description: Option Attributes for All Features
ms.assetid: 0d269fdf-f4a1-431a-9f07-044289b9f0fa
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Option Attributes for All Features


## <a href="" id="ddk-option-attributes-for-all-features-gg"></a>


The following table lists, in alphabetic order, the [option attributes](option-attributes.md) available for all features and describes their parameters.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute Name</th>
<th>Attribute Parameter</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>*<strong>Command</strong></p></td>
<td><p>A <strong>CmdSelect</strong> [option selection command](option-selection-command.md), specifying the command string that must be sent to the printer in order to select the option.</p></td>
<td><p>Required.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>DisabledFeatures</strong></p></td>
<td><p>LIST of feature name strings, identifying features that should be disabled if the option is selected.</p></td>
<td><p>Optional.</p>
<p>Listed features cannot have *<strong>Installable?</strong> set to <strong>TRUE</strong>. For more information, see [Handling Installable Features and Options](handling-installable-features-and-options.md).</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>HelpIndex</strong></p></td>
<td><p>Numeric value representing an index into the help file specified by the *<strong>HelpFile</strong>[root-level-only attribute](root-level-only-attributes.md).</p></td>
<td><p>(Also a [feature attribute](feature-attributes.md).)</p>
<p>Index value cannot be zero or -1.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>Installable?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the option is installable. (<strong>FALSE</strong> means always installed.)</p>
<p>For more information, see [Handling Installable Features and Options](handling-installable-features-and-options.md).</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>. (Also a [feature attribute](feature-attributes.md).)</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>InstallableFeatureName</strong></p></td>
<td><p>Text string that is displayed to ask the user whether an installable option is actually installed.</p>
<p>For more information, see [Handling Installable Features and Options](handling-installable-features-and-options.md).</p></td>
<td><p>Required if *<strong>Installable?</strong> is <strong>TRUE</strong> and *<strong>rcInstallableFeatureNameID</strong> is not specified. (Also a [feature attribute](feature-attributes.md).)</p></td>
</tr>
<tr class="even">
<td><p>*<strong>Name</strong></p></td>
<td><p>Text string used as the option's display name on the printer's property sheet.</p></td>
<td><p>Optional. If not specified, then *<strong>rcNameID</strong> must be specified. (Also a [feature attribute](feature-attributes.md).)</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>OptionID</strong></p></td>
<td><p>Numeric value representing a unique option identifier that Unidrv stores in the printer's [<strong>DEVMODEW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure. For use only with the PaperSize, InputSlot, Halftoning, and MediaType features. Value is stored in the DEVMODE structure's <strong>dmPaperSize</strong>, <strong>dmDefaultSource</strong>, <strong>dmDitherType</strong>, or <strong>dmMediaType</strong> member, respectively.</p></td>
<td><p>Optional. If not specified, Unidrv assigns an identifier value (&gt;256). To avoid conflicts with Unidrv-assigned identifiers, the specified value must be greater than 512.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>rcIconID</strong></p></td>
<td><p>Resource ID of an icon resource associated with the option.</p></td>
<td><p>Optional. If not specified, Unidrv does not display an icon for the option on the printer property sheet. (Also a [feature attribute](feature-attributes.md).)</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>rcInstallableFeatureNameID</strong></p></td>
<td><p>Resource ID of a text string that is displayed to ask the user whether an installable option is actually installed.</p>
<p>For more information, see [Handling Installable Features and Options](handling-installable-features-and-options.md).</p></td>
<td><p>Required if *<strong>Installable?</strong> is <strong>TRUE</strong> and *<strong>InstallableFeatureName</strong> is not specified. (Also a [feature attribute](feature-attributes.md).)</p></td>
</tr>
<tr class="even">
<td><p>*<strong>rcNameID</strong></p></td>
<td><p>Resource ID of string resource representing the option name.</p></td>
<td><p>Optional. If not specified, then *<strong>Name</strong> must be specified. (Also a [feature attribute](feature-attributes.md).)</p>
<p>For [standard options](standard-options.md) of the PaperSize feature only, setting this attribute to RCID_DMPAPER_SYSTEM_NAME causes Unidrv to use a predefined option name string.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Option%20Attributes%20for%20All%20Features%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


