---
title: Feature Attributes
author: windows-driver-content
description: Feature Attributes
ms.assetid: ae1a489e-2554-46fc-8f2e-45128b073f91
keywords:
- printer attributes WDK Unidrv , features
- feature attribues WDK Unidrv
- printer features WDK Unidrv , attributes
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Feature Attributes


## <a href="" id="ddk-feature-attributes-gg"></a>


When specifying a printer feature, you use attributes to provide Unidrv with the following information:

-   A text string representing the feature's display name.

-   The set of printer options associated with the feature.

-   A Boolean value indicating whether the feature is always present or is installable.

-   The feature type and priority, if the feature is customized, indicating on which property sheet the feature is displayed and its relative priority.

The following table lists the feature attributes in alphabetic order and describes their parameters.

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
<td><p><strong>*ConcealFromUI?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the feature should be displayed in the user interface.</p></td>
<td><p>Optional. If not specified the default value is <strong>FALSE</strong>, which means the feature is displayed.</p>
<p>Should be <strong>TRUE</strong> only if a feature has only one option (for example, one resolution) and is thus not user-modifiable, or, if the feature's option selection is controlled by setting another feature's options.</p>
<p>If the <strong>*ConcealFromUI</strong> attribute is set to <strong>TRUE</strong>, then Unidrv or PrintConfig will add the psk:DisplayUI element to the Feature element for this item in the PrintCapabilities XML.</p></td>
</tr>
<tr class="even">
<td><p><strong>*ConflictPriority</strong></p></td>
<td><p>Numeric value representing the feature's priority, where 1 is the highest priority.</p></td>
<td><p>Optional. See [Feature Conflict Priority](feature-conflict-priority.md).</p></td>
</tr>
<tr class="odd">
<td><p><strong>*DefaultOption</strong></p></td>
<td><p>Name of one of the feature's options.</p></td>
<td><p>Optional. If not specified, the first option listed in a *Feature entry is the default. For the PaperSize feature, the default options for Unidrv are A4 for metric locales and Letter elsewhere. If the default PaperSize does not exist, Unidrv uses the PaperSize option that is specified by the *<strong>DefaultOption</strong> keyword.</p></td>
</tr>
<tr class="even">
<td><p><strong>*FeatureType</strong></p></td>
<td><p>DOC_PROPERTY</p>
<p>JOB_PROPERTY</p>
<p>PRINTER_PROPERTY</p>
<p>If DOC_PROPERTY or JOB_PROPERTY, the feature is assigned to the document property sheet. If PRINTER_PROPERTY, the feature is assigned to the printer property sheet.</p></td>
<td><p>Required for customized features. Optional for standard features. If not specified, the default value for standard features is DOC_PROPERTY unless otherwise noted.</p>
<p>If PRINTER_PROPERTY, the feature's option value is saved in the registry. If DOC_PROPERTY or JOB_PROPERTY, the feature's option value is saved with the document.</p></td>
</tr>
<tr class="odd">
<td><p><strong>*HelpIndex</strong></p></td>
<td><p>Numeric value representing an index into the help file specified by the *<strong>HelpFile</strong> [root-level-only attribute](root-level-only-attributes.md).</p></td>
<td><p>(Also an [option attribute](option-attributes.md).)</p></td>
</tr>
<tr class="even">
<td><p><strong>*Installable?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the feature is installable. (<strong>FALSE</strong> means always installed.)</p>
<p>For more information, see [Handling Installable Features and Options](handling-installable-features-and-options.md).</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>. If <strong>TRUE</strong>, all the feature's options are also installable, except for the first one specified. If <strong>FALSE</strong>, at least one of the feature's options must also always be installed. (Also an [option attribute](option-attributes.md).)</p></td>
</tr>
<tr class="odd">
<td><p><strong>*InstallableFeatureName</strong></p></td>
<td><p>Text string that is displayed to ask the user whether an installable feature is actually installed.</p>
<p>For more information, see [Handling Installable Features and Options](handling-installable-features-and-options.md).</p></td>
<td><p>Required if *<strong>Installable?</strong> is <strong>TRUE</strong> and *<strong>rcInstallableFeatureNameID</strong> is not specified. (Also an [option attribute](option-attributes.md).)</p></td>
</tr>
<tr class="even">
<td><p><strong>*Name</strong></p></td>
<td><p>Text string used as the feature's display name on the printer's property sheet.</p></td>
<td><p>Optional. If not specified, then *<strong>rcNameID</strong> must be specified. (Also an [option attribute](option-attributes.md).)</p></td>
</tr>
<tr class="odd">
<td><p><strong>*Option</strong></p></td>
<td><p>Option parameters, as described in [Option Entry Format](option-entry-format.md).</p></td>
<td><p>Required. Use an <strong>*Option</strong> entry for each option associated with the feature.</p></td>
</tr>
<tr class="even">
<td><p><strong>*rcIconID</strong></p></td>
<td><p>Resource ID of an icon resource associated with the feature.</p></td>
<td><p>Optional. If not specified, Unidrv does not display an icon for the feature on the printer property sheet. (Also an [option attribute](option-attributes.md).)</p></td>
</tr>
<tr class="odd">
<td><p><strong>*rcInstallableFeatureNameID</strong></p></td>
<td><p>Resource ID of a text string that is displayed to ask the user whether an installable feature is actually installed.</p>
<p>For more information, see [Handling Installable Features and Options](handling-installable-features-and-options.md).</p></td>
<td><p>Required if *<strong>Installable?</strong> is <strong>TRUE</strong> and *<strong>InstallableFeatureName</strong> is not specified. (Also an [option attribute](option-attributes.md).)</p></td>
</tr>
<tr class="even">
<td><p><strong>*rcNameID</strong></p></td>
<td><p>Resource ID of string resource representing the feature name. (Zero is not a valid resource ID.)</p></td>
<td><p>Optional. If not specified, then *<strong>Name</strong> must be specified. (Also an [option attribute](option-attributes.md).)</p></td>
</tr>
<tr class="odd">
<td><p><strong>*UpdateQualityMacro?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the feature is included in a conditional statement that specifies quality settings (see [Controlling Image Quality](controlling-image-quality.md)).</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>. (The value is forced to <strong>TRUE</strong> if the feature is included in a conditional statement that specifies quality settings.)</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Feature%20Attributes%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


