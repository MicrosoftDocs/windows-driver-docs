---
title: Setting the HDCP SRM Version
description: Setting the HDCP SRM Version
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the HDCP SRM Version


OPM configuration can set the version of the High-bandwidth Digital Content Protection (HDCP) System Renewability Message (SRM) for the protected output. To set the version, the display miniport driver's [**DxgkDdiOPMConfigureProtectedOutput**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_configure_protected_output) function receives a pointer to a [**DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgkmdt_opm_configure_parameters) structure with the **guidSetting** member set to the DXGKMDT\_OPM\_SET\_HDCP\_SRM GUID and the **abParameters** member set to a pointer to a [**DXGKMDT\_OPM\_SET\_HDCP\_SRM\_PARAMETERS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgkmdt_opm_set_hdcp_srm_parameters) structure. The DXGKMDT\_OPM\_SET\_HDCP\_SRM\_PARAMETERS structure contains a ULONG that specifies the version number. The least significant bits (bits 0 through 15) contain the SRM's version number in little-endian format. For more information about the SRM version number, see the [HDCP Specification Revision 1.1](https://go.microsoft.com/fwlink/p/?linkid=38728).

 

