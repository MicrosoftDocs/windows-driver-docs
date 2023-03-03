---
title: MB low level UICC access
description: MB low level UICC access
keywords:
- MB low level UICC access, Mobile Broadband low level UICC access, Mobile Broadband miniport driver low level UICC, MB UICC ATR, MB UICC Answer to Reset, MB UICC open channel, MB UICC close channel, MB UICC APDU, MB UICC terminal capability, MB UICC reset
ms.date: 12/05/2017
ms.custom: UpdateFrequency3
ms.custom: 19H1
---

# MB low level UICC access

## Overview

The Mobile Broadband Interface Model Revision 1.0, or MBIM1, defines an OEM- and IHV-agnostic interface between a host device and a cellular data modem.

An MBIM1 function includes a UICC smart card and provides access to some of its data and internal state. However, the smart card may have additional capabilities beyond those that are defined by the MBIM interface. These additional capabilities include support for a secure element for mobile payment solutions based upon near-field communication, or for remote provisioning of an entire UICC profile.

In a mobile broadband-enabled Windows device, the MBIM interface is used in addition to the Radio Interface Layer (RIL) interface. One of the features the RIL provides is an interface for low-level access to the UICC. This topic describes a set of Microsoft extensions to MBIM that describe this additional functionality at the MBIM interface.

The Microsoft extensions comprise a set of device service commands (both Set and Query) and notifications. These extensions do not include any new uses of device service streams.

## MBIM service and CID values

| Service name | UUID | UUID value |
| --- | --- | --- |
| Microsoft Low-Level UICC Access | UUID_MS_UICC_LOW_LEVEL | C2F6588E-F037-4BC9-8665-F4D44BD09367 |

The following table specifies the command code for each CID, as well as whether the CID supports Set, Query, or Event (notification) requests. See each CID’s individual section within this topic for more info about its parameters, data structures, and notifications. 

| CID | Command code | Set | Query | Notify |
| --- | --- | --- | --- | --- |
| MBIM_CID_MS_UICC_ATR | 1 | N | Y | N |
| MBIM_CID_MS_UICC_OPEN_CHANNEL | 2 | Y | N | N |
| MBIM_CID_MS_UICC_CLOSE_CHANNEL | 3 | Y | N | N |
| MBIM_CID_MS_UICC_APDU) | 4 | Y | N | N |
| MBIM_CID_MS_UICC_TERMINAL_CAPABILITY | 5 | Y | Y | N |
| MBIM_CID_MS_UICC_RESET | 6 | Y | Y | N |

## Status codes

