---
title: C28715
description: Warning C28715 Cast between semantically different integer types.
ms.date: 04/20/2017
ms.localizationpriority: medium 
f1_keywords: 
  - "C28715"
---

# C28715


warning C28715: Cast between semantically different integer types

This warning indicates that a Boolean is being cast to **NTSTATUS**. This is likely to give undesirable results. For example, the typical failure value for functions that return a Boolean (**FALSE**) is a success status when tested as an **NTSTATUS**.

Typically, a function that returns Boolean returns either 1 (for **TRUE**) or 0 (for **FALSE**). Both these values are treated as success codes by the **NT\_SUCCESS** macro. Thus, the failure case will never be detected.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

PREfast reports the warning for the following example.

```
extern BOOL SomeFunction(void);

if (NT_SUCCESS(SomeFunction())) {
   return 0;
} else {
   return -1;
}
```

The following example avoids the error.

```
extern BOOL SomeFunction(void);

if (SomeFunction() == TRUE) {
   return 0;
} else {
   return -1;
}
```

 

 





