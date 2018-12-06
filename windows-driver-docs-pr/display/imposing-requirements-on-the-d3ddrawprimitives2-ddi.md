---
title: Imposing Requirements on the D3dDrawPrimitives2 DDI
description: Imposing Requirements on the D3dDrawPrimitives2 DDI
ms.assetid: a016c127-14ad-42ba-aae5-97c6c97b01f6
keywords:
- asynchronous query operations WDK DirectX 9.0 , D3dDrawPrimitives2
- query operations WDK DirectX 9.0 , D3dDrawPrimitives2
- D3dDrawPrimitives2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Imposing Requirements on the D3dDrawPrimitives2 DDI


## <span id="ddk_imposing_requirements_on_the_d3ddrawprimitives2_ddi_gg"></span><span id="DDK_IMPOSING_REQUIREMENTS_ON_THE_D3DDRAWPRIMITIVES2_DDI_GG"></span>


The ability of a DirectX 9.0 version driver to handle asynchronous queries imposes two new requirements on the driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function. These requirements, which are mentioned in the [Handling Asynchronous Queries](handling-asynchronous-queries.md) topic, are summarized in the following list:

-   The driver's *D3dDrawPrimitives2* function must ensure that it can process empty command buffers because the runtime might submit them so that the driver can write more responses. The runtime submits empty command buffers in the incoming command stream if the driver previously returned the D3DDP2OP\_RESPONSECONTINUE operation code in the response buffer.

-   On success of *D3dDrawPrimitives2* (**ddrval** of the [**D3DHAL\_DRAWPRIMITIVES2DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545957) structure set to D3D\_OK), the driver must ensure that it only sets the **dwErrorOffset** member of D3DHAL\_DRAWPRIMITIVES2DATA to nonzero when responses are available. If the driver does not respond to any queries and **ddrval** is D3D\_OK, **dwErrorOffset** must be set to zero.

 

 





