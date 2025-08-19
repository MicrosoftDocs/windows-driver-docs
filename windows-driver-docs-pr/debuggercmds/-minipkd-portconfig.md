---
title: "!minipkd.portconfig"
description: "The !minipkd.portconfig extension displays information about the specified PORT_CONFIGURATION_INFORMATION data structure."
keywords: ["minipkd.portconfig Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- minipkd.portconfig
api_type:
- NA
---

# !minipkd.portconfig


The **!minipkd.portconfig** extension displays information about the specified PORT\_CONFIGURATION\_INFORMATION data structure.

```dbgcmd
!minipkd.portconfig PortConfig 
```

## Parameters


<span id="_______PortConfig______"></span><span id="_______portconfig______"></span><span id="_______PORTCONFIG______"></span> *PortConfig*   
Specifies the address of a PORT\_CONFIGURATION\_INFORMATION data structure.

## DLL

Minipkd.dll

 

## Additional Information

For more information, see [SCSI Miniport Debugging](../debugger/scsi-miniport-debugging.md).

## Remarks

The *PortConfig* address can be found in the **Port Config Info** field of the [**!minipkd.adapter**](-minipkd-adapter.md) display.

