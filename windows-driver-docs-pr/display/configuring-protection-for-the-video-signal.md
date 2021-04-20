---
title: Configuring Protection for the Video Signal
description: Configuring Protection for the Video Signal
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring Protection for the Video Signal


OPM configuration can configure protection for the video signal that goes through the physical connector that is associated with the protected output. To set signal protection, the display miniport driver's [**DxgkDdiOPMConfigureProtectedOutput**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_configure_protected_output) function receives a pointer to a [**DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgkmdt_opm_configure_parameters) structure with the **guidSetting** member set to the DXGKMDT\_OPM\_SET\_ACP\_AND\_CGMSA\_SIGNALING GUID and the **abParameters** member set to a pointer to a [**DXGKMDT\_OPM\_SET\_ACP\_AND\_CGMSA\_SIGNALING\_PARAMETERS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgkmdt_opm_set_acp_and_cgmsa_signaling_parameters) structure that specifies how to protect the signal.

 

