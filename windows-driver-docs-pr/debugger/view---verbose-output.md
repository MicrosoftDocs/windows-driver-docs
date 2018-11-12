---
title: View Verbose Output
description: View Verbose Output
ms.assetid: 728cf574-30ec-4e30-b951-2d9997d8defe
keywords: ["View Verbose Output"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# View | Verbose Output


## <span id="ddk_view_verbose_output_dbg"></span><span id="DDK_VIEW_VERBOSE_OUTPUT_DBG"></span>


Click **Verbose Output** on the **View** menu to turn verbose mode on and off.

This command is equivalent to pressing CTRL+ALT+V. (and to pressing CTRL+V in KD).

When verbose mode is turned on, some display commands (such as register dumping) produce more detailed output. Every MODULE LOAD operation that is sent to the debugger is displayed. And every time that a driver or DLL is loaded by the operating system, the debugger is notified.

 

 





