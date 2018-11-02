---
title: Handling Socket Options and Control Codes for a SAN
description: Handling Socket Options and Control Codes for a SAN
ms.assetid: 5c07d0e3-b6d7-4daf-8b3f-80aafd7c7a37
keywords:
- Windows Sockets Direct WDK , SAN socket options
- SAN sockets WDK , options
- retrieving SAN socket options
- SAN service providers WDK , status information
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Socket Options and Control Codes for a SAN





The Windows Sockets switch, in conjunction with the TCP/IP provider, handles most **WSPGetSockOpt**, **WSPSetSockOpt**, and **WSPIoctl** calls initiated by applications. These requests are generally to set and retrieve options and operating parameters associated with an application's socket. The switch does not generally forward these calls to a SAN service provider except as described in the following sections.

### Retrieving SAN socket options

The Windows Sockets switch calls a SAN service provider's [**WSPGetSockOpt**](https://msdn.microsoft.com/library/windows/hardware/ff566292) function and passes one of the following socket options to retrieve the current value of that option, if the SAN service provider supports that option:

<a href="" id="so-debug"></a>SO\_DEBUG  
SAN service providers are not required to support this option. They are encouraged, but not required, to supply output debug information if applications set the SO\_DEBUG option.

<a href="" id="so-max-msg-size"></a>SO\_MAX\_MSG\_SIZE  
A SAN service provider must support this option if the underlying SAN transport is message-oriented and the transport limits the amount of data that the switch can send in a call to the SAN service provider's [**WSPSend**](https://msdn.microsoft.com/library/windows/hardware/ff566316) function. The switch does not subsequently pass send requests to the SAN service provider that exceed the size that the SAN service provider returns for the value of this option.

<a href="" id="so-max-rdma-size"></a>SO\_MAX\_RDMA\_SIZE  
A SAN service provider must support this option if the underlying SAN transport limits the amount of data that the switch can transfer in calls to either the SAN service provider's [**WSPRdmaRead**](https://msdn.microsoft.com/library/windows/hardware/ff566304) or [**WSPRdmaWrite**](https://msdn.microsoft.com/library/windows/hardware/ff566306) function. The switch does not subsequently pass RDMA transfer requests to the SAN service provider that exceed the size that the SAN service provider returns for the value of this option.

<a href="" id="so-rdma-threshold-size"></a>SO\_RDMA\_THRESHOLD\_SIZE  
A SAN service provider supports this option to indicate its preference for the minimum amount of data that the switch can transfer in calls to either the SAN service provider's **WSPRdmaRead** or **WSPRdmaWrite** function. However, the switch can set the actual threshold to a value different from the value returned by the SAN service provider. The switch subsequently calls the **WSPRdmaRead** or **WSPRdmaWrite** function to transfer data blocks (RDMA transfers) that exceed the size of this threshold and the **WSPSend** or **WSPRecv** function to transfer data blocks (message-oriented transfers) that are less than or equal to the size of this threshold.

<a href="" id="so-group-id--so-group-priority"></a>SO\_GROUP\_ID, SO\_GROUP\_PRIORITY  
A SAN service provider must support these options if it supports quality of service (QoS). Otherwise, the switch forwards these options to the TCP/IP provider, which maintains default values. A SAN service provider indicates that it supports QoS by setting the XP1\_QOS\_SUPPORTED bit in the **dwServiceFlags** member of the WSAPROTOCOL\_INFO structure.

### Setting SAN socket options

The Windows Sockets switch calls a SAN service provider's [**WSPSetSockOpt**](https://msdn.microsoft.com/library/windows/hardware/ff566318) function and passes one of the following socket options to set a value for that option, if the SAN service provider supports that option:

<a href="" id="so-debug"></a>SO\_DEBUG  
For a description of this socket option, see the preceding list.

<a href="" id="so-group-priority"></a>SO\_GROUP\_PRIORITY  
For a description of this socket option, see the preceding list.

### Accessing SAN socket information

The Windows Sockets switch calls a SAN service provider's [**WSPIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff566296) function and passes one of the following control codes to set or retrieve information for that SAN service provider, if the SAN service provider supports that control code:

