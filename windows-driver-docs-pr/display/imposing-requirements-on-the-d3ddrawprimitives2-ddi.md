---
title: Imposing Requirements on the D3dDrawPrimitives2 DDI
description: Imposing Requirements on the D3dDrawPrimitives2 DDI
ms.assetid: a016c127-14ad-42ba-aae5-97c6c97b01f6
keywords:
- asynchronous query operations WDK DirectX 9.0 , D3dDrawPrimitives2
- query operations WDK DirectX 9.0 , D3dDrawPrimitives2
- D3dDrawPrimitives2
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Imposing Requirements on the D3dDrawPrimitives2 DDI


## <span id="ddk_imposing_requirements_on_the_d3ddrawprimitives2_ddi_gg"></span><span id="DDK_IMPOSING_REQUIREMENTS_ON_THE_D3DDRAWPRIMITIVES2_DDI_GG"></span>


The ability of a DirectX 9.0 version driver to handle asynchronous queries imposes two new requirements on the driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function. These requirements, which are mentioned in the [Handling Asynchronous Queries](handling-asynchronous-queries.md) topic, are summarized in the following list:

-   The driver's *D3dDrawPrimitives2* function must ensure that it can process empty command buffers because the runtime might submit them so that the driver can write more responses. The runtime submits empty command buffers in the incoming command stream if the driver previously returned the D3DDP2OP\_RESPONSECONTINUE operation code in the response buffer.

-   On success of *D3dDrawPrimitives2* (**ddrval** of the [**D3DHAL\_DRAWPRIMITIVES2DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545957) structure set to D3D\_OK), the driver must ensure that it only sets the **dwErrorOffset** member of D3DHAL\_DRAWPRIMITIVES2DATA to nonzero when responses are available. If the driver does not respond to any queries and **ddrval** is D3D\_OK, **dwErrorOffset** must be set to zero.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Imposing%20Requirements%20on%20the%20D3dDrawPrimitives2%20DDI%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




