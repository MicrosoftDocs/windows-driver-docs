---
title: Requesting User Interaction
description: Requesting User Interaction
keywords:
- user interaction WDK Native 802.11 IHV Extensions DLL
- requesting user interaction WDK Native 802.11 IHV Extensions DLL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requesting User Interaction




 

At any time after the call to [*Dot11ExtIhvInitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_adapter), the IHV Extensions DLL can request interaction with the user by calling the [**Dot11ExtSendUIRequest**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_ui_request) function. The operating system forwards all user interaction requests to the IHV UI Extensions DLL, which will process the request and display the appropriate user interface (UI) pages to the user.

When the request has been completed, the operating system calls the [*Dot11ExtIhvProcessUIResponse*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_process_ui_response) function to forward the results from the IHV UI Extensions DLL for the user interaction. For more information about the IHV UI Extensions DLL, see [Native 802.11 IHV UI Extensions DLL](native-802-11-ihv-ui-extensions-dll2.md).

For example, the IHV Extensions DLL can request user interaction for any of the following.

-   Notify the user regarding the stages of a pre or post-association operation.

-   Prompt the user to enter his/her credentials for authentication during the post-association operation.

When it calls the [**Dot11ExtSendUIRequest**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_ui_request) function, the IHV Extensions DLL passes a pointer to a [**DOT11EXT\_IHV\_UI\_REQUEST**](/windows-hardware/drivers/ddi/wlanihv/ns-wlanihv-_dot11ext_ihv_ui_request) structure to the *pIhvUIRequest* parameter. The DOT11EXT\_IHV\_UI\_REQUEST structure specifies the request, such as the globally unique ID (GUID), which identifies the UI request as well as the COM class ID (CLSID) of the target UI page that will handle this request.

When the IHV UI Extensions DLL has completed the user notification, the operating system calls the [*Dot11ExtIhvProcessUIResponse*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_process_ui_response) function. If the user had entered any data through the notification, the operating system passes a pointer to the buffer, which contains the data, to the *pvResponseBuffer* parameter.

The operating system might periodically query the status of pending notification requests. In this situation, the operating system calls the [*Dot11ExtIhvIsUIRequestPending*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_is_ui_request_pending) and passes the GUID of the UI request to the *guidUIRequest* parameter.

When calling [**Dot11ExtSendUIRequest**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_ui_request), the IHV Extensions DLL must follow these guidelines.

-   The IHV Extensions DLL does not need to serialize the calls to [**Dot11ExtSendUIRequest**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_ui_request). The DLL can have more than one pending UI request at any time.

-   The UI request for a particular GUID is completed only when [*Dot11ExtIhvProcessUIResponse*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_process_ui_response) is called for that GUID. In this situation, the IHV Extensions DLL must not free any allocated resources for the UI request until *Dot11ExtIhvProcessUIResponse* is called.

-   All pending UI requests are canceled whenever [*Dot11ExtIhvAdapterReset*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_adapter_reset) or [*Dot11ExtIhvDeinitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_adapter) is called. All pending UI requests are also canceled whenever [*Dot11ExtIhvProcessSessionChange*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_process_session_change) is called with the *uEventType* parameter set to WTS\_SESSION\_LOGOFF.

    In these situations, the IHV Extensions DLL must free all allocated resources for each pending UI request.

The operating system can initiate user interaction itself whenever the connection state changes on the basic service set (BSS) network. In this situation, the operating system calls the [*Dot11ExtIhvQueryUIRequest*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_query_ui_request) function. The IHV Extensions DLL allocates a buffer and formats it as a [**DOT11EXT\_IHV\_UI\_REQUEST**](/windows-hardware/drivers/ddi/wlanihv/ns-wlanihv-_dot11ext_ihv_ui_request) structure. The DLL sets the members of the DOT11EXT\_IHV\_UI\_REQUEST structure to reference a UI page that is appropriate for the change in connection status. The operating system is responsible for displaying the UI page.

**Note**  The IHV Extensions must allocate the buffer that contains the [**DOT11EXT\_IHV\_UI\_REQUEST**](/windows-hardware/drivers/ddi/wlanihv/ns-wlanihv-_dot11ext_ihv_ui_request) structure through [**Dot11ExtAllocateBuffer**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_allocate_buffer). The DLL must not free the buffer after returning from [*Dot11ExtIhvQueryUIRequest*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_query_ui_request).

 

 

 
