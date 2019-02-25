---
title: How do I change the prefix output on every trace line
description: How do I change the prefix output on every trace line
ms.assetid: be2b6207-79f5-4d71-a6a2-075f3078a873
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I change the prefix output on every trace line?


Use the following command to change the prefix output on every trace line:

```
set TRACE_FORMAT_PREFIX=[%9!d!]%8!04X!.%3!04X!::%4!s! [%1!s!] 
tracefmt -f mytracefile 
```

For information about the TRACE\_FORMAT\_PREFIX parameters, see the [Trace Message Prefix](trace-message-prefix.md) topic.