<a href="" id="sio-get-extension-function-pointer"></a>SIO\_GET\_EXTENSION\_FUNCTION\_POINTER  
Retrieves a pointer to an extension function that a SAN service provider must support. For more information about extension functions, see [Windows Sockets SPI Extensions for SANs](windows-sockets-spi-extensions-for-sans.md). The input buffer of the **WSPIoctl** call contains the GUID whose value identifies the specified extension function. The SAN service provider returns the pointer to the requested function in **WSPIoctl**'s output buffer. The following table contains GUIDs for extension functions that a SAN service provider can support:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Extension function</th>
<th align="left">GUID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566311" data-raw-source="[&lt;strong&gt;WSPRegisterMemory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566311)"><strong>WSPRegisterMemory</strong></a></p></td>
<td align="left"><p>{C0B422F5-F58C-11d1-AD6C-00C04FA34A2D}</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566279" data-raw-source="[&lt;strong&gt;WSPDeregisterMemory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566279)"><strong>WSPDeregisterMemory</strong></a></p></td>
<td align="left"><p>{C0B422F6-F58C-11d1-AD6C-00C04FA34A2D}</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566313" data-raw-source="[&lt;strong&gt;WSPRegisterRdmaMemory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566313)"><strong>WSPRegisterRdmaMemory</strong></a></p></td>
<td align="left"><p>{C0B422F7-F58C-11d1-AD6C-00C04FA34A2D}</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566281" data-raw-source="[&lt;strong&gt;WSPDeregisterRdmaMemory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566281)"><strong>WSPDeregisterRdmaMemory</strong></a></p></td>
<td align="left"><p>{C0B422F8-F58C-11d1-AD6C-00C04FA34A2D}</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566306" data-raw-source="[&lt;strong&gt;WSPRdmaWrite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566306)"><strong>WSPRdmaWrite</strong></a></p></td>
<td align="left"><p>{C0B422F9-F58C-11d1-AD6C-00C04FA34A2D}</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566304" data-raw-source="[&lt;strong&gt;WSPRdmaRead&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566304)"><strong>WSPRdmaRead</strong></a></p></td>
<td align="left"><p>{C0B422FA-F58C-11d1-AD6C-00C04FA34A2D}</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566299" data-raw-source="[&lt;strong&gt;WSPMemoryRegistrationCacheCallback&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566299)"><strong>WSPMemoryRegistrationCacheCallback</strong></a></p></td>
<td align="left"><p>{E5DA4AF8-D824-48CD-A799-6337A98ED2AF}</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="sio-get-qos--sio-get-group-qos--sio-set-qos--sio-set-group-qos"></a>SIO\_GET\_QOS, SIO\_GET\_GROUP\_QOS, SIO\_SET\_QOS, SIO\_SET\_GROUP\_QOS  
A SAN service provider must support these control codes if it supports QoS. Otherwise, the switch forwards these options to the TCP/IP provider, which maintains default values. A provider indicates that it supports QoS by setting the XP1\_QOS\_SUPPORTED bit in the **dwServiceFlags** member of the WSAPROTOCOL\_INFO structure.

<a href="" id="sio-address-list-query"></a>SIO\_ADDRESS\_LIST\_QUERY  
Retrieves the list of local IP addresses that are assigned to the network interface cards (NICs) that the SAN service provider controls. The SAN service provider uses a SOCKET\_ADDRESS\_LIST structure, defined as follows, to return the list in **WSPIoctl**'s output buffer:

```C++
typedef struct _SOCKET_ADDRESS_LIST {
    INT             iAddressCount; 
    SOCKET_ADDRESS  Address[1]; 
} SOCKET_ADDRESS_LIST, FAR * LPSOCKET_ADDRESS_LIST;
```

The members of this structure contain the following information:

<a href="" id="iaddresscount"></a>**iAddressCount**  
Specifies the number of address structures in the list.

<a href="" id="address"></a>**Address**  
Array of IP address structures.

The switch uses this IOCTL code internally to decide whether to use a given SAN service provider to execute an application's requests to make connections or to listen for incoming connections. The switch forwards actual application requests for the list of local IP addresses to the TCP/IP provider. The switch also uses the TCP/IP provider to detect changes in address lists that all SAN service providers service. After TCP/IP reports a change, the switch queries all SAN service providers to refresh their lists.

 

 





