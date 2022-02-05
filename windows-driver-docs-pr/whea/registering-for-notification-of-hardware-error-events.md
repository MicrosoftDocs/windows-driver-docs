---
title: Registering for Notification of Hardware Error Events
description: Registering for Notification of Hardware Error Events
keywords:
- events WDK WHEA , registering for notifications
- registering hardware event notifications
- notifications WDK WHEA
- WHEA WDK , registering for event notifications
- Windows Hardware Error Architecture WDK , registering for event notifications
ms.date: 02/03/2022
---

# Registering for Notification of Hardware Error Events

To register to be notified about new hardware error events, an application creates a subscription to all events that are raised by the **Microsoft-Windows-Kernel-WHEA/Errors** channel.

This channel is recommended for server scenarios. While the data is not immediately human readable, it is an ACPI/UEFI-defined [Common Platform Error Record (CPER)](/windows-hardware/drivers/whea/error-records).
In comparison with the **Microsoft-Windows-WHEA-Logger** provider, this format provides much more detail on the exact specifics of each hardware error event.

The following code example shows how to register for the notification of new hardware error events.

```cpp
// Prototype for the notification callback function
DWORD WINAPI HwErrorEventCallback(
  EVT_SUBSCRIBE_NOTIFY_ACTION Action,
  PVOID Context,
  EVT_HANDLE EventHandle
  );

// Function to create a subscription to all hardware error
// events that are raised by the WHEA provider.
EVT_HANDLE SubscribeHwErrorEvents(VOID)
{
  EVT_HANDLE SubHandle;

  // Create a subscription to all events that are sent
  // to the WHEA channel.
#if (WINVER <= _WIN32_WINNT_LONGHORN)
  SubHandle =
    EvtSubscribe(
      NULL,
      NULL,
      L"Microsoft-Windows-Kernel-WHEA", 
      L"*",
      NULL,
      NULL,
      HwErrorEventCallback,
      EvtSubscribeToFutureEvents
      );
#else
  SubHandle =
    EvtSubscribe(
      NULL,
      NULL,
      L" Microsoft-Windows-Kernel-WHEA/Errors", 
      L"*",
      NULL,
      NULL,
      HwErrorEventCallback,
      EvtSubscribeToFutureEvents
      );
#endif

   // Return the subscription handle
   return SubHandle;
}

// Notification callback function
DWORD WINAPI HwErrorEventCallback(
  EVT_SUBSCRIBE_NOTIFY_ACTION Action,
  PVOID Context,
  EVT_HANDLE EventHandle
  )
{
  // Check the action
  if (Action == EvtSubscribeActionDeliver) {

    // Process the hardware error event
    ProcessHwErrorEvent(EventHandle);
  }

  // Return success status
  return ERROR_SUCCESS;
}

// Function to terminate the subscription
VOID UnsubscribeHwErrorEvents(EVT_HANDLE SubHandle)
{
  // Close the subscription handle
  EvtClose(SubHandle);
}
```

> [!NOTE]
> All of the **Evt*Xxx*** functions and the EVT\_*XXX* data types that were used in the previous examples are documented in the [Windows Event Log](/windows/win32/wes/windows-event-log) section in the Microsoft Windows SDK documentation.
