---
title: TCPMON Xcv Commands
description: TCPMON Xcv Commands
ms.assetid: 89aebc89-d81e-4d86-942e-d13b16c55fb3
keywords:
- print monitors WDK , TCPMON Xcv
- transceive (Xcv) commands WDK print
- Xcv commands WDK print
- TCPMON Xcv commands WDK print
- AddPort
- ConfigPort
- DeletePort
- GetConfigInfo
- HostAddress
- IPAddress
- MonitorUI
- SNMPCommunity
- SNMPDeviceIndex
- SNMPEnabled
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TCPMON Xcv Commands





This section describes the commands that can be specified in a call to the [**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) or [**XcvDataPort**](https://msdn.microsoft.com/library/windows/hardware/ff564258) function, when it is communicating with the standard TCP/IP port monitor (TCPMON). Each command is specified by the *pszDataName* string in the call to these functions. Certain commands require an input buffer, or an output buffer, or both. The *pInputData* and *pOutputData* parameters of these functions hold the addresses of these buffers.

The table that appears in the description of each of the following commands lists the **XcvData** and **XcvDataPort** parameters that are used with the commands. Note that the *hXcv* parameter (common to both functions) is not listed, nor is the **XcvData** function's *pdwStatus* parameter.

### AddPort Command

The **AddPort** command adds a standard TCP/IP port, which can be either an LPR port or a RAW TCP/IP port.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>XcvData Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>pszDataName</em></p></td>
<td><p>L&quot;AddPort&quot;</p></td>
</tr>
<tr class="even">
<td><p><em>pInputData</em></p></td>
<td><p>Address of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff559892" data-raw-source="[&lt;strong&gt;PORT_DATA_1&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559892)"><strong>PORT_DATA_1</strong></a> structure</p></td>
</tr>
<tr class="odd">
<td><p><em>cbInputData</em></p></td>
<td><p><strong>sizeof</strong>(PORT_DATA_1)</p></td>
</tr>
<tr class="even">
<td><p><em>pOutputData</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
<tr class="odd">
<td><p><em>cbOutputData</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>pcbOutputNeeded</em></p></td>
<td><p>Address of a DWORD</p></td>
</tr>
</tbody>
</table>

 

[**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) returns NO\_ERROR if it can add the port. In addition to the normal error codes, **XcvData** returns ERROR\_ACCESS\_DENIED if the user has insufficient privileges to create a port on the server. This command requires SERVER\_ACCESS\_ADMINISTER privilege. If the *pInputData* parameter is **NULL**, the function returns ERROR\_INVALID\_DATA. If *pInputData*--&gt;*dwVersion* is not equal to 1, the function returns ERROR\_INVALID\_LEVEL.

### ConfigPort Command

The **ConfigPort** command configures an existing standard TCP/IP port monitor port.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>XcvData Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>pszDataName</em></p></td>
<td><p>L&quot;ConfigPort&quot;</p></td>
</tr>
<tr class="even">
<td><p><em>pInputData</em></p></td>
<td><p>Address of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff559892" data-raw-source="[&lt;strong&gt;PORT_DATA_1&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559892)"><strong>PORT_DATA_1</strong></a> structure</p></td>
</tr>
<tr class="odd">
<td><p><em>cbInputData</em></p></td>
<td><p><strong>sizeof</strong>(PORT_DATA_1)</p></td>
</tr>
<tr class="even">
<td><p><em>pOutputData</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
<tr class="odd">
<td><p><em>cbOutputData</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>pcbOutputNeeded</em></p></td>
<td><p>Address of a DWORD</p></td>
</tr>
</tbody>
</table>

 

[**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) returns NO\_ERROR if it can configure the port. In addition to the normal error codes, **XcvData** returns ERROR\_ACCESS\_DENIED if the caller has insufficient privileges to perform the request. This command requires SERVER\_ACCESS\_ADMINISTER privilege. If the *pInputData* parameter is **NULL**, or the value in *cbInputData* is smaller than required, the function returns ERROR\_INVALID\_DATA. If *pInputData*--&gt;*dwVersion* is not equal to 1, the function returns ERROR\_INVALID\_LEVEL.

### DeletePort Command

The **DeletePort** command deletes a port from the standard TCP/IP port monitor.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>XcvData Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>pszDataName</em></p></td>
<td><p>L&quot;DeletePort&quot;</p></td>
</tr>
<tr class="even">
<td><p><em>pInputData</em></p></td>
<td><p>Address of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547436" data-raw-source="[&lt;strong&gt;DELETE_PORT_DATA_1&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547436)"><strong>DELETE_PORT_DATA_1</strong></a> structure</p></td>
</tr>
<tr class="odd">
<td><p><em>cbInputData</em></p></td>
<td><p><strong>sizeof</strong>(DELETE_PORT_DATA_1)</p></td>
</tr>
<tr class="even">
<td><p><em>pOutputData</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
<tr class="odd">
<td><p><em>cbOutputData</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>pcbOutputNeeded</em></p></td>
<td><p>Address of a DWORD</p></td>
</tr>
</tbody>
</table>

 

**XcvData** returns NO\_ERROR if the port is successfully deleted. In addition to the normal error codes, **XcvData** returns ERROR\_ACCESS\_DENIED if the caller has insufficient privileges on the server. This command requires SERVER\_ACCESS\_ADMINISTER privilege. If the *pInputData* parameter is **NULL**, or if the *cbInputData* parameter is smaller than required, the function returns ERROR\_INVALID\_DATA. If *pInputData*--&gt;*dwVersion* is not equal to 1, the function returns ERROR\_INVALID\_LEVEL.

### GetConfigInfo Command

The **GetConfigInfo** command obtains the configuration information of a particular port. In this case, the Xcv data handle must point to a particular standard TCP/IP port monitor port so that the port can be identified.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>XcvData Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>pszDataName</em></p></td>
<td><p>L&quot;GetConfigInfo&quot;</p></td>
</tr>
<tr class="even">
<td><p><em>pInputData</em></p></td>
<td><p>Address of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546300" data-raw-source="[&lt;strong&gt;CONFIG_INFO_DATA_1&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546300)"><strong>CONFIG_INFO_DATA_1</strong></a> structure</p></td>
</tr>
<tr class="odd">
<td><p><em>cbInputData</em></p></td>
<td><p><strong>sizeof</strong>(CONFIG_INFO_DATA_1)</p></td>
</tr>
<tr class="even">
<td><p><em>pOutputData</em></p></td>
<td><p>Address of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff559892" data-raw-source="[&lt;strong&gt;PORT_DATA_1&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559892)"><strong>PORT_DATA_1</strong></a> structure</p></td>
</tr>
<tr class="odd">
<td><p><em>cbOutputData</em></p></td>
<td><p><strong>sizeof</strong>(PORT_DATA_1)</p></td>
</tr>
<tr class="even">
<td><p><em>pcbOutputNeeded</em></p></td>
<td><p>Address of a DWORD containing the number of bytes needed for the buffer pointed to by <em>pOutputData</em></p></td>
</tr>
</tbody>
</table>

 

**XcvData** returns NO\_ERROR if it can obtain the configuration information for the port. If *pInputData* is **NULL**, or if *cbInputData* is smaller than required, the function returns ERROR\_INVALID\_DATA. If *pInputData*--&gt;*dwVersion* is not equal to 1, the function returns ERROR\_INVALID\_LEVEL. If *cbOutputData* is smaller than required, the function returns ERROR\_INVALID\_PARAMETER when *pcbOutputNeeded* is **NULL**, and ERROR\_INSUFFICIENT\_BUFFER when *pcbOutputNeeded* is non-**NULL**.

### HostAddress Command

The **HostAddress** command gets the printer's host name.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>XcvData Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>pszDataName</em></p></td>
<td><p>L&quot;HostAddress&quot;</p></td>
</tr>
<tr class="even">
<td><p><em>pInputData</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
<tr class="odd">
<td><p><em>cbInputData</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>pOutputData</em></p></td>
<td><p>Address of a buffer that receives a string containing the printer&#39;s host name</p></td>
</tr>
<tr class="odd">
<td><p><em>cbOutputData</em></p></td>
<td><p>Size of the buffer pointed to by <em>pOutputData</em></p></td>
</tr>
<tr class="even">
<td><p><em>pcbOutputNeeded</em></p></td>
<td><p>Address of a DWORD containing the number of bytes needed for the buffer pointed to by <em>pOutputData</em></p></td>
</tr>
</tbody>
</table>

 

[**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) returns NO\_ERROR if it can obtain the name of the printer's host. If *cbOutputData* is smaller than required, the function returns ERROR\_INVALID\_PARAMETER when *pcbOutputNeeded* is **NULL**, and ERROR\_INSUFFICIENT\_BUFFER when *pcbOutputNeeded* is non-**NULL**. If *pOutputData* is **NULL**, the function returns ERROR\_INVALID\_PARAMETER.

### IPAddress Command

The **IPAddress** command gets the printer's IP address.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>XcvData Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>pszDataName</em></p></td>
<td><p>L&quot;IPAddress&quot;</p></td>
</tr>
<tr class="even">
<td><p><em>pInputData</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
<tr class="odd">
<td><p><em>cbInputData</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>pOutputData</em></p></td>
<td><p>Address of a buffer that receives a string containing the printer&#39;s IP address</p></td>
</tr>
<tr class="odd">
<td><p><em>cbOutputData</em></p></td>
<td><p>Size of the buffer pointed to by <em>pOutputData</em></p></td>
</tr>
<tr class="even">
<td><p><em>pcbOutputNeeded</em></p></td>
<td><p>Address of a DWORD containing the number of bytes needed for the buffer pointed to by <em>pOutputData</em></p></td>
</tr>
</tbody>
</table>

 

[**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) returns NO\_ERROR if it can obtain the printer's IP address. If *cbOutputData* is smaller than required, the function returns ERROR\_INVALID\_PARAMETER when *pcbOutputNeeded* is **NULL**, and ERROR\_INSUFFICIENT\_BUFFER when *pcbOutputNeeded* is non-**NULL**. If *pOutputData* is **NULL**, the function returns ERROR\_INVALID\_PARAMETER.

### MonitorUI Command

The **MonitorUI** command gets the name of the port monitor UI DLL that provides an interface to TCPMON.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>XcvData Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>pszDataName</em></p></td>
<td><p>L&quot;MonitorUI&quot;</p></td>
</tr>
<tr class="even">
<td><p><em>pInputData</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
<tr class="odd">
<td><p><em>cbInputData</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>pOutputData</em></p></td>
<td><p>Address of a buffer that receives the name of the port monitor user interface DLL</p></td>
</tr>
<tr class="odd">
<td><p><em>cbOutputData</em></p></td>
<td><p>Number of bytes in the string containing the name of the port monitor user interface DLL</p></td>
</tr>
<tr class="even">
<td><p><em>pcbOutputNeeded</em></p></td>
<td><p>Address of a DWORD containing the number of bytes needed for the buffer pointed to by <em>pOutputData</em></p></td>
</tr>
</tbody>
</table>

 

[**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) returns NO\_ERROR if it is able to obtain the name of the user interface DLL. In addition to the normal error codes, **XcvData** returns ERROR\_ACCESS\_DENIED if the caller has insufficient privileges on the server. This command requires SERVER\_ACCESS\_ADMINISTER privilege. If *cbOutputData* is smaller than required, the function returns ERROR\_INVALID\_PARAMETER when *pcbOutputNeeded* is **NULL**, and ERROR\_INSUFFICIENT\_BUFFER when *pcbOutputNeeded* is non-**NULL**. If *pOutputData* is **NULL**, the function returns ERROR\_INVALID\_PARAMETER.

### SNMPCommunity

The **SNMPCommunity** command gets the Simple Network Management Protocol (SNMP) community name for a printer.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>XcvData Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>pszDataName</em></p></td>
<td><p>L&quot;SNMPCommunity&quot;</p></td>
</tr>
<tr class="even">
<td><p><em>pInputData</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
<tr class="odd">
<td><p><em>cbInputData</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>pOutputData</em></p></td>
<td><p>Address of a buffer that receives a string containing the printer&#39;s SNMP community</p></td>
</tr>
<tr class="odd">
<td><p><em>cbOutputData</em></p></td>
<td><p>Size of the buffer needed to contain the string pointed to by the <em>pOutputData</em> parameter</p></td>
</tr>
<tr class="even">
<td><p><em>pcbOutputNeeded</em></p></td>
<td><p>Address of a DWORD containing the number of bytes needed for the buffer pointed to by <em>pOutputData</em></p></td>
</tr>
</tbody>
</table>

 

[**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) returns NO\_ERROR if it can get the printer's SNMP community name. If *cbOutputData* is smaller than required, the function returns ERROR\_INVALID\_PARAMETER when *pcbOutputNeeded* is **NULL**, and ERROR\_INSUFFICIENT\_BUFFER when *pcbOutputNeeded* is non-**NULL**. If *pOutputData* is **NULL**, the function returns ERROR\_INVALID\_PARAMETER.

### SNMPDeviceIndex

The **SNMPDeviceIndex** command gets the Simple Network Management Protocol (SNMP) device index of the printer.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>XcvData Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>pszDataName</em></p></td>
<td><p>L&quot;SNMPDeviceIndex&quot;</p></td>
</tr>
<tr class="even">
<td><p><em>pInputData</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
<tr class="odd">
<td><p><em>cbInputData</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>pOutputData</em></p></td>
<td><p>Address of a buffer that receives the device index</p></td>
</tr>
<tr class="odd">
<td><p><em>cbOutputData</em></p></td>
<td><p><strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="even">
<td><p><em>pcbOutputNeeded</em></p></td>
<td><p>Address of a DWORD that contains <strong>sizeof</strong>(DWORD)</p></td>
</tr>
</tbody>
</table>

 

[**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) returns NO\_ERROR if it can get the printer's SNMP device index. If *cbOutputData* is smaller than required, the function returns ERROR\_INVALID\_PARAMETER when *pcbOutputNeeded* is **NULL**, and ERROR\_INSUFFICIENT\_BUFFER when *pcbOutputNeeded* is non-**NULL**. If *pOutputData* is **NULL**, the function returns ERROR\_INVALID\_PARAMETER.

### SNMPEnabled

The **SNMPEnabled** command determines whether the Simple Network Management Protocol (SNMP) is enabled for the current device.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>XcvData Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>pszDataName</em></p></td>
<td><p>L&quot;SNMPEnabled&quot;</p></td>
</tr>
<tr class="even">
<td><p><em>pInputData</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
<tr class="odd">
<td><p><em>cbInputData</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>pOutputData</em></p></td>
<td><p>Address of a buffer that receives a DWORD value</p></td>
</tr>
<tr class="odd">
<td><p><em>cbOutputData</em></p></td>
<td><p><strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="even">
<td><p><em>pcbOutputNeeded</em></p></td>
<td><p>Address of a DWORD that contains <strong>sizeof</strong>(DWORD)</p></td>
</tr>
</tbody>
</table>

 

**XcvData** returns NO\_ERROR if SNMP is enabled for the device. If *cbOutputData* is smaller than required, the function returns ERROR\_INVALID\_PARAMETER when *pcbOutputNeeded* is **NULL**, and ERROR\_INSUFFICIENT\_BUFFER when *pcbOutputNeeded* is non-**NULL**. If *pOutputData* is **NULL**, the function returns ERROR\_INVALID\_PARAMETER.

 

 




