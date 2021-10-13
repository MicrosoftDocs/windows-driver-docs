---
title: Opening a Session to the Filter Engine
description: Opening a Session to the Filter Engine
keywords:
- Windows Filtering Platform callout drivers WDK , opening sessions
- callout drivers WDK Windows Filtering Platform , opening sessions
- filter engine WDK Windows Filtering Platform
- opening filter engine sessions WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Opening a Session to the Filter Engine


A callout driver must open a session to the filter engine to perform management tasks such as adding filters to the filter engine. A callout driver opens a session to the filter engine by calling the [**FwpmEngineOpen0**](/windows-hardware/drivers/ddi/fwpmk/nf-fwpmk-fwpmengineopen0) function. For example:

```cpp
HANDLE engineHandle;
NTSTATUS status;

// Open a session to the filter engine
status =
 FwpmEngineOpen0(
    NULL,              // The filter engine on the local system
    RPC_C_AUTHN_WINNT, // Use the Windows authentication service
    NULL,              // Use the calling thread's credentials
    NULL,              // There are no session-specific parameters
    &engineHandle      // Pointer to a variable to receive the handle
    );
```

After a callout driver has successfully opened a session to the filter engine, it can use the returned handle to call the other Windows Filtering Platform management functions.

 

