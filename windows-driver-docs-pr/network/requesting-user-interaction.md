---
title: Requesting User Interaction
description: Requesting User Interaction
ms.assetid: 888faeb0-1984-4b0f-b955-2772a6bd86f7
keywords:
- user interaction WDK Native 802.11 IHV Extensions DLL
- requesting user interaction WDK Native 802.11 IHV Extensions DLL
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Requesting User Interaction


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

At any time after the call to [*Dot11ExtIhvInitAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff547469), the IHV Extensions DLL can request interaction with the user by calling the [**Dot11ExtSendUIRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547567) function. The operating system forwards all user interaction requests to the IHV UI Extensions DLL, which will process the request and display the appropriate user interface (UI) pages to the user.

When the request has been completed, the operating system calls the [*Dot11ExtIhvProcessUIResponse*](https://msdn.microsoft.com/library/windows/hardware/ff547504) function to forward the results from the IHV UI Extensions DLL for the user interaction. For more information about the IHV UI Extensions DLL, see [Native 802.11 IHV UI Extensions DLL](https://msdn.microsoft.com/library/windows/hardware/ff560635).

For example, the IHV Extensions DLL can request user interaction for any of the following.

-   Notify the user regarding the stages of a pre or post-association operation.

-   Prompt the user to enter his/her credentials for authentication during the post-association operation.

When it calls the [**Dot11ExtSendUIRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547567) function, the IHV Extensions DLL passes a pointer to a [**DOT11EXT\_IHV\_UI\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff547637) structure to the *pIhvUIRequest* parameter. The DOT11EXT\_IHV\_UI\_REQUEST structure specifies the request, such as the globally unique ID (GUID), which identifies the UI request as well as the COM class ID (CLSID) of the target UI page that will handle this request.

When the IHV UI Extensions DLL has completed the user notification, the operating system calls the [*Dot11ExtIhvProcessUIResponse*](https://msdn.microsoft.com/library/windows/hardware/ff547504) function. If the user had entered any data through the notification, the operating system passes a pointer to the buffer, which contains the data, to the *pvResponseBuffer* parameter.

The operating system might periodically query the status of pending notification requests. In this situation, the operating system calls the [*Dot11ExtIhvIsUIRequestPending*](https://msdn.microsoft.com/library/windows/hardware/ff547479) and passes the GUID of the UI request to the *guidUIRequest* parameter.

When calling [**Dot11ExtSendUIRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547567), the IHV Extensions DLL must follow these guidelines.

-   The IHV Extensions DLL does not need to serialize the calls to [**Dot11ExtSendUIRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547567). The DLL can have more than one pending UI request at any time.

-   The UI request for a particular GUID is completed only when [*Dot11ExtIhvProcessUIResponse*](https://msdn.microsoft.com/library/windows/hardware/ff547504) is called for that GUID. In this situation, the IHV Extensions DLL must not free any allocated resources for the UI request until *Dot11ExtIhvProcessUIResponse* is called.

-   All pending UI requests are canceled whenever [*Dot11ExtIhvAdapterReset*](https://msdn.microsoft.com/library/windows/hardware/ff547434) or [*Dot11ExtIhvDeinitAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff547452) is called. All pending UI requests are also canceled whenever [*Dot11ExtIhvProcessSessionChange*](https://msdn.microsoft.com/library/windows/hardware/ff547501) is called with the *uEventType* parameter set to WTS\_SESSION\_LOGOFF.

    In these situations, the IHV Extensions DLL must free all allocated resources for each pending UI request.

The operating system can initiate user interaction itself whenever the connection state changes on the basic service set (BSS) network. In this situation, the operating system calls the [*Dot11ExtIhvQueryUIRequest*](https://msdn.microsoft.com/library/windows/hardware/ff547507) function. The IHV Extensions DLL allocates a buffer and formats it as a [**DOT11EXT\_IHV\_UI\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff547637) structure. The DLL sets the members of the DOT11EXT\_IHV\_UI\_REQUEST structure to reference a UI page that is appropriate for the change in connection status. The operating system is responsible for displaying the UI page.

**Note**  The IHV Extensions must allocate the buffer that contains the [**DOT11EXT\_IHV\_UI\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff547637) structure through [**Dot11ExtAllocateBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff547419). The DLL must not free the buffer after returning from [*Dot11ExtIhvQueryUIRequest*](https://msdn.microsoft.com/library/windows/hardware/ff547507).

 

 

 





