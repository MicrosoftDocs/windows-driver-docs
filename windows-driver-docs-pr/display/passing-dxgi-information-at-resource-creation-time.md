---
title: Passing DXGI Information at Resource Creation Time
description: Passing DXGI Information at Resource Creation Time
ms.assetid: d99fc77a-7192-4e45-852a-7a2ae87cc9a2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Passing DXGI Information at Resource Creation Time


The Direct3D version 10 runtime can pass DXGI-specific information when it calls the user-mode display driver's [**CreateResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540691) function to create a resource. The runtime can pass a pointer to a [**DXGI\_DDI\_PRIMARY\_DESC**](https://msdn.microsoft.com/library/windows/hardware/ff557511) structure in the **pPrimaryDesc** member of the [**D3D10DDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff541697) structure to specify that the resource can be used as a primary (that is, the resource can be scanned out to the display). The runtime sets **pPrimaryDesc** to a non-NULL value only if the runtime also sets the D3D10\_DDI\_BIND\_PRESENT bit in the **BindFlags** member of D3D10DDIARG\_CREATERESOURCE.

The runtime can specify the DXGI\_DDI\_PRIMARY\_OPTIONAL flag in the **Flags** member of DXGI\_DDI\_PRIMARY\_DESC to notify the user-mode display driver that the driver can opt out from using the resource in a flip-style presentation. To notify the runtime that it should not use the resource in flip-style presentations, the driver sets the DXGI\_DDI\_PRIMARY\_DRIVER\_FLAG\_NO\_SCANOUT flag in the **DriverFlags** member of DXGI\_DDI\_PRIMARY\_DESC.

If the driver returns DXGI\_DDI\_PRIMARY\_DRIVER\_FLAG\_NO\_SCANOUT in the [**CreateResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540691) call to create the resource, the runtime will always perform a bit-block transfer (bitblt)-style presentation (instead of a flip-style presentation) when the resource is the source of the presentation. This functionality is useful if graphics hardware cannot scan out a particular subset of a given resource type. For example, graphics hardware might or might not be able to scan out a multisampled back buffer type of resource. In addition, the ability to scan out multisampled back buffers might further depend on the format of the surface. If the graphics hardware was not able to scan out a particular multisampled format, the user-mode display driver would set the DXGI\_DDI\_PRIMARY\_DRIVER\_FLAG\_NO\_SCANOUT flag in the **DriverFlags** member of DXGI\_DDI\_PRIMARY\_DESC for the resource with this format.

If the runtime does not set the DXGI\_DDI\_PRIMARY\_OPTIONAL flag in the **Flags** member of DXGI\_DDI\_PRIMARY\_DESC to notify the driver about the possibility of opting out of using the resource in a flip-style presentation, the driver can still return the DXGI\_DDI\_ERR\_UNSUPPORTED error code along with the DXGI\_DDI\_PRIMARY\_DRIVER\_FLAG\_NO\_SCANOUT flag from a call to [**CreateResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540691). The driver's *CreateResource(D3D10)* passes DXGI\_DDI\_ERR\_UNSUPPORTED in a call to the [**pfnSetErrorCb**](https://msdn.microsoft.com/library/windows/hardware/ff568929) function if the driver cannot scan out such a primary. Returning DXGI\_DDI\_ERR\_UNSUPPORTED along with DXGI\_DDI\_PRIMARY\_DRIVER\_FLAG\_NO\_SCANOUT causes DXGI to interpose a proxy surface in the presentation path, between the back buffers and the primary surface. The proxy surface always matches the primary (scanned-out) surface in terms of size, multisample, and rotation. The first step in this process is for DXGI to determine which of the multisample or rotation settings cause the driver to refuse to scan out a surface with those settings. DXGI makes this determination by scaling back and trying to create a primary without rotation, without multisampling, or without both. After DXGI determines the driver's support for scan-out features, DXGI creates the primary and proxy surfaces, and the driver should be able to flip between these two surfaces. DXGI will still subsequently satisfy an application's requests for auto-rotated or multisampled back buffers by calling the driver's [**BltDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff538252) function to perform bitblts from back buffers to the proxy surface. These bitblts request the driver to perform multisample resolves or rotates. For more information about *BltDXGI*, see the **BltDXGI** reference page.

 

 





