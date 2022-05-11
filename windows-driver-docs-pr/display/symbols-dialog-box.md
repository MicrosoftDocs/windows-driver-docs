---
title: Symbols Dialog Box
description: "The Symbols dialog box is used for resolving symbols. "
ms.date: 05/10/2022
---

# Symbols Dialog Box  

The **Symbols** dialog box is used for resolving symbols. If symbols are available, the names of the threads, in GPUView's main window, will be resolved along with function addresses decoded in certain events like **NT - StackWalk** and **NT - DPC**.  

When the dialog is first launched, it looks like the following figure.  

When GPUView processes the events in the trace it is viewing, it reconstructs the Windows build location based on the Windows build number and machine architecture. Externally, this will not be a valid path. In any case, if you know the location of the symbols that GPUView should use to resolve information in the file, enter the path or semicolon-separated paths in the **Path for resolving symbols** control.  

The following diagram is a screen shot showing that GPUView has not used symbols to resolve thread names.  

Notice that the first thread name in the csrss.exe process is winsrv.dll+0x42B0. Viewing the same file with symbols enabled, you get the following.  

Notice that the thread name has changed to winsrv.dll!StartCreateSystemThreads.  

### Resolve Symbols  

To turn on symbol resolution, select the Resolve Symbols check box and then press the **Ok** button. During the processing of the **Ok** button, the symbol changes will be applied. 

### Use Symbol Server  

If **Use Symbol Server** is selected before the **Ok** button is pressed, GPUView uses the standard symbol path to locate symbols. When doing so, it follows the standard symbol lookup that XPerfView.exe does in GPUView's parent directory. For more information, see XPerfView documentation.



 