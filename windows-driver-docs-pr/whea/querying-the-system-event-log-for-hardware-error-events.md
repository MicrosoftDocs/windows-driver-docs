---
title: Querying the System Event Log for Hardware Error Events
author: windows-driver-content
description: Querying the System Event Log for Hardware Error Events
MS-HAID:
- 'whea\_84eb347d-808d-4a6d-8dd5-ee8a7a688bb6.xml'
- 'whea.querying\_the\_system\_event\_log\_for\_hardware\_error\_events'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e2290a1b-6fde-4843-9c52-17279f93a887
keywords: ["events WDK WHEA , querying system event log", "querying system event log WDK WHEA", "logs WDK WHEA", "WHEA WDK , querying system event log", "Windows Hardware Error Architecture WDK , querying system event log", "event log WDK WHEA"]
---

# Querying the System Event Log for Hardware Error Events


The name of the provider that logs the hardware error events is as follows:

-   **Microsoft-Windows-Kernel-WHEA** (Windows Vista).

-   **Microsoft-Windows-WHEA-Logger** (Windows Server 2008, Windows Vista SP1 and later versions).

### Windows Vista

The following code example shows how to query the system event log to retrieve any hardware error events that were previously logged by WHEA.

```
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

```
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Querying%20the%20System%20Event%20Log%20for%20Hardware%20Error%20Events%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


