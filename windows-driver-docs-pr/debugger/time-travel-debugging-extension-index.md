---
title: Time Travel Debugging Extension !index Command
description: The !index extension indexes time travel traces or displays index status information.
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

#  !index

![Small time travel logo showing clock](images/ttd-time-travel-debugging-logo.png)

The **!index** extension indexes time travel traces or displays index status information.

```dbgsyntax
!index [-status] [-force] 
```


Use `!index` to run an indexing pass over the current trace. 

```dbgcmd
0:000> !index
Indexed 10/14 keyframes
Indexed 14/14 keyframes
Successfully created the index in 535ms.
```

If the current trace is already indexed, the !index command does nothing.

```dbgcmd
0:000> !index
Successfully created the index in 0ms.
```



## <span id="ddk__analyze_dbg"></span><span id="DDK__ANALYZE_DBG"></span>Parameters

**-status**

Use `!index -status` to report the status of the trace index.

```dbgcmd
0:000> !tt.index -status
Index file loaded.
```
**-force**

Use `!index -force` to reindex the trace even if an unloadable index file exists on disk.

```dbgcmd
0:000> !tt.index -force
Successfully created the index in 152ms.
```


### <span id="DLL"></span><span id="dll"></span>DLL

ttdext.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

This extension only works with time travel traces. For more information about time travel, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).


## See Also

[Time Travel Debugging - Extension Commands](time-travel-debugging-extension-commands.md)


-------

 





