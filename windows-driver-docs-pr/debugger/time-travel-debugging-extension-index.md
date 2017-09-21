---
title: !index
description: The !index extension indexes time travel traces or displays index status information.
keywords: ["index Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 09/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- index
api_type:
- NA
---

# ![Small logo on windbg preview](images/windbgx-preview-logo.png) !index

The **!index** extension indexes time travel traces or displays index status information.

```
!index [-status] [-force] 
```


Use ```!index``` to run an indexing pass over the current trace. 

```
0:000> !index
Indexed 10/14 keyframes
Indexed 14/14 keyframes
Successfully created the index in 535ms.
```

If the current trace is already indexed, the !index command does nothing.

```
0:000> !index
Successfully created the index in 0ms.
```



## <span id="ddk__analyze_dbg"></span><span id="DDK__ANALYZE_DBG"></span>Parameters

**-status**

Use ```!index -status``` to report the status of the trace index.

```
0:000> !tt.index -status
Index file loaded.
```
**-force**

Use ```!index -force``` to reindex the trace even if an an unloadable index file exists on disk.

??? TBD Output look right - Wasn't able to properly test 

```
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

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!analyze%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




