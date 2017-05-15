---
title: Introduction to the AMLI Debugger
description: Introduction to the AMLI Debugger
ms.assetid: f210171c-2226-4bd6-bbb4-aee4b087e575
keywords: ["AMLI Debugger, overview", "ACPI debugging, machine language", "AML interpreter"]
---

# Introduction to the AMLI Debugger


## <span id="ddk_introduction_to_the_amli_debugger_dbg"></span><span id="DDK_INTRODUCTION_TO_THE_AMLI_DEBUGGER_DBG"></span>


There are significant differences between debugging standard kernel-mode code and debugging an ACPI (Advanced Configuration and Power Interface) BIOS.

Whereas Windows and its drivers are composed of binary machine code compiled for a specific processor, the core of an ACPI BIOS is not in machine code. Rather, it is stored as ACPI Machine Language (AML) and is processed by the Microsoft AML interpreter as it is run.

The Microsoft AMLI Debugger is a special debugging tool that can debug AML code. The AMLI Debugger is not actually a free-standing program. Rather, it consists of two components. One component is the checked build of the Microsoft Windows ACPI driver (Acpi.sys). The other component is located in certain debugger extensions included in the Debugging Tools for Windows package.

On Windows XP and later versions of Windows, the AMLI Debugger is completely 64-bit aware. No matter what processor is being used by the target computer or the host computer, the AMLI Debugger will function correctly.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Introduction%20to%20the%20AMLI%20Debugger%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




