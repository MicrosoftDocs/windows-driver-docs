---
title: Supporting the DXGI DDI
description: Supporting the DXGI DDI
ms.assetid: 3a49d7cb-984f-4e4f-a549-5c0442e1c45a
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Supporting the DXGI DDI


To support the Microsoft DirectX Graphics Infrastructure (DXGI) device driver interface (DDI), the user-mode display driver must include the Dxgiddi.h header file. Dxgiddi.h also includes the Dxgitype.h header file, which contains definitions that are shared with application-level DXGI constructs. Dxgiddi.h defines several user-mode display driver entry points and a DXGI callback function that the driver can use to communicate with the kernel (including the display miniport driver).

The Microsoft Direct3D runtime supplies access to the DXGI DDI in the [**DXGI\_DDI\_BASE\_ARGS**](https://msdn.microsoft.com/library/windows/hardware/ff557485) structure that the **DXGIBaseDDI** member of the [**D3D10DDIARG\_CREATEDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff541664) structure points to in a call to the [**CreateDevice(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540635) function. The user-mode display driver supplies pointers to these DXGI functions:

-   [Direct3D Version 10 DXGI Functions](https://msdn.microsoft.com/library/windows/hardware/ff552905)
-   [Direct3D Version 11.1 DXGI Functions](https://msdn.microsoft.com/library/windows/hardware/dn458435)
-   [Direct3D Version 11.2 DXGI Functions](https://msdn.microsoft.com/library/windows/hardware/dn458008)

The driver implements these functions through members of the structures that the **pDXGIDDIBaseFunctionsXxx** members of **DXGI\_DDI\_BASE\_ARGS** point to. The driver should record the pointer to the [DXGI callback function table](https://msdn.microsoft.com/library/windows/hardware/ff552877) that the **pDXGIBaseCallbacks** member of **DXGI\_DDI\_BASE\_ARGS** points to for later use. The driver should record the pointer to the DXGI callback function table rather than record the individual pointer to the DXGI callback function because the Direct3D runtime can change the address of the callback function whenever there is no thread inside the user-mode display driver.
A further DXGI user-mode display driver requirement exists for software rasterizers. Such a user-mode display driver (more specifically, any driver that does not support hardware that is shared with the Direct3D version 9 DDI implementation on the graphics adapter) must return the **DXGI\_STATUS\_NO\_REDIRECTION** value instead of the S\_OK value from its [**CreateDevice(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540635) function. Returning **DXGI\_STATUS\_NO\_REDIRECTION** indicates to DXGI that it should not use the shared resource presentation path to effect communication with the Desktop Window Manager (DWM). The shared resource presentation path is created when calls to shared-resource functions (that is, [**CreateResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540691) and [**OpenResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff568612) functions with the **D3D10\_DDI\_RESOURCE\_MISC\_SHARED** flag set) occur. However, DXGI should instead use techniques relevant to a swapchain whose buffers are available only to the CPU. For example, DXGI should move rendered data from the back buffer to the desktop by means other than the shared resource presentation path. In this situation, DXGI actually calls the driver's [**PresentDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff569179) function to move rendered data rather than effect communication with the DWM.

 

 





