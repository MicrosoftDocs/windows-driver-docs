---
title: C28720 warning
description: Warning C28720 Banned API Usage.
ms.date: 04/20/2017
f1_keywords: 
  - "C28720"
---

# C28720


**warning C28720: IsBadXXXPtr API Usage**\
_Banned API Usage:  *function name* is a Banned API as listed in dontuse.h for security purposes._

Using one of these APIs indicates that you are testing to see if memory is mapped, which implies that you either don't own the memory at all (so you shouldn't be trying to access it), or it indicates a need for better [object lifetime management](https://docs.microsoft.com/en-us/cpp/cpp/object-lifetime-and-resource-management-modern-cpp?view=msvc-170) (if you need to test if something still exists). 
There are no 1:1 replacement APIs for this rule. Instead, we recommend reevaluating your code to avoid the need to utilize these functions. 

## Banned Functions
| banned API |
| -----------|
|```IsBadCodePtr```|
|```IsBadHugeReadPtr```|
|```IsBadHugeWritePtr```|
|```IsBadReadPtr```|
|```IsBadStringPtr```|
|```IsBadWritePtr```|



 

 





