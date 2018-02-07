---
title: Microsoft-defined Bluetooth HCI commands and events
description: The Bluetooth Host-Controller Interface (HCI) specifies all interactions between a host and a Bluetooth radio controller. Bluetooth specifications allow vendor-defined HCI commands and events to enable non-standardized interaction between hosts and controllers. Microsoft defines vendor-specific HCI commands and events that are consumed by Windows. Bluetooth controller implementers can use these extensions to implement special features.
ms.assetid: 68E34B92-155B-401E-8D90-5BD1AF036B4D
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Microsoft-defined Bluetooth HCI extensions
The Bluetooth Host-Controller Interface (HCI) specifies all interactions between a host and a Bluetooth radio controller. Bluetooth specifications allow vendor-defined HCI commands and events to enable non-standardized interaction between hosts and controllers. Microsoft defines vendor-specific HCI commands and events that are consumed by Windows. Bluetooth controller implementers can use these extensions to implement special features.

## Microsoft-defined HCI commands 

Bluetooth HCI commands are identified by a 16-bit command code. The Bluetooth organization defines values in the range 0x0000 through 0xFBFF. Vendors define values in the range 0xFC00 through 0xFFFF, allowing for 1024 different possible vendor-assigned command codes.

The vendor must choose the value of the Microsoft-defined command code. Microsoft can't choose a command code and assume that no other vendor uses the code for a conflicting purpose. It is unsafe to issue a vendor-specific command and depend on the controller to reject the command if it does not understand it. The controller could interpret the command as a destructive operation such as updating the controller’s firmware.

The vendor must communicate the chosen value through a method other than the controller. Microsoft does not specify how to get the chosen code.

### Notifying Windows Bluetooth stack of the vendor specific command code
The Windows Bluetooth stack reads the vendor-specific command code from a registry key.

The VsMsftOpCode registry key has a type of REG_DWORD and the key data is the vendor specific opcode.

The registry path to the VsMsftOpCode key is:

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\<Device instance path>\Device Parameters\VsMsftOpCode

This example command adds the registry value from the command line.

```
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\<Device instance path>\Device Parameters" /v VsMsftOpCode /t REG_DWORD /d <Vendor specific command code>

```

### Using INF to set the VsMsftOpCode registry key
The vendor-specific command code can also be added via INF Files. This sample shows how and where to add the vendor specific command code so that it is automatically added to the registry.

``` 
[radio.NTamd64.HW]
AddReg=radio.NTamd64.HW.AddReg
[radio.NTamd64.HW.AddReg]
HKR,,"VsMsftOpCode",0x00010001,<Vendor Specific Opcode>
```
### Microsoft-defined HCI command and subcommands

The controller understands there is only one Microsoft-specific HCI command. The Microsoft-specific command set is extended through the use of an opcode. The first command parameter for the Microsoft-defined HCI command is an opcode that specifies the subcommand.

Controllers must support HCI_VS_MSFT_Read_Supported_Features in order to support any other Microsoft HCI subcommands. Support for other commands is optional and depends on the values returned by HCI_VS_MSFT_Read_Supported_Features. Windows does not send any Microsoft-defined subcommands unless the controller indicates support for the subcommand through a response to HCI_VS_MSFT_Read_Supported_Features.

### HCI_VS_MSFT_Read_Supported_Features

HCI_VS_MSFT_Read_Supported_Features provides a bitmap that describes which Microsoft-defined features the controller supports, and specifies the prefix for Microsoft-defined events that are returned by the controller.

The controller shall always complete this command promptly with a Command Completed event.


<table>
<tr>
<th>Command</th>
<th>Code</th>
<th>Command parameters</th>
<th>Return parameters</th>
</tr>
<tr>
<td>
<p>HCI_VS_MSFT_Read_Supported_Features</p>
</td>
<td>
<p>Chosen base  code </p>
</td>
<td>
<p><i>Subcommand_opcode</i></p>
</td>
<td>
<p><i>Status</i></p>
<p><i>Subcommand_opcode</i></p>
<p><i>Supported_features</i></p>
<p><i>Microsoft_event_prefix_length</i></p>
<p><i>Microsoft_event_prefix</i></p>
</td>
</tr>
</table>
<p> </p>
<h2><a id="Command_parameters"></a><a id="command_parameters"></a><a id="COMMAND_PARAMETERS"></a>Command parameters</h2>
<dl>
<dd>
<p><b><i>Subcommand_opcode</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>The subcommand opcode for HCI_VS_MSFT_Read_Supported_Features.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
<h2><a id="Return_parameters"></a><a id="return_parameters"></a><a id="RETURN_PARAMETERS"></a>Return parameters</h2>
<dl>
<dd>
<p><b><i>Status</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>The command succeeded.</p>
</td>
</tr>
<tr>
<td>
<p>0x01&#160;-&#160;0xFF</p>
</td>
<td>
<p>The command failed. See <i>Error Codes</i> in the Bluetooth Core specification for details.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Subcommand_opcode</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>The subcommand opcode for HCI_VS_MSFT_Read_Supported_Features.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Supported_features</i></b> (8 octets):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00000000&#160;00000001</p>
</td>
<td>
<p>Controller supports the RSSI Monitoring feature for BR/EDR connections. In addition, the controller supports <a href="hci_vs_msft_read_absolute_rssi.htm"><b>HCI_VS_MSFT_Read_Absolute_RSSI</b></a> to read the absolute RSSI metric of a BR/EDR connection.</p>
</td>
</tr>
<tr>
<td>
<p>0x00000000&#160;00000002</p>
</td>
<td>
<p>Controller supports the RSSI Monitoring feature for LE connections.</p>
</td>
</tr>
<tr>
<td>
<p>0x00000000&#160;00000004</p>
</td>
<td>
<p>Controller supports the RSSI Monitoring of LE advertisements.</p>
</td>
</tr>
<tr>
<td>
<p>0x00000000&#160;00000008</p>
</td>
<td>
<p>Controller supports Advertising Monitoring of LE advertisements.</p>
</td>
</tr>
<tr>
<td>
<p>0xFFFFFFFF&#160;FFFFFFF0</p>
</td>
<td>
<p>Bits reserved for future definition. Must be zero.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Microsoft_event_prefix_length</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00&#160;-&#160;0x20</p>
</td>
<td>
<p>Number of bytes in the Microsoft event prefix field as specified in the returned <i>Microsoft_event_prefix</i>. This is the number of bytes of constant information at the beginning of every Microsoft-specified HCI event.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Microsoft_event_prefix</i></b> (variable length):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p><i>Event&#160;prefix&#160;value</i></p>
</td>
<td>
<p>The constant information to expect at the beginning of each Microsoft-defined event. This information is used to distinguish Microsoft-defined events from other custom events.</p>
</td>
</tr>
</table>

 ### HCI_VS_MSFT_Monitor_Rssi

