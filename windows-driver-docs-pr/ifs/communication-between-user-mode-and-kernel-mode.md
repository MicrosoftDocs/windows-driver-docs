---
title: Communication Between User Mode and Kernel Mode
description: Communication Between User Mode and Kernel Mode
ms.assetid: ddfec0d0-ec7d-4f76-91b8-2cc34cfacf4e
keywords:
- filter manager WDK file system minifilter , communication server ports
- communication server ports WDK file system minifilter
- filter manager WDK file system minifilter , user-mode/kernel-mode communication
- kernel-mode communication WDK file system minifilter
- user-mode communication WDK file system minifilter
- ports WDK , file system minifilter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Communication Between User Mode and Kernel Mode


The filter manager supports communication between user mode and kernel mode through communication ports. The minifilter driver controls security on the port by specifying a security descriptor to be applied to the communication port object. Communication through a communication port is not buffered, so it is faster and more efficient. A user-mode application or service can reply to messages from a minifilter driver for bidirectional communication.

When the minifilter driver creates a communication server port, it implicitly begins to listen for incoming connections on the port. When a user-mode caller attempts to connect to the port, the filter manager calls the minifilter driver's [**ConnectNotifyCallback**](https://msdn.microsoft.com/library/windows/hardware/ff541931) routine with a handle to the newly created connection. When the filter manager regains control, it passes the user-mode caller a separate file handle that represents the user-mode caller's endpoint to the connection. This handle can be used to associate I/O completion ports with the listener port.

A connection is accepted only if the user-mode caller has sufficient access as specified by the security descriptor on the port. Each connection to the port gets its own message queue and private endpoints.

Closing either endpoint (kernel or user) terminates that connection. When a user-mode caller closes its handle to the endpoint, the filter manager calls the minifilter driver's [**DisconnectNotifyCallback**](https://msdn.microsoft.com/library/windows/hardware/ff541931) routine so the minifilter driver can close its handle to the connection.

Closing the communication server port prevents new connections but does not terminate existing connections. The filter manager terminates existing connections when the minifilter driver unloads.

### <span id="Filter_Manager_Routines_for_Communication_Between_User_Mode_and_Kernel_Mode"></span><span id="filter_manager_routines_for_communication_between_user_mode_and_kernel_mode"></span><span id="FILTER_MANAGER_ROUTINES_FOR_COMMUNICATION_BETWEEN_USER_MODE_AND_KERNEL_MODE"></span>Filter Manager Routines for Communication Between User Mode and Kernel Mode

The filter manager provides the following support routines for kernel-mode minifilter drivers to communicate with user-mode applications:

[**FltCloseClientPort**](https://msdn.microsoft.com/library/windows/hardware/ff541867)

[**FltCloseCommunicationPort**](https://msdn.microsoft.com/library/windows/hardware/ff541871)

[**FltCreateCommunicationPort**](https://msdn.microsoft.com/library/windows/hardware/ff541931)

[**FltSendMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544378)

The following support routines are provided for user-mode applications to communicate with minifilter drivers:

[**FilterConnectCommunicationPort**](https://msdn.microsoft.com/library/windows/hardware/ff540460)

[**FilterGetMessage**](https://msdn.microsoft.com/library/windows/hardware/ff540506)

[**FilterReplyMessage**](https://msdn.microsoft.com/library/windows/hardware/ff541508)

[**FilterSendMessage**](https://msdn.microsoft.com/library/windows/hardware/ff541513)

### <span id="Minifilter_Driver_Callback_Routines_for_Communication_Between_User_Mode_and_Kernel_Mode"></span><span id="minifilter_driver_callback_routines_for_communication_between_user_mode_and_kernel_mode"></span><span id="MINIFILTER_DRIVER_CALLBACK_ROUTINES_FOR_COMMUNICATION_BETWEEN_USER_MODE_AND_KERNEL_MODE"></span>Minifilter Driver Callback Routines for Communication Between User Mode and Kernel Mode

The following minifilter driver callback routines are passed as parameters to [**FltCreateCommunicationPort**](https://msdn.microsoft.com/library/windows/hardware/ff541931):

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Callback Routine Name</th>
<th align="left">Callback Routine Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>ConnectNotifyCallback</em></p></td>
<td align="left"><p>PFLT_CONNECT_NOTIFY</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>DisconnectNotifyCallback</em></p></td>
<td align="left"><p>PFLT_DISCONNECT_NOTIFY</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>MessageNotifyCallback</em></p></td>
<td align="left"><p>PFLT_MESSAGE_NOTIFY</p></td>
</tr>
</tbody>
</table>

 

 

 




