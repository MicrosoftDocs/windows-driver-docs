---
title: WIA Microdriver Commands
description: WIA Microdriver Commands
ms.assetid: 54d0c35b-d8b3-4e38-85cf-d5b4f80f6daa
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





