---
title: TCPMON Xcv commands
description: Provides information about TCPMON Xcv commands.
keywords:
- print monitors WDK, TCPMON Xcv
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
ms.date: 09/08/2022
---

# TCPMON Xcv commands

This section describes the commands that can be specified in a call to the [**XcvData**](/previous-versions/ff564255(v=vs.85)) or [**XcvDataPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-xcvdataport) function, when it is communicating with the standard TCP/IP port monitor (TCPMON). Each command is specified by the *pszDataName* string in the call to these functions. Certain commands require an input buffer, or an output buffer, or both. The *pInputData* and *pOutputData* parameters of these functions hold the addresses of these buffers.

The table that appears in the description of each of the following commands lists the **XcvData** and **XcvDataPort** parameters that are used with the commands. Note that the *hXcv* parameter (common to both functions) is not listed, nor is the **XcvData** function's *pdwStatus* parameter.

## AddPort command

The **AddPort** command adds a standard TCP/IP port, which can be either an LPR port or a RAW TCP/IP port.

| XcvData parameter | Value |
|--|--|
| *pszDataName* | L"AddPort" |
| *pInputData* | Address of a [**PORT_DATA_1**](/windows-hardware/drivers/ddi/tcpxcv/ns-tcpxcv-_port_data_1) structure |
| *cbInputData* | **sizeof**(PORT_DATA_1) |
| *pOutputData* | **NULL** |
| *cbOutputData* | 0 |
| *pcbOutputNeeded* | Address of a DWORD |

[**XcvData**](/previous-versions/ff564255(v=vs.85)) returns NO_ERROR if it can add the port. In addition to the normal error codes, **XcvData** returns ERROR_ACCESS_DENIED if the user has insufficient privileges to create a port on the server. This command requires SERVER_ACCESS_ADMINISTER privilege. If the *pInputData* parameter is **NULL**, the function returns ERROR_INVALID_DATA. If *pInputData*--&gt;*dwVersion* is not equal to 1, the function returns ERROR_INVALID_LEVEL.

## ConfigPort command

The **ConfigPort** command configures an existing standard TCP/IP port monitor port.

| XcvData parameter | Value |
|--|--|
| *pszDataName* | L"ConfigPort" |
| *pInputData* | Address of a [**PORT_DATA_1**](/windows-hardware/drivers/ddi/tcpxcv/ns-tcpxcv-_port_data_1) structure |
| *cbInputData* | **sizeof**(PORT_DATA_1) |
| *pOutputData* | **NULL** |
| *cbOutputData* | 0 |
| *pcbOutputNeeded* | Address of a DWORD |

[**XcvData**](/previous-versions/ff564255(v=vs.85)) returns NO_ERROR if it can configure the port. In addition to the normal error codes, **XcvData** returns ERROR_ACCESS_DENIED if the caller has insufficient privileges to perform the request. This command requires SERVER_ACCESS_ADMINISTER privilege. If the *pInputData* parameter is **NULL**, or the value in *cbInputData* is smaller than required, the function returns ERROR_INVALID_DATA. If *pInputData*--&gt;*dwVersion* is not equal to 1, the function returns ERROR_INVALID_LEVEL.

## DeletePort command

The **DeletePort** command deletes a port from the standard TCP/IP port monitor.

| XcvData parameter | Value |
|--|--|
| *pszDataName* | L"DeletePort" |
| *pInputData* | Address of [**DELETE_PORT_DATA_1**](/windows-hardware/drivers/ddi/tcpxcv/ns-tcpxcv-_delete_port_data_1) structure |
| *cbInputData* | **sizeof**(DELETE_PORT_DATA_1) |
| *pOutputData* | **NULL** |
| *cbOutputData* | 0 |
| *pcbOutputNeeded* | Address of a DWORD |

**XcvData** returns NO_ERROR if the port is successfully deleted. In addition to the normal error codes, **XcvData** returns ERROR_ACCESS_DENIED if the caller has insufficient privileges on the server. This command requires SERVER_ACCESS_ADMINISTER privilege. If the *pInputData* parameter is **NULL**, or if the *cbInputData* parameter is smaller than required, the function returns ERROR_INVALID_DATA. If *pInputData*--&gt;*dwVersion* is not equal to 1, the function returns ERROR_INVALID_LEVEL.

