---
title: TCPMON Xcv interface
description: Provides information about TCPMON Xcv interface.
keywords:
- print monitors WDK, TCPMON Xcv
- transceive (Xcv) interface WDK print
- Xcv interface WDK print
- TCPMON Xcv interface WDK print
ms.date: 09/08/2022
---

# TCPMON Xcv interface

This section describes the transceive (Xcv) interface for the standard TCP/IP port monitor (TCPMON). This interface, which is implemented using [**XcvData**](/previous-versions/ff564255(v=vs.85)) and [**XcvDataPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-xcvdataport) function calls, enables those using it to configure a TCP/IP printer port or to obtain information about a TCP/IP printer port configuration. The Xcv interface described in this section is specific to TCP/IP ports. Other Xcv interfaces might be available for other port types.

To obtain a handle to an Xcv interface for either a local machine or a remote machine, call the [**OpenPrinter**](/windows/win32/printdocs/openprinter) function. The following code example illustrates how to obtain an Xcv handle to a port:

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

In the code example, *ServerName* and *PortName* represent server and port name strings. Once you have obtained the handle, you can query information that is specific to the TCPMON port monitor, or you can change the port configuration. Note that the access you require for the port monitor must be specified in the **DesiredAccess** member of the PRINTER_DEFAULTS structure or pass **NULL** if no special security is required. For certain calls to the [**XcvData**](/previous-versions/ff564255(v=vs.85)) function, such as when the AddPort and DeletePort commands are specified (see [TCPMON Xcv Commands](tcpmon-xcv-commands.md)), SERVER_ACCESS_ADMINISTER privilege is required. For details about the **OpenPrinter** function and the access rights that may be requested in the PRINTER_DEFAULTS structure, see the [**OpenPrinter**](/windows/win32/printdocs/openprinter) function documentation.

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

In the code example, *ServerName* and *PortName* represent server and port name strings. Once you have obtained the Xcv data handle, you can issue instructions and requests to the monitor by calling the [**XcvData**](/previous-versions/ff564255(v=vs.85)) function.

Note that the return value from the **XcvData** function indicates only whether the data was correctly sent to the port monitor. A return value of **TRUE** does not indicate that the operation was successful. To determine whether the operation was successful, inspect the value in \**pdwStatus*. These status values are summarized in the following table:

| Status value | Meaning |
|--|--|
| NO_ERROR | The operation was successful. |
| ERROR_ACCESS_DENIED | The user has insufficient privileges. The command requires SERVER_ACCESS_ADMINISTER privilege. |
| ERROR_INSUFFICIENT_BUFFER | An output buffer is required, but is smaller than required. |
| ERROR_INVALID_DATA | An input buffer is required, but the pointer to it is **NULL**, or the size of the input buffer is smaller than required. |
| ERROR_INVALID_HANDLE | The Xcv data handle is invalid. |
| ERROR_INVALID_LEVEL | The input or output data structure is not the correct version. |
| ERROR_INVALID_PARAMETER | An output buffer is required, but it is **NULL**, or the output required parameter is **NULL** and the output buffer is too small, or the standard TCP/IP port monitor does not understand the command being issued. |
