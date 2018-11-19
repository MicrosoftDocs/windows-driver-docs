---
title: TCPMON Xcv Interface
description: TCPMON Xcv Interface
ms.assetid: 7b2b1cff-ab8f-44e0-9327-dc60a0072bf5
keywords:
- print monitors WDK , TCPMON Xcv
- transceive (Xcv) interface WDK print
- Xcv interface WDK print
- TCPMON Xcv interface WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TCPMON Xcv Interface





This section describes the transceive (Xcv) interface for the standard TCP/IP port monitor (TCPMON). This interface, which is implemented using [**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) and [**XcvDataPort**](https://msdn.microsoft.com/library/windows/hardware/ff564258) function calls, enables those using it to configure a TCP/IP printer port or to obtain information about a TCP/IP printer port configuration. The Xcv interface described in this section is specific to TCP/IP ports. Other Xcv interfaces might be available for other port types.

To obtain a handle to an Xcv interface for either a local machine or a remote machine, call the **OpenPrinter** function (described in the Microsoft Windows SDK documentation). The following code example illustrates how to obtain an Xcv handle to a port:

```cpp
HANDLE hXcv = INVALID_HANDLE_VALUE;
PRINTER_DEFAULTS Defaults = { NULL, NULL, <Required Access> };

// Handle to a local machine
if (OpenPrinter(",XcvPort <PortName>", &hXcv, &Defaults )
{
 // hXvc contains an Xcv data handle to a local TCPMON port
}

// Handle to a remote machine
if (OpenPrinter("<ServerName>\\,XcvPort <PortName>", &hXcv, &Defaults )
{
 // hXvc contains an Xcv data handle to a TCPMON port on <ServerName>
}
```

In the code example, *ServerName* and *PortName* represent server and port name strings. Once you have obtained the handle, you can query information that is specific to the TCPMON port monitor, or you can change the port configuration. Note that the access you require for the port monitor must be specified in the **DesiredAccess** member of the PRINTER\_DEFAULTS structure (or pass **NULL** if no special security is required). For certain calls to the [**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) function (such as when the AddPort and DeletePort commands are specified -- see [TCPMON Xcv Commands](tcpmon-xcv-commands.md)), SERVER\_ACCESS\_ADMINISTER privilege is required. For details about the **OpenPrinter** function and the access rights that may be requested in the PRINTER\_DEFAULTS structure, see the Windows SDK documentation.

If the port does not yet exist, the Xcv handle can be obtained from the server by specifying the monitor name. (In the case of the standard TCP/IP port monitor port, this is "Standard TCP/IP Port".) The following code example illustrates how to obtain an Xcv data handle to a port monitor:

```cpp
HANDLE hXcv = INVALID_HANDLE_VALUE;
PRINTER_DEFAULTS Defaults = { NULL, NULL, <Required Access> };

// Handle to a local machine
if (OpenPrinter(",XcvMonitor <MonitorName>", &hXcv, &Defaults )
{
 // hXcv contains an Xcv data handle to the monitor <MonitorName>
}

// Handle to a remote machine
if (OpenPrinter("<ServerName>\\,XcvMonitor <MonitorName>", &hXcv, &Defaults )
{
 // hXcv contains an Xcv data handle to the monitor 
 // <MonitorName> on the server <ServerName>
}
```

In the code example, *ServerName* and *PortName* represent server and port name strings. Once you have obtained the Xcv data handle, you can issue instructions and requests to the monitor by calling the [**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) function.

Note that the return value from the **XcvData** function indicates only whether the data was correctly sent to the port monitor. A return value of **TRUE** does not indicate that the operation was successful. To determine whether the operation was successful, inspect the value in \**pdwStatus*. These status values are summarized in the following table:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>NO_ERROR</p></td>
<td><p>The operation was successful.</p></td>
</tr>
<tr class="even">
<td><p>ERROR_ACCESS_DENIED</p></td>
<td><p>The user has insufficient privileges. The command requires SERVER_ACCESS_ADMINISTER privilege.</p></td>
</tr>
<tr class="odd">
<td><p>ERROR_INSUFFICIENT_BUFFER</p></td>
<td><p>An output buffer is required, but is smaller than required.</p></td>
</tr>
<tr class="even">
<td><p>ERROR_INVALID_DATA</p></td>
<td><p>An input buffer is required, but the pointer to it is <strong>NULL</strong>, or</p>
<p>the size of the input buffer is smaller than required.</p></td>
</tr>
<tr class="odd">
<td><p>ERROR_INVALID_HANDLE</p></td>
<td><p>The Xcv data handle is invalid.</p></td>
</tr>
<tr class="even">
<td><p>ERROR_INVALID_LEVEL</p></td>
<td><p>The input or output data structure is not the correct version.</p></td>
</tr>
<tr class="odd">
<td><p>ERROR_INVALID_PARAMETER</p></td>
<td><p>An output buffer is required, but it is <strong>NULL</strong>, or</p>
<p>the output required parameter is <strong>NULL</strong> and the output buffer is too small, or</p>
<p>the standard TCP/IP port monitor does not understand the command being issued.</p></td>
</tr>
</tbody>
</table>

 

 

 




