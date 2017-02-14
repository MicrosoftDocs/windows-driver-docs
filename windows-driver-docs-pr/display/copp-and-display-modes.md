---
title: COPP and Display Modes
description: COPP and Display Modes
ms.assetid: e7da753d-0ccd-428e-b51f-3fd0a19674e8
keywords: ["copy protection WDK COPP , display modes", "video copy protection WDK COPP , display modes", "COPP WDK DirectX VA , display modes", "protected video WDK COPP , display modes", "display modes WDK COPP"]
---

# COPP and Display Modes


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

The video miniport driver should report all the protection types that are supported on the physical connector associated with the DirectX VA COPP device, regardless of the display mode currently being used. The video miniport driver reports supported protection types when it receives a call to its [*COPPQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff539652) function with the DXVA\_COPPQueryProtectionType set in the **guidStatusRequestID** member of the [**DXVA\_COPPStatusInput**](https://msdn.microsoft.com/library/windows/hardware/ff563899) structure. For more information, see [COPP Status](copp-status.md).

If the current resolution is too high for a particular protection type, then when the video miniport driver's [*COPPCommand*](https://msdn.microsoft.com/library/windows/hardware/ff539642) function is called to set the protection level for that protection type, the driver should return an error. The following scenarios give examples of when the driver's *COPPCommand* function should return success or an error:

-   If the DirectX VA COPP device is associated with an S-Video output connector, a call to the video miniport driver's [*COPPQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff539652) function with DXVA\_COPPQueryProtectionType set should indicate support of the analog content protection (ACP) type (COPP\_ProtectionType\_ACP). Thereafter, if the driver's [*COPPCommand*](https://msdn.microsoft.com/library/windows/hardware/ff539642) function is called to set a level for the ACP type on this connector, the driver should return success because the output resolution of S-Video is fixed, even though desktop resolution (display mode) might be higher.

-   If the DirectX VA COPP device is associated with component output connectors, a call to the video miniport driver's [*COPPQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff539652) function with DXVA\_COPPQueryProtectionType set should also indicate support of the ACP type. However, if the driver's [*COPPCommand*](https://msdn.microsoft.com/library/windows/hardware/ff539642) function is called to set a level for the ACP type on this output when the display resolution is 720p or 1080i, the driver should return the DDERR\_TOOBIGSIZE error code because the resolution is too high to set the protection level for the ACP type on component output connectors.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20COPP%20and%20Display%20Modes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




