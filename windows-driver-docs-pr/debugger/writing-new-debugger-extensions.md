---
title: Writing New Debugger Extensions
description: Writing New Debugger Extensions
ms.assetid: 6a0d3478-1c7a-44e0-8e48-1334de228c64
keywords: ["extension commands ( commands), writing extensions", "writing extension commands", "dbgeng.h header file, writing extension commands", "wdbgexts.h header file, writing extension commands"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Writing New Debugger Extensions


## <span id="ddk_writing_new_debugger_extensions_dbg"></span><span id="DDK_WRITING_NEW_DEBUGGER_EXTENSIONS_DBG"></span>


You can create your own debugging commands by writing an extension DLL. For example, you might want to write a command to display a complex data structure, or a command that will stop and start the target depending on the value of certain variables or memory locations.

There are two different types of debugger extensions:

-   *DbgEng extensions*. These are based on the prototypes in the dbgeng.h header file, and also those in the wdbgexts.h header file.

-   *WdbgExts extensions*. These are based on the prototypes in the wdbgexts.h header file alone.

For information about how to write debugger extensions, see [Writing DbgEng Extensions](writing-dbgeng-extensions.md) and [Writing WdbgExts Extensions](writing-wdbgexts-extensions.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Writing%20New%20Debugger%20Extensions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