<p>HCI_VS_MSFT_Monitor_Rssi requests that the controller starts monitoring the measured link RSSI for a specified connection, and generates an event when the connection's measured link RSSI goes outside of the specified bounds.</p>
<table>
<tr>
<th>Command</th>
<th>Code</th>
<th>Command parameters</th>
<th>Return parameters</th>
</tr>
<tr>
<td>
<p>HCI_VS_MSFT_Monitor_Rssi</p>
</td>
<td>
<p>Chosen base  code </p>
</td>
<td>
<p><i>Subcommand_opcode</i></p>
<p><i>Connection_handle</i></p>
<p><i>RSSI_threshold_high</i></p>
<p><i>RSSI_threshold_low</i></p>
<p><i>RSSI_threshold_low_time_interval</i></p>
<p><i>RSSI_sampling_period</i></p>
</td>
<td>
<p><i>Status</i></p>
<p><i>Subcommand_opcode</i></p>
</td>
</tr>
</table>
<p> </p>
<p>The controller shall notify the host of the RSSI value with a periodically generated event (based on the <i>RSSI_sampling_period</i>). The measured link RSSI shall be the <b>absolute</b> receiver signal strength value in dBm for the BR/EDR connection.</p>
<p>In response to a HCI_VS_MSFT_Monitor_Rssi command, the controller shall generate a Command Complete event with status equaling zero if the controller can begin monitoring, or a non-zero status otherwise. If the status value is non-zero, the controller shall not generate an <a href="hci_vs_msft_rssi_event.htm"><b>HCI_VS_MSFT_Rssi_Event</b></a> in response to this command.</p>
<p>The controller shall refuse the command if another HCI_VS_MSFT_Monitor_Rssi command with the same <i>Connection_handle</i> is outstanding, or if the specified connection handle is invalid. The controller may also refuse the command for other reasons, such as resource exhaustion.</p>
<h2><a id="State_diagram"></a><a id="state_diagram"></a><a id="STATE_DIAGRAM"></a>State diagram</h2>
<p>This state diagram shows the transition states on the controller when monitoring RSSI for a connection.</p><img src="images/HCI_VS_MSFT_Monitor_Rssi_State_Diagram.png" alt="State diagram of HCI_VS_MSFT_Monitor_Rssi"/><p>The controller shall generate an HCI_VS_MSFT_Rssi_Event when the received RSSI is greater than or equal to the specified <i>RSSI_threshold_high</i>. After this event has been generated, the controller shall not generate a new HCI_VS_MSFT_Rssi_Event to specify that the <i>RSSI_threshold_high</i> has been exceeded until it generates an HCI_VS_MSFT_Rssi_Event that specifies the RSSI has fallen below <i>RSSI_threshold_low</i>.</p>
<p>The controller shall generate an HCI_VS_MSFT_Rssi_Event when the received RSSI equals or falls below the specified <i>RSSI_threshold_low</i> over the specified <i>RSSI_threshold_low_time_interval</i>. After this event has been generated, the controller shall not generate a new HCI_VS_MSFT_Rssi_Event to specify that the RSSI has fallen below the <i>RSSI_threshold_low</i> until an HCI_VS_MSFT_Rssi_Event event is generated to specify that <i>RSSI_threshold_high</i> has been reached or exceeded.</p>
<p>If the <i>RSSI_sampling_period</i> is between 0x01 and 0xFE, the controller shall generate an HCI_VS_MSFT_Rssi_Event periodically every <i>RSSI_sampling_period</i>. This event shall contain the average of the RSSI calculated over the <i>RSSI_sampling_period</i>.</p>
<p>If the <i>RSSI_sampling_period</i> is 0x00 or 0xFF, the controller shall <b>not</b> notify the host periodically with HCI_VS_MSFT_Rssi_Event.</p>
<h2><a id="Command_parameters"></a><a id="command_parameters"></a><a id="COMMAND_PARAMETERS"></a>Command parameters</h2>
<dl>
<dd>
<p><b><i>Subcommand_opcode</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x01</p>
</td>
<td>
<p>The subcommand opcode for HCI_VS_MSFT_Monitor_Rssi.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Connection_handle</i></b> (2 octets):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x<i>XXXX</i></p>
</td>
<td>
<p>The handle for the connection whose RSSI must be monitored.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>RSSI_threshold_high</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p><i>N</i> = <i>High&#160;RSSI threshold&#160;value</i></p>
</td>
<td>
<p>The maximum expected RSSI value. The controller will generate an event if the observed RSSI becomes greater than or equal to this value.</p>
<p>For BR/EDR:</p>
<ul>
<li>Range: -128 &lt;= <i>N</i> &lt;= 127 (signed integer)</li>
<li>Unit: dBm</li>
</ul>
<p>For LE:</p>
<ul>
<li>Range: -127 to 20 (signed integer)</li>
<li>Unit: dBm</li>
</ul>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>RSSI_threshold_low</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p><i>N</i> = <i>Low&#160;RSSI threshold&#160;value</i></p>
</td>
<td>
<p>The minimum expected RSSI value. The controller will generate an event if the observed RSSI becomes less than or equal to this value.</p>
<p>For BR/EDR:</p>
<ul>
<li>Range: -128 &lt;= <i>N</i> &lt;= 127 (signed integer)</li>
<li>Unit: dBm</li>
</ul>
<p>For LE:</p>
<ul>
<li>Range: -127 to 20 (signed integer)</li>
<li>Unit: dBm</li>
</ul>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>RSSI_threshold_low_time_interval</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>Reserved value.</p>
</td>
</tr>
<tr>
<td>
<p><i>N</i>&#160;=&#160;0x01&#160;-&#160;0x3C</p>
</td>
<td>
<p>Time period = <i>N</i> * 1 second</p>
<p>The time in seconds over which the RSSI value should be below <i>RSSI_threshold_low</i> before an <a href="hci_vs_msft_rssi_event.htm"><b>HCI_VS_MSFT_Rssi_Event</b></a> is generated.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>RSSI_sampling_period</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>Reserved value.</p>
</td>
</tr>
<tr>
<td>
<p><i>N</i>&#160;=&#160;0x01&#160;-&#160;0xFE</p>
</td>
<td>
<p>Time period = <i>N</i> * 100 milliseconds</p>
<p>The sampling interval in milliseconds.</p>
</td>
</tr>
<tr>
<td>
<p>0xFF</p>
</td>
<td>
<p>Reserved value.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
<h2><a id="Return_parameters"></a><a id="return_parameters"></a><a id="RETURN_PARAMETERS"></a>Return parameters</h2>
<dl>
<dd>
<p><b><i>Status</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>The command succeeded.</p>
</td>
</tr>
<tr>
<td>
<p>0x07</p>
</td>
<td>
<p>The controller shall return <i>Memory Capacity Exceeded</i> if it does not have enough memory to process the command.</p>
</td>
</tr>
<tr>
<td>
<p><i>Error&#160;code</i></p>
</td>
<td>
<p>The command failed. See <i>Error Codes</i> in the Bluetooth Core specification for details.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Subcommand_opcode</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>0x01</td>
<td>The subcommand opcode for HCI_VS_MSFT_Monitor_Rssi.</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
<h2><a id="Events_generated__unless_masked_away_"></a><a id="events_generated__unless_masked_away_"></a><a id="EVENTS_GENERATED__UNLESS_MASKED_AWAY_"></a>Events generated (unless masked away)</h2>
<p>The controller shall promptly generate a Command Complete event when the HCI_VS_MSFT_Monitor_Rssi command is received. If the Command Complete event returns a status of  0, the controller shall generate an <a href="hci_vs_msft_rssi_event.htm"><b>HCI_VS_MSFT_Rssi_Event</b></a> when one of the following occurs.</p>
<ul>
<li>The observed RSSI for the device over <i>RSSI_threshold_low_time_interval</i> becomes equal to or less than the specified <i>RSSI_threshold_low</i> value.</li>
<li>The observed RSSI for the device becomes greater than or equal to the specified <i>RSSI_threshold_high</i> value. </li>
<li>The <i>RSSI_sampling_period</i> is valid and the sampling period expires.</li>
</ul>
<p>The controller should do all necessary cleanup if connectivity with the specified device is lost. In this case, an <a href="hci_vs_msft_cancel_monitor_rssi.htm"><b>HCI_VS_MSFT_Cancel_Monitor_Rssi</b></a> command is not sent to the controller.</p>
<h2>Requirements</h2>
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows 10 for desktop editions (Home, Pro, Enterprise, and Education),  Windows 10 Mobile, and later versions.</p>
</td>
</tr>
</table>
<h2><a id="see_also"></a>See also</h2>
<dl>
<dt><a href="hci_vs_msft_rssi_event.htm"><b>HCI_VS_MSFT_Rssi_Event</b></a></dt>
<dt><a href="hci_vs_msft_cancel_monitor_rssi.htm"><b>HCI_VS_MSFT_Cancel_Monitor_Rssi</b></a></dt>
</dl>

