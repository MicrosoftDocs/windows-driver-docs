---
title: Reporting Multisample Support
description: Reporting Multisample Support
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multisample rendering, reporting
- multisample rendering WDK DirectX 8.0 , reporting
- rendering multisamples WDK DirectX 8.0 , reporting
ms.date: 04/20/2017
---

# Reporting Multisample Support


## <span id="ddk_reporting_multisample_support_gg"></span><span id="DDK_REPORTING_MULTISAMPLE_SUPPORT_GG"></span>


A driver reports the multisample capabilities of its associated hardware by specifying the number of samples per pixel for each surface format it reports. The [**DDPIXELFORMAT**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ddpixelformat) structure has been extended to include a structure called **MultiSampleCaps**. This structure has members that let the driver express the number of samples per pixel for both flip (fullscreen) and blt (windowed) multisampling. Each of these members is a WORD type in which each bit of the WORD value indicates support for a given number of samples per pixel. Hence, the driver can express support for several different sample counts with a single surface format entry.

 

