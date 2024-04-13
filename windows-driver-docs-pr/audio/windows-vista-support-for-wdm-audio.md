---
title: Windows Vista Support for WDM Audio
description: Windows Vista Support for WDM Audio
ms.date: 04/20/2017
---

# Windows Vista Support for WDM Audio


## <span id="windows_xp_support_for_wdm_audio"></span><span id="WINDOWS_XP_SUPPORT_FOR_WDM_AUDIO"></span>


Windows Vista supports the following WDM audio capabilities:

-   WDM version 1.40

-   All the features that Windows XP supports, with the following exceptions.
    -   Hardware peak meters are supported, except when the Windows Vista mixer API runs in per-application mode.
    -   Wave and MIDI NT4 drivers function normally, but they are not supported by the new audio user interface.
    -   AUX devices are not supported, and the [**auxGetNumDevs**](/previous-versions/dd756713(v=vs.85)) function in Mmsystem.h will always return a count of zero.
    -   Windows NT4-style mixer drivers (DRIVERS32) are not supported.

 

