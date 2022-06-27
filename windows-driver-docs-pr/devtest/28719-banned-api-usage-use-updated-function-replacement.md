---
title: C28719 warning
description: Warning C28719 Banned API Usage.
ms.date: 04/20/2017
f1_keywords: 
  - "C28719"
---

# C28719


**Warning C28719: Banned API Usage**\
_Banned API Usage:  *function name* is a Banned API as listed in dontuse.h for security purposes._

This warning indicates that a function is being used that has been banned and has a more robust or secure replacement.
A list of all banned functions covered by this error, why they are banned, and recommended replacements can be found after the following example: 

## Example 

The following code generates this warning: 
```
void example_func(PSTR src) 
{ 
    char dst[100]; 
    strcpy(dst, src);
} 
```
This is due to the use of the unsafe function strcpy.
strcpy does not check if the destination buffer is large enough to fit the source data.
To fix this issue, we can use strcpy_s, C++11’s safe replacement to this function.
strcpy_s has a third parameter (the size of the destination buffer) to ensure only that many bytes are copied.
For example, the following code is safe: 
```
void example_func(PSTR src) 
{ 
    char dst[100]; 
    strcpy_s(dst, sizeof(dst), src); 
}
```
## Banned Functions  
_NOTE: This list is actively being updated and improved_
 | banned API | replacement(s) | rationale / notes |
