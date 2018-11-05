---
title: COPP Processing
description: COPP Processing
ms.assetid: c9ff0fd3-c063-4450-ae66-54153b3dc53c
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , COPP
- Video Acceleration WDK DirectX , COPP
- VA WDK DirectX , COPP
- Certified Output Protection Protocol WDK DirectX VA
- copy protection WDK COPP
- video copy protection WDK COPP
- COPP WDK DirectX VA
- protected video WDK COPP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# COPP Processing


## <span id="ddk_certified_output_protection_protocol_processing_gg"></span><span id="DDK_CERTIFIED_OUTPUT_PROTECTION_PROTOCOL_PROCESSING_GG"></span>


This section applies only to Microsoft Windows Server 2003 with Service Pack 1 (SP1) and later, and Windows XP with Service Pack 2 (SP2) and later.

The Certified Output Protection Protocol (COPP) device driver interface (DDI) extends DirectX Video Acceleration (VA) to support copy protection of video that is output by various connectors of the graphics adapter. The COPP DDI is an interface between the Video Mixing Renderer ([*VMR*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-video-mixer-renderer--vmr-)) and the video miniport driver. The COPP DDI maps to the existing DirectDraw and DirectX VA DDI. The DDI is not accessible via the **IAMVideoAccelerator** interface. The DDI is accessible to applications via the **IAMCertifiedOutputProtection** interface.

For more information about the **IAMCertifiedOutputProtection** and **IAMVideoAccelerator** interfaces, see the latest DirectX Software Development Kit (SDK) documentation.

If a video miniport driver supports the passing of protected commands and status between applications and the driver, the VMR will initiate a call to the driver to create a DirectX VA COPP device.

The following topics describe the COPP DDI and how to support COPP:

[Introduction to COPP](introduction-to-copp.md)

[Mapping the COPP DDI to DirectDraw and DirectX VA](mapping-the-copp-ddi-to-directdraw-and-directx-va.md)

[Sample Functions for COPP](sample-functions-for-copp.md)

[Returning Error Codes from COPP Functions](returning-error-codes-from-copp-functions.md)

[Performing COPP Operations](performing-copp-operations.md)

[Implementation Tips and Requirements for COPP](implementation-tips-and-requirements-for-copp.md)

 

 