### HCI_VS_MSFT_Cancel_Monitor_Rssi

</div>
<p>HCI_VS_MSFT_Cancel_Monitor_Rssi cancels a previously-issued <a href="hci_vs_msft_monitor_rssi.htm"><b>HCI_VS_MSFT_Monitor_Rssi</b></a> command.</p>
<p>The controller shall promptly generate a Command Completed event in response to this command.</p>
<table>
<tr>
<th>Command</th>
<th>Code</th>
<th>Command parameters</th>
<th>Return parameters</th>
</tr>
<tr>
<td>
<p>HCI_VS_MSFT_Cancel_Monitor_Rssi</p>
</td>
<td>
<p>Chosen base  code </p>
</td>
<td>
<p><i>Subcommand_opcode</i></p>
<p><i>Connection_handle</i></p>
</td>
<td>
<p><i>Status</i></p>
<p><i>Subcommand_opcode</i></p>
</td>
</tr>
</table>
<p> </p>
<h2><a id="Command_parameters"></a><a id="command_parameters"></a><a id="COMMAND_PARAMETERS"></a>Command parameters</h2>
<dl>
<dd>
<p><b><i>Subcommand_opcode</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x02</p>
</td>
<td>
<p>The subcommand opcode for HCI_VS_MSFT_Cancel_Monitor_Rssi.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Connection_handle</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x<i>XXXX</i></p>
</td>
<td>
<p>The handle for the connection whose RSSI monitoring should be cancelled.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
<h2><a id="Return_parameters"></a><a id="return_parameters"></a><a id="RETURN_PARAMETERS"></a>Return parameters</h2>
<dl>
<dd>
<p><b><i>Status</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>The command succeeded.</p>
</td>
</tr>
<tr>
<td>
<p>0x01&#160;-&#160;0xFF</p>
</td>
<td>
<p>The command failed. See <i>Error Codes</i> in the Bluetooth Core specification for details.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Subcommand_opcode</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x02</p>
</td>
<td>
<p>The subcommand opcode for HCI_VS_MSFT_Cancel_Monitor_Rssi.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
<h2><a id="Events_generated__unless_masked_away_"></a><a id="events_generated__unless_masked_away_"></a><a id="EVENTS_GENERATED__UNLESS_MASKED_AWAY_"></a>Events generated (unless masked away)</h2>
<p>The controller shall generate a Command Complete event when the HCI_VS_MSFT_Cancel_Monitor_RSSI command is received.</p>
<h2>Requirements</h2>
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows 10 for desktop editions (Home, Pro, Enterprise, and Education),  Windows 10 Mobile, and later versions.</p>
</td>
</tr>
</table>
<h2><a id="see_also"></a>See also</h2>
<dl>
<dt><a href="hci_vs_msft_monitor_rssi.htm"><b>HCI_VS_MSFT_Monitor_Rssi</b></a></dt>
</dl>
<p> </p>
<p> </p>

 ### HCI_VS_MSFT_LE_Monitor_Advertisement

