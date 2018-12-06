---
title: C28636
description: Warning C28636 Calling LocalFree on non-allocated pointer obtained from calls to GetSecurityDescriptorOwner/Group/Dacl/Sacl.
ms.assetid: cad12c6c-5d65-4c5b-98fa-4e0fa9e75166
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28636


warning C28636: Calling LocalFree on non-allocated pointer obtained from calls to GetSecurityDescriptorOwner/Group/Dacl/Sacl

These functions do not allocate any memory—they set the pointer that is passed in. For this reason, it is wrong to free memory using that pointer.

 

 





