---
title: Microsoft-defined Bluetooth HCI commands and events
description: The Bluetooth Host-Controller Interface (HCI) specifies all interactions between a host and a Bluetooth radio controller.
ms.date: 04/17/2023
---

# Microsoft-defined Bluetooth HCI extensions

The Bluetooth Host-Controller Interface (HCI) specifies all interactions between a host and a Bluetooth radio controller. Bluetooth specifications allow vendor-defined HCI commands and events to enable nonstandardized interaction between hosts and controllers. Microsoft defines vendor-specific HCI commands and events that are consumed by Windows. Bluetooth controller implementers can use these extensions to implement special features.

## Requirements

Bluetooth HCI commands are identified by a 16-bit command code. The Bluetooth organization defines values in the range 0x0000 through 0xFBFF. Vendors define values in the range 0xFC00 through 0xFFFF, allowing for 1024 different possible vendor-assigned command codes.

The vendor must choose the value of the Microsoft-defined command code. Microsoft can't choose a command code and assume that no other vendor uses the code for a conflicting purpose. It's unsafe to issue a vendor-specific command and depend on the controller to reject the command if it doesn't understand it. The controller could interpret the command as a destructive operation such as updating the controller's firmware.

The vendor must communicate the chosen value through a method other than the controller. Microsoft doesn't specify how to get the chosen code.

### Notifying Windows Bluetooth stack of the vendor specific command code

The Windows Bluetooth stack reads the vendor-specific command code from a registry key, `VsMsftOpCode`.

The `VsMsftOpCode` registry key has a type of REG_DWORD and the key data is the vendor specific opcode.

To specify the vendor specific opcode, use the `AddReg` directive under *DDInstall.HW* section in the driver's INF. The add registry section should contain:

```inf
HKR,,"VsMsftOpCode",0x00010001,<Vendor Specific Opcode>
```

Example:

```inf
[radio.NTamd64.HW]
AddReg=radio.NTamd64.HW.AddReg
[radio.NTamd64.HW.AddReg]
HKR,,"VsMsftOpCode",0x00010001,<Vendor Specific Opcode>
```

## Microsoft-defined HCI commands

| HCI Commands | Description |
|--|--|
| [HCI_VS_MSFT_Read_Supported_Features][ref_HCI_VS_MSFT_Read_Supported_Features] | Provides a bitmap that describes which Microsoft-defined features the controller supports, and specifies the prefix for Microsoft-defined events that are returned by the controller. |
| [HCI_VS_MSFT_Monitor_Rssi][ref_HCI_VS_MSFT_Monitor_Rssi] | Requests that the controller starts monitoring the measured link RSSI for a specified connection, and generates an event when the connection's measured link RSSI goes outside of the specified bounds. |
| [HCI_VS_MSFT_Cancel_Monitor_Rssi][ref_HCI_VS_MSFT_Cancel_Monitor_Rssi] | Cancels a previously issued [HCI_VS_MSFT_Monitor_Rssi][ref_HCI_VS_MSFT_Monitor_Rssi] command. |
| [HCI_VS_MSFT_LE_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Monitor_Advertisement] | Requests that the controller starts monitoring for advertisements that fall within the specified RSSI range and also satisfy other requirements. |
| [HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement] | Cancels a previously issued [HCI_VS_MSFT_LE_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Monitor_Advertisement] command. |
| [HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable][ref_HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable] | Sets the state of the advertisement filters. |
| [HCI_VS_MSFT_Read_Absolute_RSSI][ref_HCI_VS_MSFT_Read_Absolute_RSSI] | Reads the absolute Received Signal Strength Indication (RSSI) value for a BR/EDR connection from the controller. |

### Microsoft-defined HCI command and subcommands

The controller understands there's only one Microsoft-specific HCI command. The Microsoft-specific command set is extended by using an opcode. The first command parameter for the Microsoft-defined HCI command is an opcode that specifies the subcommand.

Controllers must support [HCI_VS_MSFT_Read_Supported_Features][ref_HCI_VS_MSFT_Read_Supported_Features] in order to support any other Microsoft HCI subcommands. Support for other commands is optional and depends on the values returned by HCI_VS_MSFT_Read_Supported_Features. Windows doesn't send any Microsoft-defined subcommands unless the controller indicates support for the subcommand through a response to HCI_VS_MSFT_Read_Supported_Features.

### HCI_VS_MSFT_Read_Supported_Features

[ref_HCI_VS_MSFT_Read_Supported_Features]: #hci_vs_msft_read_supported_features

HCI_VS_MSFT_Read_Supported_Features provides a bitmap that describes which Microsoft-defined features the controller supports, and specifies the prefix for Microsoft-defined events that are returned by the controller.

The controller shall always complete this command promptly with a Command Completed event.

| Command | Code | Command parameters | Return parameters |
|--|--|--|--|
| HCI_VS_MSFT_Read_Supported_Features | Chosen base code | Subcommand_opcode | Status,<br>Subcommand_opcode,<br>Supported_features,<br>Microsoft_event_prefix_length,<br>Microsoft_event_prefix |

#### Command_parameters

