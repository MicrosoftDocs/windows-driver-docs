---
title: Multiple Session Copy Protection
description: Multiple Session Copy Protection
ms.assetid: f6ac9854-3326-48da-9153-1eec596a157b
keywords:
- copy protection WDK video miniport , multiple session
- multiple session copy protection WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multiple Session Copy Protection


## <span id="ddk_multiple_session_copy_protection_gg"></span><span id="DDK_MULTIPLE_SESSION_COPY_PROTECTION_GG"></span>


The miniport driver of a device that has copy protection can optionally support multiple simultaneous copy protection sessions. To do so, the miniport driver should do the following:

-   Return a unique copy protection key in **dwCPKey** for each copy protection activation.

-   Keep copy protection enabled until all sessions have been temporarily turned off (through VP\_CP\_CMD\_CHANGE) or deactivated (VP\_CP\_CMD\_DEACTIVATE). For example, the miniport driver could increment or decrement a reference count every time copy protection is activated (VP\_CP\_CMD\_ACTIVATE) or deactivated/turned off, disabling copy protection entirely only when the reference count is zero.

 

 





