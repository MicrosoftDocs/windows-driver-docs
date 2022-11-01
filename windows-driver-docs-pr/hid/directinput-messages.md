---
title: DirectInput Messages (Windows Drivers)
description: Learn more about DirectInput Messages.
ms.date: 10/27/2022
---

# DirectInput Messages

## DirectInput Application Access Message

DirectInput supports new notification messages that are broadcast to notify when DirectInput applications have begun to use DirectInput services. These notifications can be used to detect recently started applications that use DirectInput and how those applications are making use of DirectInput's features. Your application can register for notifications by calling the Win32 function, **RegisterWindowMessage**, and passing DIRECTINPUT\_NOTIFICATION\_MSGSTRING (defined in Dinputd.h).

As with any other call to RegisterNotificationMessageString, the UINT value returned by the function is the message value that registered applications should hook in their window process. Once received, the *wParam* parameter for the message describes the type of notification being sent. The value of *wParam* is one of the following constants, defined in Dinputd.h:

## Messages (wParam)

- DIMSGWP\_NEWAPPSTART  
  DirectInput has been initialized by an application that has not been used by the current user before.

- DIMSGWP\_DX8APPSTART  
  DirectInput has been initialized by an application that is using DirectX 8.0 DirectInput features, but did not use DirectInput mapper functions on any previous run by the current user.

- DIMSGWP\_DX8MAPPERAPPSTART  
  DirectInput has been initialized by an application that uses DirectInput mapper functions provided in DirectX 8.0.

## Remarks

Upon receiving these notifications, an application can query for additional information by calling the [**IDirectInputJoyConfig8::OpenAppStatusKey**](/windows/win32/api/dinputd/nf-dinputd-idirectinputjoyconfig8-openappstatuskey) method.
