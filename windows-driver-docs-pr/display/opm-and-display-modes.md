---
title: OPM and Display Modes
description: OPM and Display Modes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# OPM and Display Modes


The display miniport driver should report all the protection types that are supported on the physical connector that is associated with the protected output, regardless of the display mode that is currently being used. The display miniport driver reports supported protection types when it receives a call to its [**DxgkDdiOPMGetInformation**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_information) or [**DxgkDdiOPMGetCOPPCompatibleInformation**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_copp_compatible_information) function with DXGKMDT\_OPM\_GET\_SUPPORTED\_PROTECTION\_TYPES set in the **guidInformation** member of the [**DXGKMDT\_OPM\_GET\_INFO\_PARAMETERS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgkmdt_opm_get_info_parameters) structure. For more information about retrieving supported protection types, see [Retrieving Information About a Protected Output](retrieving-information-about-a-protected-output.md) or [Retrieving COPP-Compatible Information about a Protected Output](retrieving-copp-compatible-information-about-a-protected-output.md).

If the current resolution is too high for a particular protection type, the driver should return an error when the display miniport driver's [**DxgkDdiOPMConfigureProtectedOutput**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_configure_protected_output) function is called to set the protection level for that protection type. The following scenarios give examples of when the driver's *DxgkDdiOPMConfigureProtectedOutput* function should return success and when an error:

-   If the protected output is associated with an S-Video output connector, a call to the display miniport driver's *DxgkDdiOPMGetCOPPCompatibleInformation* function with DXGKMDT\_OPM\_GET\_SUPPORTED\_PROTECTION\_TYPES set should indicate support of the analog content protection (ACP) type (DXGKMDT\_OPM\_PROTECTION\_TYPE\_ACP). Thereafter, if the driver's *DxgkDdiOPMConfigureProtectedOutput* function is called to set a level for the ACP type on this connector, the driver should return success because the output resolution of S-Video is fixed, even though desktop resolution (display mode) might be higher.

-   If the protected output is associated with component output connectors, a call to the display miniport driver's *DxgkDdiOPMGetCOPPCompatibleInformation* function with DXGKMDT\_OPM\_GET\_SUPPORTED\_PROTECTION\_TYPES set should also indicate support of the ACP type. However, if the driver's *DxgkDdiOPMConfigureProtectedOutput* function is called to set a level for the ACP type on this output when the display resolution is 720p or 1080i, the driver should return the STATUS\_GRAPHICS\_OPM\_RESOLUTION\_TOO\_HIGH error code. 720p or 1080i is too high of a resolution to set the protection level for the ACP type to on component output connectors.

 

