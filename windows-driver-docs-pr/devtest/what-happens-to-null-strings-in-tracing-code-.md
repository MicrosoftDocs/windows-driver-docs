---
title: What happens to NULL strings in tracing code
description: What happens to NULL strings in tracing code
ms.assetid: a2226cbd-28cf-48eb-b129-5c4d12eb2564
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What happens to NULL strings in tracing code?


By default, the tracing components in this version of the Windows Driver Kit (WDK) search for **NULL** strings in the arguments that you pass in functions. As a result, you do not have to verify each argument to prevent **NULL** strings from causing an exception.

In earlier versions of the WDK, the WPP\_CHECK\_FOR\_NULL\_STRING macro performed this function. If you build your kernel-mode driver or user-mode application by using this version of the WDK, you can remove the macro from your source code.

 

 





