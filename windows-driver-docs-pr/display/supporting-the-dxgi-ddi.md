---
title: Supporting the DXGI DDI
description: Supporting the DXGI DDI
ms.assetid: 3a49d7cb-984f-4e4f-a549-5c0442e1c45a
---

# Supporting the DXGI DDI


To support the Microsoft DirectX Graphics Infrastructure (DXGI) device driver interface (DDI), the user-mode display driver must include the Dxgiddi.h header file. Dxgiddi.h also includes the Dxgitype.h header file, which contains definitions that are shared with application-level DXGI constructs. Dxgiddi.h defines several user-mode display driver entry points and a DXGI callback function that the driver can use to communicate with the kernel (including the display miniport driver).

The Microsoft Direct3D runtime supplies access to the DXGI DDI in the [**DXGI\_DDI\_BASE\_ARGS**](https://msdn.microsoft.com/library/windows/hardware/ff557485) structure that the **DXGIBaseDDI** member of the [**D3D10DDIARG\_CREATEDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff541664) structure points to in a call to the [**CreateDevice(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540635) function. The user-mode display driver supplies pointers to these DXGI functions:

-   [Direct3D Version 10 DXGI Functions](https://msdn.microsoft.com/library/windows/hardware/ff552905)
-   [Direct3D Version 11.1 DXGI Functions](https://msdn.microsoft.com/library/windows/hardware/dn458435)
-   [Direct3D Version 11.2 DXGI Functions](https://msdn.microsoft.com/library/windows/hardware/dn458008)

The driver implements these functions through members of the structures that the **pDXGIDDIBaseFunctionsXxx** members of **DXGI\_DDI\_BASE\_ARGS** point to. The driver should record the pointer to the [DXGI callback function table](https://msdn.microsoft.com/library/windows/hardware/ff552877) that the **pDXGIBaseCallbacks** member of **DXGI\_DDI\_BASE\_ARGS** points to for later use. The driver should record the pointer to the DXGI callback function table rather than record the individual pointer to the DXGI callback function because the Direct3D runtime can change the address of the callback function whenever there is no thread inside the user-mode display driver.
A further DXGI user-mode display driver requirement exists for software rasterizers. Such a user-mode display driver (more specifically, any driver that does not support hardware that is shared with the Direct3D version 9 DDI implementation on the graphics adapter) must return the **DXGI\_STATUS\_NO\_REDIRECTION** value instead of the S\_OK value from its [**CreateDevice(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540635) function. Returning **DXGI\_STATUS\_NO\_REDIRECTION** indicates to DXGI that it should not use the shared resource presentation path to effect communication with the Desktop Window Manager (DWM). The shared resource presentation path is created when calls to shared-resource functions (that is, [**CreateResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540691) and [**OpenResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff568612) functions with the **D3D10\_DDI\_RESOURCE\_MISC\_SHARED** flag set) occur. However, DXGI should instead use techniques relevant to a swapchain whose buffers are available only to the CPU. For example, DXGI should move rendered data from the back buffer to the desktop by means other than the shared resource presentation path. In this situation, DXGI actually calls the driver's [**PresentDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff569179) function to move rendered data rather than effect communication with the DWM.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20the%20DXGI%20DDI%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




