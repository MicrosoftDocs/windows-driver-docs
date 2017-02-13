---
title: Overlay DDI Programming Considerations
description: Overlay DDI Programming Considerations
ms.assetid: 887624a7-0293-4add-94a7-d490ebd93205
keywords: ["Overlay DDI WDK Windows 7 display , programming considerations", "Overlay DDI WDK Server 2008 R2 display , programming considerations"]
---

# Overlay DDI Programming Considerations


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

When you implement the [Overlay DDI](overlay-ddi.md) in your user-mode display driver, you should consider the following programming tips:

-   If the driver supports the Overlay DDI, it must set the D3DCAPS\_OVERLAY bit in the **Caps** member of [D3DCAPS9](http://go.microsoft.com/fwlink/p/?linkid=122122) structure. The D3DCAPS9 structure is described in the DirectX 9.0 SDK documentation. The driver sets the D3DCAPS\_OVERLAY bit in response to a call to its [**GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff566762) function in which the D3DDDICAPS\_GETD3D9CAPS value is set in the **Type** member of the [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148) structure that the *pData* parameter points to.

-   When the display format is 64 bits rather than 32 bits (for example, when the DWM uses the D3DDDIFMT\_A16B16G16R16F value from the [**D3DDDIFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff544312) enumeration for the display mode), the Direct3D runtime places the low 32 bits of the overlay color key in the **DstColorKeyLow** member of the [**D3DDDI\_OVERLAYINFO**](https://msdn.microsoft.com/library/windows/hardware/ff544621) structure and the upper 32 bits in the **DstColorKeyHigh** member of **D3DDDI\_OVERLAYINFO**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Overlay%20DDI%20Programming%20Considerations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