MBIM status codes are defined in Section 9.4.5 of the [MBIM standard](https://www.usb.org/document-library/mobile-broadband-interface-model-v10-errata-1-and-adopters-agreement). In addition, the following additional failure status codes are defined:

| Status Code | Value (hex) | Description |
| --- | --- | --- |
| MBIM_STATUS_MS_NO_LOGICAL_CHANNELS | 87430001 | The logical channel open was not successful because no logical channels are available on the UICC (either it does not support them or all of them are in use). |
| MBIM_STATUS_MS_SELECT_FAILED | 87430002 | The logical channel open was not successful because SELECT failed. |
| MBIM_STATUS_MS_INVALID_LOGICAL_CHANNEL | 87430003 | The logical channel number is invalid (it was not opened by MBIM_CID_MS_UICC_OPEN_CHANNEL). |

### MBIM_SUBSCRIBER_READY_STATE

| Type | Value | Description |
| --- | --- | --- |
| MBIMSubscriberReadyStateNoEsimProfile | 7 | The card is ready but does not have any enabled profiles. |

## UICC responses and status

The UICC may implement either a character-based or record-based interface, or both. Although the specific mechanism is different, the result is that the UICC responds to each command with two status bytes (named SW1 and SW2) and a response (which may be empty). A normal success status is indicated by 90 00. However, if the UICC supports the card application toolkit and the UICC wishes to send a proactive command to the terminal, a successful return will be indicated by a status of 91 XX (where XX varies). The MBIM function, or terminal, is responsible for handling this proactive command just as it would handle a proactive command received during any other UICC operation (sending a FETCH to the UICC, handling the proactive command, or sending it to the host with MBIM_CID_STK_PAC). When the MBIM host sends either MBIM_CID_MS_UICC_OPEN_CHANNEL or MBIM_CID_MS_UICC_APDU it should consider both 90 00 and 91 XX as a normal status.

Commands must be able to return responses that are larger than 256 bytes. This mechanism is described in Section 5.1.3 of the [ISO/IEC 7816-4:2013 standard](https://go.microsoft.com/fwlink/p/?linkid=864596). In this case, the card will return SW1 SW2 status words of 61 XX, rather than 90 00, where XX is either the number of remaining bytes or 00 if there are 256 bytes or more remaining. The modem must issue a GET RESPONSE with the same class byte repeatedly until all the data has been received. This will be indicated by the final status words 90 00. The sequence must be uninterrupted within a specific logical channel. Additional APDUs should be handled at the modem and should be transparent to the host. If handled in the host, there is no guarantee that some other APDU may asynchronously reference the card during the sequence of APDUs.

## Comparison to IHVRIL

Sections 5.2.3.3.10 through 5.2.3.3.14 of the IHVRIL specification define a similar interface upon which this specification is based. Some differences include:

- The RIL interface does not provide a way to specify secure messaging. The MBIM command to exchange APDUs specifies this as an explicit parameter.
- The RIL interface does not clearly define the interpretation of the class byte within the APDU. The MBIM specification states that the class byte sent from the host must be present but is not used (and instead the MBIM function constructs this byte).
- The RIL interface uses a separate function to close all UICC channels in a group, whereas the MBIM interface accomplishes this with variant arguments to a single CID.
- The relationship between MBIM error status and UICC status (SW1 SW2) is more clearly defined than the relationship between RIL errors and UICC status.
- The MBIM interface distinguishes failure to allocate a new logical channel from failure to SELECT a specified application.
- The MBIM interface permits sending the modem terminal capability objects to send to the card.

## MBIM_CID_MS_UICC_ATR

The Answer to Reset (ATR) is the first string of bytes sent by the UICC after a reset has been performed. It describes the capabilities of the card, such as the number of logical channels that it supports. The MBIM function must save the ATR when it is received from the UICC. Subsequently, the host may use the MBIM_CID_MS_UICC_ATR command to retrieve the ATR.

### Parameters

|  Type | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | Not applicable | Empty | Not applicable |
| Response | Not applicable | MBIM_MS_ATR_INFO | Not applicable |

### Query

The InformationBuffer of a Query message is empty. 

### Set

Not applicable.

### Response

The InformationBuffer of MBIM_COMMAND_DONE contains the following MBIM_MS_ATR_INFO structure describing the answer to reset for the UICC attached to this function.

#### MBIM_MS_ATR_INFO

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | AtrSize | SIZE(0..33) | The length of **AtrData**. |
| 4 | 4 | AtrOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to a byte array called **AtrData** that contains the ATR data. |
| 8 | AtrSize | DataBuffer | DATABUFFER | The **AtrData** byte array. |

### Unsolicited events

Not applicable.

### Status codes

The following status codes are applicable.

| Status code | Description |
| --- | --- |
| MBIM_STATUS_SUCCESS | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_BUSY | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_FAILURE | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_NO_DEVICE_SUPPORT | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_SIM_NOT_INSERTED | Unable to perform the UICC operation because the UICC is missing. |
| MBIM_STATUS_BAD_SIM | Unable to perform the UICC operation because the UICC is in an error state. |
| MBIM_STATUS_NOT_INITIALIZED | Unable to perform the UICC operation because the UICC is not yet fully initialized. |

## MBIM_CID_MS_UICC_OPEN_CHANNEL

The host uses the MBIM_CID_MS_UICC_OPEN_CHANNEL command to request that the function open a new logical channel on the UICC card and select a specified UICC application (specified by its application ID).

The function implements this MBIM command using a sequence of UICC commands:

1.	The function sends a MANAGE CHANNEL command to the UICC, as described by section 11.1.17 of the [ETSI TS 102 221 technical specification](https://go.microsoft.com/fwlink/p/?linkid=864594), to create a new logical channel. If this command fails, the function returns the MBIM_STATUS_MS_NO_LOGICAL_CHANNELS status with SW1 SW2 and takes no further action. 
2.	If the MANAGE CHANNEL command succeeds, the UICC reports the channel number of the new logical channel to the function. The function sends a SELECT [by name] command where P1 = 04, as described by section 11.1.1 of the [ETSI TS 102 221 technical specification](https://go.microsoft.com/fwlink/p/?linkid=864594). If this operation fails, the function sends a MANAGE CHANNEL command to the UICC to close the logical channel and returns the MBIM_STATUS_MS_SELECT_FAILED status with SW1 SW2 from the SELECT.
3.	If the SELECT command succeeds, the function records the logical channel number and the channel group specified by the host for future reference. It will then return the logical channel number, SW1 SW2 from the SELECT, and the response from the SELECT to the host.

### Parameters

| Operation | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | MBIM_MS_SET_UICC_OPEN_CHANNEL | Not applicable | Not applicable |
| Response | MBIM_MS_UICC_OPEN_CHANNEL_INFO | Not applicable | Not applicable |

### Query

Not applicable.

### Set

The InformationBuffer of MBIM_COMMAND_MSG contains the following MBIM_MS_SET_UICC_OPEN_CHANNEL structure.

#### MBIM_MS_SET_UICC_OPEN_CHANNEL

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | AppIdSize | SIZE(0..32) | The size of the application ID (AppId). |
| 4 | 4 | AppIdOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to a byte array called **AppId** that defines the AppId to be SELECTed. |
| 8 | 4 | SelectP2Arg | UINT32(0..255) | The *P2* argument to the SELECT command. |
| 12 | 4 | ChannelGroup | UINT32 | A tag value that identifies the channel group for this channel. |
| 16 | AppIdSize | DataBuffer | DATABUFFER | The **AppId** byte array. |

### Response

The InformationBuffer of MBIM_COMMAND_DONE contains the following MBIM_MS_UICC_OPEN_CHANNEL_INFO structure.

#### MBIM_MS_UICC_OPEN_CHANNEL_INFO

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | Status | BYTE[2] | SW1 and SW2, in that byte order. For more info, see the notes following this table. |
| 4 | 4 | Channel | UINT32(0..19) | The logical channel identifier. If this member is 0, then the operation failed. |
| 8 | 4 | ResponseLength | SIZE(0..256) | The response length in bytes. |
| 12 | 4 | ResponseOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to a byte array called **Response** that contains the response from the SELECT. |
| 16 | - | DataBuffer | DATABUFFER | The **Response** byte array data. |

If the command returns MBIM_STATUS_MS_NO_LOGICAL_CHANNELS, the **Status** field shall contain the UICC status words SW1 and SW2 from the MANAGE CHANNEL command and the remaining fields will be zero. If the command returns MBIM_STATUS_MS_SELECT_FAILED, the **Status** field shall contain the UICC status words SW1 and SW2 from the SELECT command and the remaining fields will be zero. For any other status, the InformationBuffer shall be empty.

### Unsolicited events

Not applicable.

### Status codes

The following status codes are applicable:

| Status code | Description |
| --- | --- |
| MBIM_STATUS_SUCCESS | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_BUSY | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_FAILURE | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_NO_DEVICE_SUPPORT | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_SIM_NOT_INSERTED | Unable to perform the UICC operation because the UICC is missing. |
| MBIM_STATUS_BAD_SIM | Unable to perform the UICC operation because the UICC is in an error state. |
| MBIM_STATUS_NOT_INITIALIZED | Unable to perform the UICC operation because the UICC is not yet fully initialized. |
| MBIM_STATUS_MS_NO_LOGICAL_CHANNELS | The logical channel open failed because no logical channels are available on the UICC (either it does not support them or all of them are in use). |
| MBIM_STATUS_MS_SELECT_FAILED | The logical channel open was not successful because SELECT failed. |

## MBIM_CID_MS_UICC_CLOSE_CHANNEL

The host sends MBIM_CID_MS_UICC_CLOSE_CHANNEL to the function to close a logical channel on the UICC. The host may specify a channel number or may specify a channel group.

If the host specifies a channel number, the function should check whether this channel was opened by a previous MBIM_CID_MS_UICC_OPEN_CHANNEL. If so, it should send a MANAGE CHANNEL command to the UICC to close the channel, return a status of MBIM_STATUS_SUCCESS, and return the SW1 SW2 from the MANAGE CHANNEL. If not, it should take no action and return the MBIM_STATUS_MS_INVALID_LOGICAL_CHANNEL failure status.

If the host specifies a channel group, the function determines which (if any) logical channels were opened with that channel group and sends a MANAGE CHANNEL command to the UICC for each such channel. It returns a status of MBIM_STATUS_SUCCESS with the SW1 SW2 of the last MANAGE CHANNEL. If no channels were closed it shall return 90 00.

### Parameters

| Operation | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | MBIM_MS_SET_UICC_CLOSE_CHANNEL | Not applicable | Not applicable |
| Response | MBIM_MS_UICC_CLOSE_CHANNEL_INFO | Not applicable | Not applicable |

### Query

Not applicable.

### Set

The InformationBuffer of MBIM_COMMAND_MSG contains the following MBIM_MS_SET_UICC_CLOSE_CHANNEL structure.

#### MBIM_MS_SET_UICC_CLOSE_CHANNEL

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | Channel | UINT32(0..19) | If nonzero, specifies the channel to be closed. If zero, specifies that the channel(s) associated with **ChannelGroup** are to be closed. |
| 4 | 4 | ChannelGroup | UINT32 | If **Channel** is zero, this specifies a tag value and all channels with this tag are closed. If **Channel** is nonzero, this field is ignored.

### Response

The InformationBuffer of MBIM_COMMAND_DONE contains the following MBIM_MS_UICC_CLOSE_CHANNEL_INFO structure.

#### MBIM_MS_UICC_CLOSE_CHANNEL_INFO

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | Status | BYTE[2] | SW1 and SW2 of the last MANAGE CHANNEL executed by the function on behalf of this command. |

### Unsolicited events

Not applicable.

### Status codes

| Status code | Description |
| --- | --- |
| MBIM_STATUS_SUCCESS | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_BUSY | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_FAILURE | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_NO_DEVICE_SUPPORT | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_SIM_NOT_INSERTED | Unable to perform the UICC operation because the UICC is missing. |
| MBIM_STATUS_BAD_SIM | Unable to perform the UICC operation because the UICC is in an error state. |
| MBIM_STATUS_NOT_INITIALIZED | Unable to perform the UICC operation because the UICC is not yet fully initialized. |
| MBIM_STATUS_MS_INVALID_LOGICAL_CHANNEL | The logical channel number is not valid (in other words, it was not opened with MBIM_CID_MS_UICC_OPEN_CHANNEL). |

## MBIM_CID_MS_UICC_APDU

The host uses MBIM_CID_MS_UICC_APDU to send a command APDU to a specified logical channel on the UICC and receive the response. The MBIM function should ensure that the logical channel was previously opened with MBIM_CID_MS_UICC_OPEN_CHANNEL and fail with status MBIM_STATUS_MS_INVALID_LOGICAL_CHANNEL if it was not.

The host must send a complete APDU to the function. The APDU may be sent with a class byte value defined in the first interindustry definition in section 4 of the [ISO/IEC 7816-4:2013 standard](https://go.microsoft.com/fwlink/p/?linkid=864596), or in the extended definition in Section 10.1.1 of the [ETSI TS 102 221 technical specification](https://go.microsoft.com/fwlink/p/?linkid=864594). The APDU may be sent without secure messaging or with secure messaging. The command header not authenticated. The host specifies the type of class byte, logical channel number, and secure messaging along with the APDU.

The first byte of the command APDU is the class byte, coded as defined by section 4 of the [ISO/IEC 7816-4:2013 standard](https://go.microsoft.com/fwlink/p/?linkid=864596) or section 10.1.1 of the [ETSI TS 102 221 technical specification](https://go.microsoft.com/fwlink/p/?linkid=864594). The host may send 0X, 4X, 6X, 8X, CX, or EX class bytes. However, the function does not pass this byte directly to the UICC. Instead, before sending the APDU to the UICC the function will replace the first byte from the host with a new class byte (encoded as defined by section 4 of the [ISO/IEC 7816-4:2013 standard](https://go.microsoft.com/fwlink/p/?linkid=864596) or section 10.1.1 of the [ETSI TS 102 221 technical specification](https://go.microsoft.com/fwlink/p/?linkid=864594)) based upon the Type, Channel, and SecureMessaging values specified by the host:

| Byte class | Description |
| --- | --- |
| 0X | 7816-4 interindustry, 1 <= channel <= 3, encodes security in low nibble if relevant |
| 4X | 7816-4 interindustry, 4 <= channel <= 19, no secure messaging |
| 6X | 7816-4 interindustry, 4 <= channel <= 19, secure (header not authenticated) |
| 8X | 102 221 extended, 1<= channel <= 3, encodes security in low nibble if relevant |
| CX | 102 221 extended, 4 <= channel <= 19, no secure messaging |
| EX | 102 221 extended, 4 <= channel <= 19, secure (header not authenticated) |

The function shall return the status, SW1 SW2, and response from the UICC to the host.

### Parameters

| Operation | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | MBIM_MS_SET_UICC_APDU | Not applicable | Not applicable |
| Response | MBIM_MS_UICC_APDU_INFO | Not applicable | Not applicable |

### Query

Not applicable.

### Set

The InformationBuffer of MBIM_COMMAND_MSG contains the following MBIM_MS_SET_UICC_APDU structure.

#### MBIM_MS_SET_UICC_APDU

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | Channel | UINT32(1..19) | Specifies the channel on which the APDU will be sent. |
| 4 | 4 | SecureMessaging | MBIM_MS_UICC_SECURE_MESSAGING | Specifies whether the APDU is exchanged using secure messaging. |
| 8 | 4 | Type | MBIM_MS_UICC_CLASS_BYTE_TYPE | Specifies the type of class byte definition. |
| 12 | 4 | CommandSize | UINT32(0..261) | The **Command** length in bytes. |
| 16 | 4 | CommandOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to a byte array called **Command** that contains the APDU. |
| 20 | - | DataBuffer | DATABUFFER | The **Command** byte array. |

The MBIM_MS_SET_UICC_APDU structure uses the following MBIM_MS_UICC_SECURE_MESSAGING and MBIM_MS_UICC_CLASS_BYTE_TYPE data structures.

##### MBIM_MS_UICC_SECURE_MESSAGING

| Type | Value | Description |
| --- | --- | --- |
| MBIMMsUiccSecureMessagingNone | 0 | No secure messaging. |
| MBIMMsUiccSecureMessagingNoHdrAuth | 1 | Secure messaging, command header not authenticated. |

##### MBIM_MS_UICC_CLASS_BYTE_TYPE

| Type | Value | Description |
| --- | --- | --- |
| MBIMMsUiccInterindustry | 0 | Defined according to first interindustry definition in ISO 7816-4. |
| MBIMMsUiccExtended | 1 | Defined according to the extended definition in ETSI 102 221. |

### Response

The InformationBuffer of MBIM_COMMAND_DONE contains the following MBIM_MS_UICC_APDU_INFO structure.

#### MBIM_MS_UICC_APDU_INFO

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | Status | BYTE[2] | The SW1 and SW2 status words resulting from the command. |
| 4 | 4 | ResponseLength | SIZE | The Response length in bytes. |
| 8 | 4 | ResponseOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to a byte array called **Response** that contains the response from the SELECT. |
| 12 | - | DataBuffer | DATABUFFER | The **Response** byte array. |

### Unsolicited events

Not applicable.

### Status codes

The following status codes are applicable:

| Status code | Description |
| --- | --- |
| MBIM_STATUS_SUCCESS | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_BUSY | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_FAILURE | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_NO_DEVICE_SUPPORT | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_SIM_NOT_INSERTED | Unable to perform the UICC operation because the UICC is missing. |
| MBIM_STATUS_BAD_SIM | Unable to perform the UICC operation because the UICC is in an error state. |
| MBIM_STATUS_NOT_INITIALIZED | Unable to perform the UICC operation because the UICC is not yet fully initialized. |
| MBIM_STATUS_MS_INVALID_LOGICAL_CHANNEL | The logical channel number is not valid (in other words, it was not opened with MBIM_CID_MS_UICC_OPEN_CHANNEL). |

If the function can send the APDU to the UICC, it returns MBIM_STATUS_SUCCESS along with the SW1 SW2 status words and the response from the UICC (if any). The host must examine the status (SW1 SW2) to determine whether the APDU command succeeded on the UICC or the reason that it failed.

## MBIM_CID_MS_UICC_TERMINAL_CAPABILITY

The host sends MBIM_CID_MS_UICC_TERMINAL_CAPABILITY to inform the modem about the capabilities of the host. The TERMINAL CAPABILITY APDU, specified in Section 11.1.19 of the [ETSI TS 102 221 technical specification](https://go.microsoft.com/fwlink/p/?linkid=864594), must be sent to the card before the first application is selected (if it is supported). Therefore, the host cannot directly send the TERMINAL CAPABILITY APDU but rather sends the MBIM_CID_MS_UICC_TERMINAL_CAPABILITY command containing one or more terminal capability objects which would be stored persistently by the modem. On the next card insertion or reset, after the ATR, the modem would SELECT the MF and check whether TERMINAL CAPABILITY is supported. If so, the modem would send the TERMINAL CAPABILITY APDU with the information specified by the MBIM_CID_MS_UICC_TERMINAL_CAPABILITY command as well as any modem-generated information.

### Parameters

| Operation | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | MBIM_MS_SET_UICC_TERMINAL_CAPABILITY | Empty | Not applicable |
| Response | Not applicable | MBIM_MS_TERMINAL_CAPABILITY_INFO | Not applicable |

### Query

The InformationBuffer shall be null and InformationBufferLength shall be zero.

### Set

The InformationBuffer of MBIM_COMMAND_MSG contains the following MBIM_MS_SET_UICC_TERMINAL_CAPABILITY structure.

#### MBIM_MS_SET_UICC_TERMINAL_CAPABILITY

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ElementCount | UINT32 | The element count of terminal capability objects. |
| 4 | 8*EC | CapabilityList	OL_PAIR_LIST| An offset-length pair list for each terminal capability object TLV. |
| 4+8*EC | - | DataBuffer | DATABUFFER | A byte array of the actual terminal capability object TLVs. |

### Response

Responses will contain the exact SET command with the last sent terminal capability objects to the modem. Therefore, MBIM_MS_TERMINAL_CAPABILITY_INFO is identical to MBIM_MS_SET_UICC_TERMINAL_CAPABILITY.

#### MBIM_MS_TERMINAL_CAPABILITY_INFO

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ElementCount | UINT32 | The element count of terminal capability objects. |
| 4 | 8*EC | CapabilityList	OL_PAIR_LIST| An offset-length pair list for each terminal capability object TLV. |
| 4+8*EC | - | DataBuffer | DATABUFFER | A byte array of the actual terminal capability object TLVs. |

### Unsolicited events

Not applicable.

### Status codes

| Status code | Description |
| --- | --- |
| MBIM_STATUS_SUCCESS | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_BUSY | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_FAILURE | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_NO_DEVICE_SUPPORT | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_SIM_NOT_INSERTED | Unable to perform the UICC operation because the UICC is missing. |
| MBIM_STATUS_BAD_SIM | Unable to perform the UICC operation because the UICC is in an error state. |
| MBIM_STATUS_NOT_INITIALIZED | Unable to perform the UICC operation because the UICC is not yet fully initialized. |
| MBIM_STATUS_MS_INVALID_LOGICAL_CHANNEL | The logical channel number is not valid (in other words, it was not opened with MBIM_CID_MS_UICC_OPEN_CHANNEL). |

## MBIM_CID_MS_UICC_RESET

The host sends MBIM_CID_MS_UICC_RESET to the MBIM function to reset the UICC or to query the passthrough state of the function.

When the host requests that the function reset the UICC, it specifies a passthrough action.

If the host specifies the *MBIMMsUICCPassThroughEnable* passthrough action, the function resets the UICC and, upon UICC power up, treats the UICC as if it were in a passthrough mode that enables communication between the host and UICC (even if the UICC has no Telecom UICC file system). The function does not send any APDUs to the card and does not interfere at any time with the communication between the host and the UICC.

If the host specifies the *MBIMMsUICCPassThroughDisable* passthrough action, the function resets the UICC and, upon UICC power up, treats the UICC as a regular Telecom UICC and expects a Telecom UICC file system to be present on the UICC.

When the host queries the function to determine the passthrough status, if the function responds with the *MBIMMsUICCPassThroughEnabled* status, it means that passthrough mode is enabled. If the function responds with the *MBIMMsUICCPassThroughDisabled* status, it means that passthrough mode is disabled.

### Parameters

| Type  | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | MBIM_MS_SET_UICC_RESET | Empty | Not applicable |
| Response | MBIM_MS_UICC_RESET_INFO | MBIM_MS_UICC_RESET_INFO | Not applicable |

### Query

The InformationBuffer shall be null and *InformationBufferLength* shall be zero.

### Set

#### MBIM_SET_MS_UICC_RESET

The MBIM_SET_MS_UICC_RESET structure contains the passthrough action specified by the host.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | PassThroughAction | MBIM_MS_UICC_PASSTHROUGH_ACTION | For more info, see [MBIM_MS_UICC_PASSTHROUGH_ACTION](#mbim_ms_uicc_passthrough_action). |

#### <a name="mbim_ms_uicc_passthrough_action">MBIM_MS_UICC_PASSTHROUGH_ACTION</a>

The MBIM_MS_UICC_PASSTHROUGH_ACTION enumeration defines the types of passthrough actions the host can specify to the MBIM function.

| Types | Value |
| --- | --- |
| MBIMMsUiccPassThroughDisable | 0 |
| MBIMMsUiccPassThroughEnable | 1 |

### Response

#### MBIM_MS_UICC_RESET_INFO

The MBIM_MS_UICC_RESET_INFO structure contains the passthrough status of the MBIM function.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | PassThroughStatus | MBIM_MS_UICC_PASSTHROUGH_STATUS | For more info, see [MBIM_MS_UICC_PASSTHROUGH_STATUS](#mbim_ms_uicc_passthrough_status). |

#### <a name="mbim_ms_uicc_passthrough_status">MBIM_MS_UICC_PASSTHROUGH_STATUS</a> 

The MBIM_MS_UICC_PASSTHROUGH_STATUS enumeration defines the types of passthrough status the MBIM function specifies to the host.

| Types | Value |
| --- | --- |
| MBIMMsUiccPassThroughDisabled | 0 |
| MBIMMsUiccPassThroughEnabled | 1 |

### Unsolicited events

Not applicable.

### Status codes

| Status code | Description |
| --- | --- |
| MBIM_STATUS_SUCCESS | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_BUSY | The device is busy. |
| MBIM_STATUS_FAILURE | The operation failed. |
| MBIM_STATUS_NO_DEVICE_SUPPORT | The device does not support this operation. |

### OID_WWAN_UICC_RESET

The NDIS equivalent for MBIM_CID_MS_UICC_RESET is [OID_WWAN_UICC_RESET](oid-wwan-uicc-reset.md). 


