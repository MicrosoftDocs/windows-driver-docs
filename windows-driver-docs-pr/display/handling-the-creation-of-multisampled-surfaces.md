---
title: Handling the Creation of Multisampled Surfaces
description: Handling the Creation of Multisampled Surfaces
ms.assetid: 78557c9d-b741-4eb9-b8e2-56387cad80c4
keywords: ["DirectX 8.0 release notes WDK Windows 2000 display , multisample rendering, creating", "multisample rendering WDK DirectX 8.0 , creating", "rendering multisamples WDK DirectX 8.0 , creating"]
---

# Handling the Creation of Multisampled Surfaces


## <span id="ddk_handling_the_creation_of_multisampled_surfaces_gg"></span><span id="DDK_HANDLING_THE_CREATION_OF_MULTISAMPLED_SURFACES_GG"></span>


When a multisampled surface is being created, the number of samples can be found in the **ddsCapsEx.dwCaps3** of the [**DD\_SURFACE\_MORE**](https://msdn.microsoft.com/library/windows/hardware/ff551737) structure. This field holds one of the values of the enumerated type D3DMULTISAMPLE\_TYPE. It is not a bitfield like **wFlipMSTypes** or **wBltMSTypes**. If a surface is not multisampled, **dwCaps3** has the value D3DMULTISAMPLE\_NONE (0).

When determining whether a creation request for a multisample surface can be satisfied or not, the driver should not take into account the current value of the D3DRS\_MULTISAMPLEANTIALIAS render state. It is not permissible for a driver to fail a request to set D3DRS\_MULTISAMPLEANTIALIAS **FALSE**. Therefore, any restriction that affects the ability to perform multisample rendering should be enforced at context create time even if D3DRS\_MULTISAMPLEANTIALIAS is **FALSE** at that time.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Handling%20the%20Creation%20of%20Multisampled%20Surfaces%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