<p>HCI_VS_MSFT_LE_Monitor_Advertisement requests that the controller starts monitoring for advertisements that fall within the specified RSSI range and also satisfy one of the following conditions:</p>
<ul>
<li>A specified pattern can be matched to the received advertisement packet.</li>
<li>A specified UUID can be matched to the received advertisement packet.</li>
<li>A specified Identity Resolution Key (IRK) can be used to resolve the private address of the device from which the advertisement packet originated.</li>
<li>A specified Bluetooth Address can be matched to the received advertisement packet.</li>
</ul>
<table>
<tr>
<th>Command</th>
<th>Code</th>
<th>Command parameters</th>
<th>Return parameters</th>
</tr>
<tr>
<td>
<p>HCI_VS_MSFT_LE_Monitor_Advertisement</p>
</td>
<td>
<p>Chosen base code</p>
</td>
<td>
<p><i>Subcommand_opcode</i></p>
<p><i>RSSI_threshold_high</i></p>
<p><i>RSSI_threshold_low</i></p>
<p><i>RSSI_threshold_low_time_interval</i></p>
<p><i>RSSI_sampling_period</i></p>
<p><i>Condition_type</i></p>
<p><i>Condition</i></p>
</td>
<td>
<p><i>Status</i></p>
<p><i>Subcommand_opcode</i></p>
<p><i>Monitor_handle</i></p>
</td>
</tr>
</table>
<p> </p>
<p>The controller shall generate a Command Complete event in response to this command. The status value should be set to zero if the controller can begin monitoring, or a non-zero status otherwise.</p>
<p>If the controller does not support RSSI monitoring for LE Advertisements, it shall ignore the <i>RSSI_threshold_high</i>, <i>RSSI_threshold_low</i>, <i>RSSI_threshold_low_time_interval</i>, and <i>RSSI_sampling_period</i> parameter values.</p>
<h2><a id="State_diagram"></a><a id="state_diagram"></a><a id="STATE_DIAGRAM"></a>State diagram</h2>
<p>This state diagram shows the transition states on the controller when monitoring RSSI for an advertisement.</p><img src="images/HCI_VS_MSFT_LE_Monitor_Advertisement_State_Diagram.png" alt="State diagram for HCI_VS_MSFT_LE_Monitor_Advertisement"/><p>The controller shall propagate the first advertisement packet to the host only when the received RSSI is greater than or equal to <i>RSSI_threshold_high</i> for a particular device. The controller shall generate an <a href="hci_vs_msft_le_monitor_device_event.htm"><b>HCI_VS_MSFT_LE_Monitor_Device_Event</b></a> with <i>Monitor_state</i> set to 1 and <i>Monitor_handle</i> set to the handle for this <i>Condition</i>, to notify the host that the controller is monitoring this particular device for <i>Condition</i>.</p>
<p>The controller shall stop monitoring for <i>Condition</i> if the RSSI of the received advertisements equals or falls below  <i>RSSI_threshold_low</i> over <i>RSSI_threshold_low_interval</i> for the particular device. The controller shall generate an <a href="hci_vs_msft_le_monitor_device_event.htm"><b>HCI_VS_MSFT_LE_Monitor_Device_Event</b></a> with <i>Monitor_state</i> set to 0 to notify the host that the controller has stopped monitoring the particular device for the <i>Condition</i>. After the controller specifies the HCI_VS_MSFT_LE_Monitor_Device_Event with <i>Monitor_state</i> set to 0, the controller shall not allow further advertisement packets to flow to the host for the device until the controller has notified the host that the RSSI for the particular device has risen to or above <i>RSSI_threshold_high</i> for the particular device for the <i>Condition</i>.</p>
<p>Additionally, the controller shall generate an <a href="hci_vs_msft_le_monitor_device_event.htm"><b>HCI_VS_MSFT_LE_Monitor_Device_Event</b></a> with <i>Monitor_state</i> set to 0 to notify the host that the controller has stopped monitoring the device for the <i>Condition</i> if the specified <i>RSSI_threshold_low_time_interval</i> expires without receiving any advertising packets from the device. If the controller is monitoring a device for a particular condition, the following statements are true.</p>
<ul>
<li>If <i>RSSI_sampling_period</i> is set to 0xFF, the controller shall not allow further advertisement packets to flow to the host for the device for the <i>Condition</i> until the controller has notified the host that the particular device’s RSSI has fallen below <i>RSSI_threshold_low</i> for <i>RSSI_threshold_low_time_interval</i> for the particular device for this <i>Condition</i>. This notification is done by generating an <a href="hci_vs_msft_le_monitor_device_event.htm"><b>HCI_VS_MSFT_LE_Monitor_Device_Event</b></a> with <i>Monitor_state</i> set to 0.</li>
<li>If the <i>RSSI_sampling_period</i> is set to 0x0, the controller shall propagate all received advertisement packets to the host for the device for this <i>Condition</i> unless the controller previously received an <a href="hci_vs_msft_le_set_advertisement_filter_enable.htm"><b>HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable</b></a> command with <i>Enable</i> set to 0x00. The controller shall propagate an advertisement packet to the host even if the received RSSI is less than or equal to <i>RSSI_threshold_low</i> as long as <i>RSSI_threshold_low_time_interval</i> has not expired for the particular device for this <i>Condition</i>. The RSSI value of this advertisement packet shall be the RSSI value of the received advertisement.</li>
</ul>
<p>If <i>RSSI_sampling_period</i> is between 0x01 and 0xFE, the controller shall propagate advertisement packets to the host every <i>RSSI_sampling_period</i> specified unless the controller previously received an <a href="hci_vs_msft_le_set_advertisement_filter_enable.htm"><b>HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable</b></a> command with <i>Enable</i> set to 0x00. The RSSI value specified for the advertisement shall be the average of the RSSI value received during this sampling interval. If the controller does not receive an advertisement packet during the sampling period, it shall not propagate an advertisement to the host. It is possible that <i>RSSI_sampling_period</i> is less than <i>RSSI_threshold_low_time_interval</i> and all advertisements received during the <i>RSSI_sampling_period</i> have RSSI below <i>RSSI_threshold_low</i>. The controller shall still propagate the advertisement with the average of the RSSI value received during this sampling interval.</p>
<p>If the controller previously received an <a href="hci_vs_msft_le_set_advertisement_filter_enable.htm"><b>HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable</b></a> command with <i>Enable</i> set to 0x00, the sampling period timer shall not be stopped. See Example: HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable on filters with sampling period for more information.</p>
<p>If the controller receives non-duplicate advertisement packets from the same device, it shall match each advertisement packet against the Conditions stored on the controller.</p>
<p>If the controller receives an advertisement packet from a device that matches multiple Conditions, then the controller shall generate an <a href="hci_vs_msft_le_monitor_device_event.htm"><b>HCI_VS_MSFT_LE_Monitor_Device_Event</b></a> for each <i>Condition</i> that matched, with <i>Monitor_handle</i> set to the <i>Condition</i> that matched.</p>
<p>If the controller is unable to monitor the RSSI values for all devices in range that match the <i>Condition</i>, it will keep monitoring as many devices as it can. The decision on what devices should be monitored will depend on the RSSI values of the received advertisements. The controller shall monitor devices with the greater received signal strength.</p>
<p>If the controller has notified the host about a particular device (<i>A</i>) and it is monitoring devices at maximum hardware capacity, and if another device (<i>B</i>) comes into range with a higher RSSI value, then the controller shall notify the host that it has stopped monitoring the device (<i>A</i>) by generating an <a href="hci_vs_msft_le_monitor_device_event.htm"><b>HCI_VS_MSFT_LE_Monitor_Device_Event</b></a> with <i>Monitor_state</i> set to 0. The controller shall also generate an HCI_VS_MSFT_LE_Monitor_Device_Event with <i>Monitor_state</i> set to 1 to notify the host that the device (<i>B</i>) is now being monitored.</p>
<h2><a id="Condition_type_and_Condition_parameters"></a><a id="condition_type_and_condition_parameters"></a><a id="CONDITION_TYPE_AND_CONDITION_PARAMETERS"></a><i>Condition_type</i> and <i>Condition</i> parameters</h2>
<p>The <i>Condition_type</i> parameter specifies whether the <i>Condition</i> parameter specifies a pattern, UUID, IRK, or BD_ADDR.</p>
<p>If the <i>Condition_type</i> parameter specifies a pattern, the <i>Condition</i> contains 2 sections which contain the number of patterns present within the <i>Condition</i>, and the pattern data.</p><img src="images/HCI_VS_MSFT_LE_Monitor_Advertisement_Conditions.png" alt="Pattern condition data layout"/><dl>
<dd><i>Number of Patterns</i> specifies the number of patterns that need to be matched.</dd>
<dd><i>Pattern Data</i> has the following format.<ul>
<li><i>Length</i> specifies the length of this pattern include the data type and start byte of the pattern.</li>
<li><i>AD Type</i> specifies the AD Type field</li>
<li><i>Start of Pattern</i> specifies the starting byte position of the pattern immediately following AD Type.</li>
<li><i>Pattern</i> has a size of (<i>Length</i> - 0x2) and is the pattern to be matched for the specified AD Type within the advertisement packet from the specified starting byte.</li>
</ul>
</dd>
</dl>
<p>If there are multiple patterns specified, the controller shall ensure that at least one pattern matches the received advertisement.</p>
<p>If the <i>Condition_type</i> parameter specifies a UUID, the <i>Condition</i> parameter contains a UUID Type and a UUID. The UUID Type specifies whether the UUID is 16-bit, 32-bit, or 128-bit. The controller shall parse the Service UUID of the advertisement packet to check for the specified UUID. If UUID Type is defined as 0x01, the controller shall parse the Incomplete List of 16-bit service UUIDs and complete list of 16-bit service UUIDs specified in the Service UUID AD Type. If the UUID Type is defined as 0x02, the controller shall parse the Incomplete List of 32-bit service UUIDs and complete list of 32-bit UUIDs specified in the Service UUID AD Type. If the UUID Type specified is 0x03, the controller shall parse the Incomplete List of 128-bit Service UUIDs and complete list of 128-bit Service UUIDs specified in the Service UUID AD Type.</p>
<p>If the <i>Condition_type</i> parameter specifies an IRK, the <i>Condition</i> parameter contains the IRK.</p>
<p>If the <i>Condition_type</i> parameter specifies a Bluetooth Address, the <i>Condition</i> parameter contains the address type and BD_ADDR.</p>
<p>The controller shall keep monitoring based on the conditions, even when scanning (Active or Passive) is enabled.</p>
<p>When active scanning is enabled, the scan response for an advertisement matching a filter shall be propagated to the host.</p>
<p>If the controller receives a HCI_VS_MSFT_LE_Monitor_Advertisement command when the filters are disabled (due to  a previously received <a href="hci_vs_msft_le_set_advertisement_filter_enable.htm"><b>HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable</b></a> command with <i>Enable</i> set to 0x00), the controller shall accept the command if it can, but set it to a disabled state.</p>
<p>The controller may also refuse the command for other reasons such as resource exhaustion.</p>
<h2><a id="Command_parameters"></a><a id="command_parameters"></a><a id="COMMAND_PARAMETERS"></a>Command parameters</h2>
<dl>
<dd>
<p><b><i>Subcommand_opcode</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x03</p>
</td>
<td>
<p>The subcommand opcode for HCI_VS_MSFT_LE_Monitor_Advertisement.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>RSSI_threshold_high</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p><i>High&#160;RSSI threshold&#160;value</i></p>
</td>
<td>
<p>The maximum expected RSSI value. The controller will generate an event if the observed RSSI becomes greater than or equal to this value.</p>
<ul>
<li>Range: -127 to 20 (signed integer)</li>
<li>Unit: dBm</li>
</ul>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>RSSI_threshold_low</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p><i>Low&#160;RSSI threshold&#160;value</i></p>
</td>
<td>
<p>The minimum expected RSSI value. The controller will generate an event if the observed RSSI becomes less than or equal to this value.</p>
<ul>
<li>Range: -127 to 20 (signed integer)</li>
<li>Unit: dBm</li>
</ul>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>RSSI_threshold_low_time_interval</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>Reserved value.</p>
</td>
</tr>
<tr>
<td>
<p><i>N</i>&#160;=&#160;0x01&#160;-&#160;0x3C</p>
</td>
<td>
<p>Time period = <i>N</i> * 1 second</p>
<p>The time in seconds over which the RSSI value should be below <i>RSSI_threshold_low</i> before an <a href="hci_vs_msft_rssi_event.htm"><b>HCI_VS_MSFT_Rssi_Event</b></a> is generated.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>RSSI_sampling_period</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>The controller should propagate all received advertisements matching the specified condition to the host.</p>
</td>
</tr>
<tr>
<td>
<p><i>N</i>&#160;=&#160;0x01&#160;-&#160;0xFE</p>
</td>
<td>
<p>Time period = <i>N</i> * 100 milliseconds</p>
<p>The sampling interval in milliseconds.</p>
</td>
</tr>
<tr>
<td>
<p>0xFF</p>
</td>
<td>
<p>The controller should not propagate any of the received advertisements to the host.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Condition_type</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x01</p>
</td>
<td>
<p>The condition is a pattern that has to be matched on the advertisement.</p>
</td>
</tr>
<tr>
<td>
<p>0x02</p>
</td>
<td>
<p>The condition is a UUID Type and a UUID.</p>
</td>
</tr>
<tr>
<td>
<p>0x03</p>
</td>
<td>
<p>The condition is the resolution of an IRK.</p>
</td>
</tr>
<tr>
<td>
<p>0x04</p>
</td>
<td>
<p>The condition is a Bluetooth address.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Condition</i></b>:</p>
<p>The applicable fields for <i>Condition</i> depends on the value of <i>Condition_type</i>. See the <i>Condition_type and Condition parameters</i> section for more information.</p>
<dl>
<dd>
<p><b><i>Number_of_patterns</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x<i>XX</i></p>
</td>
<td>
<p>The number of patterns specified within the <i>Pattern_data</i> parameter.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Pattern_data</i></b> (&gt;3 octets):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p><i>Length</i></p>
</td>
<td>
<p>Length of this pattern.</p>
</td>
</tr>
<tr>
<td>
<p><i>Data type</i></p>
</td>
<td>
<p>Data Type of the advertisement section. The values are listed in the Bluetooth Assigned Numbers document.</p>
</td>
</tr>
<tr>
<td>
<p><i>Start byte</i></p>
</td>
<td>
<p>Starting position of the pattern to be matched for the specified Data Type.</p>
</td>
</tr>
<tr>
<td>
<p><i>Pattern</i></p>
</td>
<td>
<p>Pattern to be matched (size of <i>Length</i> – 0x2 bytes).</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>UUID_type</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x01</p>
</td>
<td>
<p>The UUID is a 16-bit service.</p>
</td>
</tr>
<tr>
<td>
<p>0x02</p>
</td>
<td>
<p>The UUID is a 32-bit service.</p>
</td>
</tr>
<tr>
<td>
<p>0x03</p>
</td>
<td>
<p>The UUID is a 128-bit service.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>UUID</i></b> (2, 4, or 16 octets):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x<i>XXXX</i></p>
</td>
<td>
<p>2 bytes if <i>UUID_type</i> is 0x01.</p>
<p>4 bytes if <i>UUID_type</i> is 0x02.</p>
<p>16 bytes if <i>UUID_type</i> is 0x03.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>IRK</i></b> (16 octets):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x<i>XXXXXXXX XXXXXXXX</i></p>
<p><i>XXXXXXXX XXXXXXXX</i></p>
</td>
<td>
<p>The IRK to be used to resolve the private address.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Address_type</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>Public Device Address.</p>
</td>
</tr>
<tr>
<td>
<p>0x01</p>
</td>
<td>
<p>Random Device Address.</p>
</td>
</tr>
<tr>
<td>
<p>0x02&#160;-&#160;0xFF</p>
</td>
<td>
<p>Reserved values for future use.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>BD_ADDR</i></b> (6 octets):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x<i>XXXXXXXXXXXX</i></p>
</td>
<td>
<p>The Bluetooth address of the device to be monitored.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
</dd>
</dl>
<h2><a id="Return_parameters"></a><a id="return_parameters"></a><a id="RETURN_PARAMETERS"></a>Return parameters</h2>
<dl>
<dd>
<p><b><i>Status</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>The command succeeded.</p>
</td>
</tr>
<tr>
<td>
<p>0x07</p>
</td>
<td>
<p>The controller shall return <i>Memory Capacity Exceeded</i> if it does not have enough memory to process the command.</p>
</td>
</tr>
<tr>
<td>
<p><i>Error&#160;code</i></p>
</td>
<td>
<p>The command failed. See <i>Error Codes</i> in the Bluetooth Core specification for details.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Subcommand_opcode</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>0x03</td>
<td>The subcommand opcode for HCI_VS_MSFT_LE_Monitor_Advertisement.</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Monitor_handle</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00&#160;-&#160;0xFF</p>
</td>
<td>
<p>The handle to this rule. This handle is used as a parameter for <a href="hci_vs_msft_le_cancel_monitor_advertisement.htm"><b>HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement</b></a> to  cancel monitoring the advertisement.</p>
<p>This parameter is only valid if <i>Status</i> is 0x00.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
<h2><a id="Events_generated__unless_masked_away_"></a><a id="events_generated__unless_masked_away_"></a><a id="EVENTS_GENERATED__UNLESS_MASKED_AWAY_"></a>Events generated (unless masked away)</h2>
<p>When the HCI_VS_MSFT_LE_Monitor_Advertisement command is received, the controller shall generate a Command Complete event.</p>
<h2>Requirements</h2>
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows 10 for desktop editions (Home, Pro, Enterprise, and Education),  Windows 10 Mobile, and later versions.</p>
</td>
</tr>
</table>
<h2><a id="see_also"></a>See also</h2>
<dl>
<dt><a href="hci_vs_msft_le_set_advertisement_filter_enable.htm"><b>HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable</b></a></dt>
<dt><a href="hci_vs_msft_le_cancel_monitor_advertisement.htm"><b>HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement</b></a></dt>
<dt><a href="hci_vs_msft_le_monitor_device_event.htm"><b>HCI_VS_MSFT_LE_Monitor_Device_Event</b></a></dt>
</dl>
<p> </p>
<p> </p>

### HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement

<p>HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement cancels a previously-issued <a href="hci_vs_msft_le_monitor_advertisement.htm"><b>HCI_VS_MSFT_LE_Monitor_Advertisement</b></a> command.</p>
<table>
<tr>
<th>Command</th>
<th>Code</th>
<th>Command parameters</th>
<th>Return parameters</th>
</tr>
<tr>
<td>
<p>HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement</p>
</td>
<td>
<p>Chosen base code</p>
</td>
<td>
<p><i>Subcommand_opcode</i></p>
<p><i>Monitor_handle</i></p>
</td>
<td>
<p><i>Status</i></p>
<p><i>Subcommand_opcode</i></p>
</td>
</tr>
</table>
<p> </p>
<p>The controller shall promptly generate a Command Completed event in response to this command.</p>
<h2><a id="Command_parameters"></a><a id="command_parameters"></a><a id="COMMAND_PARAMETERS"></a>Command parameters</h2>
<dl>
<dd>
<p><b><i>Subcommand_opcode</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x04</p>
</td>
<td>
<p>The subcommand opcode for HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Connection_handle</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x<i>XX</i></p>
</td>
<td>
<p>The handle to the filter that is being cancelled.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
<h2><a id="Return_parameters"></a><a id="return_parameters"></a><a id="RETURN_PARAMETERS"></a>Return parameters</h2>
<dl>
<dd>
<p><b><i>Status</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>The command succeeded.</p>
</td>
</tr>
<tr>
<td>
<p>0x01&#160;-&#160;0xFF</p>
</td>
<td>
<p>The command failed. See <i>Error Codes</i> in the Bluetooth Core specification for details.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Subcommand_opcode</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x04</p>
</td>
<td>
<p>The subcommand opcode for HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
<h2><a id="Events_generated__unless_masked_away_"></a><a id="events_generated__unless_masked_away_"></a><a id="EVENTS_GENERATED__UNLESS_MASKED_AWAY_"></a>Events generated (unless masked away)</h2>
<p>The controller shall generate a Command Complete event when the HCI_VS_MSFT_LE_Cancel_Monitor_Advertisement command is received.</p>
<h2>Requirements</h2>
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows 10 for desktop editions (Home, Pro, Enterprise, and Education),  Windows 10 Mobile, and later versions.</p>
</td>
</tr>
</table>
<h2><a id="see_also"></a>See also</h2>
<dl>
<dt><a href="hci_vs_msft_le_monitor_advertisement.htm"><b>HCI_VS_MSFT_LE_Monitor_Advertisement</b></a></dt>
</dl>
<p> </p>
<p> </p>

### HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable

<p>HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable sets the state of the advertisement filters.</p>
<table>
<tr>
<th>Command</th>
<th>Code</th>
<th>Command parameters</th>
<th>Return parameters</th>
</tr>
<tr>
<td>
<p>HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable</p>
</td>
<td>
<p>Chosen base code</p>
</td>
<td>
<p><i>Subcommand_opcode</i></p>
<p><i>Enable</i></p>
</td>
<td>
<p><i>Status</i></p>
<p><i>Subcommand_opcode</i></p>
</td>
</tr>
</table>
<p> </p>
<p>If <i>Enable</i> is set to 0x00, the controller shall propagate received advertisements to the host based on existing white list settings. The controller shall continue monitoring the devices that are currently being monitored and generate an <a href="hci_vs_msft_le_monitor_device_event.htm"><b>HCI_VS_MSFT_LE_Monitor_Device_Event</b></a> with <i>Monitor_state</i> set to 0 if the device is no longer being monitored. The controller shall generate an HCI_VS_MSFT_LE_Monitor_Device_Event with <i>Monitor_state</i> set to 1 if a new device is being monitored. The host may issue HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable with <i>Enable</i> set to 0x01 to reenable all the filter conditions.</p>
<p>If <i>Enable</i> is set to 0x01, this command enables all filters that were set with a previously-issued <a href="hci_vs_msft_le_monitor_advertisement.htm"><b>HCI_VS_MSFT_LE_Monitor_Advertisement</b></a> command. The controller shall reject an HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable command if it does not toggle the filter state:</p>
<ul>
<li>The controller shall reject an HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable command with <i>Enable</i> set to 0x01 if it previously received an HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable command with <i>Enable</i> set to 0x01.</li>
<li>The controller shall reject the HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable command with <i>Enable</i> set to 0x00 if it previously received an HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable command with <i>Enable</i> set to 0x00.</li>
</ul>
<p>The default state of the advertisement filter shall be off. This state is equivalent to the controller previously receiving a HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable command with <i>Enable</i> set to 0x00.</p>
<p>The controller shall promptly generate a Command Completed event in response to this command.</p>
<h2><a id="Command_parameters"></a><a id="command_parameters"></a><a id="COMMAND_PARAMETERS"></a>Command parameters</h2>
<dl>
<dd>
<p><b><i>Subcommand_opcode</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x05</p>
</td>
<td>
<p>The subcommand opcode for HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Enable</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>Revert to current white list behavior, but continue monitoring devices based on the <i>Condition</i>s from  <a href="hci_vs_msft_le_monitor_advertisement.htm"><b>HCI_VS_MSFT_LE_Monitor_Advertisement</b></a> commands.</p>
</td>
</tr>
<tr>
<td>
<p>0x01</p>
</td>
<td>
<p>Enable all issued HCI_VS_MSFT_LE_Monitor_Advertisement commands on the controller.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
<h2><a id="Return_parameters"></a><a id="return_parameters"></a><a id="RETURN_PARAMETERS"></a>Return parameters</h2>
<dl>
<dd>
<p><b><i>Status</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>The command succeeded.</p>
</td>
</tr>
<tr>
<td>
<p>0x0C</p>
</td>
<td>
<p>The controller shall return <i>Command Disallowed</i> if the controller rejected the command because it previously saw an HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable command with <i>Enable</i> set to the same value as this command.</p>
</td>
</tr>
<tr>
<td>
<p><i>Error&#160;code</i></p>
</td>
<td>
<p>The command failed. See <i>Error Codes</i> in the Bluetooth Core specification for details.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Subcommand_opcode</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x05</p>
</td>
<td>
<p>The subcommand opcode for HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
<h2><a id="Events_generated__unless_masked_away_"></a><a id="events_generated__unless_masked_away_"></a><a id="EVENTS_GENERATED__UNLESS_MASKED_AWAY_"></a>Events generated (unless masked away)</h2>
<p>The controller shall generate a Command Complete event when the HCI_VS_MSFT_LE_Set_Advertisement_Filter_Enable command is received.</p>
<h2>Requirements</h2>
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows 10 for desktop editions (Home, Pro, Enterprise, and Education),  Windows 10 Mobile, and later versions.</p>
</td>
</tr>
</table>
<h2><a id="see_also"></a>See also</h2>
<dl>
<dt><a href="hci_vs_msft_le_monitor_advertisement.htm"><b>HCI_VS_MSFT_LE_Monitor_Advertisement</b></a></dt>
<dt><a href="hci_vs_msft_le_monitor_device_event.htm"><b>HCI_VS_MSFT_LE_Monitor_Device_Event</b></a></dt>
</dl>
<p> </p>
<p> </p>