| -----------|----------------|--------------|
|```_fstrcat```| |
|```_fstrcpy```| |
|```_fstrncat```| |
|```_fstrncpy```| |
|```_ftccat```| |
|```_ftccpy```| |
|```_ftcscat```| |
|```_ftcscpy```| |
|```_getts```| ```StringCbGets```, ```StringCbGetsEx```, ```StringCchGets```, ```StringCchGetsEx```, ```gets_s``` | No size limit on data |
|```_gettws```| ```gets_s```|
|```_getws```| ```_getws_s```|
|```_mbccat```| |
|```_makepath```| ```_makepath_s``` |
|```_mbscat```| ```_mbscat_s``` | |
|```_snprintf```| ```_snprintf_s```| Does not NULL-terminate |
|```_sntprintf```| |
|```_sntscanf```| |
|```_snwprintf```| ```_snwprintf_s```, ```StringCbPrintf```, ```StringCbPrintf_l```, ```StringCbPrintf_lEx```, ```StringCbPrintfEx```, ```StringCchPrintf```, ```StringCchPrintfEx``` | Does not NULL-terminate |
|```_splitpath```| ```_splitpath_s``` |
|```_stprintf```| ```StringCbPrintf```, ```StringCbPrintf_l```, ```StringCbPrintf_lEx```, ```StringCbPrintfEx```, ```StringCchPrintf```, ```StringCchPrintfEx``` | Limited error detection |
|```_stscanf```| |
|```_tccat```| |
|```_tccpy```| |
|```_tcscat```| |
|```_tcscpy```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | Limited error detection |
|```_tcsncat```| |
|```_tcsncpy```| ```StringCbCopyN```, ```StringCbCopyNEx```, ```StringCchCopyN```, ```StringCchCopyNEx```| Limited error detection |
|```_tmakepath```| |
|```_tscanf```| |
|```_tsplitpath```| |
|```_vsnprintf```| ```_vsnprintf_s```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx```| Limited error detection |
|```_vsntprintf```| ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx```| Limited error detection |
|```_vsnwprintf```| ```_vsnwprintf_s```, ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```| Limited error detection |
|```_vstprintf```| ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrinfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx```| No maximum length |
|```_wmakepath```| ```_wmakepath_s```|
|```_wsplitpath```| ```_wsplitpath_s``` |
|```OemToCharW```| |
|```StrCat```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx```| Limited error detection |
|```StrCatA```| |
|```StrCatBuff```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | No NULL-termination |
|```StrCatBuffA```| |
|```StrCatBuffW```| |
|```StrCatChainW```| |
|```StrCatN```| |
|```StrCatNA```| |
|```StrCatNW```| |
|```StrCatW```| |
|```StrCpy```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | No bounds checking |
|```StrCpyA```| |
|```StrCpyN```| |
|```StrCpyNA```| |
|```StrCpyNW```| |
|```strcpyW```| |
|```StrCpyW```| |
|```StrNCat```| ```StringCbCatN```, ```StringCbCatNEx```, ```StringCchCatN```, ```StringCchCatNEx``` | Limited error detection |
|```StrNCatA```| |
|```StrNCatW```| |
|```StrNCpy```| |
|```StrNCpyA```| |
|```StrNCpyW```| |
|```gets```| ```gets_s```, ```fgets```, ```StringCbGets```, ```StringCbGetsEx```, ```StringCchGets```, ```StringCchGetsEx``` | Deprecated by C11 standard |
|```lstrcat```| ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx``` | Limited error detection |
|```lstrcatA```| |
|```lstrcatn```| |
|```lstrcatnA```| |
|```lstrcatnW```| |
|```lstrcatW```| |
|```lstrcpy```| ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx``` | Limited error detection |
|```lstrcpyA```| |
|```lstrcpyn```| |
|```lstrcpynA```| |
|```lstrcpynW```| |
|```lstrcpyW```| |
|```snscanf```| |
|```snwscanf```| |
|```sprintf```| ```sprintf_s```| Limited error detection |
|```sprintfA```| |
|```sprintfW```| |
|```lstrncat```| |
|```makepath```| |
|```nsprintf```| |
|```strcat```| ```strcat_s```, ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx```, ```strlcat``` | Limited error detection |
|```strcatA```| |
|```strcatW```| |
|```strcpy```| ```strcpy_s```, ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx```, ```strlcpy``` | No bounds checking |
|```strcpyA```| |
|```strncat```| ```strncat_s```, ```StringCbCatN```, ```StringCbCatNEx```, ```StringCchCatN```, ```StringCchCatNEx```, ```strlcat```| Limited error detection |
|```strncpy```| ```strncpy_s```, ```StringCbCopyN```, ```StringCbCopyNEx```, ```StringCchCopyN```, ```StringCchCopyNEx```, ```strlcpy``` | Limited error detection |
|```swprintf```| ```swprintf_s``` ```StringCbPrintf```, ```StringCbPrintf_l```, ```StringCbPrintf_lEx```, ```StringCbPrintf```, ```StringCbPrintfEx``` | Limited error detection |
|```ualstrcpyW```| |
|```vsnprintf```| ```vsnprintf_s```, ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx```| Limited error detection |
|```vsprintf```| ```vsprintf_s```, ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx```, ```vasprintf``` | Limited error detection |
|```vswprintf```| ```vswprintf_s``` |
|```wcscat```| ```wcscat_s```, ```StringCbCat```, ```StringCbCatEx```, ```StringCchCat```, ```StringCchCatEx```, ```wcslcat``` | Limited error detection |
|```wcscpy```| ```wcscpy_s```, ```StringCbCopy```, ```StringCbCopyEx```, ```StringCchCopy```, ```StringCchCopyEx```, ```wcslcpy``` | No bounds checking |
|```wcsncat```| ```wcsncat_s```, ```wcslcat``` | Limited error detection |
|```wcsncpy```| ```wcsncpy_s```, ```StringCbCopyN```, ```StringCbCopyNEx```, ```StringCchCopyN```, ```StringCchCopyNEx```, ```wcslcpy``` | Limited error detection |
|```wnsprintf```| ```StringCbPrintf```, ```StringCbPrintf_l```, ```StringCbPrintf_lEx```, ```StringCbPrintfEx```, ```StringCchPrintf```, ```StringCchPrintfEx``` | No NULL-termination |
|```wnsprintfA```| |
|```wsprintf```| | No NULL-termination |
|```wsprintfA```| |
|```wsprintfW```| |
|```wvnsprintf```| ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx``` | No NULL-termination |
|```wvnsprintfA```| |
|```wvnsprintfW```| |
|```wvsprintf```| ```StringCbVPrintf```, ```StringCbVPrintf_l```, ```StringCbVPrintf_lEx```, ```StringCbVPrintfEx```, ```StringCchVPrintf```, ```StringCchVPrintf_l```, ```StringCchVPrintf_lEx```, ```StringCchVPrintfEx```| No NULL-termination |
|```wvsprintfA```| |
|```wvsprintfW```| |

 





