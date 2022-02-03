---
title: Querying the System Event Log for Hardware Error Events
description: Querying the System Event Log for Hardware Error Events
keywords:
- events WDK WHEA , querying system event log
- querying system event log WDK WHEA
- logs WDK WHEA
- WHEA WDK , querying system event log
- Windows Hardware Error Architecture WDK , querying system event log
- event log WDK WHEA
ms.date: 02/03/2021
---

# Querying the System Event Log for Hardware Error Events

The name of the provider that logs the hardware error events is **Microsoft-Windows-WHEA-Logger**.

This provider is designed for users in desktop scenarios. It provides a human readable message with the main details of the event so a user can get a basic idea of what occurred.

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

> [!NOTE]
> All of the **Evt_Xxx_** functions and the EVT\_*XXX* data types that were used in the previous examples are documented in the [Windows Event Log](/windows/win32/wes/windows-event-log) section in the Microsoft Windows SDK documentation.
