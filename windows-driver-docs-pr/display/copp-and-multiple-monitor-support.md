---
title: COPP and Multiple-Monitor Support
description: COPP and Multiple-Monitor Support
ms.assetid: 96bd24f6-4aba-4605-8fd4-465c86061044
keywords: ["copy protection WDK COPP , multiple monitors", "video copy protection WDK COPP , multiple monitors", "COPP WDK DirectX VA , multiple monitors", "protected video WDK COPP , multiple monitors", "multiple monitors WDK COPP", "monitors WDK COPP"]
---

# COPP and Multiple-Monitor Support


## <span id="ddk_copp_and_multiple_monitor_support_gg"></span><span id="DDK_COPP_AND_MULTIPLE_MONITOR_SUPPORT_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

The only multiple-monitor mode supported by COPP is DualView. Various clone and theater modes are not supported. The only exception to this rule is the case where a graphics adapter uses both composite and S-Video connectors and simultaneously feeds the same display signal through both connectors. In this case, the video miniport driver should report that the connector is S-Video and should ensure that the appropriate protections are applied to both display outputs when requested by COPP calls initiated through applications.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20COPP%20and%20Multiple-Monitor%20Support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




