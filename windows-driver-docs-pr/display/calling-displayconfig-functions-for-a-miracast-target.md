---
title: Calling DisplayConfig functions for a Miracast target
ms.assetid: D408986B-B33B-4A96-B93C-2A2F301E74AF
description: 
---

# Calling DisplayConfig functions for a Miracast target


To reduce compatibility issues of existing apps being exposed to new Miracast targets, the [**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215) and [**SetDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569533) function implementations have ways for apps to find Miracast targets:

-   A value of **DISPLAYCONFIG\_OUTPUT\_TECHNOLOGY\_MIRACAST** in the [**DISPLAYCONFIG\_VIDEO\_OUTPUT\_TECHNOLOGY**](https://msdn.microsoft.com/library/windows/hardware/ff554003) enumeration indicates that the VidPN target is a Miracast device.
-   The Flags parameter value of **QDC\_ALL\_PATHS** in a call to [**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215) wonâ€™t return any paths that connect to a Miracast target that does not have an active monitor attached.
-   For each path that has a connected Miracast monitor, [**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215) returns the connector type thatâ€™s reported by the Miracast sink. Internal Miracast sinks report a value of **DISPLAYCONFIG\_OUTPUT\_TECHNOLOGY\_MIRACAST** in the [**DISPLAYCONFIG\_VIDEO\_OUTPUT\_TECHNOLOGY**](https://msdn.microsoft.com/library/windows/hardware/ff554003) enumeration. For example, if a Miracast sink reports that a TV is connected to the sink with a High-Definition Multimedia Interface (HDMI) cable, then **QueryDisplayConfig** would report the target type as **DISPLAYCONFIG\_OUTPUT\_TECHNOLOGY\_HDMI**.
-   The [**DISPLAYCONFIG\_VIDEO\_SIGNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff554007) structure has a VSync frequency divider member, **vSyncFreqDivider**, thatâ€™s used similarly to [**D3DKMDT\_VIDEO\_SIGNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff546625).**vSyncFreqDivider**.
-   The [**DisplayConfigGetDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553903) function provides the base connector type for any target. In the case of a Miracast target, this function always returns a value of **DISPLAYCONFIG\_OUTPUT\_TECHNOLOGY\_MIRACAST** in the [**DISPLAYCONFIG\_VIDEO\_OUTPUT\_TECHNOLOGY**](https://msdn.microsoft.com/library/windows/hardware/ff554003) enumeration.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Calling%20DisplayConfig%20functions%20for%20a%20Miracast%20target%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




