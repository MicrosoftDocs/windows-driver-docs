---
title: DevCon Dp_delete
description: Deletes a third-party (OEM) driver package from the driver store on the local computer. This command deletes the INF file, the PNF file, and the associated catalog file (.cat).
ms.assetid: bc9d8d66-4aa1-423b-b907-40a8c0194eb1
keywords:
- DevCon Dp_delete Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Dp_delete
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DevCon Dp\_delete


Deletes a third-party (OEM) driver package from the driver store on the local computer. This command deletes the INF file, the PNF file, and the associated catalog file (.cat).

```
    devcon dp_delete [-f] inf
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-f______"></span><span id="_______-F______"></span> **-f**   
This parameter deletes the driver package even if a device is using it at the time.

<span id="_______inf______"></span><span id="_______INF______"></span> *inf*   
The OEM\*.inf file name of the INF file. Windows assigns a file name with this format to the INF file when you add the driver package to the driver store, such as by using [**DevCon dp\_add**](devcon-dp-add.md).

### <span id="comments"></span><span id="COMMENTS"></span>Comments

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon dp_delete oem2.inf
devcon dp_delete oem0.inf -f
```









