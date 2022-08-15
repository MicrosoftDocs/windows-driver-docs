---
title: No Header Information Available
description: No Header Information Available
keywords: ["No header information available (warning)", "header information not available (warning)"]
ms.date: 05/23/2017
---

# No Header Information Available


## <span id="ddk_no_header_information_available_dbg"></span><span id="DDK_NO_HEADER_INFORMATION_AVAILABLE_DBG"></span>


The debugger identifies the proper symbols by examining the headers of the relevant modules. If these module headers are paged out, the debugger (and the symbol server) are unable to find the proper symbols. When this occurs, "No Header Information Available" is displayed within the symbol error message.

For information about how to debug a target when module headers are paged out, see [Reading Symbols from Paged-Out Headers](reading-symbols-from-paged-out-headers.md).

 

 





