---
title: Configuring a Protected Output
description: Configuring a Protected Output
keywords:
- OPM WDK display , configuring protected outputs
ms.date: 04/20/2017
---

# Configuring a Protected Output


The display miniport driver can receive requests to configure the protected output that is associated with a graphics adapter's physical output connector. The display miniport driver's [**DxgkDdiOPMConfigureProtectedOutput**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_configure_protected_output) function is passed a pointer to a [**DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgkmdt_opm_configure_parameters) structure that specifies how to configure the protected output. The **guidSetting** and **abParameters** members of DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS specify the configuration request.

**Note**   Before **DxgkDdiOPMConfigureProtectedOutput** returns, the display miniport driver must verify that the One-key Cipher Block Chaining (CBC)-mode message authentication code (OMAC) that is specified in the **omac** member of DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS is correct. For more information about verifying OMAC, see [OMAC-1 algorithm](https://go.microsoft.com/fwlink/p/?linkid=70417). The driver must also verify that the sequence number that is specified in the **ulSequenceNumber** member of DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS matches the sequence number that the driver currently has stored. The driver must then increment the stored sequence number.

 

The display miniport driver should support the following configuration requests:

-   [Setting the Protection Level for a Protected Output](setting-the-protection-level-for-a-protected-output.md)

-   [Configuring Protection for the Video Signal](configuring-protection-for-the-video-signal.md)

-   [Setting the HDCP SRM Version](setting-the-hdcp-srm-version.md)

 

