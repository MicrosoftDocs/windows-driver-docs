---
title: C28750 warning
description: Warning C28750 Banned usage of lstrlen and its variants.
ms.date: 04/20/2017
f1_keywords: 
  - "C28750"
---

# C28750


**Warning C28750: Banned API Usage lstrlen**\
_Banned usage of lstrlen and its variants: *function_name* is a banned API for improved error handling purposes._

This warning indicates that a function is being used that has been banned and has a more robust or secure replacement. This specific error indicates usage of lstrlen or a variant thereof. The lstrlen function and its variants are banned because they fail to transmit exceptions. This can cause error conditions to occur much later, potentially on a different thread. This makes the error conditions harder to diagnose. In addition, equivalent substitute functions can be optimized by the compiler and avoid the performance overhead of exception handlers (_try and _except blocks).  

The correct mitigation is to use a safer string length function (usually strlen, wcslen, _tcslen). However, while you review the lstrlen changes, you should confirm that the string buffer is coming from trusted code. If you are dealing with untrusted data, you should instead switch from the strlen family of functions to the strnlen family (or StringCchLength family), which will ensure they don't go past the bounds of the untrusted data block. 

Note that unlike lstrlen, none of the replacements catch exceptions. Also, lstrlen handles NULL pointers while the replacements do not, so an explicit NULL check is required when replacing lstrlen with strlen or strnlen (if NULL pointers are possible at that point in the code).  

A list of all banned functions covered by this error and recommended replacements (for both trusted and untrusted data) can be found after the following example: 

## Example

The following code generates this warning: 
```
int example_func(char* in)
{ 
    int size = lstrlen(in);
    return size; 
} 
```
This is due to the use of the unsafe function lstrlen. To fix this issue, we can use the strlen as the replacement, making sure to check if the pointer is NULL: 
```
int example_func(char* in) 
{ 
    if (in != NULL)
        int size = strlen(in);
        return size;
    else {
        // handle error.
    }
} 
```

## Banned Functions

| Banned API | Trusted data replacement(s) | Untrusted data replacement(s) |
| -----------|----------------|--------------|
|```lstrlen```| ```_tcslen``` | ```_tcsnlen```, ```StringCchLength``` |
|```lstrlenA```| ```strlen``` | ```strnlen```, ```StringCchLengthA``` |
|```lstrlenW```| ```wcslen``` | ```wcsnlen```, ```StringCchLengthW``` |

 





