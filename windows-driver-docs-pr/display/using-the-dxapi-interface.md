---
title: Using the DxApi Interface
description: Using the DxApi Interface
ms.assetid: 9de96d20-6cfc-42e7-821b-8256e0dd9b38
keywords: ["drawing kernel-mode video transport WDK DirectDraw , DxApi interface", "DirectDraw kernel-mode video transport WDK Windows 2000 display , DxApi interface", "kernel-mode video transport WDK DirectDraw , DxApi interface", "video transport kernel-mode WDK DirectDraw , DxApi interface", "DxApi interface WDK DirectDraw", "video capture WDK video transport kernel-mode"]
---

# Using the DxApi Interface


## <span id="ddk_using_the_dxapi_interface_gg"></span><span id="DDK_USING_THE_DXAPI_INTERFACE_GG"></span>


As described in [Using Kernel-Mode Video Transport](using-kernel-mode-video-transport.md), a video capture driver (hardware decoder) must call the [**DxApi**](https://msdn.microsoft.com/library/windows/hardware/ff557364) function to access the DxApi interface. As described in [VPE and Kernel-Mode Video Transport Architecture](vpe-and-kernel-mode-video-transport-architecture.md), a [video miniport driver](video-miniport-drivers-in-the-windows-2000-display-driver-model.md) implements the DxApi interface on Windows 2000 and later platforms. The following section describes how the DxApi interface is supported on these platforms:

[DxApi Miniport Driver Functions For Windows 2000 and Later](dxapi-miniport-driver-functions-for-windows-2000-and-later.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20the%20DxApi%20Interface%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




