---
title: Unidrv/PScript5 Driver Default DEVMODE Setup Behavior Changes
author: windows-driver-content
description: Unidrv/PScript5 Driver Default DEVMODE Setup Behavior Changes
ms.assetid: 9760d527-0205-477b-bc16-d6aa65b1eaf7
---

# Unidrv/PScript5 Driver Default DEVMODE Setup Behavior Changes


A Unidrv/PScript5 driver that is running in XPSDrv mode creates the following driver default DEVMODE setup behavior changes.

(In the following table, "PS only" means the behavior change is specific to a PScript5 driver. "Unidrv only" means the behavior change is specific to Unidrv driver. If both of these phrases do not appear, the behavior change applies to both Unidrv and PScript5 drivers.)

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Affected default DEVMODE fields</th>
<th>Non-XPSDrv behavior</th>
<th>XPSDrv behavior</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>dmFields</strong>:</p>
<p>DM_ORIENTATION</p>
<p><strong>dmOrientation</strong></p></td>
<td><p>Hard-coded to always set the DM_ORIENTATION flag in <strong>dmFields</strong>, and set <strong>dmOrientation</strong> = DMORIENT_PORTRAIT.</p></td>
<td><p>(Unidrv only) Only set the DM_ORIENTATION flag in <strong>dmFields</strong> if the GPD file supports the &quot;Orientation&quot; GPD feature. <strong>dmOrientation</strong> is set based on the &quot;Orientation&quot; GPD feature's default option that is specified in the GPD file.</p>
<p>(PS only) Only set the DM_ORIENTATION flag in <strong>dmFields</strong> if the PPD file supports a feature with the &quot;PageOrientation&quot; Print Schema keyword.</p>
<p><strong>dmOrientation</strong> is set to <strong>DMORIENT_LANDSCAPE</strong> if that feature has the default option with the &quot;Landscape&quot; or &quot;ReverseLandscape&quot; Print Schema keyword. Otherwise, <strong>dmOrientation</strong> is set to <strong>DMORIENT_PORTRAIT</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>dmFields</strong>:</p>
<p>DM_SCALE</p></td>
<td><p>(Unidrv only) Hard-coded to never set the DM_SCALE flag in <strong>dmFields</strong>.</p>
<p>(PS only) Hard-coded to always set the DM_SCALE flag in <strong>dmFields</strong>.</p></td>
<td><p>Only set the DM_SCALE flag in <strong>dmFields</strong> if GPD or PPD supports a feature with the &quot;PageScaling&quot; Print Schema keyword.</p></td>
</tr>
<tr class="odd">
<td><p><strong>dmFields</strong>:</p>
<p>DM_TTOPTION</p>
<p><strong>dmTTOption</strong></p></td>
<td><p>Hard-coded to always set DM_TTOPTION flag in dmFields, and set dmTTOption = DMTT_SUBDEV.</p></td>
<td><p>If GPD or PPD supports a feature with the &quot;PageDeviceFontSubstitution&quot; Print Schema keyword and the feature has the default option with the &quot;On&quot; Print Schema keyword, set the DM_TTOPTION flag and set <strong>dmTTOption</strong> = <strong>DMTT_SUBDEV</strong>.</p>
<p>Otherwise, if GPD or PPD supports a feature with the &quot;PageTrueTypeFontMode&quot; Print Schema keyword and one of the following:</p>
<ul>
<li><p>If the feature has a default option with the &quot;DownloadAsOutlineFont&quot; Print Schema keyword, then set the DM_TTOPTION flag and set <strong>dmTTOption</strong> = <strong>DMTT_DOWNLOAD_OUTLINE</strong>.</p></li>
<li><p>If the feature has a default option with the &quot;RenderAsBitmap&quot; Print Schema keyword, then set the DM_TTOPTION flag and set <strong>dmTTOption</strong> = <strong>DMTT_BITMAP</strong>;</p></li>
<li><p>If the feature has a default option with &quot;Automatic&quot;, &quot;DownloadAsRasterFont&quot;, or &quot;DownloadAsNativeTrueTypeFont&quot; Print Schema keyword, then set the DM_TTOPTION flag and set <strong>dmTTOption</strong> = <strong>DMTT_DOWNLOAD</strong>.</p></li>
</ul>
<p>Otherwise, the DM_TTOPTION flag will be cleared in <strong>dmFields</strong> because the printer does not indicate that it supports TrueType font substitution or downloading.</p></td>
</tr>
<tr class="even">
<td><p><strong>dmFields</strong>:</p>
<p>DM_NUP</p></td>
<td><p>Hard-coded to always set the DM_NUP flag in <strong>dmFields</strong>.</p></td>
<td><p>Only set the DM_NUP flag in <strong>dmFields</strong> if GPD or PPD supports a feature with the &quot;JobNUpAllDocumentsContiguously or &quot;DocumentNUp&quot; Print Schema keyword.</p></td>
</tr>
<tr class="odd">
<td><p><strong>dmFields</strong>:</p>
<p>DM_COLOR</p></td>
<td><p>Hard-coded to always set the DM_COLOR flag in <strong>dmFields</strong>.</p></td>
<td><p>Only set the DM_COLOR flag in <strong>dmFields</strong> if GPD or PPD specifies that the printer is a color printer.</p></td>
</tr>
<tr class="even">
<td><p><strong>dmFields</strong>:</p>
<p>DM_PRINTQUALITY, DM_YRESOLUTION</p></td>
<td><p>(Unidrv only) Hard-coded to always set the DM_PRINTQUALITY flag in <strong>dmFields</strong>.</p>
<p>(PS only) Hard-coded to always set the DM_PRINTQUALITY and DM_YRESOLUTION flags in <strong>dmFields</strong>.</p></td>
<td><p>Only set the DM_PRINTQUALITY and DM_YRESOLUTION flags in <strong>dmFields</strong> if GPD or PPD supports the &quot;Resolution&quot; GPD or PPD feature.</p></td>
</tr>
<tr class="odd">
<td><p><strong>dmFields</strong>:</p>
<p>DM_COLLATE</p>
<p><strong>dmCollate</strong></p></td>
<td><p>Hard-coded to always set the DM_COLLATE flag in <strong>dmFields</strong>, and set <strong>dmCollate</strong> = DMCOLLATE_TRUE.</p></td>
<td><p>Only set the DM_COLLATE flag in <strong>dmFields</strong> if GPD or PPD supports the &quot;Collate&quot; GPD or PPD feature. <strong>dmCollate</strong> is set based on the &quot;Collate&quot; GPD or PPD feature's default option that is specified in GPD or PPD.</p></td>
</tr>
<tr class="even">
<td><p><strong>dmFields</strong>:</p>
<p>DM_ICMMETHOD, DM_ICMINTENT</p></td>
<td><p>(Unidrv only) Hard-coded to always set the DM_ICMMETHOD and DM_ICMINTENT flags in <strong>dmFields</strong>.</p>
<p>(PS only) If PPD specifies that the printer is a color printer, set the DM_ICMMETHOD and DM_ICMINTENT flags in <strong>dmFields</strong>.</p></td>
<td><p>Never set the DM_ICMMETHOD or DM_ICMINTENT flags in <strong>dmFields</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>dmFields</strong>:</p>
<p>DM_DITHERTYPE</p></td>
<td><p>(Unidrv only) Hard-coded to always set the DM_DITHERTYPE flag in <strong>dmFields</strong>.</p></td>
<td><p>(Unidrv only) Never set the DM_DITHERTYPE flag in <strong>dmFields</strong>.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Unidrv/PScript5%20Driver%20Default%20DEVMODE%20Setup%20Behavior%20Changes%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


