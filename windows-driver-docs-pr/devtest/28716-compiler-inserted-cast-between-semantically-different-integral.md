---
title: C28716 Warning
description: Warning C28716 Compiler-inserted cast between semantically different integral types.
ms.date: 04/20/2017
f1_keywords: 
  - "C28716"
---

# C28716


warning C28716: Compiler-inserted cast between semantically different integral types

This warning indicates that a Boolean is being used as an **NTSTATUS** without being explicitly cast. This is likely to give undesirable results. For instance, the typical failure value for functions that return a Boolean (false) indicates a success status when tested as an **NTSTATUS**.

### <span id="example"></span><span id="EXAMPLE"></span>Example

PREfast reports the warning for the following example.

```
extern bool SomeMemAllocFunction(void **);

return SomeMemAllocFunction(&MyPtr);
```

The following example avoids the error.

```
extern bool SomeMemAllocFunction(void **);

if (SomeMemAllocFunction(&MyPtr) == true) {
 return STATUS_SUCCESS;
} else {
 return STATUS_NO_MEMORY;
}
```

