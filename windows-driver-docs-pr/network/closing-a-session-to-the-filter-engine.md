---
title: Closing a Session to the Filter Engine
description: Closing a Session to the Filter Engine
keywords:
- Windows Filtering Platform callout drivers WDK , closing sessions
- callout drivers WDK Windows Filtering Platform , closing sessions
- filter engine WDK Windows Filtering Platform
- closing filter engine sessions WDK Windows Filtering Platform
ms.date: 04/20/2017
---

# Closing a Session to the Filter Engine


After a callout driver has performed the desired management tasks, it should close the session to the filter engine. A callout driver does this by calling the [**FwpmEngineClose0**](/windows-hardware/drivers/ddi/fwpmk/nf-fwpmk-fwpmengineclose0) function. For example:

```C++
status =
 FwpmEngineClose0(
 engineHandle  // An handle to the open session
    );
```

 

