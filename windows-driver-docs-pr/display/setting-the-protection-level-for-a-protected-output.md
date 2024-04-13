---
title: Setting the Protection Level for a Protected Output
description: Setting the Protection Level for a Protected Output
ms.date: 04/20/2017
---

# Setting the Protection Level for a Protected Output


OPM configuration can set the protection level of a protection type on a protected output. To set the protection level, the display miniport driver's [**DxgkDdiOPMConfigureProtectedOutput**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_configure_protected_output) function receives a pointer to a [**DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgkmdt_opm_configure_parameters) structure with the **guidSetting** member set to the DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL GUID and the **abParameters** member set to a pointer to a [**DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgkmdt_opm_set_protection_level_parameters) structure that specifies the type of protection to set and the level at which to set the protection. The following protection levels can be set for the indicated protection types:

-   For DXGKMDT\_OPM\_PROTECTION\_TYPE\_ACP specified in the **ulProtectionType** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS, one of the protection-level values from the [**DXGKMDT\_OPM\_ACP\_PROTECTION\_LEVEL**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_dxgkmdt_opm_acp_protection_level) enumeration can be specified in the **ulProtectionLevel** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS.

-   For DXGKMDT\_OPM\_PROTECTION\_TYPE\_CGMSA specified in the **ulProtectionType** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS, one of the protection-level values from the [**DXGKMDT\_OPM\_CGMSA**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_dxgkmdt_opm_cgmsa) enumeration can be specified in the **ulProtectionLevel** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS.

-   For DXGKMDT\_OPM\_PROTECTION\_TYPE\_HDCP or DXGKMDT\_OPM\_PROTECTION\_TYPE\_COPP\_COMPATIBLE\_HDCP specified in the **ulProtectionType** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS, one of the protection-level values from the [**DXGKMDT\_OPM\_HDCP\_PROTECTION\_LEVEL**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_dxgkmdt_opm_hdcp_protection_level) enumeration can be specified in the **ulProtectionLevel** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS.

-   For DXGKMDT\_OPM\_PROTECTION\_TYPE\_DPCP specified in the **ulProtectionType** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS, one of the protection-level values from the [**DXGKMDT\_OPM\_DPCP\_PROTECTION\_LEVEL**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_dxgkmdt_dpcp_protection_level) enumeration can be specified in the **ulProtectionLevel** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS.

**Note**   The DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_ACCORDING\_TO\_CSS\_DVD GUID is new for Windows 7 and is used to indicate that the driver should enable HDCP according to the new CSS rules. Setting the DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_ACCORDING\_TO\_CSS\_DVD command is identical to setting the existing DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL command except that DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_ACCORDING\_TO\_CSS\_DVD has no absolute requirement to enable the requested protection.

 

 