## GetConfigInfo command

The **GetConfigInfo** command obtains the configuration information of a particular port. In this case, the Xcv data handle must point to a particular standard TCP/IP port monitor port so that the port can be identified.

| XcvData parameter | Value |
|--|--|
| *pszDataName* | L"GetConfigInfo" |
| *pInputData* | Address of a [**CONFIG_INFO_DATA_1**](/windows-hardware/drivers/ddi/tcpxcv/ns-tcpxcv-_config_info_data_1) structure |
| *cbInputData* | **sizeof**(CONFIG_INFO_DATA_1) |
| *pOutputData* | Address of a [**PORT_DATA_1**](/windows-hardware/drivers/ddi/tcpxcv/ns-tcpxcv-_port_data_1) structure |
| *cbOutputData* | **sizeof**(PORT_DATA_1) |
| *pcbOutputNeeded* | Address of a DWORD containing the number of bytes needed for the buffer pointed to by *pOutputData* |

**XcvData** returns NO_ERROR if it can obtain the configuration information for the port. If *pInputData* is **NULL**, or if *cbInputData* is smaller than required, the function returns ERROR_INVALID_DATA. If *pInputData*--&gt;*dwVersion* is not equal to 1, the function returns ERROR_INVALID_LEVEL. If *cbOutputData* is smaller than required, the function returns ERROR_INVALID_PARAMETER when *pcbOutputNeeded* is **NULL**, and ERROR_INSUFFICIENT_BUFFER when *pcbOutputNeeded* is non-**NULL**.

## HostAddress command

The **HostAddress** command gets the printer's host name.

| XcvData parameter | Value |
|--|--|
| *pszDataName* | L"HostAddress" |
| *pInputData* | **NULL** |
| *cbInputData* | 0 |
| *pOutputData* | Address of a buffer that receives a string containing the printer's host name |
| *cbOutputData* | Size of the buffer pointed to by *pOutputData* |
| *pcbOutputNeeded* | Address of a DWORD containing the number of bytes needed for the buffer pointed to by *pOutputData* |

[**XcvData**](/previous-versions/ff564255(v=vs.85)) returns NO_ERROR if it can obtain the name of the printer's host. If *cbOutputData* is smaller than required, the function returns ERROR_INVALID_PARAMETER when *pcbOutputNeeded* is **NULL**, and ERROR_INSUFFICIENT_BUFFER when *pcbOutputNeeded* is non-**NULL**. If *pOutputData* is **NULL**, the function returns ERROR_INVALID_PARAMETER.

## IPAddress command

The **IPAddress** command gets the printer's IP address.

| XcvData parameter | Value |
|--|--|
| *pszDataName* | L"IPAddress" |
| *pInputData* | **NULL** |
| *cbInputData* | 0 |
| *pOutputData* | Address of a buffer that receives a string containing the printer's IP address |
| *cbOutputData* | Size of the buffer pointed to by *pOutputData* |
| *pcbOutputNeeded* | Address of a DWORD containing the number of bytes needed for the buffer pointed to by *pOutputData* |

[**XcvData**](/previous-versions/ff564255(v=vs.85)) returns NO_ERROR if it can obtain the printer's IP address. If *cbOutputData* is smaller than required, the function returns ERROR_INVALID_PARAMETER when *pcbOutputNeeded* is **NULL**, and ERROR_INSUFFICIENT_BUFFER when *pcbOutputNeeded* is non-**NULL**. If *pOutputData* is **NULL**, the function returns ERROR_INVALID_PARAMETER.

## MonitorUI command

The **MonitorUI** command gets the name of the port monitor UI DLL that provides an interface to TCPMON.

