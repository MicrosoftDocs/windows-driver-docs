---
title: C28129 warning
description: Warning C28129 An assignment has been made to an operand, which should only be modified using bit sets and clears.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
f1_keywords: 
  - "C28129"
---

# C28129


warning C28129: An assignment has been made to an operand, which should only be modified using bit sets and clears

The driver is using an assignment to modify an operand. Assigning a value might unintentionally change the values of bits other than those that it needs to change, resulting in unexpected consequences.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
fdo->Flags = DO_BUFFERED_IO;
```

The following code example avoids this warning.

```
fdo->Flags |= DO_BUFFERED_IO;
```

 

 





