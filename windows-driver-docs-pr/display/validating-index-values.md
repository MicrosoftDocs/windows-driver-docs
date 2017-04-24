---
title: Validating Index Values
description: Validating Index Values
ms.assetid: 09247df3-0c87-48cf-9c94-bda23c6b38d2
keywords:
- user-mode display drivers WDK Windows Vista , index validation
- validating index values WDK display
- index validation WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Validating Index Values


A user-mode display driver can pass "Designed for Microsoft Windows" for Hardware Logo testing, regardless of whether it performs index validation. However, to ensure that the driver works with Microsoft DirectX applications that might pass invalid indexes, a user-mode display driver should perform index validation.

You should consider the following items:

-   DirectX 8.0 and DirectX 9.0 applications can pass a stride value of 0 when they render with a vertex buffer. In this situation, only vertex 0 should be referenced. The stride value is set in the **Stride** member of the [**D3DDDIARG\_SETSTREAMSOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff543352) structure in a call to the user-mode display driver's [**SetStreamSource**](https://msdn.microsoft.com/library/windows/hardware/ff569660) function.

-   A call to the driver's [**SetStreamSourceUM**](https://msdn.microsoft.com/library/windows/hardware/ff569662) function does not include the size of the vertex data. That is, the size of the user-memory buffer that supplies the vertex data that the *pUMBuffer* parameter of *SetStreamSourceUM* points to is not specified.

-   The **NumVertices** member of the [**D3DDDIARG\_DRAWINDEXEDPRIMITIVE**](https://msdn.microsoft.com/library/windows/hardware/ff543048) or [**D3DDDIARG\_DRAWINDEXEDPRIMITIVE2**](https://msdn.microsoft.com/library/windows/hardware/ff543054) structure is never set to 0 in a call to the driver's [**DrawIndexedPrimitive**](https://msdn.microsoft.com/library/windows/hardware/ff556133) or [**DrawIndexedPrimitive2**](https://msdn.microsoft.com/library/windows/hardware/ff556135) function. The driver should set the maximum allowable index to (NumVerticesÂ -Â 1).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Validating%20Index%20Values%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