### HCI_VS_MSFT_Read_Absolute_RSSI

<p>HCI_VS_MSFT_Read_Absolute_RSSI reads the <b>absolute</b> Received Signal Strength Indication (RSSI) value for a BR/EDR connection from the controller.</p>
<table>
<tr>
<th>Command</th>
<th>Code</th>
<th>Command parameters</th>
<th>Return parameters</th>
</tr>
<tr>
<td>
<p>HCI_VS_MSFT_Read_Absolute_RSSI</p>
</td>
<td>
<p>Chosen base code</p>
</td>
<td>
<p><i>Subcommand_opcode</i></p>
<p><i>Handle</i></p>
</td>
<td>
<p><i>Status</i></p>
<p><i>Subcommand_opcode</i></p>
<p><i>Handle</i></p>
<p><i>RSSI</i></p>
</td>
</tr>
</table>
<p> </p>
<p>A connection handle is provided as both a command and return parameter to identify the ACL connection whose RSSI is being read. The RSSI metric is the <b>absolute</b> receiver signal strength in dBm to ± 6 dB accuracy. If the RSSI cannot be read, the RSSI metric shall be set to 127.</p>
<p>The controller shall always complete this command promptly with a Command Completed event.</p>
<h2><a id="Command_parameters"></a><a id="command_parameters"></a><a id="COMMAND_PARAMETERS"></a>Command parameters</h2>
<dl>
<dd>
<p><b><i>Subcommand_opcode</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x06</p>
</td>
<td>
<p>The subcommand opcode for HCI_VS_MSFT_Read_Absolute_RSSI.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Handle</i></b> (2 octets):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x<i>XXXX</i></p>
</td>
<td>
<p>The handle for the BR/EDR connection whose RSSI has to be read.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd></dd>
</dl>
<h2><a id="Return_parameters"></a><a id="return_parameters"></a><a id="RETURN_PARAMETERS"></a>Return parameters</h2>
<dl>
<dd>
<p><b><i>Status</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>The command succeeded.</p>
</td>
</tr>
<tr>
<td>
<p>0x01&#160;-&#160;0xFF</p>
</td>
<td>
<p>The command failed. See <i>Error Codes</i> in the Bluetooth Core specification for details.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Subcommand_opcode</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x06</p>
</td>
<td>
<p>The subcommand opcode for HCI_VS_MSFT_Read_Absolute_RSSI.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Handle</i></b> (2 octets):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x<i>XXXX</i></p>
</td>
<td>
<p>The handle for the BR/EDR connection whose RSSI was read.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>RSSI</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p><i>N</i> = <i>RSSI&#160;value</i></p>
</td>
<td>
<p>The RSSI value for the BR/EDR connection.</p>
<ul>
<li>Range: -128 &lt;= <i>N</i> &lt;= 127 (signed integer)</li>
<li>Unit: dBm</li>
</ul>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
<h2><a id="Events_generated__unless_masked_away_"></a><a id="events_generated__unless_masked_away_"></a><a id="EVENTS_GENERATED__UNLESS_MASKED_AWAY_"></a>Events generated (unless masked away)</h2>
<p>The controller shall generate a Command Complete event when the HCI_VS_MSFT_Read_Absolute_RSSI command has completed.</p>
<h2>Requirements</h2>
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows 10 for desktop editions (Home, Pro, Enterprise, and Education),  Windows 10 Mobile, and later versions.</p>
</td>
</tr>
</table>
<p> </p>
<p> </p>

## Microsoft-defined Bluetooth HCI events

All Microsoft-defined Bluetooth HCI events are vendor-defined events and use event code 0xFF. The event data for Microsoft events always starts with a constant string of bytes to distinguish the Microsoft-defined events from other vendor-defined events. The length and value of the constant string are defined by the controller implementer and returned in response to HCI_VS_MSFT_Read_Supported_Features.

### HCI_VS_MSFT_RSSI_Event

