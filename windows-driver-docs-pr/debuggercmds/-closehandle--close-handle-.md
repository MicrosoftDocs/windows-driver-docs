---
title: .closehandle (Close Handle)
description: The .closehandle command closes a handle owned by the target application.
keywords: [".closehandle (Close Handle) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .closehandle (Close Handle)
api_type:
- NA
---

# .closehandle (Close Handle)


The **.closehandle** command closes a handle owned by the target application.

```dbgsyntax
.closehandle Handle 
.closehandle -a 
```

## <span id="ddk_meta_close_handle_dbg"></span><span id="DDK_META_CLOSE_HANDLE_DBG"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
Specifies the handle to be closed.

<span id="_______-a______"></span><span id="_______-A______"></span> **-a**   
Causes all handles owned by the target application to be closed.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes | user mode only |
|Targets | live debugging only |
|Platforms | all  |
 

## Remarks

You can use the [**!handle**](-handle.md) extension to display the existing handles.

 

 





