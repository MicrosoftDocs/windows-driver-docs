---
title: Overlay DDI Programming Considerations
description: Overlay DDI Programming Considerations
ms.assetid: 887624a7-0293-4add-94a7-d490ebd93205
keywords:
- Overlay DDI WDK Windows 7 display , programming considerations
- Overlay DDI WDK Server 2008 R2 display , programming considerations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overlay DDI Programming Considerations


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

When you implement the [Overlay DDI](overlay-ddi.md) in your user-mode display driver, you should consider the following programming tips:

-   If the driver supports the Overlay DDI, it must set the D3DCAPS\_OVERLAY bit in the **Caps** member of [D3DCAPS9](http://go.microsoft.com/fwlink/p/?linkid=122122) structure. The D3DCAPS9 structure is described in the DirectX 9.0 SDK documentation. The driver sets the D3DCAPS\_OVERLAY bit in response to a call to its [**GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff566762) function in which the D3DDDICAPS\_GETD3D9CAPS value is set in the **Type** member of the [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148) structure that the *pData* parameter points to.

-   When the display format is 64 bits rather than 32 bits (for example, when the DWM uses the D3DDDIFMT\_A16B16G16R16F value from the [**D3DDDIFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff544312) enumeration for the display mode), the Direct3D runtime places the low 32 bits of the overlay color key in the **DstColorKeyLow** member of the [**D3DDDI\_OVERLAYINFO**](https://msdn.microsoft.com/library/windows/hardware/ff544621) structure and the upper 32 bits in the **DstColorKeyHigh** member of **D3DDDI\_OVERLAYINFO**.

 

 





