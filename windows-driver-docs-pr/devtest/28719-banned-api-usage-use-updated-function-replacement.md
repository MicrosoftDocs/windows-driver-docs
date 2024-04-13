---
title: C28719 Warning
description: Warning C28719 Banned API Usage.
ms.date: 08/18/2022
f1_keywords: ["C28719", "BANNED_API_USAGE", "__WARNING_BANNED_API_USAGE"]
---
# Warning C28719

> Banned API Usage:  *function-name* is insecure and has been marked deprecated.

This warning indicates that a function is being used that has been banned and has a more robust or secure replacement.

## Remarks

A list of all banned functions covered by this error, why they are banned, and recommended replacements can be found after the following example.

Code analysis name: BANNED_API_USAGE

## Example 

The following code generates this warning: 

```cpp
void example_func(PSTR src) 
{ 
    char dst[100]; 
    strcpy(dst, src);
} 
```

This issue stems from the use of the unsafe function strcpy.
strcpy does not check if the destination buffer is large enough to fit the source data.
To fix this issue, we can use strcpy_s, C++11’s safer replacement to this function.
strcpy_s has a third parameter (the size of the destination buffer) to ensure only that many bytes are copied.
For example, the following code is safer: 

```cpp
void example_func(PSTR src) 
{ 
    char dst[100]; 
    strcpy_s(dst, sizeof(dst), src); 
}
```

## Banned Functions  

_NOTE: This list is actively being updated and improved_

