---
title: Porting TDI Drivers to Winsock Kernel
description: To port your TDI driver to Winsock Kernel (WSK), you'll need to convert TDI tasks to their WSK equivalents as shown in the following table.
ms.assetid: 23662BF1-92EC-4C07-9A8D-F8F1D7D51692
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting TDI Drivers to Winsock Kernel


To port your TDI driver to Winsock Kernel (WSK), you'll need to convert TDI tasks to their WSK equivalents as shown in the following table.

| Tasks                            | TDI                                                                                       | Winsock Kernel (WSK)                                                                                                          |
|----------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Register and Deregister          | N/A                                                                                       | [**WskRegister**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nf-wsk-wskregister) and [**WskDeregister**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nf-wsk-wskderegister)                                       |
| Capture and Release Provider NPI | N/A                                                                                       | [**WskCaptureProviderNPI**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nf-wsk-wskcaptureprovidernpi) and [**WskReleaseProviderNPI**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nf-wsk-wskreleaseprovidernpi)   |
| Create Address File Object       | Create *EaBuffer*, then call [**ZwCreateFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)                      | No longer necessary. See [**WskSocket**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_socket).                                                                 |
| Create Connection File Object    | Create connection *EaBuffer*, then call [**ZwCreateFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)           | No longer necessary. See [**WskSocket**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_socket) and [*WskAcceptEvent*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_accept_event).                 |
| Associate Address                | [**TDI\_ASSOCIATE\_ADDRESS**](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff565080(v=vs.85))                                | [**WskBind**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_bind)                                                                                               |
| Set Event Handlers               | [**TDI\_SET\_EVENT\_HANDLER**](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff565576(v=vs.85))                               | [**WskControlSocket**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket) or static variation using [**WskControlClient**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_client) |
| Clear Event Handlers             | [**TDI\_SET\_EVENT\_HANDLER**](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff565576(v=vs.85))                               | [**WskControlSocket**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket)                                                                             |
| Connect                          | [**TDI\_CONNECT**](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff565083(v=vs.85))                                                     | [**WskConnect**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_connect)                                                                                         |
| Disconnect                       | [**TDI\_DISCONNECT**](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff565090(v=vs.85))                                               | [**WskDisconnect**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_disconnect)                                                                                   |
| Send                             | [**TDI\_SEND**](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff565549(v=vs.85))                                                           | [**WskSend**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_send)                                                                                               |
| Receive                          | [**TDI\_RECEIVE**](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff565131(v=vs.85))                                                     | [**WskReceive**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_receive)                                                                                         |
| Disassociate Address             | [**TDI\_DISASSOCIATE\_ADDRESS**](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff565089(v=vs.85))                          | N/A                                                                                                                           |
| Receive Handler                  | [**ClientEventReceive**](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff545260(v=vs.85)), [**TDI\_RECEIVE**](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff565131(v=vs.85)) | [*WskReceiveEvent*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_receive_event)                                                                                 |
| Connect Handler                  | [**ClientEventConnect**](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff544257(v=vs.85)), [**TDI\_CONNECT**](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff565083(v=vs.85)) | [**WskAccept**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_accept)                                                                                           |
| Close Socket or Connection       | [**ObDereferenceObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject) or [**ZwClose**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose)    | [**WskCloseSocket**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_close_socket)                                                                                 |

 

 

 





