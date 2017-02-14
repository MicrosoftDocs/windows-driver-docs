---
title: Enabling Debug Output for the Video Memory Manager
description: Enabling Debug Output for the Video Memory Manager
ms.assetid: c17648dc-56c2-4751-80e6-262b222ccfb7
keywords: ["debug output enabled WDK display", "video memory manager debug output WDK display", "messages WDK display", "errors WDK display", "warnings WDK display", "low-resource messages WDK display", "trace messages WDK display", "events WDK display"]
---

# Enabling Debug Output for the Video Memory Manager


The video memory manager has an extensive logging mechanism to help catch and debug issues in a driver during its development. To enable debugger output for the video memory manager, driver writers must first modify the debug filter in the kernel debugger. The video memory manager currently uses the same filter as the video port driver. Therefore, driver writers should submit the following command in the kernel debugger so that debug messages received from the video memory manager can be displayed in the kernel debugger:

```
ed nt!Kd_VIDEOPRT_Mask ff
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Enabling%20Debug%20Output%20for%20the%20Video%20Memory%20Manager%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




