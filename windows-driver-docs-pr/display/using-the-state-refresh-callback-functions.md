---
title: Using the State-Refresh Callback Functions
description: Using the State-Refresh Callback Functions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the State-Refresh Callback Functions

The user-mode display driver can use the [Direct3D Runtime Version 10 State-Refresh Callback Functions](direct3d-runtime-functions-called-by-user-mode.md) to achieve a stateless driver or to build up command buffer preamble data.

The Direct3D runtime supplies pointers to its state-refresh callback functions in the [**D3D10DDI\_CORELAYER\_DEVICECALLBACKS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10ddi_corelayer_devicecallbacks) structure that the **pUMCallbacks** member of the [**D3D10DDIARG\_CREATEDEVICE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10ddiarg_createdevice) structure points to in a call to the [**CreateDevice(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function.

The user-mode display driver might call, for example, the [**pfnStateIaIndexBufCb**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_state_ia_indexbuf_cb) state-refresh callback function, while the driver is within a call to the driver's [**IaSetIndexBuffer**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_ia_setindexbuffer) function. This call is quite possible, especially because the user-mode display driver might use the **pfnStateIaIndexBufCb** callback function to build a preamble, and the call to *IaSetIndexBuffer* might exhaust the size of the command buffer and cause a flush. For such a situation, the call to **pfnStateIaIndexBufCb** passes the same "new" binding information as the original call to *IaSetIndexBuffer*. This situation results in a more optimal preamble.
