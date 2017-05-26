---
title: Registering for Notification of Hardware Error Events
author: windows-driver-content
description: Registering for Notification of Hardware Error Events
ms.assetid: 86816fc7-fa69-4ecf-9d50-822b0fa6992d
keywords:
- events WDK WHEA , registering for notifications
- registering hardware event notifications
- notifications WDK WHEA
- WHEA WDK , registering for event notifications
- Windows Hardware Error Architecture WDK , registering for event notifications
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registering for Notification of Hardware Error Events


To register to be notified about new hardware error events, an application creates a subscription to all events that are raised by the WHEA provider. The name of the WHEA provider is **Microsoft-Windows-Kernel-WHEA**.

The channel to which the WHEA provider raises the hardware error events is as follows:

-   The **System** channel (Windows Vista).

-   The **Microsoft-Windows-Kernel-WHEA** channel (Windows Server 2008 and Windows Vista SP1).

-   The **Microsoft-Windows-Kernel-WHEA/Errors** channel (Windows 7 and later versions).

### Windows Vista

The following code example shows how to register for the notification of new hardware error events for this version of Windows.

```
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

```
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Registering%20for%20Notification%20of%20Hardware%20Error%20Events%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


