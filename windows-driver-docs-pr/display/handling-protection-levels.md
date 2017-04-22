---
title: Handling Protection Levels
description: Handling Protection Levels
ms.assetid: d8237a48-9e1c-4b9e-8f55-70820ff08460
keywords:
- copy protection WDK COPP , protection levels
- video copy protection WDK COPP , protection levels
- COPP WDK DirectX VA , protection levels
- protected video WDK COPP , protection levels
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Protection Levels


## <span id="ddk_handling_protection_levels_gg"></span><span id="DDK_HANDLING_PROTECTION_LEVELS_GG"></span>


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

For each output connector of the graphics adapter that supports protection, the video miniport driver should maintain a global reference count for each protection type and for each protection level. Note that the default global reference counters are initialized to 0.

When the DirectX VA COPP device is created for a video session, the COPP device should contain a local reference count for each protection type at each protection level. The driver should set the default protection-level counter for each protection type to the value 1 and the remaining protection-level counters for each protection type to the value 0.

When a video session sets a new protection level for a particular protection type, the driver should decrement the reference count for the current protection level and should increment the reference count for the new protection level. Corresponding changes should also be made to the global reference-level counters.

Whenever any global-level counters change, the driver should inspect all the counters for a particular output connector and ensure that the protection level is set to a level that corresponds to the highest level counter whose value is greater than 0. For more information, see the example code in the [*COPPCommand*](https://msdn.microsoft.com/library/windows/hardware/ff539642) and [*COPPQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff539652) reference pages.

While the global reference counter is greater than 0, the video miniport driver should apply content protection to the output connector. As soon as the global reference counter reaches 0, the video miniport driver should remove content protection from the output connector. Whenever the display driver receives a call to its [*DdMoCompDestroy*](https://msdn.microsoft.com/library/windows/hardware/ff549664) callback function (and, in turn, the video miniport driver receives a call to its [*COPPCloseVideoSession*](https://msdn.microsoft.com/library/windows/hardware/ff539638) function), the video miniport driver should decrement the global reference counter by the current level of the COPP device's local reference counter. The video miniport driver should only remove content protection from the certified output connector if the global reference counter for the connector reaches 0.

**Note**   The *DdMoCompDestroy* function might be called while the COPP device's local reference counter is still set to greater than 0 (for example, if the user-mode process terminated abnormally).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Handling%20Protection%20Levels%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




