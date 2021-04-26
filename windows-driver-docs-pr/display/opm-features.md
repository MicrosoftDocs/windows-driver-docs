---
title: OPM Features
description: OPM Features
keywords:
- OPM WDK display , features
- OPM WDK display , COPP and OPM comparison
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# OPM Features

OPM supports all of Certified Output Protection Protocol's (COPP) features. The following describes some new OPM features and how some OPM features compare to COPP features:

-   OPM requires that applications sign requests for information from the video output while COPP does not require that applications sign requests for information from the graphics driver.

    > [!NOTE]
    > A COPP graphics driver is equivalent to an OPM video output.

    COPP applications request information from a graphics driver by causing a [**DXVA\_COPPStatusInput**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_coppstatusinput) structure to be passed to the driver.

-   OPM supports High-bandwidth Digital Content Protection (HDCP) repeaters. For more information about HDCP repeaters, see the [HDCP Specification Revision 1.1](https://go.microsoft.com/fwlink/p/?linkid=38728).

-   Applications can more easily support HDCP in OPM. Applications are not required to parse HDCP System Renewability Messages (SRMs) and to determine if a monitor was revoked. For more information about HDCP SRMs, see the [HDCP Specification Revision 1.1](https://go.microsoft.com/fwlink/p/?linkid=38728).

-   OPM uses X.509 certificates and COPP uses proprietary XML certificates. The COPP certificate format is based on the signature format in the XML-Signature Syntax and Processing specification. For information about X.509 certificates, see the [X.509 Certificate Profile](https://go.microsoft.com/fwlink/p/?linkid=70416).

-   COPP applications get the COPP **IAMCertifiedOutputProtection** interface by creating version 7 or 9 of the Video Mixing Renderer ([*VMR*](/windows/desktop/DirectShow/using-the-video-mixing-renderer)) and then passing IID\_IAMCertifiedOutputProtection to the VMR filter's implementation of **IUnknown::QueryInterface**. OPM applications get the **IOPMVideoOutput** interface by passing an HMONITOR or an **IDirect3DDevice9** object to the **OPMGetVideoOutputsFromHMONITOR** or **OPMGetVideoOutputsFromIDirect3DDevice9Object** function respectively. For more information about these functions and interfaces, see the Microsoft Windows SDK documentation.

-   OPM supports clone mode in all cases while COPP supports clone mode only in one specific case.

-   OPM's redistribution control flag has slightly different semantics than COPP's redistribution control flag (COPP\_CGMSA\_RedistributionControlRequired).
