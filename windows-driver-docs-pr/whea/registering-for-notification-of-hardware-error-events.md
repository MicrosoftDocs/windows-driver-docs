---
title: Registering for Notification of Hardware Error Events
description: Registering for Notification of Hardware Error Events
ms.assetid: 86816fc7-fa69-4ecf-9d50-822b0fa6992d
keywords:
- events WDK WHEA , registering for notifications
- registering hardware event notifications
- notifications WDK WHEA
- WHEA WDK , registering for event notifications
- Windows Hardware Error Architecture WDK , registering for event notifications
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering for Notification of Hardware Error Events


To register to be notified about new hardware error events, an application creates a subscription to all events that are raised by the WHEA provider. The name of the WHEA provider is **Microsoft-Windows-Kernel-WHEA**.

The channel to which the WHEA provider raises the hardware error events is as follows:

-   The **System** channel (Windows Vista).

-   The **Microsoft-Windows-Kernel-WHEA** channel (Windows Server 2008 and Windows Vista SP1).

-   The **Microsoft-Windows-Kernel-WHEA/Errors** channel (Windows 7 and later versions).

### Windows Vista

The following code example shows how to register for the notification of new hardware error events for this version of Windows.

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

  // Create a subscription to all events that are sent to
  // the System channel by the WHEA provider.
  SubHandle =
    EvtSubscribe(
      NULL,
      NULL,
      L"System", 
      L"*[System/Provider[@Name=\"Microsoft-Windows-Kernel-WHEA\"]]",
      NULL,
      NULL,
      HwErrorEventCallback,
      EvtSubscribeToFutureEvents
      );

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

### Windows Server 2008, Windows Vista SP1 and later versions

The following code example shows how to register for the notification of new hardware error events for these versions of Windows.

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

**Note**  All of the **Evt*Xxx*** functions and the EVT\_*XXX* data types that were used in the previous examples are documented in the [Windows Event Log](http://go.microsoft.com/fwlink/p/?linkid=81187) section in the Microsoft Windows SDK documentation.

 

 

 




