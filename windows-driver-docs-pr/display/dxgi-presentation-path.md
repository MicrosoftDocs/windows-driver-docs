---
title: DXGI Presentation Path
description: DXGI Presentation Path
ms.assetid: 3519172d-261c-4b33-b1e7-c4abf33b15f3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DXGI Presentation Path


DXGI provides applications with a presentation methodology that "just works." For example, applications are not required to perform any special operations to transition between windowed mode and full-screen mode. This presentation methodology is possible because DXGI and the user-mode display driver work together to preserve presentation across combinations of Multiple Sample Anti Aliasing (MSAA), monitor rotation, back and front buffer differences in size and format, and full-screen versus windowed modes. Another advantage of DXGI is that it allows a display adapter to have limited ability to scan-out MSAA and rotated surfaces because DXGI provides a "stateless" DDI. In a stateless DDI, the adapter's driver is not required to record data across DDI calls.

The basic task of presentation is to move data from a rendered back buffer to the primary surface for viewing. This task is performed in the different situations that are described in the following sections.

### <span id="windowed_mode_with_dwm_on"></span><span id="WINDOWED_MODE_WITH_DWM_ON"></span>Windowed mode with DWM on

In the windowed mode with Desktop Windows Manager (DWM)-on case, DXGI communicates with DWM and opens a view of a shared resource that is a render target for the DXGI producer and a texture for DWM. This shared resource exists in addition to any back buffers that the application creates. DXGI calls the driver's [**BltDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff538252) function to move data from any of the back buffers to the shared surface. This operation might require stretch, color conversion, and MSAA resolve. However, this operation never requires source and destination sub-rectangles. In fact, these sub-rectangles cannot be expressed in the call to *BltDXGI*. This bit-block transfer (bitblt) always has the **Present** flag set in the **Flags** member of the [**DXGI\_DDI\_ARG\_BLT**](https://msdn.microsoft.com/library/windows/hardware/ff557447) structure that the *pBltData* parameter points to. Setting the **Present** flag indicates that the driver should perform the operation atomically. The driver performs the bitblt operation atomically to minimize the possibility of tearing while the DWM reads the shared resource for composition.

### <span id="windowed_mode_with_dwm_off"></span><span id="WINDOWED_MODE_WITH_DWM_OFF"></span>Windowed mode with DWM off

In the windowed mode with DWM-off case, DXGI calls the driver's [**PresentDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff569179) function with the **Blt** flag set in the **Flags** member of the [**DXGI\_DDI\_ARG\_PRESENT**](https://msdn.microsoft.com/library/windows/hardware/ff557464) structure that the *pPresentData* parameter points to. In this *PresentDXGI* call, DXGI can specify any of the application-created back buffers in the **hSurfaceToPresent** and **SrcSubResourceIndex** members of DXGI\_DDI\_ARG\_PRESENT. There is no additional shared surface.

### <span id="full_screen_mode"></span><span id="FULL_SCREEN_MODE"></span>Full-screen mode

The full-screen case is more complicated than the windowed mode with DWM either on or off.

When DXGI makes the transition to full-screen mode, it attempts to exploit a flip operation in order to reduce bandwidth and gain vertical-sync synchronization. The following conditions can prevent the use of a flip operation:

-   The application did not re-allocate its back buffers in a way that they match the primary surface.

-   The driver specified that it will not scan-out the back buffer (for example, because the back buffer is rotated or is MSAA).

-   The application specified that it cannot accept the Direct3D runtime discarding of the back buffer's contents and requested only one buffer (total) in the chain. (In this case, DXGI allocates a back surface and a primary surface; however, DXGI uses the driver's *PresentDXGI* function with the **Blt** flag set.)

