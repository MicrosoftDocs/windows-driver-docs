---
title: C28726 warning
description: Warning C28726 Banned API Usage.
ms.date: 08/22/2022
f1_keywords: 
  - "C28726", "BANNED_API_USAGEL2", "__WARNING_BANNED_API_USAGEL2"
---
# Warning C28726

> Banned API Usage:  '\**function-name*' is insecure and has been marked deprecated.

This warning indicates that a function is being used that has been banned and has a more robust or secure replacement. This specific error indicates that the banned function has potential to overflow a buffer.

## Remarks

A list of all banned functions covered by this error, why they are banned, and recommended replacements can be found after the following example.

Code analysis name: BANNED_API_USAGEL2

## Example 

The following code generates this warning: 

```cpp
void example_func() 
{ 
    char user_input[10]; 
    scanf(“%s”, input); // scanf is banned for security purposes 
} 
```

This is due to the use of the unsafe function scanf. scanf does place any limit on the size of the data copied to the buffer. To fix this issue, we can use scanf_s, the safer replacement to this function. scanf_s requires the developer to specify how many bytes are intended to be copied. scanf_s will ensure only that many bytes are copied. For example, the following code is safer: 

```cpp
void example_func() 
{ 
    char user_input[10]; 
    scanf_s(“%9s”, input, sizeof(input)); // 9 bytes leaves room for the \0 byte at the end  
} 
```

## Banned Functions 

_NOTE: This list is actively being updated and improved_

| Banned API | Replacement(s) | Rationale / Notes |
| -----------|----------------|--------------|
|```_itoa```| ```_itoa_s``` | Does not NULL-terminate |
|```_i64toa```| ```_i64toa_s``` | Does not NULL-terminate |
|```_i64tow```| ```_i64tow_s``` | Does not NULL-terminate |
|```_mbccpy```| ```_mbccpy_s``` | |
|```_mbscpy```| ```_mbscpy_s``` | |
|```_mbsnbcpy```| ```_mbsnbcpy_s```| |
|```_mbsnbcat```| ```_mbsnbcat_s``` | |
|```_mbsncat```| ```_mbsncat_s``` | |
|```_mbsncpy```| ```_mbsncpy_s``` | |
|```_mbstok```| ```_mbstok_s``` | |
|```_snscanf```| ```_snscanf_s``` | |
|```_snwscanf```| ```_snwscanf_s``` | |
|```_ui64toa```| ```ui64toa_s``` | |
|```_ui64tow```| ```_ui64tow_s``` | |
|```_ultoa```| ```_ultoa_s``` | |
|```CharToOemA```| | |
|```CharToOemBuffA```| | |
|```CharToOemBuffW```| | |
|```CharToOemW```| | |
|```OemToCharA```| | |
|```OemToCharBuffA```| | |
|```OemToCharBuffW```| | |
|```scanf```| ```scanf_s``` | Limited error detection |
|```sscanf```| ```sscanf_s``` | Limited error detection |
|```wmemcpy```| ```wmemcpy_s``` | Limited error detection |
|```wnsprintfW```| | |
|```wscanf```| ```wscanf_s``` | |