p>HCI_VS_MSFT_RSSI_Event indicates that an <a href="hci_vs_msft_monitor_rssi.htm"><b>HCI_VS_MSFT_Monitor_Rssi</b></a> command has completed.</p>
<p>If the <i>Status</i> parameter is zero, the command completed because the RSSI value for the remote device changed to a value outside of the specified range. If the <i>Status</i> parameter is non-zero, the command completed because the RSSI value of the connection can no longer be monitored.</p>
<table>
<tr>
<th>Event</th>
<th>Event Code</th>
<th>Microsoft event code</th>
<th>Event parameters</th>
</tr>
<tr>
<td>
<p>HCI_VS_MSFT_RSSI_Event</p>
</td>
<td>
<p>0xFF</p>
</td>
<td>
<p>0x01</p>
</td>
<td>
<p><i>Event_prefix</i></p>
<p><i>Microsoft_event_code</i></p>
<p><i>Status</i></p>
<p><i>Connection_handle</i></p>
<p><i>RSSI</i></p>
</td>
</tr>
</table>
<p> </p>
<h2><a id="Event_parameters"></a><a id="event_parameters"></a><a id="EVENT_PARAMETERS"></a>Event parameters</h2>
<dl>
<dd>
<p><b><i>Event_prefix</i></b> (variable size):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p><i>Event prefix</i></p>
</td>
<td>
<p>The event prefix that flags this event as Microsoft-defined. The size and value are as returned by the <a href="hci_vs_msft_read_supported_features.htm"><b>HCI_VS_MSFT_Read_Supported_Features</b></a> command.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Microsoft_event_code</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x01</p>
</td>
<td>
<p>The event code for HCI_VS_MSFT_RSSI_Event.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Status</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>Success. The RSSI value of the connection has met one of the following conditions.</p>
<ul>
<li>
<p>The RSSI reached or exceeded <i>RSSI_threshold_high</i>.</p>
</li>
<li>
<p>The RSSI reached or dropped below <i>RSSI_threshold_low</i> over <i>RSSI_threshold_low_time_interval</i> seconds.</p>
</li>
<li>
<p>The <i>RSSI_sampling_period</i> has expired and this event was generated to notify the host of the RSSI value.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>0x01&#160;-&#160;0xFF</p>
</td>
<td>
<p>Failure. The RSSI value of the connection can no longer be monitored. The error code is usually one of codes that describes why the underlying ACL connection was lost.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Connection_handle</i></b> (2 octets):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x<i>XXXX</i></p>
</td>
<td>
<p>The handle for the connection whose RSSI is to be monitored.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>RSSI</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p><i>N</i> = <i>RSSI&#160;value</i></p>
</td>
<td>
<p>The measured link RSSI value for the connection.</p>
<p>For BR/EDR:</p>
<ul>
<li>Range: -128 &lt;= <i>N</i> &lt;= 127 (signed integer)</li>
<li>Unit: dBm</li>
</ul>
<p>For LE:</p>
<ul>
<li>Range: -127 to 20 (signed integer)</li>
<li>Unit: dBm</li>
</ul>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
<h2>Requirements</h2>
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows 10 for desktop editions (Home, Pro, Enterprise, and Education),  Windows 10 Mobile, and later versions.</p>
</td>
</tr>
</table>
<h2><a id="see_also"></a>See also</h2>
<dl>
<dt><a href="hci_vs_msft_monitor_rssi.htm"><b>HCI_VS_MSFT_Monitor_Rssi</b></a></dt>
</dl>
<p> </p>
<p> </p>

## HCI_VS_MSFT_LE_Monitor_Device_Event

<p>HCI_VS_MSFT_LE_Monitor_Device_Event indicates that the controller has either started or stopped monitoring a Bluetooth LE device. </p>
<p>If the <i>Monitor_state</i> parameter value is 1, the controller started monitoring the Bluetooth device with the specified BD_ADDR. If the <i>Monitor_state</i> parameter value is 0, the controller stopped monitoring the Bluetooth device with the specified BD_ADDR.</p>
<table>
<tr>
<th>Event</th>
<th>Event Code</th>
<th>Microsoft event code</th>
<th>Event parameters</th>
</tr>
<tr>
<td>
<p>HCI_VS_MSFT_LE_Monitor_Device_Event</p>
</td>
<td>
<p>0xFF</p>
</td>
<td>
<p>0x02</p>
</td>
<td>
<p><i>Event_prefix</i></p>
<p><i>Microsoft_event_code</i></p>
<p><i>Address_type</i></p>
<p><i>BD_ADDR</i></p>
<p><i>Monitor_handle</i></p>
<p><i>Monitor_state</i></p>
</td>
</tr>
</table>
<p> </p>
<p>The controller shall not generate an HCI_VS_MSFT_LE_Monitor_Device_Event with the <i>Monitor_state</i> parameter set to 0 if it has not already generated an HCI_VS_MSFT_LE_Monitor_Device_Event with <i>Monitor_state</i> set to 1.</p>
<h2><a id="Event_parameters"></a><a id="event_parameters"></a><a id="EVENT_PARAMETERS"></a>Event parameters</h2>
<dl>
<dd>
<p><b><i>Event_prefix</i></b> (variable size):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p><i>Event prefix</i></p>
</td>
<td>
<p>The event prefix that flags this event as Microsoft-defined. The size and value are as returned by the <a href="hci_vs_msft_read_supported_features.htm"><b>HCI_VS_MSFT_Read_Supported_Features</b></a> command.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Microsoft_event_code</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x02</p>
</td>
<td>
<p>The event code for HCI_VS_MSFT_LE_Monitor_Device_Event.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Address_type</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>Public Device Address.</p>
</td>
</tr>
<tr>
<td>
<p>0x01</p>
</td>
<td>
<p>Random Device Address.</p>
</td>
</tr>
<tr>
<td>
<p>0x02&#160;-&#160;0xFF</p>
</td>
<td>
<p>Reserved values for future use.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>BD_ADDR</i></b> (6 octets):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x<i>XXXXXXXXXXXX</i></p>
</td>
<td>
<p>The Bluetooth address of the device.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Monitor_handle</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x<i>XX</i></p>
</td>
<td>
<p>The handle to the filter that was specified for the <a href="hci_vs_msft_le_monitor_advertisement.htm"><b>HCI_VS_MSFT_LE_Monitor_Advertisement</b></a> command.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
<dd>
<p><b><i>Monitor_state</i></b> (1 octet):</p>
<table>
<tr>
<th>Value</th>
<th>Parameter description</th>
</tr>
<tr>
<td>
<p>0x00</p>
</td>
<td>
<p>The controller stopped monitoring the device specified by <i>BD_ADDR</i> and <i>Monitor_handle</i>.</p>
</td>
</tr>
<tr>
<td>
<p>0x01</p>
</td>
<td>
<p>The controller started monitoring the device specified by <i>BD_ADDR</i> and <i>Monitor_handle</i>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
<h2>Requirements</h2>
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows 10 for desktop editions (Home, Pro, Enterprise, and Education),  Windows 10 Mobile, and later versions.</p>
</td>
</tr>
</table>
<h2><a id="see_also"></a>See also</h2>
<dl>
<dt><a href="hci_vs_msft_le_monitor_advertisement.htm"><b>HCI_VS_MSFT_LE_Monitor_Advertisement</b></a></dt>
</dl>
<p> </p>
<p> </p>

