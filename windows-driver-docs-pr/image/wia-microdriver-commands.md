---
title: WIA Microdriver Commands
description: WIA Microdriver Commands
ms.assetid: 54d0c35b-d8b3-4e38-85cf-d5b4f80f6daa
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Microdriver Commands


## <span id="ddk_wia_microdriver_commands_si"></span><span id="DDK_WIA_MICRODRIVER_COMMANDS_SI"></span>


The following set of constants form the set of WIA microdriver commands. The commands are passed to the microdriver from the WIA Flatbed driver in the *lCommand* parameter of the [**MicroEntry**](https://msdn.microsoft.com/library/windows/hardware/ff545248) function. The commands are grouped into the following categories:

-   [Automatic Document Feeder Commands](automatic-document-feeder-commands.md)

    Commands for microdrivers that support an automatic document feeder (ADF).

-   [Event Commands](event-commands.md)

    Commands for microdriver event support.

-   [Required Commands](required-commands.md)

    Commands that must be implemented by the microdriver.

-   [Optional Commands](optional-commands.md)

    Commands that can be implemented by the microdriver as enhancements to its basic operation.

These commands are defined in *Wiamicro.h*, and are available in Windows Me and in Windows XP and later.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Microdriver%20Commands%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




