---
title: Pscript-Specific Customized Rendering
description: Pscript-Specific Customized Rendering
ms.assetid: e984f0f0-1435-4cfd-9a99-297f6a9521f5
keywords:
- rendering plug-ins WDK print , Pscript5
- Pscript WDK print , customized rendering
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pscript-Specific Customized Rendering





Pscript5 allows device-specific customized code to inject Postscript commands into the data stream that the Pscript5 driver sends to the printer device. If you want to provide this type of customized code, you must provide a rendering plug-in that implements the [**IPrintOemPS::Command**](https://msdn.microsoft.com/library/windows/hardware/ff553199) method.

Pscript5 calls the **IPrintOemPS::Command** method at a variety of points within the print job's data stream. One of the function's arguments specifies an index value that represents the current point in the data stream. Each time the function is called, it can check the index value and either provide additional stream data or not.

 

 




