---
title: NDIS 6.0 Support for Task Offload
description: NDIS 6.0 Support for Task Offload
ms.assetid: b083be9e-3b06-4bb0-b7e6-13b246fddd90
keywords:
- checksum tasks WDK networking
- LSOV1 WDK networking
- IPsec WDK networking
- large send offload WDK networking
- LSOV2 WDK networking
- connection offload WDK networking
- chimney offload WDK networking
- task offload porting WDK networking , type
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS 6.0 Support for Task Offload





NDIS 6.0 and later support updated versions of the following task offload services, which are provided by NDIS 5.1 and earlier drivers:

<a href="" id="checksum-tasks"></a>Checksum tasks  
The TCP/IP transport can offload the calculation and validation of IP and TCP checksums.

<a href="" id="internet-protocol-security--ipsec-"></a>Internet protocol security (IPsec)  
The TCP/IP transport can offload the calculation and validation of encrypted checksums for authentication headers (AH), encapsulating security payloads (ESP), or both. The TCP/IP transport can also offload the encryption and decryption of ESP payloads and the encryption and decryption of user datagram protocol (UDP)-encapsulated ESP data packets.

<a href="" id="large-send-offload-version-1--lsov1-"></a>Large send offload version 1 (LSOV1)  
The TCP/IP transport supports large send offload version 1 (LSOV1). With LSOV1, the TCP/IP transport can offload the segmentation of large TCP packets.

In addition to the updated task offload services, NDIS 6.0 also supports the following TCP/IP offload services:

<a href="" id="large-send-offload-version-2--lsov2-"></a>Large send offload version 2 (LSOV2)  
The NDIS large send offload version 2 (LSOV2) interface is an enhanced version of LSOV1. For more information about offloading the segmentation of large packets in NDIS 6.0, see [Offloading the Segmentation of Large TCP Packets in NDIS 6.0](offloading-the-segmentation-of-large-tcp-packets-in-ndis-6-0.md).

<a href="" id="connection-offload"></a>Connection offload  
The NDIS connection offload interface provides hooks to enable configuration of connection offload services such as TCP chimney offload. For more information about connection offload services in NDIS 6.0, see [Offloading TCP/IP Connections in NDIS 6.0](offloading-tcp-ip-connections-in-ndis-6-0.md).

The TCP/IP transport in NDIS 6.0 and later supports task offload for both IPv4 and IPv6 packets.

Unlike NDIS 5.1 and earlier drivers, NDIS 6.0 and later miniport drivers support task offload in a multiple-protocol driver environment. Multiple NDIS 6.0 and later protocol drivers that are bound to a task offload-capable miniport adapter can configure task offload services.

 

 





