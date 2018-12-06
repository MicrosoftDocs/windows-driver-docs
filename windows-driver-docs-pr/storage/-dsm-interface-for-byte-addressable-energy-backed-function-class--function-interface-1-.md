---
title: \_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)
description: This interface is designed to map to the JEDEC Byte Addressable Energy Backed Interface standard in order to minimize BIOS complexity.
ms.assetid: 895F1B13-4F2D-4B6B-A3CE-60A8AC9EE7B0
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# \_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)


This interface is designed to map to the JEDEC Byte Addressable Energy Backed Interface standard in order to minimize BIOS complexity. It provides a common basis of reporting device functions & capabilities, such that OS software can interact with various implementations through the same mechanisms. Further, it allows support for vendor-specific functionality through access to I2C registers.

Platforms that conform to \_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1) can support an NVDIMM-N that implements the *JEDEC Byte Addressable Energy Backed Interface* specification (function class 0x01 and function interface 0x01 per [JEDEC SPD Annex L: Serial Presence Detect for DDR4 SDRAM DDR4 SPD Document Release](http://go.microsoft.com/fwlink/p/?LinkId=627481)). For more info, see the [JEDEC Byte Addressable Energy Backed Interface specification (document JESD245)](https://www.jedec.org/standards-documents/docs/jesd245).

## <span id="DSM_Interface_for_Byte_Addressable_Energy_Backed_Function_Class_Function_Interface_1"></span><span id="dsm_interface_for_byte_addressable_energy_backed_function_class_function_interface_1"></span><span id="DSM_INTERFACE_FOR_BYTE_ADDRESSABLE_ENERGY_BACKED_FUNCTION_CLASS_FUNCTION_INTERFACE_1"></span>\_DSM Interface for Byte Addressable Energy Backed Function Class, Function Interface 1


The \_DSM GUID is 1EE68B36-D4BD-4a1a-9A16-4F8E53D46E05.

The \_DSM functions defined in this document shall be implemented in NVDIMM ACPI Namespace Devices objects. The term **Mandatory** refers to whether the function must return valid data or not.

### <span id="Mandatory_functions_and_fields"></span><span id="mandatory_functions_and_fields"></span><span id="MANDATORY_FUNCTIONS_AND_FIELDS"></span>Mandatory functions and fields

The following table specifies the functions & fields that are mandatory.

| Function Index | Function Name                                                                                                                                | Mandatory For Device-Managed Energy Source (ES) Policy | Mandatory For Host-Managed Energy Source (ES) Policy |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|------------------------------------------------------|
| 0              | [Query Implemented Functions (Function Index 0)](query-implemented-functions--function-index-0-.md)                                         | Yes                                                    | Yes                                                  |
| 1              | [Get NVDIMM-N Identification (Function Index 1)](get-nvdimm-n-identification--function-index-1-.md)                                         | Yes                                                    | Yes                                                  |
| 2              | [Get Save Operation Requirements (Function Index 2)](get-save-operation-requirements--function-index-2-.md)                                 | Yes                                                    | Yes                                                  |
| 3              | [Get Energy Source Identification (Function Index 3)](get-energy-source-identification--function-index-3-.md)                               | Yes                                                    | Yes                                                  |
| 4              | [Get Last Backup Information (Function Index 4)](get-last-backup-information--function-index-4-.md)                                         | Yes                                                    | Yes                                                  |
| 5              | [Get NVM Thresholds (Function Index 5)](get-nvm-thresholds--function-index-5-.md)                                                           | Yes                                                    | Yes                                                  |
| 6              | [Set NVM Lifetime Percentage Warning Threshold (Function Index 6)](set-nvm-lifetime-percentage-warning-threshold--function-index-6-.md)     | Yes                                                    | Yes                                                  |
| 7              | [Get Energy Source Thresholds (Function Index 7)](get-energy-source-thresholds--function-index-7-.md)                                       | Yes                                                    | No                                                   |
| 8              | [Set Energy Source Lifetime Warning Threshold (Function Index 8)](set-energy-source-lifetime-warning-threshold--function-index-8-.md)       | Yes                                                    | No                                                   |
| 9              | [Set Energy Source Temperature Warning Threshold (Function Index 9)](set-energy-source-temperature-warning-threshold--function-index-9-.md) | Yes                                                    | No                                                   |
| 10             | [Get Critical Health Info (Function Index 10)](get-critical-health-info--function-index-10-.md)                                             | Yes                                                    | Yes                                                  |
| 11             | [Get NVDIMM-N Health Info (Function Index 11)](get-nvdimm-n-health-info--function-index-11-.md)                                             | Yes                                                    | Yes                                                  |
| 12             | [Get Energy Source Health Info (Function Index 12)](get-energy-source-health-info--function-index-12-.md)                                   | Yes                                                    | No                                                   |
| 13             | [Get Operational Statistics (Function Index 13)](get-operational-statistics--function-index-13-.md)                                         | Yes                                                    | Yes                                                  |
| 14             | [Get Vendor Log Page Size (Function Index 14)](get-vendor-log-page-size--function-index-14-.md)                                             | Yes                                                    | Yes                                                  |
| 15             | [Get Vendor Log Page (Function Index 15)](get-vendor-log-page--function-index-15-.md)                                                       | Yes                                                    | Yes                                                  |
| 16             | [Query Error Injection Status (Function Index 16)](query-error-injection-status--function-index-16-.md)                                     | Yes                                                    | Yes                                                  |
| 17             | [Inject Error (Function Index 17)](inject-error--function-index-17-.md)                                                                     | Yes                                                    | Yes                                                  |
| 18             | [Get Injected Errors (Function Index 18)](get-injected-errors--function-index-18-.md)                                                       | Yes                                                    | Yes                                                  |
| 19             | [Erase NVM Image (Function Index 19)](erase-nvm-image--function-index-19-.md)                                                               | Yes                                                    | Yes                                                  |
| 20             | [Arm NVDIMM-N (Function Index 20)](arm-nvdimm-n--function-index-20-.md)                                                                     | Yes                                                    | Yes                                                  |
| 21             | [Reset to Factory Defaults (Function Index 21)](reset-to-factory-defaults--function-index-21-.md)                                           | Yes                                                    | Yes                                                  |
| 22             | [Start Firmware Update (Function Index 22)](start-firmware-update--function-index-22-.md)                                                   | Yes                                                    | Yes                                                  |
| 23             | [Send Firmware Update Data (Function Index 23)](send-firmware-update-data--function-index-23-.md)                                           | Yes                                                    | Yes                                                  |
| 24             | [Finish Firmware Update (Function Index 24)](finish-firmware-update--function-index-24-.md)                                                 | Yes                                                    | Yes                                                  |
| 25             | [Select Firmware Image Slot (Function Index 25)](select-firmware-image-slot--function-index-25-.md)                                         | Yes                                                    | Yes                                                  |
| 26             | [Get Firmware Info (Function Index 26)](get-firmware-info--function-index-26-.md)                                                           | Yes                                                    | Yes                                                  |
| 27             | [I2C Read (Function Index 27)](i2c-read--function-index-27-.md)                                                                             | Yes                                                    | Yes                                                  |
| 28             | [I2C Write (Function Index 28)](i2c-write--function-index-28-.md)                                                                           | Yes                                                    | Yes                                                  |
| 29             | [Read Typed Data (Function Index 29)](read-typed-data--function-index-29-.md)                                                               | Yes                                                    | Yes                                                  |
| 30             | [Write Typed Data (Function Index 30)](write-typed-data--function-index-30-.md)                                                             | Yes                                                    | Yes                                                  |
| 31             | [Set Memory Error Counters (Function Index 31)](set-memory-error-counters--function-index-31-.md)                                           | Yes                                                    | Yes                                                  |

 

## <span id="DSM_METHOD_INPUT"></span><span id="dsm_method_input"></span>\_DSM Method Input


*Arg3* to all functions is a Package value. If the function does not take an input argument, the Package value contains no data. If the function takes an input argument, the Package value contains a buffer.

If the function does not take an input argument and *Arg3* is not an empty Package, the function shall return the **General Status Code** of Invalid Input Parameters.

## \_DSM Method Output


All methods will return a buffer of length greater than or equal to 4 bytes. The first 4 bytes of the return buffer are structured as follows:

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
<td align="left">General Status Code</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left"><p>0 – Success</p>
<p>1 – Not Supported</p>
<p>2 – Invalid Input Parameters</p>
<p>3 – I2C Communication Error</p>
<p>4 – Function-Specific Error Code</p>
<p>5 – Vendor-Specific Error Code</p>
<p>6 - 0xFFFF – Reserved</p></td>
</tr>
<tr class="even">
<td align="left">Function-Specific Error Code</td>
<td align="left">1</td>
<td align="left">2</td>
<td align="left">This field contains an error code that is specific to the function that was called. This field only contains valid information if <strong>General Status Code</strong> is equal to <strong>Function-Specific Error Code</strong>.</td>
</tr>
<tr class="odd">
<td align="left">Vendor-Specific Error Code</td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left">This field contains vendor-specific status codes. It only contains valid information if <strong>General Status Code</strong> is equal to <strong>Vendor-Specific Error Code</strong>.</td>
</tr>
</tbody>
</table>

 

Any non-zero **General Status Code** indicates that the function failed. No function defined in this version of the specification shall return the **General Status Code** of **Not Supported**. All mandatory functions shall return valid data or an error code indicating a runtime error. Non-mandatory functions may return a Function-Specific Error Code to signal that there is no valid data to be returned.

All reserved bits and bytes shall have a value of 0. Unless specifically stated otherwise, all multi-byte fields shall be represented in a little-endian manner.

&gt; \[!Note\]   
&gt;A reference to a Byte Addressable Energy-Backed Interface register describes many return fields for functions specified in this interface. These fields shall be identical to the register defined in the "Byte Addressable Energy Backed Interface, version 1.0, JEDEC Standard No. 2233-22" revision of the Byte-Addressable Energy-Backed Interface specification. The specification version is reported in the **Specification Revision** field returned by the [Get NVDIMM-N Identification (Function Index 1)](get-nvdimm-n-identification--function-index-1-.md) function.

&gt;Some return fields refer to information about the Energy Source (ES). When the ES policy is device-managed, the platform shall read the hardware register specified in the field description to retrieve all ES-related information. When the ES policy is host-managed, the platform shall obtain the ES-related information through platform-specific mechanisms. In this case, all ES-related information shall be presented in the same binary layout as the hardware register specified in the field description.

&gt;

 

## <span id="related_topics"></span>Related topics


[Storage driver design guide](http://go.microsoft.com/fwlink/p/?LinkId=798409)

[JEDEC Byte-Addressable Energy-Backed Interface NVDIMM Device-Specific Method (\_DSM)](jedec-byte-addressable-energy-backed-interface-nvdimms-device-specific-method---dsm-.md)

 

 






