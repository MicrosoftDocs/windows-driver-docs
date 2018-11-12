---
title: .continue
description: The .continue token behaves like the continue keyword in C.
ms.assetid: c8f6c69c-d912-4ce4-a9c2-d82c349484a9
keywords: [".continue Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .continue
api_type:
- NA
ms.localizationpriority: medium
---

# .continue


The **.continue** token behaves like the **continue** keyword in C.

```dbgsyntax
.for (...) { ... ; .if (Condition) .continue ; ... } 

.while (...) { ... ; .if (Condition) .continue ; ... } 

.do { ... ; .if (Condition) .continue ; ... } (...) 
```

## <span id="ddk_token_continue_dbg"></span><span id="DDK_TOKEN_CONTINUE_DBG"></span>


### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about other control flow tokens and their use in debugger command programs, see [Using Debugger Command Programs](using-debugger-command-programs.md).

Remarks
-------

The **.continue** token can be used within any [**.for**](-for.md), [**.while**](-while.md), or [**.do**](-do.md) loop.

Since there is no control flow token equivalent to the C goto statement, you will usually use the **.continue** token within an [**.if**](-if.md) conditional, as shown in the syntax examples above. However, this is not actually required.

 

 





