---
title: Unidrv/PScript5 Driver Default DEVMODE Setup Behavior Changes
description: Unidrv/PScript5 Driver Default DEVMODE Setup Behavior Changes
ms.date: 06/07/2024
ms.topic: concept-article
---

# Unidrv/PScript5 Driver Default DEVMODE Setup Behavior Changes

[!include[Print Support Apps](../includes/print-support-apps.md)]

A Unidrv/PScript5 driver that is running in XPSDrv mode creates the following driver default DEVMODE setup behavior changes.

In the following table, "PS only" means the behavior change is specific to a PScript5 driver. "Unidrv only" means the behavior change is specific to Unidrv driver. If both of these phrases don't appear, the behavior change applies to both Unidrv and PScript5 drivers.

| Affected default DEVMODE fields | Non-XPSDrv behavior | XPSDrv behavior |
|--|--|--|
| **dmFields:**<br><br>DM_ORIENTATION<br><br>dmOrientation | Hard-coded to always set the DM_ORIENTATION flag in **dmFields**, and set **dmOrientation** = DMORIENT_PORTRAIT. | (Unidrv only) Only set the DM_ORIENTATION flag in **dmFields** if the GPD file supports the "Orientation" GPD feature. **dmOrientation** is set based on the "Orientation" GPD feature's default option that is specified in the GPD file.<br><br>(PS only) Only set the DM_ORIENTATION flag in **dmFields** if the PPD file supports a feature with the "PageOrientation" Print Schema keyword.<br><br>**dmOrientation** is set to **DMORIENT_LANDSCAPE** if that feature has the default option with the "Landscape" or "ReverseLandscape" Print Schema keyword. Otherwise, **dmOrientation** is set to **DMORIENT_PORTRAIT**. |
| **dmFields:**<br><br>DM_SCALE | (Unidrv only) Hard-coded to never set the DM_SCALE flag in dmFields.<br><br>(PS only) Hard-coded to always set the DM_SCALE flag in dmFields. | Only set the DM_SCALE flag in **dmFields** if GPD or PPD supports a feature with the "PageScaling" Print Schema keyword. |
| **dmFields:**<br><br>DM_TTOPTION<br><br>**dmTTOption** | Hard-coded to always set DM_TTOPTION flag in dmFields, and set **dmTTOption** = **DMTT_SUBDEV**. | If GPD or PPD supports a feature with the "PageDeviceFontSubstitution" Print Schema keyword and the feature has the default option with the "On" Print Schema keyword, set the DM_TTOPTION flag and set **dmTTOption** = **DMTT_SUBDEV**.<br><br>Otherwise, if GPD or PPD supports a feature with the "PageTrueTypeFontMode" Print Schema keyword and one of the following:<br><br>If the feature has a default option with the "DownloadAsOutlineFont" Print Schema keyword, then set the DM_TTOPTION flag and set **dmTTOption** = **DMTT_DOWNLOAD_OUTLINE**.<br><br>If the feature has a default option with the "RenderAsBitmap" Print Schema keyword, then set the DM_TTOPTION flag and set **dmTTOption** = **DMTT_BITMAP**.<br><br>If the feature has a default option with "Automatic", "DownloadAsRasterFont", or "DownloadAsNativeTrueTypeFont" Print Schema keyword, then set the DM_TTOPTION flag and set **dmTTOption** = **DMTT_DOWNLOAD**.<br><br>Otherwise, the DM_TTOPTION flag is cleared in dmFields because the printer doesn't indicate that it supports TrueType font substitution or downloading. |
| **dmFields:**<br><br>DM_NUP | Hard-coded to always set the DM_NUP flag in **dmFields**. | Only set the DM_NUP flag in **dmFields** if GPD or PPD supports a feature with the "JobNUpAllDocumentsContiguously or "DocumentNUp" Print Schema keyword. |
| **dmFields:**<br><br>DM_COLOR | Hard-coded to always set the DM_COLOR flag in **dmFields**. | Only set the DM_COLOR flag in **dmFields** if GPD or PPD specifies that the printer is a color printer. |
| **dmFields:**<br><br>DM_PRINTQUALITY, DM_YRESOLUTION | (Unidrv only) Hard-coded to always set the DM_PRINTQUALITY flag in dm****Fields.<br><br>(PS only) Hard-coded to always set the DM_PRINTQUALITY and DM_YRESOLUTION flags in **dmFields**. |  |
| **dmFields:**<br><br>DM_COLLATE | Hard-coded to always set the DM_COLLATE flag in **dmFields**, and set **dmCollate** = DMCOLLATE_TRUE. | Only set the DM_COLLATE flag in dmFields if GPD or PPD supports the "Collate" GPD or PPD feature. **dmCollate** is set based on the "Collate" GPD or PPD feature's default option that is specified in GPD or PPD. |
| **dmFields:**<br><br>DM_ICMMETHOD, DM_ICMINTENT | (Unidrv only) Hard-coded to always set the DM_ICMMETHOD and DM_ICMINTENT flags in **dmFields**.<br><br>(PS only) If PPD specifies that the printer is a color printer, set the DM_ICMMETHOD and DM_ICMINTENT flags in **dmFields**. | Never set the DM_ICMMETHOD or DM_ICMINTENT flags in **dmFields**. |
| **dmFields:**<br><br>DM_DITHERTYPE | (Unidrv only) Hard-coded to always set the DM_DITHERTYPE flag in **dmFields**. | (Unidrv only) Never set the DM_DITHERTYPE flag in **dmFields**. |
