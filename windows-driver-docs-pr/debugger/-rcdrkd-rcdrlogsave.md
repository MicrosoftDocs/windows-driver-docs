---
title: rcdrkd.rcdrlogsave
description: The rcdrkd.rcdrlogsave extension saves the recorder buffers of a driver.
ms.assetid: 2A79064C-A899-4351-A8A6-D8DF31CF9A17
keywords: ["rcdrkd.rcdrlogsave Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- rcdrkd.rcdrlogsave
api_type:
- NA
ms.localizationpriority: medium
---

# !rcdrkd.rcdrlogsave


The **!rcdrkd.rcdrlogsave** extension saves the recorder buffers of a driver.

```dbgcmd
!rcdrkd.rcdrlogsave DriverName [CaptureFilename ]
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DriverName______"></span><span id="_______drivername______"></span><span id="_______DRIVERNAME______"></span> *DriverName*   
The name of the driver, not including the .sys extension.

<span id="_______CaptureFileName______"></span><span id="_______capturefilename______"></span><span id="_______CAPTUREFILENAME______"></span> *CaptureFileName*   
The name of the file (not including the .etl extension) in which to save the recorder buffers. If *CaptureFileName* is not specified, the recorder buffers are saved in *DriverName*.etl.

## <span id="DLL"></span><span id="dll"></span>DLL


Rcdrkd.dll

## <span id="see_also"></span>See also


[RCDRKD Extensions](rcdrkd-extensions.md)

 

 






