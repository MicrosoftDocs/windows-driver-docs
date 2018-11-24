---
title: Enabling Debug Output for the Video Memory Manager
description: Enabling Debug Output for the Video Memory Manager
ms.assetid: c17648dc-56c2-4751-80e6-262b222ccfb7
keywords:
- debug output enabled WDK display
- video memory manager debug output WDK display
- messages WDK display
- errors WDK display
- warnings WDK display
- low-resource messages WDK display
- trace messages WDK display
- events WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling Debug Output for the Video Memory Manager


The video memory manager has an extensive logging mechanism to help catch and debug issues in a driver during its development. To enable debugger output for the video memory manager, driver writers must first modify the debug filter in the kernel debugger. The video memory manager currently uses the same filter as the video port driver. Therefore, driver writers should submit the following command in the kernel debugger so that debug messages received from the video memory manager can be displayed in the kernel debugger:

```cmd
ed nt!Kd_VIDEOPRT_Mask ff
```

 

 





