---
title: Pure Devices
description: Pure Devices
ms.assetid: 6ad3412c-fd80-41c0-9abc-117aacc5ddae
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , pure devices
- pure devices WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pure Devices


## <span id="ddk_pure_devices_gg"></span><span id="DDK_PURE_DEVICES_GG"></span>


DirectX 8.0 introduces the concept of a "pure" device. When using a pure device the runtime does not track state or state blocks or perform any software vertex processing on behalf of the hardware. Furthermore, the application cannot query back state from the runtime. The lack of state tracking, particularly when state blocks are being used, can result in a significant performance boost for the application.

Only vertex processing directly supported by the hardware is available to the application when using a pure device. For example, for cards that do not support hardware transform and lighting, only pretransformed vertices can be passed to Direct3D. Furthermore, the API functions **SetClipStatus**, **GetClipStatus** and **ProcessVertices** cannot be used with the pure device.

In order to use a pure device the application must request it with the device creation flag D3DCREATE\_PUREDEVICE and the driver must report its ability to act as a pure device.

 

 





