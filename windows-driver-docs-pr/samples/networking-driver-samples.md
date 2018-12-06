---
title: Networking driver samples
description: The driver samples in this directory provide a starting point for writing a custom network driver for your device.
ms.assetid: 97C88E82-96AA-41AD-9B1F-3EB848A08BD8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Networking driver samples


The driver samples in this directory provide a starting point for writing a custom network driver for your device.

## Networking


| Sample Name                                                | Solution                                                                 | Description                                                                                                                                                                                                                            |
|------------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bindview                                                   | [bindview](http://go.microsoft.com/fwlink/p/?LinkId=617732)              | An application that demonstrates how to use INetCfg APIs to enumerate, install, uninstall, bind and unbind network components.                                                                                                         |
| Fakemodem                                                  | [fakemodem](http://go.microsoft.com/fwlink/p/?LinkId=617733)             | Demonstrates a simple controller-less modem driver.                                                                                                                                                                                    |
| Hyper-V Extensible Switch Extension Filter                 | [extensions](http://go.microsoft.com/fwlink/p/?LinkId=617913)            | A base library used to implement a Hyper-V Extensible Switch extension filter driver.                                                                                                                                                  |
| NDIS 6.0 Filter                                            | [filter](http://go.microsoft.com/fwlink/p/?LinkId=617915)                | The sample is a do-nothing pass-through NDIS 6 filter driver demonstrating the basic principles of an NDIS 6.0 Filter driver.                                                                                                          |
| NDIS MUX Intermediate Driver and Notify Object             | [mux](http://go.microsoft.com/fwlink/p/?LinkId=617916)                   | An NDIS 6.0 driver that demonstrates the operation of an “N:1” MUX driver. The sample create multiple virtual network devices on top of a single lower adapter.                                                                        |
| Connectionless NDIS 6.0 and 6.3 Protocol Driver            | [ndisprot60](http://go.microsoft.com/fwlink/p/?LinkId=617917)            | This driver supports sending and receiving raw Ethernet frames using ReadFile/WriteFile calls from user-mode. As an NDIS protocol driver, it illustrates how to establish and tear down bindings to Ethernet adapters.                 |
| Connectionless NDIS 6.0 Protocol Driver                    | [ndisprot\_kmdf](http://go.microsoft.com/fwlink/p/?LinkId=620197)        | This driver supports sending and receiving raw Ethernet frames using ReadFile/WriteFile calls from user-mode. As an NDIS protocol driver, it illustrates how to establish and tear down bindings to Ethernet adapters.                 |
| NDIS Virtual Miniport Driver                               | [netvmini](http://go.microsoft.com/fwlink/p/?LinkId=617918)              | Demonstrates the functionality of an NDIS miniport driver without requiring a physical network adapter.                                                                                                                                |
| Radio Switch Test Driver for OSR USB-FX2 Development Board | [HidSwitchDriverSample](http://go.microsoft.com/fwlink/p/?LinkId=617919) | Demonstrates how to structure a HID driver for radio switches for the OSR USB-FX2 Development Board.                                                                                                                                   |
| Radio Manager                                              | [RadioManagerSample](http://go.microsoft.com/fwlink/p/?LinkId=617920)    | Demonstrates how to structure a Radio Manager for use with the Windows Radio Management APIs.                                                                                                                                          |
| WFP Packet Modification                                    | [ddproxy](http://go.microsoft.com/fwlink/p/?LinkId=617930)               | Demonstrates the packet modification capabilities of the Windows Filtering Platform (WFP).                                                                                                                                             |
| WFP Traffic Inspection                                     | [inspect](http://go.microsoft.com/fwlink/p/?LinkId=617931)               | Demonstrates the traffic inspection capabilities of the Windows Filtering Platform (WFP).                                                                                                                                              |
| WFP MSN Messenger Monitor                                  | [msnmntr](http://go.microsoft.com/fwlink/p/?LinkId=617932)               | A sample application and driver demonstrating the stream inspection capabilities of the Windows Filtering Platform (WFP).                                                                                                              |
| WFP Stream Edit                                            | [stmedit](http://go.microsoft.com/fwlink/p/?LinkId=617933)               | Demonstrates replacing a string pattern for a Transmission Control Protocol (TCP) connection using the Windows Filtering Platform (WFP).                                                                                               |
| Windows Filtering Platform                                 | [WFPSampler](http://go.microsoft.com/fwlink/p/?LinkId=620198)            | This is a sample firewall. It has a command-line interface which allows adding filters at various WFP layers under various conditions. Additionally, it exposes callouts for injection, basic action, proxying, and stream inspection. |
| Native Wi-Fi IHV Service                                   | [wlan](http://go.microsoft.com/fwlink/p/?LinkId=617934)                  | Demonstrates IHV extensibility for native Wi-Fi.                                                                                                                                                                                       |
| WSK TCP Echo Server                                        | [echosrv](http://go.microsoft.com/fwlink/p/?LinkId=617935)               | This sample driver is a minimal driver meant to demonstrate the usage of the Winsock Kernel (WSK) programming interface.                                                                                                               |

 

 

 




