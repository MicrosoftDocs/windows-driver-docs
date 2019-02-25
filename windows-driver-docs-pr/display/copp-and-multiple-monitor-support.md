---
title: COPP and Multiple-Monitor Support
description: COPP and Multiple-Monitor Support
ms.assetid: 96bd24f6-4aba-4605-8fd4-465c86061044
keywords:
- copy protection WDK COPP , multiple monitors
- video copy protection WDK COPP , multiple monitors
- COPP WDK DirectX VA , multiple monitors
- protected video WDK COPP , multiple monitors
- multiple monitors WDK COPP
- monitors WDK COPP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# COPP and Multiple-Monitor Support


## <span id="ddk_copp_and_multiple_monitor_support_gg"></span><span id="DDK_COPP_AND_MULTIPLE_MONITOR_SUPPORT_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

The only multiple-monitor mode supported by COPP is DualView. Various clone and theater modes are not supported. The only exception to this rule is the case where a graphics adapter uses both composite and S-Video connectors and simultaneously feeds the same display signal through both connectors. In this case, the video miniport driver should report that the connector is S-Video and should ensure that the appropriate protections are applied to both display outputs when requested by COPP calls initiated through applications.

 

 





