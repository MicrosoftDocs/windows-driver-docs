---
title: Handling Protection Levels
description: Handling Protection Levels
keywords:
- copy protection WDK COPP , protection levels
- video copy protection WDK COPP , protection levels
- COPP WDK DirectX VA , protection levels
- protected video WDK COPP , protection levels
ms.date: 04/20/2017
---

# Handling Protection Levels


## <span id="ddk_handling_protection_levels_gg"></span><span id="DDK_HANDLING_PROTECTION_LEVELS_GG"></span>


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

For each output connector of the graphics adapter that supports protection, the video miniport driver should maintain a global reference count for each protection type and for each protection level. Note that the default global reference counters are initialized to 0.

When the DirectX VA COPP device is created for a video session, the COPP device should contain a local reference count for each protection type at each protection level. The driver should set the default protection-level counter for each protection type to the value 1 and the remaining protection-level counters for each protection type to the value 0.

When a video session sets a new protection level for a particular protection type, the driver should decrement the reference count for the current protection level and should increment the reference count for the new protection level. Corresponding changes should also be made to the global reference-level counters.

Whenever any global-level counters change, the driver should inspect all the counters for a particular output connector and ensure that the protection level is set to a level that corresponds to the highest level counter whose value is greater than 0. For more information, see the example code in the [*COPPCommand*](./coppcommand.md) and [*COPPQueryStatus*](./coppquerystatus.md) reference pages.

While the global reference counter is greater than 0, the video miniport driver should apply content protection to the output connector. As soon as the global reference counter reaches 0, the video miniport driver should remove content protection from the output connector. Whenever the display driver receives a call to its [*DdMoCompDestroy*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_destroy) callback function (and, in turn, the video miniport driver receives a call to its [*COPPCloseVideoSession*](./coppclosevideosession.md) function), the video miniport driver should decrement the global reference counter by the current level of the COPP device's local reference counter. The video miniport driver should only remove content protection from the certified output connector if the global reference counter for the connector reaches 0.

**Note**   The *DdMoCompDestroy* function might be called while the COPP device's local reference counter is still set to greater than 0 (for example, if the user-mode process terminated abnormally).

 

 

