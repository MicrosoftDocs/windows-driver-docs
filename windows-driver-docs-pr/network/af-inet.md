---
title: AF_INET
description: AF_INET
ms.assetid: 59e12f8d-02eb-413c-bc04-6b9b6e4adde6
ms.date: 08/08/2017
keywords: 
 -AF_INET Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# AF\_INET


The AF\_INET address family is the address family for IPv4.

### Socket Address Structure

An IPv4 transport address is specified with the [**SOCKADDR\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff570823) structure.

### Socket Types

IPv4 supports the following socket types:

<a href="" id="sock-stream"></a>SOCK\_STREAM  
Supports reliable connection-oriented byte stream communication.

<a href="" id="sock-dgram"></a>SOCK\_DGRAM  
Supports unreliable connectionless datagram communication.

<a href="" id="sock-raw"></a>SOCK\_RAW  
Supports raw access to the transport protocol.

A WSK application specifies a socket type when it calls the [**WskSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571149) function or the [**WskSocketConnect**](https://msdn.microsoft.com/library/windows/hardware/ff571150) function to create a new socket.

### Protocols

The following IPv4 IPPROTO\_*XXX* protocol values of the IPPROTO enumeration are defined in the WSK header files:

<a href="" id="ipproto-ip"></a>IPPROTO\_IP  
Internet protocol options

<a href="" id="ipproto-icmp"></a>IPPROTO\_ICMP  
Internet control message protocol

<a href="" id="ipproto-igmp"></a>IPPROTO\_IGMP  
Internet group management protocol

<a href="" id="ipproto-ggp"></a>IPPROTO\_GGP  
Gateway to gateway protocol

<a href="" id="ipproto-ipv4"></a>IPPROTO\_IPV4  
IPv4 encapsulation

<a href="" id="ipproto-st"></a>IPPROTO\_ST  
Stream protocol

<a href="" id="ipproto-tcp"></a>IPPROTO\_TCP  
Transmission control protocol

<a href="" id="ipproto-cbt"></a>IPPROTO\_CBT  
Core based trees protocol

<a href="" id="ipproto-egp"></a>IPPROTO\_EGP  
Exterior gateway protocol

<a href="" id="ipproto-igp"></a>IPPROTO\_IGP  
Private interior gateway protocol

<a href="" id="ipproto-pup"></a>IPPROTO\_PUP  
PARC universal packet protocol

<a href="" id="ipproto-udp"></a>IPPROTO\_UDP  
User datagram protocol

<a href="" id="ipproto-idp"></a>IPPROTO\_IDP  
Internet datagram protocol

<a href="" id="ipproto-rdp"></a>IPPROTO\_RDP  
Reliable data protocol

<a href="" id="ipproto-nd"></a>IPPROTO\_ND  
Net disk protocol

<a href="" id="ipproto-iclfxbm"></a>IPPROTO\_ICLFXBM  
Wideband monitoring

<a href="" id="ipproto-pim"></a>IPPROTO\_PIM  
Protocol independent multicast

<a href="" id="ipproto-pgm"></a>IPPROTO\_PGM  
Pragmatic general multicast

<a href="" id="ipproto-l2tp"></a>IPPROTO\_L2TP  
Level 2 tunneling protocol

<a href="" id="ipproto-sctp"></a>IPPROTO\_SCTP  
Stream control transmission protocol

<a href="" id="ipproto-raw"></a>IPPROTO\_RAW  
Raw IP packets

Additional protocols are supported through the use of raw sockets.

A WSK application specifies a protocol when it calls the [**WskSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571149) function or the [**WskSocketConnect**](https://msdn.microsoft.com/library/windows/hardware/ff571150) function to create a new socket.

A WSK application also specifies a protocol (as the *Level* parameter) when it calls the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function to set or retrieve transport protocol level or network protocol level socket options.

### Combinations

IPv4 supports the following combinations of socket types and protocols for each WSK [socket category](https://msdn.microsoft.com/library/windows/hardware/ff571093):

Basic Sockets
SOCK\_STREAM + IPPROTO\_TCP
SOCK\_DGRAM + IPPROTO\_UDP
SOCK\_RAW + IPPROTO\_*Xxx*
Listening Sockets
SOCK\_STREAM + IPPROTO\_TCP

Datagram Sockets
SOCK\_DGRAM + IPPROTO\_UDP
SOCK\_RAW + IPPROTO\_*Xxx*
Connection-Oriented Sockets
SOCK\_STREAM + IPPROTO\_TCP

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ws2def.h (include Wsk.h)</td>
</tr>
</tbody>
</table>

 

 




