---
title: Get NVDIMM-N Identification (Function Index 1)
description: This function returns device-specific information.
ms.assetid: 350E764D-634C-4C60-9C74-E26B01636C02
---

# <span id="storage.get_nvdimm-n_identification__function_index_1_"></span>Get NVDIMM-N Identification (Function Index 1)


This function returns device-specific information.

&gt; \[!Note\]   
&gt;All registers marked with a star (\*) are registers defined in the Byte Addressable Energy Backed Interface specification.

 

## <span id="Input"></span><span id="input"></span><span id="INPUT"></span>Input


### <span id="Arg3"></span><span id="arg3"></span><span id="ARG3"></span>Arg3

None.

## <span id="Output"></span><span id="output"></span><span id="OUTPUT"></span>Output


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Byte Length</th>
<th align="left">Byte Offset</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>Status</strong></td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left"><p>Go to [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md#dsm-method-output) for information.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Specification Revision</strong></td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left"><p>The specification version supported by the module.</p>
<p>*Byte 0 – <em>SPECREV</em> (0, 0x06) This register is a Byte Addressable Energy Backed Interface registers.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Number of Standard Pages</strong></td>
<td align="left">1</td>
<td align="left">5</td>
<td align="left"><p>The number of standard defined pages supported by the module.</p>
<p>*Byte 0 – <em>STD_NUM_PAGES</em> (0, 0x01)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>First Vendor Page</strong></td>
<td align="left">1</td>
<td align="left">6</td>
<td align="left"><p>The starting page number for vendor-specific pages.</p>
<p>*Byte 0 – <em>VENDOR_START_PAGES</em> (0, 0x02)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Number of Vendor Pages</strong></td>
<td align="left">1</td>
<td align="left">7</td>
<td align="left"><p>The number of vendor-specific pages supported by the module.</p>
<p>*Byte 0 – <em>VENDOR_NUM_PAGES</em> (0, 0x03)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Hardware Revision</strong></td>
<td align="left">4</td>
<td align="left">8</td>
<td align="left"><p>The controller hardware revision.</p>
<p>*Byte 0 – <em>HWREV</em> (0, 0x04)</p>
<p>Byte 1 - Reserved.</p>
<p>Byte 2 - Reserved.</p>
<p>Byte 3 - Reserved.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Firmware Revision</strong></td>
<td align="left">2</td>
<td align="left">12</td>
<td align="left"><p>Firmware version of the active firmware slot.</p>
<p>*Byte 0 – <em>SLOTX_FWREV0</em> (0, 0x07/0x09)</p>
<p>*Byte 1 – <em>SLOTX_FWREV1</em> (0, 0x08/0x0A)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Current Firmware Slot</strong></td>
<td align="left">1</td>
<td align="left">14</td>
<td align="left"><p>The slot number of the running firmware image.</p>
<p>*Byte 0 – Bits [7:4] of <em>FW_SLOT_INFO</em> (3, 0x42) register (<em>RUNNING_FW_SLOT</em>).</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Firmware Slot Count</strong></td>
<td align="left">1</td>
<td align="left">15</td>
<td align="left"><p>The number of firmware slots available. For JEDEC-compliant devices, this field shall be 2.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Capabilities</strong></td>
<td align="left">1</td>
<td align="left">16</td>
<td align="left"><p>Information regarding the capabilities supported by the module.</p>
<p>*Byte 0 – <em>CAPABILITIES</em> (0, 0x10)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Supported Backup Triggers</strong></td>
<td align="left">1</td>
<td align="left">17</td>
<td align="left"><p>The module's supported save triggers.</p>
<p>*Byte 0 – <em>CSAVE_TRIGGER_SUPPORT</em> (0, 0x16)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Maximum Operation Retry Count</strong></td>
<td align="left">1</td>
<td align="left">18</td>
<td align="left"><p>The recommended retry count to the host if a save, restore or erase operation fails or exceeds the maximum timeout value.</p>
<p>*Byte 0 – <em>HOST_MAX_OPERATION_RETRY</em> (0, 0x15)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Supported Notification Events</strong></td>
<td align="left">1</td>
<td align="left">19</td>
<td align="left"><p>Event information the module will generate notifications for.</p>
<p>*Byte 0 – <em>EVENT_NOTIFICATION_SUPPORT</em> (0, 0x17)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Save Operation Timeout</strong></td>
<td align="left">4</td>
<td align="left">20</td>
<td align="left"><p>The worst case save completion latency in milliseconds or seconds.</p>
<p>*Byte 0 – <em>CSAVE_TIMEOUT0</em> (0, 0x18)</p>
<p>*Byte 1 – <em>CSAVE_TIMEOUT1</em> (0, 0x19)</p>
<p>Byte 2 - Reserved.</p>
<p>Byte 3 - Reserved.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Restore Operation Timeout</strong></td>
<td align="left">4</td>
<td align="left">24</td>
<td align="left"><p>The worst case restore completion latency in milliseconds or seconds.</p>
<p>*Byte 0 – <em>RESTORE_TIMEOUT0</em> (0, 0x1C)</p>
<p>*Byte 1 – <em>RESTORE_TIMEOUT1</em> (0, 0x1D)</p>
<p>Byte 2 - Reserved.</p>
<p>Byte 3 - Reserved.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Erase Operation Timeout</strong></td>
<td align="left">4</td>
<td align="left">28</td>
<td align="left"><p>The worst case erase completion latency in milliseconds or seconds.</p>
<p>*Byte 0 – <em>ERASE_TIMEOUT0</em> (0, 0x1E)</p>
<p>*Byte 1 – <em>ERASE_TIMEOUT1</em> (0, 0x1F)</p>
<p>Byte 2 - Reserved.</p>
<p>Byte 3 - Reserved.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Arm Operation Timeout</strong></td>
<td align="left">4</td>
<td align="left">32</td>
<td align="left"><p>The worst case arm completion latency in milliseconds or seconds.</p>
<p>Byte 0 – <em>ARM_TIMEOUT0</em> (0, 0x20)</p>
<p>Byte 1 – <em>ARM_TIMEOUT1</em> (0, 0x21)</p>
<p>Byte 2 - Reserved.</p>
<p>Byte 3 - Reserved.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Firmware Operations Timeout</strong></td>
<td align="left">4</td>
<td align="left">36</td>
<td align="left"><p>The worst case firmware operations completion latency in milliseconds or seconds.</p>
<p>*Byte 0 – <em>FIRMWARE_OPS_TIMEOUT0</em> (0, 0x22)</p>
<p>*Byte 1 – <em>FIRMWARE_OPS_TIMEOUT1</em> (0, 0x23)</p>
<p>Byte 2 - Reserved.</p>
<p>Byte 3 - Reserved.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Abort Operation Timeout</strong></td>
<td align="left">4</td>
<td align="left">40</td>
<td align="left"><p></p>
<p>*Byte 0 – <em>ABORT_CMD_TIMEOUT0</em> (0, 0x24)</p>
<p>Byte 1 – Reserved.</p>
<p>Byte 2 - Reserved.</p>
<p>Byte 3 - Reserved.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Minimum Operating Temperature</strong></td>
<td align="left">1</td>
<td align="left">44</td>
<td align="left"><p>The minimum operating temperature in degrees Celsius.</p>
<p>*Byte 0 – <em>MIN_OPERATING_TEMP</em> (0, 0x25)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Maximum Operation Temperature</strong></td>
<td align="left">1</td>
<td align="left">45</td>
<td align="left"><p>The maximum operating temperature in degrees Celsius.</p>
<p>*Byte 0 – <em>MAX_OPERATING_TEMP</em> (0, 0x26)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Region Block Size</strong></td>
<td align="left">4</td>
<td align="left">46</td>
<td align="left"><p>The region size in multiples of 32 bytes.</p>
<p>*Byte 0 – <em>REGION_BLOCK_SIZE</em> (0, 0x32)</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Get%20NVDIMM-N%20Identification%20%28Function%20Index%201%29%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





