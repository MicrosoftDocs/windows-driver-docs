---
title: Bug Check 0x1D3 WFP_INVALID_OPERATION 
description: The WFP_INVALID_OPERATION  bug check has a value of 0x000001D3.
keywords: ["Bug Check 0x1D3 WFP_INVALID_OPERATION",  "WFP_INVALID_OPERATION"]
ms.date: 05/23/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- WFP_INVALID_OPERATION 
api_type:
- NA
---

# Bug Check 0x1D3: WFP_INVALID_OPERATION 

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


The WFP_INVALID_OPERATION bug check has a value of 0x000001D3. This indicates that a Windows Filtering Platform callout performed an invalid operation.

## WFP\_INVALID\_OPERATION Parameters

Parameter | Description 
|---------|--------------|
1 | The subtype of the bugcheck.
2 | Reserved
3 | Reserved
4 | Reserved

**Parameter 1 Values**

 0x1 : Callout injected an NBL with multiple NET_BUFFERS inbound.

 2 - Reserved.

 3 - Pointer to NBL.

 4 - Reserved.


## Resolution
The [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be very helpful in determining the root cause.

 




