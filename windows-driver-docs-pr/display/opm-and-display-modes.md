---
title: OPM and Display Modes
description: OPM and Display Modes
ms.assetid: d412a32b-7afd-4f48-9b8e-7cf66533349f
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OPM and Display Modes


The display miniport driver should report all the protection types that are supported on the physical connector that is associated with the protected output, regardless of the display mode that is currently being used. The display miniport driver reports supported protection types when it receives a call to its [**DxgkDdiOPMGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559725) or [**DxgkDdiOPMGetCOPPCompatibleInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559720) function with DXGKMDT\_OPM\_GET\_SUPPORTED\_PROTECTION\_TYPES set in the **guidInformation** member of the [**DXGKMDT\_OPM\_GET\_INFO\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff560868) structure. For more information about retrieving supported protection types, see [Retrieving Information About a Protected Output](retrieving-information-about-a-protected-output.md) or [Retrieving COPP-Compatible Information about a Protected Output](retrieving-copp-compatible-information-about-a-protected-output.md).

If the current resolution is too high for a particular protection type, the driver should return an error when the display miniport driver's [**DxgkDdiOPMConfigureProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559701) function is called to set the protection level for that protection type. The following scenarios give examples of when the driver's *DxgkDdiOPMConfigureProtectedOutput* function should return success and when an error:

-   If the protected output is associated with an S-Video output connector, a call to the display miniport driver's *DxgkDdiOPMGetCOPPCompatibleInformation* function with DXGKMDT\_OPM\_GET\_SUPPORTED\_PROTECTION\_TYPES set should indicate support of the analog content protection (ACP) type (DXGKMDT\_OPM\_PROTECTION\_TYPE\_ACP). Thereafter, if the driver's *DxgkDdiOPMConfigureProtectedOutput* function is called to set a level for the ACP type on this connector, the driver should return success because the output resolution of S-Video is fixed, even though desktop resolution (display mode) might be higher.

-   If the protected output is associated with component output connectors, a call to the display miniport driver's *DxgkDdiOPMGetCOPPCompatibleInformation* function with DXGKMDT\_OPM\_GET\_SUPPORTED\_PROTECTION\_TYPES set should also indicate support of the ACP type. However, if the driver's *DxgkDdiOPMConfigureProtectedOutput* function is called to set a level for the ACP type on this output when the display resolution is 720p or 1080i, the driver should return the STATUS\_GRAPHICS\_OPM\_RESOLUTION\_TOO\_HIGH error code. 720p or 1080i is too high of a resolution to set the protection level for the ACP type to on component output connectors.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20OPM%20and%20Display%20Modes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




