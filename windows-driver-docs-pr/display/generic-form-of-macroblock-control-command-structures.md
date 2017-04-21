---
title: Generic Form of Macroblock Control Command Structures
description: Generic Form of Macroblock Control Command Structures
ms.assetid: 44009238-0a8e-4018-9b50-06729640f5e4
keywords:
- macroblocks WDK DirectX VA , generic command structure
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Generic Form of Macroblock Control Command Structures


## <span id="ddk_generic_form_of_macroblock_control_command_structures_gg"></span><span id="DDK_GENERIC_FORM_OF_MACROBLOCK_CONTROL_COMMAND_STRUCTURES_GG"></span>


The following macroblock control structures explicitly defined in *dxva.h* are special cases of a generic design used for macroblock control commands in DirectX VA:

[**DXVA\_MBctrl\_I\_HostResidDiff\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563983)

[**DXVA\_MBctrl\_I\_OffHostIDCT\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563989)

[**DXVA\_MBctrl\_P\_HostResidDiff\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563993)

[**DXVA\_MBctrl\_P\_OffHostIDCT\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563997)

These structures represent only the most commonly used forms of macroblock control commands. Additional macroblock control commands can be created, based upon the design of these existing structures, to allow a driver to support other video decoding elements and to handle different configurations for the decoding process.

This section describes the members of a generic macroblock control command structure that are used as the basis for creating additional macroblock control commands. The macroblock control command structure definition in this section is divided into four parts.

**Note**   Macroblock control commands are aligned with 16-byte memory boundaries and constructed as packed data structures with single-byte alignment packing.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Generic%20Form%20of%20Macroblock%20Control%20Command%20Structures%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




