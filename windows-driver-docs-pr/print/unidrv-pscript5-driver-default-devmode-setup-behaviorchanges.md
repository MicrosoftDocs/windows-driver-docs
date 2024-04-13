---
title: Unidrv/PScript5 Driver Default DEVMODE Setup Behavior Changes
description: Unidrv/PScript5 Driver Default DEVMODE Setup Behavior Changes
ms.date: 01/30/2023
---

# Unidrv/PScript5 Driver Default DEVMODE Setup Behavior Changes

[!include[Print Support Apps](../includes/print-support-apps.md)]

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
<td><p>(Unidrv only) Only set the DM_ORIENTATION flag in <strong>dmFields</strong> if the GPD file supports the "Orientation" GPD feature. <strong>dmOrientation</strong> is set based on the "Orientation" GPD feature's default option that is specified in the GPD file.</p>
<p>(PS only) Only set the DM_ORIENTATION flag in <strong>dmFields</strong> if the PPD file supports a feature with the "PageOrientation" Print Schema keyword.</p>
<p><strong>dmOrientation</strong> is set to <strong>DMORIENT_LANDSCAPE</strong> if that feature has the default option with the "Landscape" or "ReverseLandscape" Print Schema keyword. Otherwise, <strong>dmOrientation</strong> is set to <strong>DMORIENT_PORTRAIT</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>dmFields</strong>:</p>
<p>DM_SCALE</p></td>
<td><p>(Unidrv only) Hard-coded to never set the DM_SCALE flag in <strong>dmFields</strong>.</p>
<p>(PS only) Hard-coded to always set the DM_SCALE flag in <strong>dmFields</strong>.</p></td>
<td><p>Only set the DM_SCALE flag in <strong>dmFields</strong> if GPD or PPD supports a feature with the "PageScaling" Print Schema keyword.</p></td>
</tr>
<tr class="odd">
<td><p><strong>dmFields</strong>:</p>
<p>DM_TTOPTION</p>
<p><strong>dmTTOption</strong></p></td>
<td><p>Hard-coded to always set DM_TTOPTION flag in dmFields, and set dmTTOption = DMTT_SUBDEV.</p></td>
<td><p>If GPD or PPD supports a feature with the "PageDeviceFontSubstitution" Print Schema keyword and the feature has the default option with the "On" Print Schema keyword, set the DM_TTOPTION flag and set <strong>dmTTOption</strong> = <strong>DMTT_SUBDEV</strong>.</p>
<p>Otherwise, if GPD or PPD supports a feature with the "PageTrueTypeFontMode" Print Schema keyword and one of the following:</p>
<ul>
<li><p>If the feature has a default option with the "DownloadAsOutlineFont" Print Schema keyword, then set the DM_TTOPTION flag and set <strong>dmTTOption</strong> = <strong>DMTT_DOWNLOAD_OUTLINE</strong>.</p></li>
<li><p>If the feature has a default option with the "RenderAsBitmap" Print Schema keyword, then set the DM_TTOPTION flag and set <strong>dmTTOption</strong> = <strong>DMTT_BITMAP</strong>;</p></li>
<li><p>If the feature has a default option with "Automatic", "DownloadAsRasterFont", or "DownloadAsNativeTrueTypeFont" Print Schema keyword, then set the DM_TTOPTION flag and set <strong>dmTTOption</strong> = <strong>DMTT_DOWNLOAD</strong>.</p></li>
</ul>
<p>Otherwise, the DM_TTOPTION flag will be cleared in <strong>dmFields</strong> because the printer does not indicate that it supports TrueType font substitution or downloading.</p></td>
</tr>
<tr class="even">
<td><p><strong>dmFields</strong>:</p>
<p>DM_NUP</p></td>
<td><p>Hard-coded to always set the DM_NUP flag in <strong>dmFields</strong>.</p></td>
<td><p>Only set the DM_NUP flag in <strong>dmFields</strong> if GPD or PPD supports a feature with the "JobNUpAllDocumentsContiguously or "DocumentNUp" Print Schema keyword.</p></td>
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
<td><p>Only set the DM_PRINTQUALITY and DM_YRESOLUTION flags in <strong>dmFields</strong> if GPD or PPD supports the "Resolution" GPD or PPD feature.</p></td>
</tr>
<tr class="odd">
<td><p><strong>dmFields</strong>:</p>
<p>DM_COLLATE</p>
<p><strong>dmCollate</strong></p></td>
<td><p>Hard-coded to always set the DM_COLLATE flag in <strong>dmFields</strong>, and set <strong>dmCollate</strong> = DMCOLLATE_TRUE.</p></td>
<td><p>Only set the DM_COLLATE flag in <strong>dmFields</strong> if GPD or PPD supports the "Collate" GPD or PPD feature. <strong>dmCollate</strong> is set based on the "Collate" GPD or PPD feature's default option that is specified in GPD or PPD.</p></td>
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
