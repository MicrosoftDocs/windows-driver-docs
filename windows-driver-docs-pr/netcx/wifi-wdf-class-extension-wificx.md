---
title: Introduction to the Wi-Fi WDF class extension (WiFiCx)
description: An overview of the WiFiCx class extension.
keywords:
- WiFiCx WDF class extension, WiFiCx, WiFi NetAdapterCx
ms.date: 06/17/2021
ms.localizationpriority: medium
---

# Introduction to the Wi-Fi WDF class extension (WiFiCx)

Starting in Windows 11, the Windows Driver Kit (WDK) includes a Wi-Fi WDF class extension (WiFiCx) that enables you to write a KMDF-based client driver for a Wi-Fi device. WiFiCx gives you the power and flexibility of WDF and the networking performance of NDIS, and makes it easy to write a driver for your Wi-Fi device.

In addition to being a fully-fledged WDF client driver, WiFiCx drivers are also [NetAdapterCx](../netcx/index.md) client drivers just like other NIC drivers. The client driver interacts with WiFiCx for Wi-Fi media-specific functionality.

WiFiCx drivers run on Windows 11 only. 

## WiFiCx architecture

The following block diagram illustrates the WiFiCx architecture:

![WiFiCx architecture](images/wificx.png)

A WiFiCx client driver performs three categories of tasks based on its relationships with the framework:

- Calls [standard WDF APIs](/windows-hardware/drivers/ddi/_wdf/) for common device tasks like PnP and Power management.
- Calls [NetAdapterCx APIs](/windows-hardware/drivers/ddi/_netvista/#netadaptercx) for common network device operations like transmitting or receiving network packets.
- Calls [WiFiCx APIs](/windows-hardware/drivers/ddi/_netvista/#wificx) for Wi-Fi-specific control path operations like WDI command handling.

The topics in this section assume you already know how to write a [NetAdapterCx client driver](../netcx/index.md) for a basic NIC and focus only on WiFiCx-specific code:

[Writing a WiFiCx client driver](writing-a-wificx-client-driver.md)

[WiFiCx message structure](wificx-message-structure.md)

[WiFiCx TLV generator interface](wificx-tlv-generator-interface.md)

[WiFiCx TLVs](wdi-tlv-6-ghz-band-channel.md)

[WiFiCx task commands](oid-wdi-task-change-operation-mode.md)

[WiFiCx property commands](oid-wdi-abort-task.md)

[WiFiCx unsolicited status indications](ndis-status-wdi-indication-action-frame-received.md)

[WiFiCx WPA3-SAE authentication](wificx-wpa3-sae-authentication.md)

[WiFiCx design guide](wificx-low-latency-connection-quality.md)

[Dual STA connectivity](dual-sta-connectivity.md)