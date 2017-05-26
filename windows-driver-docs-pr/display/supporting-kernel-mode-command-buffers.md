---
title: Supporting Kernel-Mode Command Buffers
description: Supporting Kernel-Mode Command Buffers
ms.assetid: c61a39b3-6fd6-461f-a68f-450ccd705f6f
keywords:
- command buffer WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Kernel-Mode Command Buffers


## <span id="ddk_introduction_to_command_and_dma_buffers_gg"></span><span id="DDK_INTRODUCTION_TO_COMMAND_AND_DMA_BUFFERS_GG"></span>


The display miniport driver should submit a command buffer in response to a call to the [**DxgkDdiRenderKm**](https://msdn.microsoft.com/library/windows/hardware/ff559800) function as described in [Submitting a Command Buffer](submitting-a-command-buffer.md).

The driver can use the **MultipassOffset** member of the [**DXGKARG\_RENDER**](https://msdn.microsoft.com/library/windows/hardware/ff557648) structure to track the progress of input command buffer processing. For example, the display miniport driver can use the high 16 bits as an offset to the last processed command, and the low 16 bits to track the processing of the command.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Kernel-Mode%20Command%20Buffers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