When one of the preceding conditions has occurred thereby preventing a flip operation and a call to the driver's [**PresentDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff569179) function with the **Blt** flag set is also not appropriate (because the back buffer does not match the front buffer exactly), DXGI allocates the *proxy surface*. This proxy surface matches the front buffer. Therefore, a flip between the proxy surface and the front buffer becomes possible. If the proxy surface exists, DXGI uses the driver's [**BltDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff538252) function with the **Present** flag cleared (0) to copy the application's back buffers to the proxy surface. In this *BltDXGI* call, DXGI might request converting, stretching, and resolving. DXGI then calls the driver's *PresentDXGI* function with the **Flip** flag set in the **Flags** member of the [**DXGI\_DDI\_ARG\_PRESENT**](https://msdn.microsoft.com/library/windows/hardware/ff557464) structure to move the proxy surface bits to scan-out.

To notify the user-mode display driver that the driver can opt out from scanning out, the driver will receive resource-creation calls for optional and non-optional classes of scan-out surfaces. Optional scan-out surfaces are designated by the DXGI\_DDI\_PRIMARY\_OPTIONAL flag. Non-optional scan-out surfaces do not have the DXGI\_DDI\_PRIMARY\_OPTIONAL flag set. For more information about these types of resource-creation calls, see [Passing DXGI Information at Resource Creation Time](passing-dxgi-information-at-resource-creation-time.md).

DXGI sets the DXGI\_DDI\_PRIMARY\_OPTIONAL flag to create all back buffer surfaces (that is, optional surfaces) and does not set the flag for any front buffer or proxy surface (that is, non-optional surface).

If DXGI\_DDI\_PRIMARY\_OPTIONAL is set for a back buffer, the driver can set the DXGI\_DDI\_PRIMARY\_DRIVER\_FLAG\_NO\_SCANOUT flag. For more information about setting this flag, see [Passing DXGI Information at Resource Creation Time](passing-dxgi-information-at-resource-creation-time.md). If the driver sets DXGI\_DDI\_PRIMARY\_DRIVER\_FLAG\_NO\_SCANOUT for an optional buffer, it has no effect other than to cause DXGI to call the driver's [**PresentDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff569179) function with the **Blt** flag set instead of with the **Flip** flag set.

If DXGI\_DDI\_PRIMARY\_OPTIONAL is not set for a front buffer or the proxy surface, the driver can still opt out of scan-out by failing the resource creation call with error code DXGI\_DDI\_ERR\_UNSUPPORTED and setting DXGI\_DDI\_PRIMARY\_DRIVER\_FLAG\_NO\_SCANOUT.

**Note**   Failing the create call without setting DXGI\_DDI\_PRIMARY\_DRIVER\_FLAG\_NO\_SCANOUT is reserved for real failure cases, like out of memory.

 

DXGI exploits this opt-out methodology when it attempts to create a full-screen presentation chain for an MSAA or rotated back buffer. If the driver will not scan-out any or both of these types, the driver will opt out. DXGI will then attempt to create a non-rotated surface, a non-MSAA surface, or both until the driver accepts the resource creation. Therefore, DXGI will fall back progressively until the non-optional surface exactly matches the front buffer format, sample count, rotation, and size.

If the driver opts out of any non-optional surface, DXGI still must have a way to move bits from the back buffer to the primary surface. Consequently, if the driver opts out of scan-out for MSAA and rotation, the driver opts in to resolving, rotating, or both when DXGI calls the driver's [**BltDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff538252) function. When the driver opts out, DXGI will create a proxy surface and call **BltDXGI** to move data from the back buffers to that proxy surface. The driver should have no reason to opt-out of this proxy surface because the proxy exactly matches the front buffer.

The following unusual situations occur when the application does not re-create its surfaces after a transition either into or out of full-screen mode:

-   If the application does not re-create its surfaces when it goes into full-screen mode, DXGI determines that the back buffers do not match the front buffer, even if they really do match on format, size, rotation, and sample count. The reason for this determination is that the operating system requires back buffers to be tagged for scan-out to a particular monitor when those buffers are created. Windowed back buffers cannot yet be definitively assigned to a particular monitor because the monitor is chosen dynamically when full screen is entered. Therefore, DXGI must not send these back buffers to the driver for scan-out (through a flip operation). Applications of this type typically force DXGI to create the proxy surface.

-   If the application does not re-create its back buffers when it returns to windowed mode, DXGI might call the driver's [**BltDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff538252) or [**PresentDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff569179) (with **Blt** set) to perform a bitblt on a surface that was previously created for a flip operation. This situation should not be an issue but is mentioned here for completeness. Note that DXGI always destroys the proxy surface when the application transitions to windowed mode.

Also, note that applications can resize their back buffers dynamically while the applications are in full-screen mode. This action causes the logic that is described in the preceding situations to occur again. Therefore, the proxy surface might be created and destroyed, and opting out might or might not be required over time even though the application remains in full-screen mode. The application can also transfer its output to another monitor dynamically without leaving full-screen mode. Therefore, the application incurs a switch back to bitblt mode because the application's back buffers were tagged for a different monitor.

Finally, you should be aware of the situation that occurs with respect to MSAA back buffers if the driver does not opt out of MSAA scan-out. In this situation, the driver opts in the scan-out of MSAA. Therefore, DXGI interchanges the MSAA back buffer and MSAA front buffer through flip operations, and performs a resolve operation by what is equivalent to the digital-to-analog converter (DAC). In this situation, the application can resize its back buffers dynamically while in full-screen mode, which forces DXGI to switch to calling the driver's [**BltDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff538252) function. Because the MSAA characteristics of the back buffer and front buffer still match, DXGI will specify that the driver perform a non-resolving, possibly color-converting, stretch bitblt. The driver should then replicate, without resolve, multisamples to the front buffer, which is necessary if a driver chooses to scan-out MSAA.

 

 





