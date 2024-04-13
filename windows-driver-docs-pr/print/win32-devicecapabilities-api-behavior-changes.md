---
title: Win32 DeviceCapabilities API Behavior Changes
description: Win32 DeviceCapabilities API Behavior Changes
ms.date: 01/31/2023
---

# Win32 DeviceCapabilities API Behavior Changes

[!include[Print Support Apps](../includes/print-support-apps.md)]

A Unidrv/PScript5 driver that is running in XPSDrv mode creates the following changes in the Microsoft Win32 **DeviceCapabilities** function.

When a GPD/PPD feature or option is mapped to a Print Schema keyword by using GPD's **PrintSchemaKeywordMap** or PPD's **MSPrintSchemaKeywordMap** keywords, GPD or PPD supports that print schema keyword.

(In the following table, "PS only" means the behavior change is specific to a PScript5 driver. "Unidrv only" means the behavior change is specific to Unidrv driver. If both of these phrases don't appear, the behavior change applies to both Unidrv and PScript5 drivers.)

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Capability</th>
<th>Non-XPSDrv behavior</th>
<th>XPSDrv behavior</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DC_COPIES</p></td>
<td><p>(Unidrv only) When EMF is enabled, <strong>DeviceCapabilitiesreturns</strong> a hard-coded value that is the maximum value of 9999 or the GPD file's specified *MaxCopies value.</p>
<p>When EMF is disabled, <strong>DeviceCapabilities</strong> returns the GPD*MaxCopies value.</p>
<p>(PS only) <strong>DeviceCapabilities</strong> returns a hard-coded value of 9999.</p></td>
<td><p>(Unidrv only) <strong>DeviceCapabilities</strong> returns the GPD *MaxCopies value.</p>
<p>(PS only) <strong>DeviceCapabilities</strong> returns the PPD file's*MSXPSMaxCopies value or 1 if the value isn't specified in the PPD file.</p></td>
</tr>
<tr class="even">
<td><p>DC_TRUETYPE</p></td>
<td><p>For Unidrv, if the *FontFormat GPD keyword is specified, <strong>DeviceCapabilities</strong> returns (DCTT_BITMAP | DCTT_DOWNLOAD); otherwise, <strong>DeviceCapabilities</strong> returns DCTT_BITMAP.</p>
<p>For PS, <strong>DeviceCapabilities</strong> always returns (DCTT_DOWNLOAD | DCTT_SUBDEV).</p></td>
<td><p>If GPD or PPD supports a feature with the "PageDeviceFontSubstitution" Print Schema keyword, the DCTT_SUBDEV flag will be set in the return value.</p>
<p>If GPD or PPD supports a feature with the "PageTrueTypeFontMode" Print Schema keyword, the following occur:</p>
<ul>
<li><p>If the feature supports an option with the "DownloadAsOutlineFont" Print Schema keyword, both the DCTT_DOWNLOAD and DCTT_DOWNLOAD_OUTLINE flags will be set in the return value.</p></li>
<li><p>If the feature supports an option with the "Automatic", "DownloadAsRasterFont", or "DownloadAsNativeTrueTypeFont" Print Schema keyword, the DCTT_DOWNLOAD flag will be set in the return value.</p></li>
<li><p>If the feature supports an option with the "RenderAsBitmap" Print Schema keyword, the DCTT_BITMAP flag will be set in the return value.</p></li>
</ul>
<p>If none of the DCTT_<em>Xxx</em> flags are set, <strong>DeviceCapabilities</strong> returns 0.</p></td>
</tr>
<tr class="odd">
<td><p>DC_ORIENTATION</p></td>
<td><p>(PS only) <strong>DeviceCapabilities</strong> returns 90 or 270 based on PPD's*LandscapeOrientation value and setting for the hard-coded Rotated Landscape orientation option in the input DEVMODE structure.</p></td>
<td><p>(PS only) The default return value is 0, which means that there's no landscape orientation.</p>
<p>If PPD supports a feature with the "PageOrientation" Print Schema keyword, the following occur:</p>
<ul>
<li><p>If the feature supports an option with the "Landscape" Print Schema keyword, <strong>DeviceCapabilities</strong> returns 90.</p></li>
<li><p>If the feature supports an option with the "ReverseLandscape" Print Schema keyword, <strong>DeviceCapabilities</strong> returns 270.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>DC_COLLATE</p></td>
<td><p>When EMF is enabled, <strong>DeviceCapabilities</strong> is hardcoded to return 1 (which means that collating is supported).</p>
<p>When EMF is disabled, <strong>DeviceCapabilities</strong> returns 1 if GPD or PPD specifies Collate as a supported feature and if the Collate GPD or PPD feature isn't constrained by any device setting features. Otherwise, <strong>DeviceCapabilities</strong> returns 0.</p></td>
<td><p>The behavior is the same as for non-XPSDrv drivers with EMF disabled.</p></td>
</tr>
<tr class="odd">
<td><p>DC_NUP</p></td>
<td><p><strong>DeviceCapabilities</strong> returns a hard-coded value to indicate support for 1, 2, 4, 6, 9, or 16 ups.</p></td>
<td><p>If GPD or PPD defines a feature with the "DocumentNUp" Print Schema keyword (the "DocumentNUp" feature is only used if no "JobNUpAllDocumentsContiguously" feature exists), then for any options of that feature that have the option GPD/PPD keyword name as a numeric number (that is, 1, 2, 6, and so on), the numeric number will be reported as one of the supported pages per sheet value.</p>
<p>Otherwise, XPSDrv will report that NUp isn't supported.</p></td>
</tr>
<tr class="even">
<td><p>DC_PERSONALITY</p></td>
<td><p>Unidrv returns the string that is defined by *Personality or*rcPersonalityID GPD keyword.</p>
<p>PS always returns "PostScript".</p></td>
<td><p>Keep the behavior the same as it is for non-XPSDrv drivers.</p></td>
</tr>
<tr class="odd">
<td><p>DC_MEDIAREADY</p></td>
<td><p>If the Form-Tray assignment table is ever created, <strong>DeviceCapabilities</strong> returns the unique form names that are listed in the table that has an assigned tray.</p>
<p>If Form-Tray assignment table hasn't been created, <strong>DeviceCapabilities</strong> returns "Letter" for non-metric system default locale, "A4" for metric system default locale, or a GPD or PPD defined default paper size if the printer doesn't support "Letter" and "A4".</p></td>
<td><p>The behavior is the same as with non-XPSDrv with no form-tray assignment table created.</p></td>
</tr>
<tr class="even">
<td><p>DC_STAPLE</p></td>
<td><p>(PS only) PPD does o't have a single "Stapling" feature. A PScript5 driver checks if any of following PPD features are defined in PPD and aren't constrained by device settings to determine if the device can support stapling.</p>
<ul>
<li><p>"StapleLocation"</p></li>
<li><p>"StapleX", "StapleY"</p></li>
<li><p>"StapleWhen"</p></li>
<li><p>"StapleOrientation"</p></li>
</ul></td>
<td><p>(PS only) If PPD supports a feature with the "JobStapleAllDocuments" or "DocumentStaple" Print Schema keyword, <strong>DeviceCapabilities</strong> returns 1 to indicate supporting stapling. Otherwise, <strong>DeviceCapabilities</strong> returns 0.</p></td>
</tr>
</tbody>
</table>
