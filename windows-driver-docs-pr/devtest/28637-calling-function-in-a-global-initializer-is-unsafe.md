---
title: C28637 Warning
description: Warning C28637 Calling the function in a global initializer is unsafe.
ms.date: 04/20/2017
f1_keywords: 
  - "C28637"
---

# C28637


warning C28637: Calling the function in a global initializer is unsafe

When you use a DLL, it is frequently the case that any static constructors are called from DllMain. There are a number of constraints that apply to call other functions from DllMain. In particular, it is possible to create memory leaks if the DLL is loaded and unloaded dynamically. For more information, see the [DllMain Callback Function](/windows/win32/dlls/dllmain).

 