**Subcommand_opcode** (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | The subcommand opcode for [HCI_VS_MSFT_Read_Supported_Features][ref_HCI_VS_MSFT_Read_Supported_Features]. |

#### Return_parameters

**Status** (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | The command succeeded. |
| 0x01&nbsp;to&nbsp;0xFF | The command failed. See *Error Codes* in the Bluetooth Core specification for details. |

**Subcommand_opcode** (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | The subcommand opcode for [HCI_VS_MSFT_Read_Supported_Features][ref_HCI_VS_MSFT_Read_Supported_Features]. |

**Supported_features** (8 octets):

| Value | Parameter description |
|--|--|
| 0x00000000&nbsp;00000001 | Controller supports the RSSI Monitoring feature for BR/EDR connections. In addition, the controller supports [HCI_VS_MSFT_Read_Absolute_RSSI][ref_HCI_VS_MSFT_Read_Absolute_RSSI] to read the absolute RSSI metric of a BR/EDR connection. |
| 0x00000000&nbsp;00000002 | Controller supports the RSSI Monitoring feature for LE connections. |
| 0x00000000&nbsp;00000004 | Controller supports the RSSI Monitoring of LE legacy advertisements. |
| 0x00000000&nbsp;00000008 | Controller supports Advertising Monitoring of LE legacy advertisements. |
| 0x00000000&nbsp;00000010 | Controller supports verifying the validity of the public X and Y coordinates on the curve during the Secure Simple pairing process for P-192 and P-256. <br>For more information, see [Bluetooth Core Specification Erratum 10734](https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=447440). |
| 0x00000000&nbsp;00000020 | Controller supports Continuous Advertising Monitoring of LE advertisements performed concurrently with other radio activities, using [HCI_VS_MSFT_LE_Monitor_Advertisement [v1]][ref_HCI_VS_MSFT_LE_Monitor_Advertisement]. |
| 0x00000000&nbsp;00000040 | Reserved. |
| 0x00000000&nbsp;00000080 | Reserved. |
| 0x00000000&nbsp;00000100 | Reserved. |
| 0x00000000&nbsp;00000200 | Reserved. |
| 0x00000000&nbsp;00000400 | Controller supports [HCI_VS_MSFT_LE_Monitor_Advertisement [v2]][ref_HCI_VS_MSFT_LE_Monitor_Advertisement]. Additionally, the Controller supports Continuous Advertising Monitoring of LE advertisements performed concurrently with other radio activities, using [HCI_VS_MSFT_LE_Monitor_Advertisement [v2]][ref_HCI_VS_MSFT_LE_Monitor_Advertisement]. |
| 0xFFFFFFFF&nbsp;FFFFF800 | Bits reserved for future definition. Must be zero. |

**Microsoft_event_prefix_length** (1 octet):

| Value | Parameter description |
|--|--|
| 0x00&nbsp;to&nbsp;0x20 | Number of bytes in the Microsoft event prefix field as specified in the returned *Microsoft_event_prefix*. This is the number of bytes of constant information at the beginning of every Microsoft-specified HCI event. |

**Microsoft_event_prefix** (variable length):

| Value | Parameter description |
|--|--|
| Event&nbsp;prefix&nbsp;value | The constant information to expect at the beginning of each Microsoft-defined event. This information is used to distinguish Microsoft-defined events from other custom events. |

### HCI_VS_MSFT_Monitor_Rssi

[ref_HCI_VS_MSFT_Monitor_Rssi]: #hci_vs_msft_monitor_rssi

HCI_VS_MSFT_Monitor_Rssi requests that the controller starts monitoring the measured link RSSI for a specified connection, and generates an event when the connection's measured link RSSI goes outside of the specified bounds.

| Command | Code | Command parameters | Return parameters |
|--|--|--|--|
| HCI_VS_MSFT_Monitor_Rssi | Chosen base code | Subcommand_opcode,<br>Connection_Handle,<br>RSSI_threshold_high,<br>RSSI_threshold_low,<br>RSSI_threshold_low_time_interval,<br>RSSI_sampling_period | Status,<br>Subcommand_opcode |

The controller shall notify the host of the RSSI value with a periodically generated event (based on the *RSSI_sampling_period*). The measured link RSSI shall be the **absolute** receiver signal strength value in dBm for the BR/EDR connection.

In response to a HCI_VS_MSFT_Monitor_Rssi command, the controller shall generate a Command Complete event with status equaling zero if the controller can begin monitoring, or a nonzero status otherwise. If the status value is nonzero, the controller shall not generate an [HCI_VS_MSFT_Rssi_Event][ref_HCI_VS_MSFT_Rssi_Event] in response to this command.

The controller shall refuse the command if another HCI_VS_MSFT_Monitor_Rssi command with the same *Connection_Handle* is outstanding, or if the specified connection handle is invalid. The controller may also refuse the command for other reasons, such as resource exhaustion.

This state diagram shows the transition states on the controller when monitoring RSSI for a connection.

:::image type="content" source="images/HCI_VS_MSFT_Monitor_Rssi_State_Diagram.png" alt-text="State diagram of HCI_VS_MSFT_Monitor_Rssi":::

The controller shall generate an [HCI_VS_MSFT_Rssi_Event][ref_HCI_VS_MSFT_Rssi_Event] when the received RSSI is greater than or equal to the specified *RSSI_threshold_high*. After this event has been generated, the controller shall not generate a new [HCI_VS_MSFT_Rssi_Event][ref_HCI_VS_MSFT_Rssi_Event] to specify that the *RSSI_threshold_high* has been exceeded until it generates an [HCI_VS_MSFT_Rssi_Event][ref_HCI_VS_MSFT_Rssi_Event] that specifies the RSSI has fallen below *RSSI_threshold_low*.

The controller shall generate an [HCI_VS_MSFT_Rssi_Event][ref_HCI_VS_MSFT_Rssi_Event] when the received RSSI equals or falls below the specified *RSSI_threshold_low* over the specified *RSSI_threshold_low_time_interval*. After this event has been generated, the controller shall not generate a new [HCI_VS_MSFT_Rssi_Event][ref_HCI_VS_MSFT_Rssi_Event] to specify that the RSSI has fallen below the *RSSI_threshold_low* until an [HCI_VS_MSFT_Rssi_Event][ref_HCI_VS_MSFT_Rssi_Event] event is generated to specify that *RSSI_threshold_high* has been reached or exceeded.

If the *RSSI_sampling_period* is between 0x01 and 0xFE, the controller shall generate an [HCI_VS_MSFT_Rssi_Event][ref_HCI_VS_MSFT_Rssi_Event] periodically every *RSSI_sampling_period*. This event shall contain the average of the RSSI calculated over the *RSSI_sampling_period*.
If the *RSSI_sampling_period* is 0x00 or 0xFF, the controller shall **not** notify the host periodically with [HCI_VS_MSFT_Rssi_Event][ref_HCI_VS_MSFT_Rssi_Event].

#### Command_parameters

Subcommand_opcode (1 octet):

| Value | Parameter description |
|--|--|
| 0x01 | The subcommand opcode for [HCI_VS_MSFT_Monitor_Rssi][ref_HCI_VS_MSFT_Monitor_Rssi]. |

Connection_Handle (2 octets):

| Value | Parameter description |
|--|--|
| 0xXXXX | The handle for the connection whose RSSI must be monitored. |

RSSI_threshold_high (1 octet):

| Value | Parameter description |
|--|--|
| 0xXX | The maximum expected RSSI value. The controller generates an event if the observed RSSI becomes greater than or equal to this value.<br>Unit: dBm<br>BR/EDR Range: -128&nbsp;to&nbsp;127 (signed integer)<br>LE Range: -127&nbsp;to&nbsp;20 (signed integer) |

RSSI_threshold_low (1 octet):

| Value | Parameter description |
|--|--|
| 0xXX | The minimum expected RSSI value. The controller generates an event if the observed RSSI becomes less than or equal to this value.<br>Unit: dBm<br>BR/EDR Mandatory Range: -128&nbsp;to&nbsp;127 (signed integer)<br>LE Mandatory Range: -127&nbsp;to&nbsp;20 (signed integer) |

RSSI_threshold_low_time_interval (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | Reserved value. |
| *N*&nbsp;=&nbsp;0xXX | The time in seconds over which the RSSI value should be below *RSSI_threshold_low* before an [HCI_VS_MSFT_Rssi_Event][ref_HCI_VS_MSFT_Rssi_Event] is generated.<br>Time period = *N* * 1 second<br>Mandatory Range: 0x01&nbsp;to&nbsp;0x3C |

RSSI_sampling_period (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | Reserved value. |
| *N*&nbsp;=&nbsp;0xXX | The sampling interval in milliseconds.<br>Time period = *N* * 100 milliseconds<br>Mandatory Range: 0x01&nbsp;to&nbsp;0xFE |
| 0xFF | Reserved value. |

#### Return_parameters

Status (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | The command succeeded. |
| 0x01&nbsp;to&nbsp;0xFF | The command failed. See *Error Codes* in the Bluetooth Core specification for details. |
| 0x07 | The controller shall return *Memory Capacity Exceeded* if it doesn't have enough memory to process the command. |
| *Error&nbsp;code* | The command failed. See *Error Codes* in the Bluetooth Core specification for details. |

Subcommand_opcode (1 octet):

| Value | Parameter description |
|--|--|
| 0x01 | The subcommand opcode for HCI_VS_MSFT_Monitor_Rssi. |

#### Events Generated Unless Masked Away

The controller shall promptly generate a Command Complete event when the [HCI_VS_MSFT_Monitor_Rssi][ref_HCI_VS_MSFT_Monitor_Rssi] command is received. If the Command Complete event returns a status of  0, the controller shall generate an [HCI_VS_MSFT_Rssi_Event][ref_HCI_VS_MSFT_Rssi_Event] when one of the following conditions occurs.

- The observed RSSI for the device over *RSSI_threshold_low_time_interval* becomes equal to or less than the specified *RSSI_threshold_low* value.
- The observed RSSI for the device becomes greater than or equal to the specified *RSSI_threshold_high* value.
- The *RSSI_sampling_period* is valid and the sampling period expires.

The controller should do all necessary cleanup if connectivity with the specified device is lost. In this case, an [HCI_VS_MSFT_Cancel_Monitor_Rssi][ref_HCI_VS_MSFT_Cancel_Monitor_Rssi] command isn't sent to the controller.

### HCI_VS_MSFT_Cancel_Monitor_Rssi

[ref_HCI_VS_MSFT_Cancel_Monitor_Rssi]: #hci_vs_msft_cancel_monitor_rssi

HCI_VS_MSFT_Cancel_Monitor_Rssi cancels a previously issued [HCI_VS_MSFT_Monitor_Rssi][ref_HCI_VS_MSFT_Monitor_Rssi] command.
The controller shall promptly generate a Command Completed event in response to this command.

| Command | Code | Command parameters | Return parameters |
|--|--|--|--|
| HCI_VS_MSFT_Cancel_Monitor_Rssi | Chosen base code | Subcommand_opcode,<br>Connection_Handle | Status,<br>Subcommand_opcode |

#### Command_parameters

Subcommand_opcode (1 octet):

| Value | Parameter description |
|--|--|
| 0x02 | The subcommand opcode for [HCI_VS_MSFT_Cancel_Monitor_Rssi][ref_HCI_VS_MSFT_Cancel_Monitor_Rssi]. |

Connection_Handle (2 octets):

| Value | Parameter description |
|--|--|
| 0xXXXX | The handle for the connection whose RSSI must be canceled. |

#### Return_parameters

Status (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | The command succeeded. |
| 0x01&nbsp;to&nbsp;0xFF | The command failed. See *Error Codes* in the Bluetooth Core specification for details. |

Subcommand_opcode (1 octet):

| Value | Parameter description |
|--|--|
| 0x02 | The subcommand opcode for [HCI_VS_MSFT_Cancel_Monitor_Rssi][ref_HCI_VS_MSFT_Cancel_Monitor_Rssi]. |

#### Events Generated Unless Masked Away

The controller shall generate a Command Complete event when the [HCI_VS_MSFT_Cancel_Monitor_RSSI][ref_HCI_VS_MSFT_Cancel_Monitor_RSSI] command is received.

### HCI_VS_MSFT_LE_Monitor_Advertisement

[ref_HCI_VS_MSFT_LE_Monitor_Advertisement]: #hci_vs_msft_le_monitor_advertisement

HCI_VS_MSFT_LE_Monitor_Advertisement requests that the controller starts monitoring for advertisements that fall within the specified RSSI range and also satisfy one of the following conditions:

- A specified pattern can be matched to the received advertisement packet.
- A specified UUID can be matched to the received advertisement packet.
- A specified Identity Resolution Key (IRK) can be used to resolve the private address of the device from which the advertisement packet originated.
- A specified Bluetooth Address can be matched to the received advertisement packet.

The v2 command permits the Host to combine some of the above conditions with options governing the source of the advertisement and the target of a directed advertisement, to further refine which advertisements are monitored. The v2 command also permits the Host to filter which monitored advertisements cause the Controller to generate advertisement reports.

| Command | Code | Command parameters | Return parameters |
|--|--|--|--|
| HCI_VS_MSFT_LE_Monitor_Advertisement [v2] | Chosen base code | Subcommand_opcode_v2,<br>RSSI_threshold_high,<br>RSSI_threshold_low,<br>RSSI_threshold_low_time_interval,<br>RSSI_sampling_period,<br>Monitor_options,<br>Advertisement_report_filtering_options,<br>Peer_device_address,<br>Peer_device_address_type,<br>Peer_device_IRK,<br>Condition_type,<br>\<Condition Parameters\> | Status,<br>Subcommand_opcode,<br>Monitor_Handle |
| HCI_VS_MSFT_LE_Monitor_Advertisement [v1] | Chosen base code | Subcommand_opcode_v1,<br>RSSI_threshold_high,<br>RSSI_threshold_low,<br>RSSI_threshold_low_time_interval,<br>RSSI_sampling_period,<br>Condition_type,<br>\<Condition Parameters\> | Status,<br>Subcommand_opcode,<br>Monitor_Handle |

The controller shall generate a Command Complete event in response to this command. The status value should be set to zero if the controller can begin monitoring, or a nonzero status otherwise.
If the controller doesn't support RSSI monitoring for LE Advertisements, it shall ignore the *RSSI_threshold_high*, *RSSI_threshold_low*, *RSSI_threshold_low_time_interval*, and *RSSI_sampling_period* parameter values.

This state diagram shows the transition states on the controller when monitoring RSSI for an advertisement.

:::image type="content" source="images/HCI_VS_MSFT_LE_Monitor_Advertisement_State_Diagram.svg" alt-text="State diagram for HCI_VS_MSFT_LE_Monitor_Advertisement.":::

The controller shall begin monitoring an advertisement only when the received RSSI is greater than or equal to *RSSI_threshold_high* for a particular device and the *Monitor_options* match (see below).  The controller shall generate an [HCI_VS_MSFT_LE_Monitor_Device_Event][ref_HCI_VS_MSFT_LE_Monitor_Device_Event] with *Monitor_state* set to 1 and *Monitor_handle* set to the handle for this *Condition*, to notify the host that the controller is monitoring this particular device for *Condition*. Additionally, the Controller shall propagate the first advertisement report of a monitored advertisement to the Host only when the *Advertisement_report_filter_options* match (see below).

The *Monitor_options* for a filter are considered a match based on the following logic:

```
MatchesCondition = (PDU Matches Condition Parameters)

IsAdvAMatch = ((_Monitor_options_ bit 0 is set) && ((AdvA == _Peer_device_address_) && (TxAdd == _Peer_device_address_type_))) ||
    ((_Monitor_options_ bit 1 is set) && (AdvA resolvable with _Peer_device_IRK_))

IsDirectedAdvAMatch = (TargetA is permitted based on the Scanning Filter Policy) &&
    (((Monitor_options bit 2 is set) && ((AdvA == Peer_device_address) && (TxAdd == Peer_device_address_type))) ||
        ((Monitor_options bit 3 is set) && (AdvA resolvable with Peer_device_IRK)))

IsDirectedTargetAMatch = (Monitor_options bit 4 is set) &&
    (TargetA is permitted based on the Scanning Filter Policy)

MonitorOptionsMatch = (MatchesCondition && IsAdvAMatch) ||
    IsDirectedAdvAMatch ||
    IsDirectedTargetAMatch ||
    ((Monitor_options bit 5 is set) && MatchesCondition)
```

And for a monitored advertisement, the *Advertisement_report_filter_options* are considered a match based on the following logic:

```
IsDuplicateFilterSatisfied = (Advertisement_report_filter_options bit 0 is NOT set || PDU is not a duplicate)

ShouldGenerateLegacyReport = (Advertisement_report_filter_options bit 1 is set) &&
    (PDU is Legacy) &&
    MonitorOptionsMatch

ShouldGenerateExtendedReport = (Advertisement_report_filter_options bit 2 is set) &&
    (PDU is Extended) &&
    MonitorOptionsMatch

ShouldGenerateDirectedReport = (Advertisement_report_filter_options bit 3 is set) &&
    (PDU is Directed) &&
    MonitorOptionsMatch

AdvertisementReportFilterOptionsMatch = IsDuplicateFilterSatisfied &&
    (ShouldGenerateLegacyReport || ShouldGenerateExtendedReport || ShouldGenerateDirectedReport)
```

The controller shall stop monitoring for *Condition* if the RSSI of the received advertisements equals or falls below  *RSSI_threshold_low* over *RSSI_threshold_low_interval* for the particular device. The controller shall generate an [HCI_VS_MSFT_LE_Monitor_Device_Event][ref_HCI_VS_MSFT_LE_Monitor_Device_Event] with *Monitor_state* set to 0 to notify the host that the controller has stopped monitoring the particular device for the *Condition*. After the controller specifies the HCI_VS_MSFT_LE_Monitor_Device_Event with *Monitor_state* set to 0, the controller shall not allow further advertisement packets to flow to the host for the device until the controller has notified the host that the RSSI for the particular device has risen to or above *RSSI_threshold_high* for the particular device for the *Condition*.

Additionally, the controller shall generate an [HCI_VS_MSFT_LE_Monitor_Device_Event][ref_HCI_VS_MSFT_LE_Monitor_Device_Event] with *Monitor_state* set to 0 to notify the host that the controller has stopped monitoring the device for the *Condition* if the specified *RSSI_threshold_low_time_interval* expires without receiving any advertising packets from the device. If the controller is monitoring a device for a particular condition, the following statements are true.

If the controller supports the RSSI monitoring of LE extended advertisements without sampling, the controller shall propagate anonymous advertisement packets to the host if the RSSI value for the packet is greater than or equal to *RSSI_threshold_high*. Anonymous advertisements shall not be tracked and the [HCI_VS_MSFT_LE_Monitor_Device_Event][ref_HCI_VS_MSFT_LE_Monitor_Device_Event] event shall not be generated.

If the controller supports the RSSI monitoring of LE advertisements without sampling, the controller shall generate a truncated advertising report in the case where the received fragment(s) of the advertisement are matching, but where the entire advertisement was not received successfully.

The Controller shall support a minimum of 30 simultaneous Monitor_handles, a minimum of 30 simultaneous tracked devices, and a minimum of 20 simultaneous tracked duplicate advertisements. The Controller shall also be capable of performing a continuous LE scan at 10% duty cycle.

If Address Resolution is enabled in the Controller and the Host intends to monitor a remote device with its IRK successfully stored in the Controller's resolving list, then the Host shall provide the Peer_Identity_Address and Peer_Identity_Address_Type parameters from the remote device’s resolving list entry as the Peer_device_address and Peer_device_address_type parameters, respectively.

| *RSSI_sampling_period* | Legacy Advertisements | Extended Advertisements (Non-Anonymous) | Extended Advertisements (Anonymous) |
|--|--|--|--|
| 0x00 | The controller shall propagate all received advertisement packets to the host for the device for this *Condition* unless the controller previously received an [HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable][ref_HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable] command with *Enable* set to 0x00. The controller shall propagate an advertisement packet to the host even if the received RSSI is less than or equal to *RSSI_threshold_low* as long as *RSSI_threshold_low_time_interval* hasn't expired for the particular device for this *Condition*. The RSSI value of this advertisement packet shall be the RSSI value of the received advertisement. | If the controller supports the RSSI monitoring of LE extended advertisements without sampling, same behavior as *Legacy Advertisements* column except that an advertisement packet is defined as all PDUs in the advertising chain. | If the controller supports the RSSI monitoring of LE extended advertisements without sampling, the controller shall propagate all received advertisement packets to the host for the device for this *Condition* unless the controller previously received an [HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable][ref_HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable] command with *Enable* set to 0x00. |
| 0x01&nbsp;to&nbsp;0xFE | The controller shall propagate legacy advertisement packets to the host every *RSSI_sampling_period* specified unless the controller previously received an [HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable][ref_HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable] command with *Enable* set to 0x00. The RSSI value specified for the advertisement shall be the average of the RSSI value received during this sampling interval. If the controller doesn't receive an advertisement packet during the sampling period, it shall not propagate an advertisement to the host. It's possible that *RSSI_sampling_period* is less than *RSSI_threshold_low_time_interval* and all advertisements received during the *RSSI_sampling_period* have RSSI below *RSSI_threshold_low*. The controller shall still propagate the advertisement with the average of the RSSI value received during this sampling interval. | If the controller supports the RSSI monitoring of LE extended advertisements without sampling, the controller shall behave as if the *RSSI_sampling_period* was 0x00. | If the controller supports the RSSI monitoring of LE extended advertisements without sampling, the controller shall behave as if the *RSSI_sampling_period* was 0x00. |
| 0xFF | The controller shall not allow further advertisement packets to flow to the host for the device for the *Condition* until the controller has notified the host that the particular device's RSSI has fallen below *RSSI_threshold_low* for *RSSI_threshold_low_time_interval* for the particular device for this *Condition*. This notification is done by generating an [HCI_VS_MSFT_LE_Monitor_Device_Event][ref_HCI_VS_MSFT_LE_Monitor_Device_Event] with *Monitor_state* set to 0. | If the controller supports the RSSI monitoring of LE extended advertisements without sampling, same behavior as *Legacy Advertisements* column. | If the controller supports the RSSI monitoring of LE extended advertisements without sampling, the controller shall behave as if the *RSSI_sampling_period* was 0x00. |

If the controller previously received an [HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable][ref_HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable] command with *Enable* set to 0x00, the sampling period timer shall not be stopped. See Example: HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable on filters with sampling period for more information.
If the controller receives nonduplicate advertisement packets from the same device, it shall match each advertisement packet against the Conditions stored on the controller.

If the controller receives an advertisement packet from a device that matches multiple Conditions, then the controller shall generate an [HCI_VS_MSFT_LE_Monitor_Device_Event][ref_HCI_VS_MSFT_LE_Monitor_Device_Event] for each *Condition* that matched, with *Monitor_handle* set to the *Condition* that matched.

If the controller is unable to monitor the RSSI values for all devices in range that match the *Condition*, it keeps monitoring as many devices as it can. The decision on what devices should be monitored will depend on the RSSI values of the received advertisements. The controller shall monitor devices with the greater received signal strength.

If the controller has notified the host about a particular device (*A*) and it's monitoring devices at maximum hardware capacity, and if another device (*B*) comes into range with a higher RSSI value, then the controller shall notify the host that it has stopped monitoring the device (*A*) by generating an [HCI_VS_MSFT_LE_Monitor_Device_Event][ref_HCI_VS_MSFT_LE_Monitor_Device_Event] with *Monitor_state* set to 0. The controller shall also generate an HCI_VS_MSFT_LE_Monitor_Device_Event with *Monitor_state* set to 1 to notify the host that the device (*B*) is now being monitored.

#### Condition Type and Condition Parameters

The *Condition_type* parameter specifies whether the *Condition* parameter specifies a pattern, UUID, IRK, or BD_ADDR.

If the *Condition_type* parameter specifies a pattern, the *Condition* contains two sections that contain the number of patterns present within the *Condition*, and the pattern data.

:::image type="content" source="images/HCI_VS_MSFT_LE_Monitor_Advertisement_Conditions.png" alt-text="Pattern condition data layout":::

*Number of Patterns* specifies the number of patterns that need to be matched.

*Pattern Data* has the following format.

- *Length* specifies the length of this pattern include the data type and start byte of the pattern.
- *AD Type* specifies the AD Type field.
- *Start of Pattern* specifies the starting byte position of the pattern immediately following AD Type.
- *Pattern* has a size of (*Length* - 0x2) and is the pattern to be matched for the specified AD Type within the advertisement packet from the specified starting byte.

If there are multiple patterns specified, the controller shall ensure that at least one pattern matches the received advertisement.

If the controller supports the RSSI monitoring of LE extended advertisements without sampling:

- The controller shall look for the pattern in the first 251 octets of the Host Advertising Data and may look in any remaining octets of the Host Advertising Data. If the AD section extends beyond the first 251 octets of the Host Advertising Data, the controller shall look for the pattern within the part of the AD section that is in the first 251 octets of the Host Advertising Data and may look in any remaining octets of the Host Advertising Data. Note: based on fragmentation by the advertiser, the first 251 octets of the Host Advertising Data may extend across the AdvData of multiple advertising PDUs. Scanners should take care to limit the number of AuxPtrs that they follow, to avoid following excessively long chains of PDUs.

- The controller shall track based on a per device address per advertising set basis. The controller shall propagate a [HCI_VS_MSFT_LE_Monitor_Device_Event][ref_HCI_VS_MSFT_LE_Monitor_Device_Event] for each advertising set that matches the pattern even if the advertisement comes from the same device address.

If the *Condition_type* parameter specifies a UUID, the *Condition* parameter contains a UUID Type and a UUID. The UUID Type specifies whether the UUID is 16-bit, 32-bit, or 128-bit. The controller shall parse the Service UUID of the advertisement packet to check for the specified UUID. If UUID Type is defined as 0x01, the controller shall parse the Incomplete List of 16-bit service UUIDs and complete list of 16-bit service UUIDs specified in the Service UUID AD Type. If the UUID Type is defined as 0x02, the controller shall parse the Incomplete List of 32-bit service UUIDs and complete list of 32-bit UUIDs specified in the Service UUID AD Type. If the UUID Type specified is 0x03, the controller shall parse the Incomplete List of 128-bit Service UUIDs and complete list of 128-bit Service UUIDs specified in the Service UUID AD Type.

If the controller supports the RSSI monitoring of LE extended advertisements without sampling:

- The controller shall look for the Service UUID in the first 251 octets of the Host Advertising Data and may look in any remaining octets of the Host Advertising Data. If the AD section extends beyond the first 251 octets of the Host Advertising Data, the controller shall look for the Service UUID within the part of the AD section that is in the first 251 octets of the Host Advertising Data and may look in any remaining octets of the Host Advertising Data. Note: based on fragmentation by the advertiser, the first 251 octets of the Host Advertising Data may span the AdvData of multiple advertising PDUs. Scanners should take care to limit the number of AuxPtrs that they follow, to avoid following excessively long chains of PDUs.

- The controller shall track based on a per device address per advertising set basis. The controller shall propagate a [HCI_VS_MSFT_LE_Monitor_Device_Event][ref_HCI_VS_MSFT_LE_Monitor_Device_Event] for each advertising set that matches the Service UUID even if the advertisement comes from the same device.

If the *Condition_type* parameter specifies an IRK, the *Condition* parameter contains the IRK.

If the *Condition_type* parameter specifies a Bluetooth Address, the *Condition* parameter contains the address type and BD_ADDR.

The controller shall keep monitoring based on the conditions, even when scanning (Active or Passive) is enabled.
When active scanning is enabled, the scan response for an advertisement matching a filter shall be propagated to the host.

If the controller receives a HCI_VS_MSFT_LE_Monitor_Advertisement command when the filters are disabled (due to  a previously received [HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable][ref_HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable] command with *Enable* set to 0x00), the controller shall accept the command if it can, but set it to a disabled state.
The controller may also refuse the command for other reasons such as resource exhaustion.

If all bits of Monitor_options are clear, the Controller should return the error code _Invalid HCI Command Parameters_ (0x12).

If bit 1 or bit 3 of Monitor_options is set and Peer_device_IRK is set to an invalid IRK, or none of the bits of Monitor_options is set, the Controller should return the error code _Invalid HCI Command Parameters_ (0x12).

If bit 0 or bit 1 or bit 2 or bit 3 of Monitor_options is set and Condition_type is set to 0x03 or 0x04, then the Controller should return the error code _Invalid HCI Command Parameters_ (0x12).

If bit 0 of Advertisement_report_filter_options is set and RSSI_sampling_period is any value other than 0x00, the Controller should return the error code _Invalid HCI Command Parameters_ (0x12).

#### Missing parameters

When a version of this command is issued that does not include all the parameters, the following shall be used:

| Parameter | Value |
|--|--|
| Monitor_options | Bit 5 set; all other bits cleared |
| Advertisement_report_filter_options | Bits 1 and 2 set; all other bits cleared |
| Peer_device_IRK | 0x0000000000000000&nbsp;0000000000000000 |
| Peer_device_address | 0x000000000000 |
| Peer_device_address_type | 0x00 |

#### Command_parameters

Subcommand_opcode_v1 (1 octet):

| Value | Parameter description |
|--|--|
| 0x03 | The subcommand opcode for [HCI_VS_MSFT_LE_Monitor_Advertisement [v1]][ref_HCI_VS_MSFT_LE_Monitor_Advertisement]. |

Subcommand_opcode_v2 (1 octet):

| Value | Parameter description |
|--|--|
| 0x0F | The subcommand opcode for [HCI_VS_MSFT_LE_Monitor_Advertisement [v2]][ref_HCI_VS_MSFT_LE_Monitor_Advertisement]. |

RSSI_threshold_high (1 octet):

| Value | Parameter description |
|--|--|
| 0xXX | The maximum expected RSSI value. The controller generates an event if the observed RSSI becomes greater than or equal to this value.<br>Unit: dBm<br>Mandatory Range: -127 to 20 (signed integer) |

RSSI_threshold_low (1 octet):

| Value | Parameter description |
|--|--|
| 0xXX | The minimum expected RSSI value. The controller generates an event if the observed RSSI becomes less than or equal to this value.<br>Unit: dBm<br>Mandatory Range: -127 to 20 (signed integer) |

RSSI_threshold_low_time_interval (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | Reserved value. |
| *N*&nbsp;=&nbsp;0xXX | The time in seconds over which the RSSI value should be below *RSSI_threshold_low* before an [HCI_VS_MSFT_Rssi_Event][ref_HCI_VS_MSFT_Rssi_Event] is generated<br>Time period = *N* * 1 second<br>Mandatory Range: 0x01&nbsp;to&nbsp;0x3C. |

RSSI_sampling_period (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | The controller shall propagate all received advertisements to the host. |
| *N*&nbsp;=&nbsp;0xXX | The sampling interval in milliseconds.<br>Time period = *N* * 100 milliseconds.<br>Mandatory Range: 0x01&nbsp;to&nbsp;0xFE |
| 0xFF | The controller shall not propagate any of the received advertisements to the host. |

Monitor_options (1 octet):

| Bit number | Parameter description |
|--|--|
| 0 | The Controller shall monitor advertising PDUs where AdvA or its resolved Identity Address matches Peer_device_address and Peer_device_address_type and where TargetA is not present or, if it is present, the TargetA is permitted based on the Scanning Filter Policy, if those PDUs match the condition specified in Condition_Type. |
| 1 | The Controller shall monitor advertising PDUs where AdvA is resolvable with Peer_device_IRK and where TargetA is not present or, if it is present, the TargetA is permitted based on the Scanning Filter Policy, if those PDUs match the condition specified in Condition_Type. This bit shall not be set if Link Layer Privacy is in use in the Controller. |
| 2 | The Controller shall monitor directed advertising PDUs where the TargetA is permitted based on the Scanning Filter Policy and where AdvA or its resolved Identity Address matches Peer_device_address and Peer_device_address_type. This is regardless of whether the PDU matches the condition specified in Condition_Type. |
| 3 | The Controller shall monitor directed advertising PDUs where the TargetA is permitted based on the Scanning Filter Policy and where AdvA is resolvable with Peer_device_IRK. This is regardless of whether the PDU matches the condition specified in Condition_Type. This bit shall not be set if Link Layer Privacy is in use in the Controller. |
| 4 | The Controller shall monitor directed advertising PDUs where the TargetA is permitted based on the Scanning Filter Policy, regardless of the value of Peer_device_address and Peer_device_address_type or  Peer_device_IRK and regardless of whether the PDU matches the condition specified in Condition_Type. |
| 5 | The Controller shall monitor advertising PDUs from any AdvA where TargetA is not present or, if it is present, the TargetA is permitted based on the Scanning Filter Policy, if those PDUs match the condition specified in Condition_Type. |
| All other bits | Reserved for future use |

Advertisement_report_filtering_options (1 octet):

| Bit number | Parameter description |
|--|--|
| 0 | Filter duplicate advertising PDUs. This bit shall only be set if RSSI_sampling_period is 0x00. |
| 1 | The Controller shall generate HCI_LE_Advertising_Report events or HCI_LE_Directed_Advertising_Report events or HCI_LE_Extended_Advertising_Report events for Legacy advertising PDUs, if those PDUs match the specified Monitor_options. |
| 2 | The Controller shall generate HCI_LE_Extended_Advertising_Report events for Extended advertising PDUs, if those PDUs match the specified Monitor_options. |
| 3 | The Controller shall generate HCI_LE_Advertising_Report events or HCI_LE_Directed_Advertising_Report events or HCI_LE_Extended_Advertising_Report events for directed advertising PDUs, if those PDUs match the specified Monitor_options. |
| All other bits | Reserved for future use |

Peer_device_address (6 octets):

| Value | Parameter description |
|--|--|
| 0xXXXXXXXXXXXX | Public Device Address or Random Device Address to match. |

Peer_device_address_type (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | Public Device Address |
| 0x01 | Random Device Address |
| All other values | Reserved for future use |

Peer_device_IRK (16 octets):

| Value | Parameter description |
|--|--|
| 0x0000000000000000&nbsp;0000000000000000 | Invalid IRK. Shall not be the value when Monitor_options bit 1 is set or when Monitor_options bit 3 is set. |
| 0xXXXXXXXXXXXXXXXX&nbsp;XXXXXXXXXXXXXXXX | IRK of the device to match. Peer_device_address and Peer_device_address_type shall be populated. |


Condition_type (1 octet):

| Value | Parameter description |
|--|--|
| 0x01 | The condition is a pattern that has to be matched on the advertisement. |
| 0x02 | The condition is a UUID Type and a UUID. |
| 0x03 | The condition is the resolution of an IRK.  Excluded if any of Monitor_options bits 0, 1, 2, or 3 are set. |
| 0x04 | The condition is a Bluetooth address Type and a Bluetooth address. Excluded if any of Monitor_options bits 0, 1, 2, or 3 are set. |

Condition:
The applicable fields for Condition depend on the value of Condition_type. See the Condition_type and Condition parameters section for more information.

Number_of_patterns (1 octet):

| Value | Parameter description |
|--|--|
| 0xXX | The number of patterns specified within the Pattern_data parameter. |

Pattern_data (>3 octets):

| Value | Parameter description |
|--|--|
| Length | Length of this pattern. |
| Data type | Data Type of the advertisement section. The values are listed in the Bluetooth Assigned Numbers document. |
| Start byte | Starting position of the pattern to be matched for the specified Data Type. |
| Pattern | Pattern to be matched (size of Length – 0x2 bytes). |

UUID_type (1 octet):

| Value | Parameter description |
|--|--|
| 0x01 | The UUID is a 16-bit service. |
| 0x02 | The UUID is a 32-bit service. |
| 0x03 | The UUID is a 128-bit service. |

UUID (2, 4, or 16 octets):

| Value | Parameter description |
|--|--|
| 0xXXXX | 2 bytes if UUID_type is 0x01.<br>4 bytes if UUID_type is 0x02.<br>16 bytes if UUID_type is 0x03. |

IRK (16 octets):

| Value | Parameter description |
|--|--|
| 0xXXXXXXXX&nbsp;XXXXXXXX&nbsp;XXXXXXXX&nbsp;XXXXXXXX | The IRK to be used to resolve the private address. |

Address_type (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | Public Device Address. |
| 0x01 | Random Device Address. |
| 0x02&nbsp;to&nbsp;0xFF | Reserved values for future use. |

BD_ADDR (6 octets):

| Value | Parameter description |
|--|--|
| 0xXXXXXXXXXXXX | The Bluetooth address of the device to be monitored. |

#### Return_parameters

Status (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | The command succeeded. |
| 0x07 | The controller shall return Memory Capacity Exceeded if it doesn't have enough memory to process the command. |
| Error code | The command failed. See *Error Codes* in the Bluetooth Core specification for details. |

Subcommand_opcode (1 octet):

| Value | Parameter description |
|--|--|
| 0x03 or 0x0F | The subcommand opcode for [HCI_VS_MSFT_LE_Monitor_Advertisement [v1]][ref_HCI_VS_MSFT_LE_Monitor_Advertisement] or [HCI_VS_MSFT_LE_Monitor_Advertisement [v2]][ref_HCI_VS_MSFT_LE_Monitor_Advertisement], depending on which command was submitted. |

Monitor_handle (1 octet):

| Value | Parameter description |
|--|--|
| 0x00&nbsp;to&nbsp;0xFF | The handle to this rule. This handle is used as a parameter for [HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement] to cancel monitoring the advertisement.<br>This parameter is only valid if Status is 0x00. |

#### Events Generated Unless Masked Away

When the [HCI_VS_MSFT_LE_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Monitor_Advertisement] command is received, the controller shall generate a Command Complete event.

### HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement

[ref_HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement]: #hci_vs_msft_le_cancel_monitor_advertisement

HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement cancels a previously issued [HCI_VS_MSFT_LE_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Monitor_Advertisement] command.

| Command | Code | Command parameters | Return parameters |
|--|--|--|--|
| HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement | Chosen base code | Subcommand_opcode,<br>Monitor_handle | Status,<br>Subcommand_opcode |

The controller shall promptly generate a Command Completed event in response to this command.

#### Command_parameters

Subcommand_opcode (1 octet):

| Value | Parameter description |
|--|--|
| 0x04 | The subcommand opcode for [HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement]. |

Connection_Handle (1 octet):

| Value | Parameter description |
|--|--|
| 0xXX | The handle to the filter that is being canceled. |

#### Return_parameters

Status (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | The command succeeded. |
| 0x07 | The controller shall return Memory Capacity Exceeded if it doesn't have enough memory to process the command. |
| Error code | The command failed. See *Error Codes* in the Bluetooth Core specification for details. |

Subcommand_opcode (1 octet):

| Value | Parameter description |
|--|--|
| 0x04 | The subcommand opcode for [HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement]. |

#### Events Generated Unless Masked Away

The controller shall generate a Command Complete event when the [HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement] command is received.

### HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable

[ref_HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable]: #hci_vs_msft_le_set_advertisement_filter_enable

HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable sets the state of the advertisement filters.

| Command | Code | Command parameters | Return parameters |
|--|--|--|--|
| HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable | Chosen base code | Subcommand_opcode,<br>Enable | Status,<br>Subcommand_opcode |

If *Enable* is set to 0x00, the controller shall propagate received advertisements to the host based on existing filter accept list settings. The controller shall continue monitoring the devices that are currently being monitored and generate an [HCI_VS_MSFT_LE_Monitor_Device_Event][ref_HCI_VS_MSFT_LE_Monitor_Device_Event] with *Monitor_state* set to 0 if the device is no longer being monitored. The controller shall generate an [HCI_VS_MSFT_LE_Monitor_Device_Event][ref_HCI_VS_MSFT_LE_Monitor_Device_Event] with *Monitor_state* set to 1 if a new device is being monitored. The host may issue HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable with *Enable* set to 0x01 to reenable all the filter conditions.

If *Enable* is set to 0x01, this command enables all filters that were set with a previously issued [HCI_VS_MSFT_LE_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Monitor_Advertisement] command. The controller shall reject an HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable command if it doesn't toggle the filter state:

- The controller shall reject an HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable command with *Enable* set to 0x01 if it previously received an HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable command with *Enable* set to 0x01.
- The controller shall reject the HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable command with *Enable* set to 0x00 if it previously received an HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable command with *Enable* set to 0x00.

The default state of the advertisement filter shall be off. This state is equivalent to the controller previously receiving a HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable command with *Enable* set to 0x00.
The controller shall promptly generate a Command Completed event in response to this command.

#### Command_parameters

Subcommand_opcode (1 octet):

| Value | Parameter description |
|--|--|
| 0x05 | The subcommand opcode for [HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable][ref_HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable]. |

Enable (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | Revert to current filter accept list behavior, but continue monitoring devices based on the *Condition* from  [HCI_VS_MSFT_LE_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Monitor_Advertisement] commands. |
| 0x01 | Enable all issued [HCI_VS_MSFT_LE_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Monitor_Advertisement] commands on the controller. |

#### Return_parameter

Status (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | The command succeeded. |
| 0x0C | The controller shall return *Command Disallowed* if the controller rejected the command because it previously saw an [HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable][ref_HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable] command with *Enable* set to the same value as this command. |
| Error&nbsp;code | The command failed. See *Error Codes* in the Bluetooth Core specification for details. |

Subcommand_opcode (1 octet):

| Value | Parameter description |
|--|--|
| 0x05 | The subcommand opcode for [HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable][ref_HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable]. |

#### Events Generated Unless Masked Away

The controller shall generate a Command Complete event when the [HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable][ref_HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable] command is received.

#### HCI_VS_MSFT_Read_Absolute_RSSI

[ref_HCI_VS_MSFT_Read_Absolute_RSSI]: #hci_vs_msft_read_absolute_rssi

HCI_VS_MSFT_Read_Absolute_RSSI reads the **absolute** Received Signal Strength Indication (RSSI) value for a BR/EDR connection from the controller.

| Command | Code | Command parameters | Return parameters |
|--|--|--|--|
| HCI_VS_MSFT_Read_Absolute_RSSI | Chosen base code | Subcommand_opcode,<br>Connection_Handle | Status,<br>Subcommand_opcode,<br>Connection_Handle,<br>RSSI |

A connection handle is provided as both a command and return parameter to identify the ACL connection whose RSSI is being read. The RSSI metric is the **absolute** receiver signal strength in dBm to ± 6 dB accuracy. If the RSSI can't be read, the RSSI metric shall be set to 127.
The controller shall always complete this command promptly with a Command Completed event.

#### Command_parameters

Subcommand_opcode (1 octet):

| Value | Parameter description |
|--|--|
| 0x06 | The subcommand opcode for HCI_VS_MSFT_Read_Absolute_RSSI. |

Connection_Handle (2 octets):

| Value | Parameter description |
|--|--|
| 0xXXXX | The handle for the BR/EDR connection whose RSSI has to be read. |

#### Return_parameters

Status (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | The command succeeded. |
| 0x01&nbsp;to&nbsp;0xFF | The command failed. See *Error Codes* in the Bluetooth Core specification for details. |

Subcommand_opcode (1 octet):

| Value | Parameter description |
|--|--|
| 0x06 | The subcommand opcode for [HCI_VS_MSFT_Read_Absolute_RSSI][ref_HCI_VS_MSFT_Read_Absolute_RSSI]. |

Connection_Handle (2 octets):

| Value | Parameter description |
|--|--|
| 0xXXXX | The handle for the BR/EDR connection whose RSSI was read. |

RSSI (1 octet):

| Value | Parameter description |
|--|--|
| N = 0xXX | The RSSI value for the BR/EDR connection.<br>Unit: dBm<br>Mandatory Range: -128&nbsp;to&nbsp;127 (signed integer) |

#### Events Generated Unless Masked Away

The controller shall generate a Command Complete event when the [HCI_VS_MSFT_Read_Absolute_RSSI][ref_HCI_VS_MSFT_Read_Absolute_RSSI] command has completed.

## Microsoft-defined Bluetooth HCI events

All Microsoft-defined Bluetooth HCI events are vendor-defined events and use event code 0xFF. The event data for Microsoft events always starts with a constant string of bytes to distinguish the Microsoft-defined events from other vendor-defined events. The length and value of the constant string are defined by the controller implementer and returned in response to [HCI_VS_MSFT_Read_Supported_Features][ref_HCI_VS_MSFT_Read_Supported_Features].

| HCI event | Description |
|--|--|
| [HCI_VS_MSFT_Rssi_Event][ref_HCI_VS_MSFT_Rssi_Event] | HCI_VS_MSFT_RSSI_Event indicates that an [HCI_VS_MSFT_Monitor_Rssi][ref_HCI_VS_MSFT_Monitor_Rssi] command has completed. |
| [HCI_VS_MSFT_LE_Monitor_Device_Event][ref_HCI_VS_MSFT_LE_Monitor_Device_Event] | HCI_VS_MSFT_LE_Monitor_Device_Event indicates that the controller has either started or stopped monitoring a Bluetooth LE device. |

### HCI_VS_MSFT_RSSI_Event

[ref_HCI_VS_MSFT_RSSI_Event]: #hci_vs_msft_rssi_event

HCI_VS_MSFT_RSSI_Event indicates that an [HCI_VS_MSFT_Monitor_Rssi][ref_HCI_VS_MSFT_Monitor_Rssi] command has completed.
If the *Status* parameter is zero, the command completed because the RSSI value for the remote device changed to a value outside of the specified range. If the *Status* parameter is nonzero, the command completed because the RSSI value of the connection can no longer be monitored.

| Event | Event Code | Microsoft event code | Event parameters |
|--|--|--|--|
| HCI_VS_MSFT_RSSI_Event | 0xFF | 0x01 | Event_prefix,<br>Microsoft_event_code,<br>Status,<br>Connection_Handle,<br>RSSI |

#### Event_parameters

Event_prefix (variable size):

| Value | Parameter description |
|--|--|
| Event prefix | The event prefix that flags this event as Microsoft-defined. The size and value are as returned by the [HCI_VS_MSFT_Read_Supported_Features][ref_HCI_VS_MSFT_Read_Supported_Features] command. |

Microsoft_event_code (1 octet):

| Value | Parameter description |
|--|--|
| 0x01 | The event code for [HCI_VS_MSFT_RSSI_Event][ref_HCI_VS_MSFT_RSSI_Event]. |

Status (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | Success. The RSSI value of the connection has met one of the following conditions. The RSSI reached or exceeded *RSSI_threshold_high*.<br>The RSSI reached or dropped below *RSSI_threshold_low* over *RSSI_threshold_low_time_interval* seconds.<br>The *RSSI_sampling_period* has expired and this event was generated to notify the host of the RSSI value. |
| 0x01&nbsp;to&nbsp;0xFF | Failure. The RSSI value of the connection can no longer be monitored. The error code is usually one of codes that describes why the underlying ACL connection was lost. |

Connection_Handle (2 octets):

| Value | Parameter description |
|--|--|
| 0xXXXX | The handle for the connection whose RSSI is to be monitored. |

RSSI (1 octet):

| Value | Parameter description |
|--|--|
| 0xXX | The measured link RSSI value for the connection.<br>Unit: dBm<br>BR/EDR Range: -128&nbsp;to&nbsp;127 (signed integer)<br>LE Range: -127&nbsp;to&nbsp;20 (signed integer) |

### HCI_VS_MSFT_LE_Monitor_Device_Event

[ref_HCI_VS_MSFT_LE_Monitor_Device_Event]: #hci_vs_msft_le_monitor_device_event

HCI_VS_MSFT_LE_Monitor_Device_Event indicates that the controller has either started or stopped monitoring a Bluetooth LE device.

If the *Monitor_state* parameter value is 1, the controller started monitoring the Bluetooth device with the specified BD_ADDR. If the *Monitor_state* parameter value is 0, the controller stopped monitoring the Bluetooth device with the specified BD_ADDR.

| Event | Event Code | Microsoft event code | Event parameters |
|--|--|--|--|
| HCI_VS_MSFT_LE_Monitor_Device_Event | 0xFF | 0x02 | Event_prefix,<br>Microsoft_event_code,<br>Address_type,<br>BD_ADDR,<br>Monitor_handle,<br>Monitor_state |

The controller shall not generate an HCI_VS_MSFT_LE_Monitor_Device_Event with the *Monitor_state* parameter set to 0 if it hasn't already generated an HCI_VS_MSFT_LE_Monitor_Device_Event with *Monitor_state* set to 1.

#### Event_parameters

Event_prefix (variable size):

| Value | Parameter description |
|--|--|
| Event prefix | The event prefix that flags this event as Microsoft-defined. The size and value are as returned by the [HCI_VS_MSFT_Read_Supported_Features][ref_HCI_VS_MSFT_Read_Supported_Features] command. |

Microsoft_event_code (1 octet):

| Value | Parameter description |
|--|--|
| 0x02 | The event code for [HCI_VS_MSFT_LE_Monitor_Device_Event][ref_HCI_VS_MSFT_LE_Monitor_Device_Event]. |

Address_type (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | Public Device Address. |
| 0x01 | Random Device Address. |
| 0x02&nbsp;to&nbsp;0xFF | Reserved values for future use. |

BD_ADDR (6 octets):

| Value | Parameter description |
|--|--|
| 0xXXXXXXXXXXXX | The Bluetooth address of the device. |

Monitor_handle (1 octet):

| Value | Parameter description |
|--|--|
| 0xXX | The handle to the filter that was specified for the [HCI_VS_MSFT_LE_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Monitor_Advertisement] command. |

Monitor_state (1 octet):

| Value | Parameter description |
|--|--|
| 0x00 | The controller stopped monitoring the device specified by *BD_ADDR* and *Monitor_handle*. |
| 0x01 | The controller started monitoring the device specified by *BD_ADDR* and *Monitor_handle*. |

## Appendix

This section contains Microsoft-defined Bluetooth HCI extension examples and diagrams.

### Example: Matching patterns for HCI_VS_MSFT_LE_Monitor_Advertisement

This example shows a received [HCI_VS_MSFT_LE_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Monitor_Advertisement] command and the evaluations of three different advertisement packets against the command parameters.

Received [HCI_VS_MSFT_LE_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Monitor_Advertisement] command
An [HCI_VS_MSFT_LE_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Monitor_Advertisement] command is received by the controller and contains the following parameters.

| Parameter | Value | Notes |
|--|--|--|
| *Subcommand_opcode* | 0x03 | Subcommand opcode for [HCI_VS_MSFT_LE_Monitor_Advertisement][ref_HCI_VS_MSFT_LE_Monitor_Advertisement] |
| *RSSI_threshold_high* | 0x01 | 1dB |
| *RSSI_threshold_low* | 0xCE | -50dB |
| *RSSI_threshold_low_time_interval* | 0x05 | 5 seconds |
| *RSSI_sampling_period* | 0xFF | No sampling |
| *Condition_type* | 0x01 | Condition |
| *Condition* | 0x02 | Two patterns should be matched |
|  | 0x03 | Length of first pattern, including AD Type and starting position |
|  | 0x01 | AD Type |
|  | 0x00 | Starting position following the AD Type |
|  | 0x01 | First pattern to be matched |
|  | 0x06 | Length of second pattern, including AD Type and starting position |
|  | 0xFF | AD Type (Manufacturer specific data) |
|  | 0x00 | Starting position following the AD Type |
|  | 0x00 | Second pattern to be matched |
|  | 0x06 |  |
|  | 0xFF |  |
|  | 0xFF |  |

The controller then receives the following advertisement packets.

- Advertisement packet [A]

  `0x02 0x01 0x01 0x07 0x09 0x54 0x61 0x62 0x6C 0x65 0x74 0x05 0xFF 0x00 0x06 0xFF 0xFF`

- Advertisement packet [B]

  `0x02 0x01 0x01 0x07 0x09 0x54 0x61 0x62 0x6C 0x65 0x74 0x04 0xFF 0x00 0x06 0xFF`

- Advertisement packet [C]

  `0x07 0x09 0x54 0x61 0x62 0x6C 0x65 0x74 0x05 0xFF 0x00 0x06 0xFF 0xFF`
  
- Advertisement packet [D]

  `0x02 0x01 0x02 0x05 0xFF 0x00 0x06 0xFF 0x01`

#### Evaluating match for Advertisement packet [A]

| Description | Value |
|--|--|
| AD Type of first pattern to be matched | 0x01 |
| Length of first pattern to be matched | 0x03 - 0x02 = 0x01 byte |
| Pattern to be matched at position 0x00 for AD Type 0x01 | 0x01 |
| Bytes at position 0x00 for the AD Type 0x01 | 0x01 *(MATCH!)* |
| AD Type of second pattern to be matched | 0xFF (Manufacturer specific data) |
| Length of second pattern to be matched | 0x06 - 0x02 = 0x04 bytes |
| Pattern to be matched at position 0x00 for AD Type 0xFF | 0x00 0x06 0xFF 0xFF |
| Bytes at position 0x00 for the AD Type 0xFF | 0x00 0x06 0xFF 0xFF *(MATCH!)* |

Verdict: **PASS** (both patterns match)

#### Evaluating match for Advertisement packet [B]

| Description | Value |
|--|--|
| AD Type of first pattern to be matched | 0x01 |
| Length of first pattern to be matched | 0x03 - 0x02 = 0x01 byte |
| Pattern to be matched at position 0x00 for AD Type 0x01 | 0x01 |
| Bytes at position 0x00 for the AD Type 0x01 | 0x01 *(MATCH!)* |
| AD Type of second pattern to be matched | 0xFF (Manufacturer specific data) |
| Length of second pattern to be matched | 0x06 - 0x02 = 0x04 bytes |
| Pattern to be matched at position 0x00 for AD Type 0xFF | 0x00 0x06 0xFF 0xFF |
| Bytes at position 0x00 for the AD Type 0xFF | 0x00 0x06 0xFF *(no match)* |

Verdict: **PASS** (only first pattern matches)

#### Evaluating match for Advertisement packet [C]

| Description | Value |
|--|--|
| AD Type of first pattern to be matched | 0x01 |
| Length of first pattern to be matched | 0x03 - 0x02 = 0x01 byte |
| Pattern to be matched at position 0x00 for AD Type 0x01 | 0x01 |
| Bytes at position 0x00 for the AD Type 0x01 | Undefined. The advertisement doesn't have data with AD Type 0x01. |
| AD Type of second pattern to be matched | 0xFF (Manufacturer specific data) |
| Length of second pattern to be matched | 0x06 - 0x02 = 0x04 bytes |
| Pattern to be matched at position 0x00 for AD Type 0xFF | 0x00 0x06 0xFF 0xFF |
| Bytes at position 0x00 for the AD Type 0xFF | 0x00 0x06 0xFF 0xFF *(MATCH!)* |

Verdict: **PASS** (only second pattern matches)

#### Evaluating match for Advertisement packet [D]

| Description | Value |
|--|--|
| AD Type of first pattern to be matched | 0x01 |
| Length of first pattern to be matched | 0x03 - 0x02 = 0x01 byte |
| Pattern to be matched at position 0x00 for AD Type 0x01 | 0x01 |
| Bytes at position 0x00 for the AD Type 0x01 | 0x02 *(no match)* |
| AD Type of second pattern to be matched | 0xFF (Manufacturer specific data) |
| Length of second pattern to be matched | 0x06 - 0x02 = 0x04 bytes |
| Pattern to be matched at position 0x00 for AD Type 0xFF | 0x00 0x06 0xFF 0xFF |
| Bytes at position 0x00 for the AD Type 0xFF | 0x00 0x06 0xFF 0x01 *(no match)* |

Verdict: **FAIL** (neither pattern matches)

### Example: Advertisement monitoring

This example illustrates RSSI advertisement monitoring. The RSSI values for received advertisements that matched a specified condition are shown below.

| Time (s) | RSSI (dB) |
|--|--|
| 1 | -100 |
| 2 | -90 |
| 3 | -5 |
| 4 | -15 |
| 5 | -30 |
| 6 | -15 |
| 7 | -45 |
| 8 | -20 |
| 9 | -35 |
| 10 | -45 |
| 11 | -70 |
| 12 | -85 |
| 13 | -85 |
| 14 | -85 |
| 15 | -90 |
| 16 | -90 |
| 17 | -70 |

| Parameter | Value |
|--|--|
| *RSSI_threshold_high* | -10dB |
| *RSSI_threshold_low* | -80dB |
| *RSSI_threshold_low_time_interval* | 3 seconds |
| *RSSI_sampling_period* | 2 seconds |

:::image type="content" source="images/HCI_Example_Advertisement_Monitoring.png" alt-text="Advertisement monitoring graph":::

The advertisement RSSI is greater than *RSSI_threshold_high* at time 3. The periodic timer for sampling starts at time 3. Every 2 seconds, the periodic timer expires and the average RSSI value of the received advertisement is propagated to the stack.

When the periodic timer expires at time 5, the average of the advertisement RSSIs received during this time (-23dB) is propagated to the stack.

When the periodic timer expires at time 13, the average of the advertisement RSSIs received during this timeframe is below *RSSI_threshold_low* (-80dB). The average of the advertisement RSSI (-85 dB) should be propagated to the host.

When *RSSI_threshold_low_time_interval* expires at instant 15, an advertisement is propagated to the host with RSSI of -85dB. No further advertisements are sent to the host in this example.

### Example: Monitoring BAP Announcements from a device

While bonded with a CAP Acceptor, but not connected, a Host could monitor BAP Announcements from that device.

| Parameter | Value |
|--|--|
| Subcommand_opcode_v2 | 0x0F |
| RSSI_threshold_high | -127 |
| RSSI_threshold_low | -127 |
| RSSI_threshold_low_time_interval | 0x05 |
| RSSI_sampling_period | 0x00 |
| Monitor_options | Bit 0 set; Bit 1 set if the device distributed an IRK |
| Advertisement_report_filtering_options | Bit 0, 1, and 2 set |
| Peer_device_address | \<address\> |
| Peer_device_address_type | \<address type\> |
| Peer_device_IRK | \<IRK, if bit 1 is set\> |
| Condition_type | 0x01 |
| Number_of_patterns | 0x01 |
| Pattern_data | 0x04 (length)<br>0x16 (Service Data – 16 bit UUID)<br>0x00 (Start byte)<br>0x4E (low byte of ASCS UUID)<br>0x18 (high byte of ASCS UUID) |

### Example: Monitoring CAP Announcements from a device

While bonded with a CAP Commander, but not connected, a Host could monitor CAP Announcements from that device.

| Parameter | Value |
|--|--|
| Subcommand_opcode_v2 | 0x0F |
| RSSI_threshold_high | -127 |
| RSSI_threshold_low | -127 |
| RSSI_threshold_low_time_interval | 0x05 |
| RSSI_sampling_period | 0x00 |
| Monitor_options | Bit 0 set; Bit 1 set if the device distributed an IRK |
| Advertisement_report_filtering_options | Bit 0, 1, and 2 set |
| Peer_device_address | \<address\> |
| Peer_device_address_type | \<address type\> |
| Peer_device_IRK | \<IRK, if bit 1 is set\> |
| Condition_type | 0x01 |
| Number_of_patterns | 0x01 |
| Pattern_data | 0x04 (length)<br>0x16 (Service Data – 16 bit UUID)<br>0x00 (Start byte)<br>0x53 (low byte of CAS UUID)<br>0x18 (high byte of CAS UUID) |

### Flowchart: Advertisement and filter accept list filtering

This flowchart provides an example controller implementation of advertisement filtering and filter accept list filtering when an advertisement is received.

A controller can implement this logic differently, as long as the host is notified of the advertisement or [HCI_VS_MSFT_LE_Monitor_Device_Event][ref_HCI_VS_MSFT_LE_Monitor_Device_Event] as specified by the flowchart.

:::image type="content" source="images/HCI_Filtering_Flowchart.png" alt-text="Microsoft HCI extension filtering flowchart":::

### Sequence diagram: Propagate scan response associated with advertisement

Sequence diagram: Propagate scan response associated with advertisement

This sequence diagram shows a propagate scan response that is associated with an advertisement that satisfies an advertisement filter when active scanning is enabled.
This diagram only shows the expected sequence of events between controller and host, and doesn't show events between the controller and a particular device.
Assume that there's an advertisement *A* that satisfies an advertisement filter, and an advertisement *B* that doesn't satisfy the advertisement filter.

:::image type="content" source="images/HCI_Propagate_Scan_Sequence.png" alt-text="HCI propagate scan sequence diagram":::
