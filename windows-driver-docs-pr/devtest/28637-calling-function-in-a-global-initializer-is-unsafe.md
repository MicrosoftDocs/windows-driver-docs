---
title: C28637
description: Warning C28637 Calling the function in a global initializer is unsafe.
ms.assetid: 9b392995-9583-4847-aded-f32e1daf28ed
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28637


warning C28637: Calling the function in a global initializer is unsafe

When you use a DLL, it is frequently the case that any static constructors are called from DllMain. There are a number of constraints that apply to call other functions from DllMain. In particular, it is possible to create memory leaks if the DLL is loaded and unloaded dynamically. For more information, see the [DllMain Callback Function](http://go.microsoft.com/fwlink/p/?linkid=133876).

 

 





