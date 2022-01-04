---
title: Imposing Requirements on the D3dDrawPrimitives2 DDI
description: Imposing Requirements on the D3dDrawPrimitives2 DDI
keywords:
- asynchronous query operations WDK DirectX 9.0 , D3dDrawPrimitives2
- query operations WDK DirectX 9.0 , D3dDrawPrimitives2
- D3dDrawPrimitives2
ms.date: 04/20/2017
---

# Imposing Requirements on the D3dDrawPrimitives2 DDI


## <span id="ddk_imposing_requirements_on_the_d3ddrawprimitives2_ddi_gg"></span><span id="DDK_IMPOSING_REQUIREMENTS_ON_THE_D3DDRAWPRIMITIVES2_DDI_GG"></span>


The ability of a DirectX 9.0 version driver to handle asynchronous queries imposes two new requirements on the driver's [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) function. These requirements, which are mentioned in the [Handling Asynchronous Queries](handling-asynchronous-queries.md) topic, are summarized in the following list:

-   The driver's *D3dDrawPrimitives2* function must ensure that it can process empty command buffers because the runtime might submit them so that the driver can write more responses. The runtime submits empty command buffers in the incoming command stream if the driver previously returned the D3DDP2OP\_RESPONSECONTINUE operation code in the response buffer.

-   On success of *D3dDrawPrimitives2* (**ddrval** of the [**D3DHAL\_DRAWPRIMITIVES2DATA**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_drawprimitives2data) structure set to D3D\_OK), the driver must ensure that it only sets the **dwErrorOffset** member of D3DHAL\_DRAWPRIMITIVES2DATA to nonzero when responses are available. If the driver does not respond to any queries and **ddrval** is D3D\_OK, **dwErrorOffset** must be set to zero.

 

