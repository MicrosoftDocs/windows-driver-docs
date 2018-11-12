---
title: Instructing How to Protect the Signal
description: Instructing How to Protect the Signal
ms.assetid: d55a3660-5b7c-43e9-b1c5-b61f8b997a1a
keywords:
- copy protection WDK COPP , signal protection
- video copy protection WDK COPP , signal protection
- COPP WDK DirectX VA , signal protection
- protected video WDK COPP , signal protection
- signal protection WDK COPP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Instructing How to Protect the Signal


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

The COPP command can provide instructions about how to protect the signal that goes through the physical connector associated with the DirectX VA COPP device. To set signal protection, the video miniport driver's [*COPPCommand*](https://msdn.microsoft.com/library/windows/hardware/ff539642) function receives a pointer to a [**DXVA\_COPPCommand**](https://msdn.microsoft.com/library/windows/hardware/ff563141) structure with the **guidCommandID** member set to the DXVA\_COPPSetSignaling GUID and the **CommandData** member set to a pointer to a [**DXVA\_COPPSetSignalingCmdData**](https://msdn.microsoft.com/library/windows/hardware/ff563146) structure that specifies how to protect the signal.

 

 





