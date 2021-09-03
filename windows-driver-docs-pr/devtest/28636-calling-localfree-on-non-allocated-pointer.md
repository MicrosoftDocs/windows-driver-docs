---
title: C28636 warning
description: Warning C28636 Calling LocalFree on non-allocated pointer obtained from calls to GetSecurityDescriptorOwner/Group/Dacl/Sacl.
ms.date: 04/20/2017
ms.localizationpriority: medium 
f1_keywords: 
  - "C28636"
---

# C28636


warning C28636: Calling LocalFree on non-allocated pointer obtained from calls to GetSecurityDescriptorOwner/Group/Dacl/Sacl

These functions do not allocate any memory—they set the pointer that is passed in. For this reason, it is wrong to free memory using that pointer.

 

 





