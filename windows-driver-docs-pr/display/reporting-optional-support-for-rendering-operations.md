---
title: Reporting Optional Support for Rendering Operations
description: Reporting Optional Support for Rendering Operations
ms.assetid: 97a0b8c6-7ff8-47df-97df-4e9714ebc903
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting Optional Support for Rendering Operations


## <span id="ddk_introduction_to_command_and_dma_buffers_gg"></span><span id="DDK_INTRODUCTION_TO_COMMAND_AND_DMA_BUFFERS_GG"></span>


Beginning with Windows 7, a display miniport driver can set additional members in the [**DXGK\_PRESENTATIONCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562004) structure to indicate certain rendering operations that the driver can or cannot support.

For further information about available rendering capability settings, see [**DXGK\_PRESENTATIONCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562004).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Optional%20Support%20for%20Rendering%20Operations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




