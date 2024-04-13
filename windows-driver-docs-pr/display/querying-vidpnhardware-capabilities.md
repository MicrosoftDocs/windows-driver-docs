---
title: Querying VidPN Hardware Capabilities
description: Querying VidPN Hardware Capabilities
keywords:
- VidPN WDK display , hardware capabilities
ms.date: 04/20/2017
---

# Querying VidPN Hardware Capabilities


Beginning in Windows 7, display miniport drivers are required to report all hardware capabilities of a specified functional VidPN. Drivers should support the following callback function and its associated structures:

-   [**DxgkDdiQueryVidPnHWCapability**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryvidpnhwcapability) function

-   [**DXGKARG\_QUERYVIDPNHWCAPABILITY**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_queryvidpnhwcapability) structure

-   [**D3DKMDT\_VIDPN\_HW\_CAPABILITY**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_hw_capability) structure

When the driver reports the hardware capabilities, it should consider cloning to be an implicit procedure that is done as part of rotation or scaling transformations: a source must first be cloned before it can be rotated or scaled.

If any of the members of D3DKMDT\_VIDPN\_HW\_CAPABILITY have no meaning on the specified VidPN path, the display mode manager (DMM) will not report any errors if the members are set to nonzero values. DMM will clear all such values before reporting them to the user-mode client. However, the driver is required to set the value of the **Reserved** member of D3DKMDT\_VIDPN\_HW\_CAPABILITY to 0.

### <span id="example_scenario"></span><span id="EXAMPLE_SCENARIO"></span>**Example Scenario**

To show how the display miniport driver should report hardware capabilities, consider the following example set of hardware configurations P1, P2, and P3:

-   **P1:** Surface is cloned from Source S1, then rotated 90 degrees and scaled to fit the target.

-   **P2:** Surface is cloned from Source S1, with no applied transformation.

-   **P3:** Source S2 has no applied transformation.

When [**DxgkDdiQueryVidPnHWCapability**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryvidpnhwcapability) is called, the driver should return values for the rotation, scaling, and cloning members of [**D3DKMDT\_VIDPN\_HW\_CAPABILITY**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_hw_capability) according to the following table:

Returned Values for Members of D3DKMDT\_VIDPN\_HW\_CAPABILITY
Hardware Capabilities
VidPN Path
DriverRotation
DriverScaling
DriverCloning
Hardware can perform all rotation, scaling, and cloning transformations.

P₁

0

0

0

P₂

0

0

0

P₃

0

0

0

Hardware can perform all transformations except cloning

P₁

0

0

0

P₂

0

0

1

P₃

0

0

0

Hardware can perform cloning and scaling transformations, but not rotation. Driver performs rotation using an intermediate rotation blit.

P₁

1

0

0

P₂

0

0

0

P₃

0

0

0

Hardware cannot perform cloning, scaling, or rotation transformations. These operations are performed by the driver.

P₁

1

1

0

P₂

0

0

1

P₃

0

0

0

 

 

