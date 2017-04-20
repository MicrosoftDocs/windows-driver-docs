---
title: OPM Features
description: OPM Features
ms.assetid: a2fc9d0c-d85c-484e-8cf2-09b2a84801f8
keywords:
- OPM WDK display , features
- OPM WDK display , COPP and OPM comparison
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OPM Features


OPM supports all of Certified Output Protection Protocol's (COPP) features. The following describes some new OPM features and how some OPM features compare to COPP features:

-   OPM requires that applications sign requests for information from the video output while COPP does not require that applications sign requests for information from the graphics driver.

    **Note**   A COPP graphics driver is equivalent to an OPM video output.

     

    COPP applications request information from a graphics driver by causing a [**DXVA\_COPPStatusInput**](https://msdn.microsoft.com/library/windows/hardware/ff563899) structure to be passed to the driver.

-   OPM supports High-bandwidth Digital Content Protection (HDCP) repeaters. For more information about HDCP repeaters, see the [HDCP Specification Revision 1.1](http://go.microsoft.com/fwlink/p/?linkid=38728).

-   Applications can more easily support HDCP in OPM. Applications are not required to parse HDCP System Renewability Messages (SRMs) and to determine if a monitor was revoked. For more information about HDCP SRMs, see the [HDCP Specification Revision 1.1](http://go.microsoft.com/fwlink/p/?linkid=38728).

-   OPM uses X.509 certificates and COPP uses proprietary XML certificates. The COPP certificate format is based on the signature format in the XML-Signature Syntax and Processing specification. For information about X.509 certificates, see the [X.509 Certificate Profile](http://go.microsoft.com/fwlink/p/?linkid=70416).

-   COPP applications get the COPP **IAMCertifiedOutputProtection** interface by creating version 7 or 9 of the Video Mixing Renderer ([*VMR*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-video-mixer-renderer--vmr-)) and then passing IID\_IAMCertifiedOutputProtection to the VMR filter's implementation of **IUnknown::QueryInterface**. OPM applications get the **IOPMVideoOutput** interface by passing an HMONITOR or an **IDirect3DDevice9** object to the **OPMGetVideoOutputsFromHMONITOR** or **OPMGetVideoOutputsFromIDirect3DDevice9Object** function respectively. For more information about these functions and interfaces, see the Microsoft Windows SDK documentation.

-   OPM supports clone mode in all cases while COPP supports clone mode only in one specific case.

-   OPM's redistribution control flag has slightly different semantics than COPP's redistribution control flag (COPP\_CGMSA\_RedistributionControlRequired).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20OPM%20Features%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