| XcvData parameter | Value |
|--|--|
| *pszDataName* | L"MonitorUI" |
| *pInputData* | **NULL** |
| *cbInputData* | 0 |
| *pOutputData* | Address of a buffer that receives the name of the port monitor user interface DLL |
| *cbOutputData* | Number of bytes in the string containing the name of the port monitor user interface DLL |
| *pcbOutputNeeded* | Address of a DWORD containing the number of bytes needed for the buffer pointed to by *pOutputData* |

[**XcvData**](/previous-versions/ff564255(v=vs.85)) returns NO_ERROR if it is able to obtain the name of the user interface DLL. In addition to the normal error codes, **XcvData** returns ERROR_ACCESS_DENIED if the caller has insufficient privileges on the server. This command requires SERVER_ACCESS_ADMINISTER privilege. If *cbOutputData* is smaller than required, the function returns ERROR_INVALID_PARAMETER when *pcbOutputNeeded* is **NULL**, and ERROR_INSUFFICIENT_BUFFER when *pcbOutputNeeded* is non-**NULL**. If *pOutputData* is **NULL**, the function returns ERROR_INVALID_PARAMETER.

## SNMPCommunity

The **SNMPCommunity** command gets the Simple Network Management Protocol (SNMP) community name for a printer.

| XcvData parameter | Value |
|--|--|
| *pszDataName* | L"SNMPCommunity" |
| *pInputData* | **NULL** |
| *cbInputData* | 0 |
| *pOutputData* | Address of a buffer that receives a string containing the printer's SNMP community |
| *cbOutputData* | Size of the buffer needed to contain the string pointed to by the *pOutputData* parameter |
| *pcbOutputNeeded* | Address of a DWORD containing the number of bytes needed for the buffer pointed to by *pOutputData* |

[**XcvData**](/previous-versions/ff564255(v=vs.85)) returns NO_ERROR if it can get the printer's SNMP community name. If *cbOutputData* is smaller than required, the function returns ERROR_INVALID_PARAMETER when *pcbOutputNeeded* is **NULL**, and ERROR_INSUFFICIENT_BUFFER when *pcbOutputNeeded* is non-**NULL**. If *pOutputData* is **NULL**, the function returns ERROR_INVALID_PARAMETER.

## SNMPDeviceIndex

The **SNMPDeviceIndex** command gets the Simple Network Management Protocol (SNMP) device index of the printer.

| XcvData parameter | Value |
|--|--|
| *pszDataName* | L"SNMPDeviceIndex" |
| *pInputData* | **NULL** |
| *cbInputData* | 0 |
| *pOutputData* | Address of a buffer that receives the device index |
| *cbOutputData* | **sizeof**(DWORD) |
| *pcbOutputNeeded* | Address of a DWORD that contains **sizeof**(DWORD) |

[**XcvData**](/previous-versions/ff564255(v=vs.85)) returns NO_ERROR if it can get the printer's SNMP device index. If *cbOutputData* is smaller than required, the function returns ERROR_INVALID_PARAMETER when *pcbOutputNeeded* is **NULL**, and ERROR_INSUFFICIENT_BUFFER when *pcbOutputNeeded* is non-**NULL**. If *pOutputData* is **NULL**, the function returns ERROR_INVALID_PARAMETER.

## SNMPEnabled

The **SNMPEnabled** command determines whether the Simple Network Management Protocol (SNMP) is enabled for the current device.

| XcvData parameter | Value |
|--|--|
| *pszDataName* | L"SNMPEnabled" |
| *pInputData* | **NULL** |
| *cbInputData* | 0 |
| *pOutputData* | Address of a buffer that receives a DWORD value |
| *cbOutputData* | **sizeof**(DWORD) |
| *pcbOutputNeeded* | Address of a DWORD that contains **sizeof**(DWORD) |

**XcvData** returns NO_ERROR if SNMP is enabled for the device. If *cbOutputData* is smaller than required, the function returns ERROR_INVALID_PARAMETER when *pcbOutputNeeded* is **NULL**, and ERROR_INSUFFICIENT_BUFFER when *pcbOutputNeeded* is non-**NULL**. If *pOutputData* is **NULL**, the function returns ERROR_INVALID_PARAMETER.
