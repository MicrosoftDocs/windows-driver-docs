---
title: Communication Between User-mode and Minifilters
description: Communication Between User Mode and Minifilters
keywords:
- filter manager WDK file system minifilter , communication server ports
- communication server ports WDK file system minifilter
- filter manager WDK file system minifilter , user-mode/kernel-mode communication
- kernel-mode communication WDK file system minifilter
- user-mode communication WDK file system minifilter
- ports WDK , file system minifilter
ms.date: 07/10/2024
---

# Communication between user-mode and minifilters

*FltMgr* supports communication between user-mode (UM) applications and kernel-mode (KM) minifilters through communication ports. An example scenario is an antivirus application that needs to communicate with its KM minifilter counterpart to scan files for viruses and malware.

The minifilter controls security on the port by specifying a security descriptor to be applied to the communication port object. Communication through a communication port isn't buffered, so it's faster and more efficient.

A UM app or service can reply to messages from a minifilter for bidirectional communication. Communication is established as follows:

* A minifilter driver calls [**FltCreateCommunicationPort**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatecommunicationport) to
create a communication server port. As the creator of the *listener port*, the minifilter immediately implicitly begins to listen for incoming connections on the created port.

* When a UM app or service calls [**FilterConnectCommunicationPort**](/windows/win32/api/fltuser/nf-fltuser-filterconnectcommunicationport) to attempt to connect to the port, *FltMgr* calls the minifilter's [**ConnectNotifyCallback**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatecommunicationport) callback routine with a handle to the newly created connection. When the callback completes, *FltMgr* then passes the UM caller a separate file handle that represents the UM caller's endpoint to the connection. The UM caller can use this handle to associate multiple I/O completion ports with the listener port. This capability is useful to apps that need to handle high volumes of I/O operations concurrently.

*FltMgr* accepts the connection request only if the UM caller has sufficient access as specified by the security descriptor on the port. Each connection to the port gets its own message queue and private endpoints.

Closing either endpoint (kernel or user) terminates that connection. When a UM caller closes its handle to the endpoint, *FltMgr* calls the minifilter driver's [**DisconnectNotifyCallback**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatecommunicationport) routine so the minifilter driver can close its handle to the connection.

Closing the communication server port prevents new connections but doesn't terminate existing connections. *FltMgr* terminates existing connections when the minifilter driver unloads.

## *FltMgr* routines for communication between UM and KM

*FltMgr* provides the following support routines for minifilters to communicate with UM applications:

* [**FltCloseClientPort**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcloseclientport)
* [**FltCloseCommunicationPort**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltclosecommunicationport)
* [**FltCreateCommunicationPort**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatecommunicationport)
* [**FltSendMessage**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsendmessage)

UM applications and services can use the following system-supplied support routines to communicate with minifilter drivers:

* [**FilterConnectCommunicationPort**](/windows/win32/api/fltuser/nf-fltuser-filterconnectcommunicationport)
* [**FilterGetMessage**](/windows/win32/api/fltuser/nf-fltuser-filtergetmessage)
* [**FilterReplyMessage**](/windows/win32/api/fltuser/nf-fltuser-filterreplymessage)
* [**FilterSendMessage**](/windows/win32/api/fltuser/nf-fltuser-filtersendmessage)

## Minifilter callback routines for communication between UM and KM

A minifilter implements the following callback routines to support communication between UM and KM. It passes pointers to these routines when it calls [**FltCreateCommunicationPort**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatecommunicationport).

| Callback Routine Name      | Callback Routine Type |
| ---------------------      | --------------------- |
| **ConnectNotifyCallback**    | [**PFLT_CONNECT_NOTIFY**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_connect_notify) |
| **DisconnectNotifyCallback** | [**PFLT_DISCONNECT_NOTIFY**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_disconnect_notify) |
| **MessageNotifyCallback**    | [**PFLT_MESSAGE_NOTIFY**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_message_notify) |
