---
title: Porting TDI Drivers to Winsock Kernel
description: To port your TDI driver to Winsock Kernel (WSK), you'll need to convert TDI tasks to their WSK equivalents as shown in the following table.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting TDI Drivers to Winsock Kernel


To port your TDI driver to Winsock Kernel (WSK), you'll need to convert TDI tasks to their WSK equivalents as shown in the following table.

| Tasks                            | TDI                                                                                       | Winsock Kernel (WSK)                                                                                                          |
|----------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Register and Deregister          | N/A                                                                                       | [**WskRegister**](/windows-hardware/drivers/ddi/wsk/nf-wsk-wskregister) and [**WskDeregister**](/windows-hardware/drivers/ddi/wsk/nf-wsk-wskderegister)                                       |
| Capture and Release Provider NPI | N/A                                                                                       | [**WskCaptureProviderNPI**](/windows-hardware/drivers/ddi/wsk/nf-wsk-wskcaptureprovidernpi) and [**WskReleaseProviderNPI**](/windows-hardware/drivers/ddi/wsk/nf-wsk-wskreleaseprovidernpi)   |
| Create Address File Object       | Create *EaBuffer*, then call [**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)                      | No longer necessary. See [**WskSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_socket).                                                                 |
| Create Connection File Object    | Create connection *EaBuffer*, then call [**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)           | No longer necessary. See [**WskSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_socket) and [*WskAcceptEvent*](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_accept_event).                 |
| Associate Address                | [**TDI\_ASSOCIATE\_ADDRESS**](/previous-versions/windows/hardware/network/ff565080(v=vs.85))                                | [**WskBind**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_bind)                                                                                               |
| Set Event Handlers               | [**TDI\_SET\_EVENT\_HANDLER**](/previous-versions/windows/hardware/network/ff565576(v=vs.85))                               | [**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket) or static variation using [**WskControlClient**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_client) |
| Clear Event Handlers             | [**TDI\_SET\_EVENT\_HANDLER**](/previous-versions/windows/hardware/network/ff565576(v=vs.85))                               | [**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket)                                                                             |
| Connect                          | [**TDI\_CONNECT**](/previous-versions/windows/hardware/network/ff565083(v=vs.85))                                                     | [**WskConnect**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_connect)                                                                                         |
| Disconnect                       | [**TDI\_DISCONNECT**](/previous-versions/windows/hardware/network/ff565090(v=vs.85))                                               | [**WskDisconnect**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_disconnect)                                                                                   |
| Send                             | [**TDI\_SEND**](/previous-versions/windows/hardware/network/ff565549(v=vs.85))                                                           | [**WskSend**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_send)                                                                                               |
| Receive                          | [**TDI\_RECEIVE**](/previous-versions/windows/hardware/network/ff565131(v=vs.85))                                                     | [**WskReceive**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_receive)                                                                                         |
| Disassociate Address             | [**TDI\_DISASSOCIATE\_ADDRESS**](/previous-versions/windows/hardware/network/ff565089(v=vs.85))                          | N/A                                                                                                                           |
| Receive Handler                  | [**ClientEventReceive**](/previous-versions/windows/hardware/network/ff545260(v=vs.85)), [**TDI\_RECEIVE**](/previous-versions/windows/hardware/network/ff565131(v=vs.85)) | [*WskReceiveEvent*](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_receive_event)                                                                                 |
| Connect Handler                  | [**ClientEventConnect**](/previous-versions/windows/hardware/network/ff544257(v=vs.85)), [**TDI\_CONNECT**](/previous-versions/windows/hardware/network/ff565083(v=vs.85)) | [**WskAccept**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_accept)                                                                                           |
| Close Socket or Connection       | [**ObDereferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject) or [**ZwClose**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose)    | [**WskCloseSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_close_socket)                                                                                 |

 

 

