---
title: "!asd (WinDbg)"
description: "The !asd extension displays a specified number of failure analysis entries from the data cache, starting at the specified address."
keywords: ["failure analysis entries, display from data cache", "!asd Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- asd
api_type:
- NA
---

# !asd


The **!asd** extension displays a specified number of failure analysis entries from the data cache, starting at the specified address.

```dbgcmd
    !asd Address DataUsed
```

## Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the first failure analysis entry to display.

<span id="_______DataUsed______"></span><span id="_______dataused______"></span><span id="_______DATAUSED______"></span> *DataUsed*   
Determines the number of tokens to display.

## DLL


Ext.dll



 

## Additional Information

You can use the [**!dumpfa**](-dumpfa.md) extension to debug the [**!analyze**](-analyze.md) extension.

## Remarks

The **!asd** extension is useful only when you are debugging the [**!analyze**](-analyze.md) extension.

