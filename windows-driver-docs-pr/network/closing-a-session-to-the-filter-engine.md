---
title: Closing a Session to the Filter Engine
description: Closing a Session to the Filter Engine
ms.assetid: e145fb8c-fe9f-4834-8df0-f2ceb5b13b09
keywords:
- Windows Filtering Platform callout drivers WDK , closing sessions
- callout drivers WDK Windows Filtering Platform , closing sessions
- filter engine WDK Windows Filtering Platform
- closing filter engine sessions WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Closing a Session to the Filter Engine


After a callout driver has performed the desired management tasks, it should close the session to the filter engine. A callout driver does this by calling the [**FwpmEngineClose0**](https://msdn.microsoft.com/library/windows/hardware/ff550072) function. For example:

```C++
status =
 FwpmEngineClose0(
 engineHandle  // An handle to the open session
    );
```

 

 





