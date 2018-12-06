---
title: Keywords Not Displayed in the User Interface
description: Keywords Not Displayed in the User Interface
ms.assetid: 0d2aeaa3-4e47-413b-907f-5e70b34f0725
keywords:
- installation keywords WDK networking , non-visible
- non-visible keywords WDK DNIS miniport
- hidden keywords WDK DNIS miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Keywords Not Displayed in the User Interface





NDIS 6.0 and later versions of NDIS provide some standardized keywords for miniport drivers of network devices. These standardized keywords appear in INF files but not in the user interface.

These general keywords are described in the following list. For more information about a particular keyword, search for the keyword in the WDK documentation.

<a href="" id="-iftype"></a>**\*IfType**  
The NDIS interface type for a device. For more information about the NDIS interface type, see [NDIS Interface Types](https://msdn.microsoft.com/library/windows/hardware/ff565767).

<a href="" id="-mediatype"></a>**\*MediaType**  
The media type for a device. For more information about the media type of the miniport adapter, see [OID\_GEN\_MEDIA\_SUPPORTED](https://msdn.microsoft.com/library/windows/hardware/ff569609).

<a href="" id="-physicalmediatype"></a>**\*PhysicalMediaType**  
The physical media type for a device. For more information about the physical media type of the miniport adapter, see [OID\_GEN\_PHYSICAL\_MEDIUM](https://msdn.microsoft.com/library/windows/hardware/ff569621).

<a href="" id="-ndisdevicetype-------"></a>**\*NdisDeviceType**   
The type of the device. The default value is zero, which indicates a standard networking device that connects to a network. Set **\*NdisDeviceType** to NDIS\_DEVICE\_TYPE\_ENDPOINT (1) if this device is an endpoint device and is not a true network interface that connects to a network. For example, you must specify NDIS\_DEVICE\_TYPE\_ENDPOINT for devices such as smart phones that use a networking infrastructure to communicate to the local computer system but do not provide connectivity to an external network.

**Note**  Windows Vista automatically identifies and monitors the networks a computer connects to. If the NDIS\_DEVICE\_TYPE\_ENDPOINT flag is set, the device is an endpoint device and is not a connection to a true external network. Consequently, Windows ignores the endpoint device when it identifies networks. The Network Awareness APIs indicate that the device does not connect the computer to a network. For end users in this situation, the Network and Sharing Center and the network icon in the notification area do not show the NDIS endpoint device as connected. However, the connection is shown in the Network Connections Folder.

 

 

 





