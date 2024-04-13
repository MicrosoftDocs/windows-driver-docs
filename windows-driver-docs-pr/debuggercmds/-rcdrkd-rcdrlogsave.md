---
title: "!rcdrkd.rcdrlogsave"
description: "The !rcdrkd.rcdrlogsave extension saves the recorder buffers of a driver."
keywords: ["!rcdrkd.rcdrlogsave Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- rcdrkd.rcdrlogsave
api_type:
- NA
---

# !rcdrkd.rcdrlogsave

The **!rcdrkd.rcdrlogsave** extension saves the recorder buffers of a driver.

```dbgcmd
!rcdrkd.rcdrlogsave DriverName [CaptureFilename ]
```

## Parameters

<span id="_______DriverName______"></span><span id="_______drivername______"></span><span id="_______DRIVERNAME______"></span> *DriverName*   
The name of the driver, not including the .sys extension.

<span id="_______CaptureFileName______"></span><span id="_______capturefilename______"></span><span id="_______CAPTUREFILENAME______"></span> *CaptureFileName*   
The name of the file (not including the .etl extension) in which to save the recorder buffers. If *CaptureFileName* is not specified, the recorder buffers are saved in *DriverName*.etl.

## DLL

Rcdrkd.dll

## See also

[RCDRKD Extensions](rcdrkd-extensions.md)
