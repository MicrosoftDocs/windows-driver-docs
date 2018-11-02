---
title: Time Travel Debugging Extension !positions Command 
description: The !positions extension displays all the active threads, including their current positions.
keywords: ["positions Windows Debugging"]
ms.author: domars
ms.date: 09/21/2017
ms.localizationpriority: medium
---

![Small time travel logo showing clock](images/ttd-time-travel-debugging-logo.png) 

# !positions


The **!positions** extension displays all the active threads, including their current positions in the time travel trace.


```dbgcmd
!postions 
```


## <span id="ddk__analyze_dbg"></span><span id="DDK__ANALYZE_DBG"></span>Parameters

None


## Example

This output shows four threads. Thread 3824 is the current thread indicated by **>** in the left column.

```dbgcmd
0:000> !positions
>Thread ID=0x3824 - Position: F:0
 Thread ID=0x2684 - Position: A5:0
 Thread ID=0x2478 - Position: 200:0
 Thread ID=0x2DC4 - Position: 401:0
```


### <span id="DLL"></span><span id="dll"></span>DLL

ttdext.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

This extension only works with time travel traces. For more information about time travel, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).


## See Also

[Time Travel Debugging - Extension Commands](time-travel-debugging-extension-commands.md)


 

 





