---
title: Querying the System Event Log for Hardware Error Events
description: Querying the System Event Log for Hardware Error Events
ms.assetid: e2290a1b-6fde-4843-9c52-17279f93a887
keywords:
- events WDK WHEA , querying system event log
- querying system event log WDK WHEA
- logs WDK WHEA
- WHEA WDK , querying system event log
- Windows Hardware Error Architecture WDK , querying system event log
- event log WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying the System Event Log for Hardware Error Events


The name of the provider that logs the hardware error events is as follows:

-   **Microsoft-Windows-Kernel-WHEA** (Windows Vista).

-   **Microsoft-Windows-WHEA-Logger** (Windows Server 2008, Windows Vista SP1 and later versions).

### Windows Vista

The following code example shows how to query the system event log to retrieve any hardware error events that were previously logged by WHEA.

```cpp
// Function to query the event log for hardware error events
VOID QueryHwErrorEvents(VOID) {

  EVT_HANDLE QueryHandle;
  EVT_HANDLE EventHandle;
  ULONG Returned;

  // Obtain a query handle to the system event log
  QueryHandle =
    EvtQuery(
      NULL, 
      L"System", 
      L"*[System/Provider[@Name=\"Microsoft-Windows-Kernel-WHEA\"]]",
      EvtQueryChannelPath | EvtQueryForwardDirection
      );

  // Check result
  if (QueryHandle != NULL) {

    // Get the next hardware error event
    while (EvtNext(
             QueryHandle,
             1,
             &EventHandle,
             -1,
             0,
             &Returned
             )) {

      // Process the hardware error event
      ProcessHwErrorEvent(EventHandle);

      // Close the event handle
      EvtClose(EventHandle);
    }

    // Close the query handle
    EvtClose(QueryHandle);
  }
}
```

### Windows Server 2008, Windows Vista SP1 and later versions

The following code example shows how to query the system event log to retrieve any hardware error events that were previously logged by WHEA.

```cpp
// Function to query the event log for hardware error events
VOID QueryHwErrorEvents(VOID) {

  EVT_HANDLE QueryHandle;
  EVT_HANDLE EventHandle;
  ULONG Returned;

  // Obtain a query handle to the system event log
  QueryHandle =
    EvtQuery(
      NULL, 
      L"System", 
      L"*[System/Provider[@Name=\"Microsoft-Windows-WHEA-Logger\"]]",
      EvtQueryChannelPath | EvtQueryForwardDirection
      );

  // Check result
  if (QueryHandle != NULL) {

    // Get the next hardware error event
    while (EvtNext(
             QueryHandle,
             1,
             &EventHandle,
             -1,
             0,
             &Returned
             )) {

      // Process the hardware error event
      ProcessHwErrorEvent(EventHandle);

      // Close the event handle
      EvtClose(EventHandle);
    }

    // Close the query handle
    EvtClose(QueryHandle);
  }
}
```

**Note**  All of the **Evt*Xxx*** functions and the EVT\_*XXX* data types that were used in the previous examples are documented in the [Windows Event Log](http://go.microsoft.com/fwlink/p/?linkid=81187) section in the Microsoft Windows SDK documentation.

 

 

 




