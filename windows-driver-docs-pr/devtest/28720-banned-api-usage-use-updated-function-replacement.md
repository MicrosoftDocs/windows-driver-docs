---
title: C28720 warning
description: Warning C28720 Banned API Usage.
ms.date: 04/20/2017
f1_keywords: 
  - "C28720"
---

# C28720


**Warning C28720: IsBadXXXPtr API Usage**\
Example output: ```Banned API Usage: *function name* is insecure and has been marked deprecated.```

Using one of these APIs indicates that you are testing to see if memory is mapped, which implies that you either don't own the memory at all (so you shouldn't be trying to access it), or it indicates a need for better object lifetime management (if you need to test if something still exists). For more information on the latter, see [Object Lifetime and Resource Management (RAII)](/cpp/cpp/object-lifetime-and-resource-management-modern-cpp?view=msvc-170). 
There are no 1:1 replacement APIs for this rule. Instead, we recommend reevaluating your code to avoid the need to utilize these functions. 

## Banned Functions
| Banned API |
| -----------|
|```IsBadCodePtr```|
|```IsBadHugeReadPtr```|
|```IsBadHugeWritePtr```|
|```IsBadReadPtr```|
|```IsBadStringPtr```|
|```IsBadWritePtr```|



 

 





