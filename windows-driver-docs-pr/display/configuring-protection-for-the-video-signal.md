---
title: Configuring Protection for the Video Signal
description: Configuring Protection for the Video Signal
ms.assetid: 557fc95b-1cf5-4b6d-b256-fe2db29ec0fa
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring Protection for the Video Signal


OPM configuration can configure protection for the video signal that goes through the physical connector that is associated with the protected output. To set signal protection, the display miniport driver's [**DxgkDdiOPMConfigureProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559701) function receives a pointer to a [**DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff560849) structure with the **guidSetting** member set to the DXGKMDT\_OPM\_SET\_ACP\_AND\_CGMSA\_SIGNALING GUID and the **abParameters** member set to a pointer to a [**DXGKMDT\_OPM\_SET\_ACP\_AND\_CGMSA\_SIGNALING\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff560913) structure that specifies how to protect the signal.

 

 





