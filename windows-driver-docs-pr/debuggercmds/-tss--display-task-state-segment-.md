---
title: ".tss (Display Task State Segment)"
description: "The .tss command displays a formatted view of the saved Task State Segment (TSS) information for the current processor."
keywords: ["Display Task State Segment (.tss) command", "task state segment (TSS)", "TSS (task state segment)", ".tss (Display Task State Segment) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .tss (Display Task State Segment)
api_type:
- NA
---

# .tss (Display Task State Segment)

The **.tss** command displays a formatted view of the saved Task State Segment (TSS) information for the current processor.

```dbgcmd
.tss [Address]
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Address of the TSS.

## Environment

| Item      | Description      |
|-----------|------------------|
| Modes     | kernel mode only |
| Targets   | live, crash dump |
| Platforms | x86 only         |

## Remarks

The address of the TSS can be found by examining the output of the [**!pcr**](-pcr.md) extension.
