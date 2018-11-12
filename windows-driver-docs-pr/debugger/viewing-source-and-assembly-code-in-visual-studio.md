---
title: Source Code Debugging in Visual Studio
description: The procedure covers Source Code Debugging in Visual Studio.
ms.assetid: C2E5BAA8-913A-4B0E-8ADF-E2758CCFEC84
ms.author: domars
ms.date: 05/11/2018
ms.localizationpriority: medium
---

# Source Code Debugging in Visual Studio

> [!IMPORTANT]
> This feature is not available in Windows 10, version 1507 and later versions of the WDK.
>

The procedures shown in this topic require that you have the Windows Driver Kit integrated into Visual Studio. To get the integrated environment, first install Microsoft Visual Studio, and then install the Windows Driver Kit (WDK). For more information, see [Windows Driver Development](https://msdn.microsoft.com/library/windows/hardware/ff557573).

To use source debugging, you must have your compiler or linker create symbol files (.pdb files) when the binaries are built. These symbol files show the debugger how the binary instructions correspond to the source lines. Also, the debugger must be able to access the actual source files. For more information, see [Source Path](source-path.md).

When you break in to the target computer, or when code running on the target computer hits a breakpoint, Visual Studio displays source code if it can find the source file. You can step through the source code by choosing one of the **Step** commands from the **Debug** menu. You can also set breakpoints by clicking in the left column of the source window. The following screen shot shows a source code window in the Visual Studio debugger.

![screen shot of source code in the visual studio debugger](images/sourcecodedebuggingvs01.png)

 

 





