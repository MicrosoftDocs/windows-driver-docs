---
title: TCPMON Xcv Interface
author: windows-driver-content
description: TCPMON Xcv Interface
MS-HAID:
- 'provider\_19c6db6a-92dd-4650-a96f-7ae24574be36.xml'
- 'print.tcpmon\_xcv\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7b2b1cff-ab8f-44e0-9327-dc60a0072bf5
keywords: ["print monitors WDK , TCPMON Xcv", "transceive (Xcv) interface WDK print", "Xcv interface WDK print", "TCPMON Xcv interface WDK print"]
---

# TCPMON Xcv Interface


## <a href="" id="ddk-tcpmon-xcv-interface-gg"></a>


This section describes the transceive (Xcv) interface for the standard TCP/IP port monitor (TCPMON). This interface, which is implemented using [**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) and [**XcvDataPort**](https://msdn.microsoft.com/library/windows/hardware/ff564258) function calls, enables those using it to configure a TCP/IP printer port or to obtain information about a TCP/IP printer port configuration. The Xcv interface described in this section is specific to TCP/IP ports. Other Xcv interfaces might be available for other port types.

To obtain a handle to an Xcv interface for either a local machine or a remote machine, call the **OpenPrinter** function (described in the Microsoft Windows SDK documentation). The following code example illustrates how to obtain an Xcv handle to a port:

```
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

```
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20TCPMON%20Xcv%20Interface%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


