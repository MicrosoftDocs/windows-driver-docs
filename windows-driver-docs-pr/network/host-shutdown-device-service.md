---
title: HOST Shutdown Device Service
description: This topic provides guidelines for Mobile Broadband Interface Model (MBIM)-compliant devices to implement and report the described device service when queried by CID_MBIM_DEVICE_SERVICES.
ms.assetid: 62BFC796-EDB2-489E-B487-65E2DD7C4256
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HOST Shutdown Device Service


This topic provides guidelines for Mobile Broadband Interface Model (MBIM)-compliant devices to implement and report the described device service when queried by CID\_MBIM\_DEVICE\_SERVICES.

The information in this topic applies to Windows 8 and later.

## Microsoft Host Shutdown


The MBIM-compliant device implements and reports the following device service when queried by CID\_MBIM\_DEVICE\_SERVICES. The existing well-known services are defined in section 10.1 of the [USB NCM Mobile Broadband Interface Model (MBIM) V1.0 specification](http://go.microsoft.com/fwlink/p/?linkid=320791). Microsoft extends this to define the following service.

Service Name = **Microsoft Host Shutdown**

UUID = **UUID\_MS\_HOSTSHUTDOWN**

UUID Value = **883b7c26-985f-43fa-9804-27d7fb80959c**

## Defined CIDs for UUID\_MS\_HOSTSHUTDOWN device service


| CID                          | Minimum OS version       |
|------------------------------|--------------------------|
| CID\_MBIM\_MSHOSTSHUTDOWN    | Windows 8                |
| CID\_MBIM\_MSHOSTPRESHUTDOWN | Windows 10, version 1511 |

 

## CID\_MBIM\_MSHOSTSHUTDOWN


This command informs the device that the host is shutting down. The MB device may lose power.

|                                      |                           |
|--------------------------------------|---------------------------|
| CID                                  | CID\_MBIM\_MSHOSTSHUTDOWN |
| Command Code                         | 1                         |
| Set                                  | Yes                       |
| Query                                | No                        |
| Event                                | No                        |
| Set InformationBuffer payload        | N/A                       |
| Query InformationBuffer payload      | N/A                       |
| Completion InformationBuffer payload | N/A                       |

 

|                   |                                                                                                      |
|-------------------|------------------------------------------------------------------------------------------------------|
| Set               | InformationBuffer on MBIM\_COMMAND\_MSG not used. InformationBuffer of MBIM\_COMMAND\_DONE not used. |
| Query             | Unsupported                                                                                          |
| Unsolicited Event | Unsupported                                                                                          |

 

### Remarks

The Mobile Broadband Class Driver sends the host shutdown notification to mobile broadband devices supporting this device service, on each host state transition into S4 and S5 states.

This notification is to provide mobile broadband devices with an early indication to allow them to initiate a mobile network deregister message and initiate SIM electrical de-initialization.

The following information summarizes the list of host sent CIDs/CMDs to the device for various system transitions and device power state transitions:

-   MSHOSTSHUTDOWN CID is sent to the device on host state transitioning into S4 and S5.
-   MBIM\_CMD\_CLOSE is sent to the device when host puts the device into D3 mode.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"></th>
<th align="left">S0</th>
<th align="left">S1/S2/S3</th>
<th align="left">S4</th>
<th align="left">S5</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>D0</p></td>
<td align="left"><p>MBIM_CMD_OPEN</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>N/A</p></td>
</tr>
<tr class="even">
<td align="left"><p>D1</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>N/A</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D2</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>N/A</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>MBIM_CMD_CLOSE</p></td>
<td align="left"><p>MSHOSTSHUTDOWN</p></td>
<td align="left"><p>MSHOSTSHUTDOWN</p></td>
</tr>
</tbody>
</table>

 

## CID\_MBIM\_MSHOSTPRESHUTDOWN


This command notifies the MBIM modem that the system is undergoing pre-shutdown and it should finish all its operations, deregister from the network, and store necessary information to the host for flashless modem cases. The pre-shutdown notification is sent down when the host is preparing to enter S4 and S5 states and is waiting for all services to shut down appropriately.

|                                      |                              |
|--------------------------------------|------------------------------|
| CID                                  | CID\_MBIM\_MSHOSTPRESHUTDOWN |
| Command Code                         | 2                            |
| Set                                  | Yes                          |
| Query                                | No                           |
| Notification                         | No                           |
| Set InformationBuffer payload        | N/A                          |
| Query InformationBuffer payload      | N/A                          |
| Completion InformationBuffer payload | N/A                          |

 

Parameters:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"></th>
<th align="left">Set</th>
<th align="left">Query</th>
<th align="left">Notification</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Command</td>
<td align="left">CID_MBIM_SET_MSHOSTPRESHUTDOWN</td>
<td align="left">N/A</td>
<td align="left">N/A</td>
</tr>
<tr class="even">
<td align="left">Response</td>
<td align="left">Empty</td>
<td align="left">N/A</td>
<td align="left">N/A</td>
</tr>
</tbody>
</table>

 

For the Set operation, InformationBuffer and InformationBufferLength are empty.

Status Codes:

| Status code                       | Description                                                                         |
|-----------------------------------|-------------------------------------------------------------------------------------|
| MBIM\_STATUS\_SUCCESS             | Pre-shutdown operations completed by the modem.                                     |
| MBIM\_STATUS\_NO\_DEVICE\_SUPPORT | The device does not support pre-shutdown and no pre-shutdown operations are needed. |

 

 

 





