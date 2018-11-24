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
| Register and Deregister          | N/A                                                                                       | [**WskRegister**](https://msdn.microsoft.com/library/windows/hardware/ff571143) and [**WskDeregister**](https://msdn.microsoft.com/library/windows/hardware/ff571128)                                       |
| Capture and Release Provider NPI | N/A                                                                                       | [**WskCaptureProviderNPI**](https://msdn.microsoft.com/library/windows/hardware/ff571122) and [**WskReleaseProviderNPI**](https://msdn.microsoft.com/library/windows/hardware/ff571145)   |
| Create Address File Object       | Create *EaBuffer*, then call [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424)                      | No longer necessary. See [**WskSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571149).                                                                 |
| Create Connection File Object    | Create connection *EaBuffer*, then call [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424)           | No longer necessary. See [**WskSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571149) and [*WskAcceptEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571120).                 |
| Associate Address                | [**TDI\_ASSOCIATE\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff565080)                                | [**WskBind**](https://msdn.microsoft.com/library/windows/hardware/ff571121)                                                                                               |
| Set Event Handlers               | [**TDI\_SET\_EVENT\_HANDLER**](https://msdn.microsoft.com/library/windows/hardware/ff565576)                               | [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) or static variation using [**WskControlClient**](https://msdn.microsoft.com/library/windows/hardware/ff571126) |
| Clear Event Handlers             | [**TDI\_SET\_EVENT\_HANDLER**](https://msdn.microsoft.com/library/windows/hardware/ff565576)                               | [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127)                                                                             |
| Connect                          | [**TDI\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff565083)                                                     | [**WskConnect**](https://msdn.microsoft.com/library/windows/hardware/ff571125)                                                                                         |
| Disconnect                       | [**TDI\_DISCONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff565090)                                               | [**WskDisconnect**](https://msdn.microsoft.com/library/windows/hardware/ff571129)                                                                                   |
| Send                             | [**TDI\_SEND**](https://msdn.microsoft.com/library/windows/hardware/ff565549)                                                           | [**WskSend**](https://msdn.microsoft.com/library/windows/hardware/ff571146)                                                                                               |
| Receive                          | [**TDI\_RECEIVE**](https://msdn.microsoft.com/library/windows/hardware/ff565131)                                                     | [**WskReceive**](https://msdn.microsoft.com/library/windows/hardware/ff571139)                                                                                         |
| Disassociate Address             | [**TDI\_DISASSOCIATE\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff565089)                          | N/A                                                                                                                           |
| Receive Handler                  | [**ClientEventReceive**](https://msdn.microsoft.com/library/windows/hardware/ff545260), [**TDI\_RECEIVE**](https://msdn.microsoft.com/library/windows/hardware/ff565131) | [*WskReceiveEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571140)                                                                                 |
| Connect Handler                  | [**ClientEventConnect**](https://msdn.microsoft.com/library/windows/hardware/ff544257), [**TDI\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff565083) | [**WskAccept**](https://msdn.microsoft.com/library/windows/hardware/ff571109)                                                                                           |
| Close Socket or Connection       | [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724) or [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417)    | [**WskCloseSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571124)                                                                                 |

 

 

 





