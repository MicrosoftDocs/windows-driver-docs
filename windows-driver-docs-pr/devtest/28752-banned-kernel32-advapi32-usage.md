---
title: C28752 warning
description: Warning C28752 Banned usage of kernel32 or advapi32 API.
ms.date: 04/20/2017
ms.localizationpriority: medium 
f1_keywords: 
  - "C28752"
---

# C28752


warning C28752: Banned usage of kernel32 or advapi32 API

This warning indicates that a function is being used that has been deprecated, and has a preferred replacement that is part of Core System.

The Core System binaries provide much of the functionality that kernel32 and advapi32 do, but in many cases a different API call is required. Calling Core System APIs is faster and requires a smaller memory footprint than calling legacy kernel32 or advapi32 APIs.

 

 





