---
title: Validating Index Values
description: Validating Index Values
keywords:
- user-mode display drivers WDK Windows Vista , index validation
- validating index values WDK display
- index validation WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Validating Index Values


A user-mode display driver can pass "Designed for Microsoft Windows" for Hardware Logo testing, regardless of whether it performs index validation. However, to ensure that the driver works with Microsoft DirectX applications that might pass invalid indexes, a user-mode display driver should perform index validation.

You should consider the following items:

-   DirectX 8.0 and DirectX 9.0 applications can pass a stride value of 0 when they render with a vertex buffer. In this situation, only vertex 0 should be referenced. The stride value is set in the **Stride** member of the [**D3DDDIARG\_SETSTREAMSOURCE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_setstreamsource) structure in a call to the user-mode display driver's [**SetStreamSource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_setstreamsource) function.

-   A call to the driver's [**SetStreamSourceUM**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_setstreamsourceum) function does not include the size of the vertex data. That is, the size of the user-memory buffer that supplies the vertex data that the *pUMBuffer* parameter of *SetStreamSourceUM* points to is not specified.

-   The **NumVertices** member of the [**D3DDDIARG\_DRAWINDEXEDPRIMITIVE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_drawindexedprimitive) or [**D3DDDIARG\_DRAWINDEXEDPRIMITIVE2**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_drawindexedprimitive2) structure is never set to 0 in a call to the driver's [**DrawIndexedPrimitive**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_drawindexedprimitive) or [**DrawIndexedPrimitive2**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_drawindexedprimitive2) function. The driver should set the maximum allowable index to (NumVerticesÂ -Â 1).

 

