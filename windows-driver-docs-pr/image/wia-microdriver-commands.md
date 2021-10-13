---
title: WIA Microdriver Commands
description: WIA Microdriver Commands
ms.date: 10/05/2021
ms.localizationpriority: medium
---

# WIA Microdriver Commands

The following set of constants form the set of WIA microdriver commands. The commands are passed to the microdriver from the WIA Flatbed driver in the *lCommand* parameter of the [**MicroEntry**](/windows-hardware/drivers/ddi/wiamicro/nf-wiamicro-microentry) function. The commands are grouped into the following categories:

- [Automatic Document Feeder Commands](automatic-document-feeder-commands.md)

    Commands for microdrivers that support an automatic document feeder (ADF).

- [Event Commands](event-commands.md)

    Commands for microdriver event support.

- [Required Commands](required-commands.md)

    Commands that must be implemented by the microdriver.

- [Optional Commands](optional-commands.md)

    Commands that can be implemented by the microdriver as enhancements to its basic operation.

These commands are defined in *Wiamicro.h*.
