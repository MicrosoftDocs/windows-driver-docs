---
title: Introduction to the AMLI Debugger
description: Introduction to the AMLI Debugger
ms.assetid: f210171c-2226-4bd6-bbb4-aee4b087e575
keywords: ["AMLI Debugger, overview", "ACPI debugging, machine language", "AML interpreter"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Introduction to the AMLI Debugger


## <span id="ddk_introduction_to_the_amli_debugger_dbg"></span><span id="DDK_INTRODUCTION_TO_THE_AMLI_DEBUGGER_DBG"></span>


There are significant differences between debugging standard kernel-mode code and debugging an ACPI (Advanced Configuration and Power Interface) BIOS.

Whereas Windows and its drivers are composed of binary machine code compiled for a specific processor, the core of an ACPI BIOS is not in machine code. Rather, it is stored as ACPI Machine Language (AML) and is processed by the Microsoft AML interpreter as it is run.

The Microsoft AMLI Debugger is a special debugging tool that can debug AML code. The AMLI Debugger is not actually a free-standing program. Rather, it consists of two components. One component is the checked build of the Microsoft Windows ACPI driver (Acpi.sys). The other component is located in certain debugger extensions included in the Debugging Tools for Windows package.

On Windows XP and later versions of Windows, the AMLI Debugger is completely 64-bit aware. No matter what processor is being used by the target computer or the host computer, the AMLI Debugger will function correctly.

 

 