| Banned API | Replacement(s) | Rationale / Notes |
| -----------|----------------|--------------|
|```_fstrcat```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | Legacy 16-bit far pointer implementation |
|```_fstrcpy```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | Legacy 16-bit far pointer implementation |
|```_fstrncat```| ```StringCbCatN```, ```StringCbCatNEx```, ```StringCchCatN```, ```StringCchCatNEx``` | Legacy 16-bit far pointer implementation |
|```_fstrncpy```| ```strncpy```, ```wcsncpy``` | Legacy 16-bit far pointer implementation |
|```_ftccat```| ```strcat```, ```wcscat``` | Legacy 16-bit far pointer implementation |
|```_ftccpy```| ```strcpy```, ```wcscpy``` | Legacy 16-bit far pointer implementation |
|```_ftcscat```| ```strcat```, ```wcscat``` | Legacy 16-bit far pointer implementation |
|```_ftcscpy```| ```strcpy```, ```wcscpy``` | Legacy 16-bit far pointer implementation |
|```_getts```| ```StringCbGets```, ```StringCbGetsEx```, ```StringCchGets```, ```StringCchGetsEx```, ```gets_s``` | No size limit on data |
|```_gettws```| ```gets_s```| No size limit on data |
|```_getws```| ```_getws_s```| No size limit on data |
|```_mbccat```| ```strcat_s```, ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx```, ```strlcat``` | No size limit on data |
|```_makepath```| ```_makepath_s``` | No size limit on data |
|```_mbscat```| ```_mbscat_s``` |  |
|```_snprintf```| ```_snprintf_s```| Does not NULL-terminate |
|```_sntprintf```| ```StringCbPrintf```, ```StringCbPrintf_l```, ```StringCbPrintf_lEx```, ```StringCbPrintfEx```, ```StringCchPrintf```, ```StringCchPrintfEx``` | Does not NULL-terminate |
|```_sntscanf```| ```_snscanf_s``` | No maximum length |
|```_snwprintf```| ```_snwprintf_s```, ```StringCbPrintf```, ```StringCbPrintf_l```, ```StringCbPrintf_lEx```, ```StringCbPrintfEx```, ```StringCchPrintf```, ```StringCchPrintfEx``` | Does not NULL-terminate |
|```_splitpath```| ```_splitpath_s``` | No bounds checking |
|```_stprintf```| ```StringCbPrintf```, ```StringCbPrintf_l```, ```StringCbPrintf_lEx```, ```StringCbPrintfEx```, ```StringCchPrintf```, ```StringCchPrintfEx``` | Limited error detection |
|```_stscanf```| ```sscanf_s``` (requires format string changes) | No bounds checking |
|```_tccat```| ```strcat_s```, ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx```, ```strlcat``` | No bounds checking |
|```_tccpy```| ```strcpy_s```, ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx```, ```strlcpy``` | No bounds checking |
|```_tcscat```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | Limited error detection |
|```_tcscpy```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | Limited error detection |
|```_tcsncat```| ```StringCbLength```, ```StringCchLength```, ```UnalignedStringCbLength```, ```UnalignedStringCchLength``` | No maximum length |
|```_tcsncpy```| ```StringCbCopyN```, ```StringCbCopyNEx```, ```StringCchCopyN```, ```StringCchCopyNEx```| Limited error detection |
|```_tmakepath```| ```_makepath_s``` | No bounds checking |
|```_tscanf```| ```scanf_s``` | No bounds checking for outputs |
|```_tsplitpath```| ```splitpath_s```, ```wsplitpath_s``` | No bounds checking |
|```_vsnprintf```| ```_vsnprintf_s```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx```| Limited error detection |
|```_vsntprintf```| ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx```| Limited error detection |
|```_vsnwprintf```| ```_vsnwprintf_s```, ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```| Limited error detection |
|```_vstprintf```| ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrinfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx```| No maximum length |
|```_wmakepath```| ```_wmakepath_s```| No bounds checking |
|```_wsplitpath```| ```_wsplitpath_s``` | No bounds checking |
|```OemToCharW```| ```WideCharToMultiByte``` | No bounds checking |
|```StrCat```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | Limited error detection |
|```StrCatA```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | Limited error detection |
|```StrCatBuff```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | No NULL-termination |
|```StrCatBuffA```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | No NULL-termination |
|```StrCatBuffW```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | No NULL-termination |
|```StrCatChainW```| ```StringCbCatEx```, ```StringCbCatNEx```, ```StringCchCatEx```, ```StringCchCatNEx``` | No NULL-termination |
|```StrCatN```| ```StringCbCat```, ```StringCbCatEx```, ```StringCbCatN```, ```StringCbCatNEx```, ```StringCchCat```, ```StringCchCatEx```, ```StringCchCatN```, ```StringCchCatNEx``` | No bounds checking |
|```StrCatNA```| ```StringCbCat```, ```StringCbCatEx```, ```StringCbCatN```, ```StringCbCatNEx```, ```StringCchCat```, ```StringCchCatEx```, ```StringCchCatN```, ```StringCchCatNEx``` | No bounds checking |
|```StrCatNW```| ```StringCbCat```, ```StringCbCatEx```, ```StringCbCatN```, ```StringCbCatNEx```, ```StringCchCat```, ```StringCchCatEx```, ```StringCchCatN```, ```StringCchCatNEx``` | No bounds checking |
|```StrCatW```| ```StringCbCat```, ```StringCbCatEx```, ```StringCbCatN```, ```StringCbCatNEx```, ```StringCchCat```, ```StringCchCatEx```, ```StringCchCatN```, ```StringCchCatNEx``` | No bounds checking |
|```StrCpy```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | No bounds checking |
|```StrCpyA```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | No bounds checking |
|```StrCpyN```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | Does not NULL-terminate |
|```StrCpyNA```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | Does not NULL-terminate |
|```StrCpyNW```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | Limited error checking |
|```strcpyW```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | No bounds checking |
|```StrCpyW```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | No bounds checking |
|```StrNCat```| ```StringCbCatN```, ```StringCbCatNEx```, ```StringCchCatN```, ```StringCchCatNEx``` | Limited error detection |
|```StrNCatA```| ```StringCbCatN```, ```StringCbCatNEx```, ```StringCchCatN```, ```StringCchCatNEx``` | Limited error detection |
|```StrNCatW```| ```StringCbCatN```, ```StringCbCatNEx```, ```StringCchCatN```, ```StringCchCatNEx``` | Limited error detection |
|```StrNCpy```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | Does not NULL-terminate |
|```StrNCpyA```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | Does not NULL-terminate |
|```StrNCpyW```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | Does not NULL-terminate |
|```gets```| ```gets_s```, ```fgets```, ```StringCbGets```, ```StringCbGetsEx```, ```StringCchGets```, ```StringCchGetsEx``` | Limited error detection; deprecated by C11 standard |
|```lstrcat```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | Limited error detection |
|```lstrcatA```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | Limited error detection |
|```lstrcatn```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | Limited error detection |
|```lstrcatnA```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | Limited error detection |
|```lstrcatnW```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | Limited error detection |
|```lstrcatW```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | Limited error detection |
|```lstrcpy```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | No bounds checking |
|```lstrcpyA```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | No bounds checking |
|```lstrcpyn```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | Limited error detection |
|```lstrcpynA```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | Limited error detection |
|```lstrcpynW```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | No bounds checking |
|```lstrcpyW```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | No bounds checking |
|```snscanf```| ```sscanf_s``` | No bounds checking |
|```snwscanf```| ```swscanf_s``` | No bounds checking |
|```sprintf```| ```sprintf_s``` | Limited error detection |
|```sprintfA```| ```sprintf_s``` | No bounds checking |
|```sprintfW```| ```swprintf_s``` | No bounds checking |
|```lstrncat```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | Limited error detection |
|```makepath```| | |
|```nsprintf```| ```sprintf_s``` | No error detection or bounds checking |
|```strcat```| ```strcat_s```, ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx```, ```strlcat``` | Limited error detection |
|```strcatA```| ```strcat_s```, ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx```, ```strlcat``` | Limited error detection |
|```strcatW```| ```strcat_s```, ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx```, ```strlcat``` | Limited error detection |
|```strcpy```| ```strcpy_s```, ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx```, ```strlcpy``` | No bounds checking |
|```strcpyA```| ```strcpy_s```, ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx```, ```strlcpy``` | No bounds checking |
|```strncat```| ```strncat_s```, ```StringCbCatN```, ```StringCbCatNEx```, ```StringCchCatN```, ```StringCchCatNEx```, ```strlcat```| Limited error detection |
|```strncpy```| ```strncpy_s```, ```StringCbCopyN```, ```StringCbCopyNEx```, ```StringCchCopyN```, ```StringCchCopyNEx```, ```strlcpy``` | Limited error detection |
|```swprintf```| ```swprintf_s``` ```StringCbPrintf```, ```StringCbPrintf_l```, ```StringCbPrintf_lEx```, ```StringCbPrintf```, ```StringCbPrintfEx``` | Limited error detection |
|```ualstrcpyW```| ```strcpy_s```, ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx```, ```strlcpy``` | No bounds checking |
|```vsnprintf```| ```vsnprintf_s```, ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx```| Limited error detection |
|```vsprintf```| ```vsprintf_s```, ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx```, ```vasprintf``` | Limited error detection |
|```vswprintf```| ```vswprintf_s``` | |
|```wcscat```| ```wcscat_s```, ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx```, ```wcslcat``` | Limited error detection |
|```wcscpy```| ```wcscpy_s```, ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx```, ```wcslcpy``` | No bounds checking |
|```wcsncat```| ```wcsncat_s```, ```wcslcat``` | Limited error detection |
|```wcsncpy```| ```wcsncpy_s```, ```StringCbCopyN```, ```StringCbCopyNEx```, ```StringCchCopyN```, ```StringCchCopyNEx```, ```wcslcpy``` | Limited error detection |
|```wnsprintf```| ```StringCbPrintf```, ```StringCbPrintf_l```, ```StringCbPrintf_lEx```, ```StringCbPrintfEx```, ```StringCchPrintf```, ```StringCchPrintfEx``` | No NULL-termination |
|```wnsprintfA```| ```StringCbPrintf```, ```StringCbPrintf_l```, ```StringCbPrintf_lEx```, ```StringCbPrintfEx```, ```StringCchPrintf```, ```StringCchPrintfEx``` | No NULL-termination |
|```wsprintf```| ```StringCbPrintf```, ```StringCbPrintf_l```, ```StringCbPrintf_lEx```, ```StringCbPrintfEx```, ```StringCchPrintf```, ```StringCchPrintfEx``` | No NULL-termination |
|```wsprintfA```| ```StringCbPrintf```, ```StringCbPrintf_l```, ```StringCbPrintf_lEx```, ```StringCbPrintfEx```, ```StringCchPrintf```, ```StringCchPrintfEx``` | No NULL-termination |
|```wsprintfW```| ```StringCbPrintf```, ```StringCbPrintf_l```, ```StringCbPrintf_lEx```, ```StringCbPrintfEx```, ```StringCchPrintf```, ```StringCchPrintfEx``` | No NULL-termination |
|```wvnsprintf```| ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx``` | No NULL-termination |
|```wvnsprintfA```| ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx``` | No NULL-termination |
|```wvnsprintfW```| ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx``` | No NULL-termination |
|```wvsprintf```| ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx```| No NULL-termination |
|```wvsprintfA```| ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx```| No NULL-termination |
|```wvsprintfW```| ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx```| No NULL-termination |
