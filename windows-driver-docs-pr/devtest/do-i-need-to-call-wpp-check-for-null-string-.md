---
title: Do I need to call WPP_CHECK_FOR_NULL_STRING
description: Do I need to call WPP_CHECK_FOR_NULL_STRING
ms.assetid: 4a4dfe91-a70b-4297-9f11-fcc4b0e5a900
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Do I need to call WPP\_CHECK\_FOR\_NULL\_STRING?


Starting with the Windows 7 version of the Windows Driver Kit (WDK), the tracing components automatically check for **NULL** strings in the arguments that you pass in to the tracing functions. As a result, you do not have to call WPP\_CHECK\_FOR\_NULL\_STRING to verify each argument in order to prevent **NULL** strings from causing an exception.

If you build your [trace provider](trace-provider.md) (such as a driver or application) with the Windows 7 and later versions of the WDK, you can remove the WPP\_CHECK\_FOR\_NULL\_STRING macro from your source code.

 

 





