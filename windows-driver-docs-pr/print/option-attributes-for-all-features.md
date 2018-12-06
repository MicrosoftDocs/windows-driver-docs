---
title: Option Attributes for All Features
description: Option Attributes for All Features
ms.assetid: 0d269fdf-f4a1-431a-9f07-044289b9f0fa
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Option Attributes for All Features





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
<td><p><em><strong>Command</strong></p></td>
<td><p>A <strong>CmdSelect</strong> <a href="option-selection-command.md" data-raw-source="[option selection command](option-selection-command.md)">option selection command</a>, specifying the command string that must be sent to the printer in order to select the option.</p></td>
<td><p>Required.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>DisabledFeatures</strong></p></td>
<td><p>LIST of feature name strings, identifying features that should be disabled if the option is selected.</p>
<p>Currently DUPLEX and COLLATE features are supported. This option attribute must be used in a feature that has FeatureType set to PRINTER_PROPERTY.</p></td>
<td><p>Optional.</p>
<p>Listed features cannot have <em><strong>Installable?</strong> set to <strong>TRUE</strong>. For more information, see <a href="handling-installable-features-and-options.md" data-raw-source="[Handling Installable Features and Options](handling-installable-features-and-options.md)">Handling Installable Features and Options</a>.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>HelpIndex</strong></p></td>
<td><p>Numeric value representing an index into the help file specified by the <em><strong>HelpFile</strong><a href="root-level-only-attributes.md" data-raw-source="[root-level-only attribute](root-level-only-attributes.md)">root-level-only attribute</a>.</p></td>
<td><p>(Also a <a href="feature-attributes.md" data-raw-source="[feature attribute](feature-attributes.md)">feature attribute</a>.)</p>
<p>Index value cannot be zero or -1.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>Installable?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the option is installable. (<strong>FALSE</strong> means always installed.)</p>
<p>For more information, see <a href="handling-installable-features-and-options.md" data-raw-source="[Handling Installable Features and Options](handling-installable-features-and-options.md)">Handling Installable Features and Options</a>.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>. (Also a <a href="feature-attributes.md" data-raw-source="[feature attribute](feature-attributes.md)">feature attribute</a>.)</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>InstallableFeatureName</strong></p></td>
<td><p>Text string that is displayed to ask the user whether an installable option is actually installed.</p>
<p>For more information, see <a href="handling-installable-features-and-options.md" data-raw-source="[Handling Installable Features and Options](handling-installable-features-and-options.md)">Handling Installable Features and Options</a>.</p></td>
<td><p>Required if *<strong>Installable?</strong> is <strong>TRUE</strong> and *<strong>rcInstallableFeatureNameID</strong> is not specified. (Also a <a href="feature-attributes.md" data-raw-source="[feature attribute](feature-attributes.md)">feature attribute</a>.)</p></td>
</tr>
<tr class="even">
<td><p></em><strong>Name</strong></p></td>
<td><p>Text string used as the option&#39;s display name on the printer&#39;s property sheet.</p></td>
<td><p>Optional. If not specified, then <em><strong>rcNameID</strong> must be specified. (Also a <a href="feature-attributes.md" data-raw-source="[feature attribute](feature-attributes.md)">feature attribute</a>.)</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>OptionID</strong></p></td>
<td><p>Numeric value representing a unique option identifier that Unidrv stores in the printer&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837" data-raw-source="[&lt;strong&gt;DEVMODEW&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552837)"><strong>DEVMODEW</strong></a> structure. For use only with the PaperSize, InputSlot, Halftoning, and MediaType features. Value is stored in the DEVMODE structure&#39;s <strong>dmPaperSize</strong>, <strong>dmDefaultSource</strong>, <strong>dmDitherType</strong>, or <strong>dmMediaType</strong> member, respectively.</p></td>
<td><p>Optional. If not specified, Unidrv assigns an identifier value (&gt;256). To avoid conflicts with Unidrv-assigned identifiers, the specified value must be greater than 512.</p></td>
</tr>
<tr class="even">
<td><p><em><strong>rcIconID</strong></p></td>
<td><p>Resource ID of an icon resource associated with the option.</p></td>
<td><p>Optional. If not specified, Unidrv does not display an icon for the option on the printer property sheet. (Also a <a href="feature-attributes.md" data-raw-source="[feature attribute](feature-attributes.md)">feature attribute</a>.)</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>rcInstallableFeatureNameID</strong></p></td>
<td><p>Resource ID of a text string that is displayed to ask the user whether an installable option is actually installed.</p>
<p>For more information, see <a href="handling-installable-features-and-options.md" data-raw-source="[Handling Installable Features and Options](handling-installable-features-and-options.md)">Handling Installable Features and Options</a>.</p></td>
<td><p>Required if <em><strong>Installable?</strong> is <strong>TRUE</strong> and *<strong>InstallableFeatureName</strong> is not specified. (Also a <a href="feature-attributes.md" data-raw-source="[feature attribute](feature-attributes.md)">feature attribute</a>.)</p></td>
</tr>
<tr class="even">
<td><p></em><strong>rcNameID</strong></p></td>
<td><p>Resource ID of string resource representing the option name.</p></td>
<td><p>Optional. If not specified, then *<strong>Name</strong> must be specified. (Also a <a href="feature-attributes.md" data-raw-source="[feature attribute](feature-attributes.md)">feature attribute</a>.)</p>
<p>For <a href="standard-options.md" data-raw-source="[standard options](standard-options.md)">standard options</a> of the PaperSize feature only, setting this attribute to RCID_DMPAPER_SYSTEM_NAME causes Unidrv to use a predefined option name string.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 




