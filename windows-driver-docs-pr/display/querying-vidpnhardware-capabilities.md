---
title: Querying VidPN Hardware Capabilities
description: Querying VidPN Hardware Capabilities
ms.assetid: fb7939bb-ff7e-4ba8-b801-ac10010c44b7
keywords:
- VidPN WDK display , hardware capabilities
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Querying VidPN Hardware Capabilities


Beginning in Windows 7, display miniport drivers are required to report all hardware capabilities of a specified functional VidPN. Drivers should support the following callback function and its associated structures:

-   [**DxgkDdiQueryVidPnHWCapability**](https://msdn.microsoft.com/library/windows/hardware/ff559771) function

-   [**DXGKARG\_QUERYVIDPNHWCAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/ff557628) structure

-   [**D3DKMDT\_VIDPN\_HW\_CAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/ff546639) structure

When the driver reports the hardware capabilities, it should consider cloning to be an implicit procedure that is done as part of rotation or scaling transformations: a source must first be cloned before it can be rotated or scaled.

If any of the members of D3DKMDT\_VIDPN\_HW\_CAPABILITY have no meaning on the specified VidPN path, the display mode manager (DMM) will not report any errors if the members are set to nonzero values. DMM will clear all such values before reporting them to the user-mode client. However, the driver is required to set the value of the **Reserved** member of D3DKMDT\_VIDPN\_HW\_CAPABILITY to 0.

### <span id="example_scenario"></span><span id="EXAMPLE_SCENARIO"></span>**Example Scenario**

To show how the display miniport driver should report hardware capabilities, consider the following example set of hardware configurations P1, P2, and P3:

-   **P1:** Surface is cloned from Source S1, then rotated 90 degrees and scaled to fit the target.

-   **P2:** Surface is cloned from Source S1, with no applied transformation.

-   **P3:** Source S2 has no applied transformation.

When [**DxgkDdiQueryVidPnHWCapability**](https://msdn.microsoft.com/library/windows/hardware/ff559771) is called, the driver should return values for the rotation, scaling, and cloning members of [**D3DKMDT\_VIDPN\_HW\_CAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/ff546639) according to the following table:

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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Querying%20VidPN%20Hardware%20Capabilities%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




