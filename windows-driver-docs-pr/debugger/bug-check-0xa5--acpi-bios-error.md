---
title: Bug Check 0xA5 ACPI_BIOS_ERROR
description: The ACPI_BIOS_ERROR bug check has a value of 0x000000A5 that indicates that the ACPI BIOS of the computer is not fully compliant with the ACPI specification.
ms.assetid: f0366a3c-a2c4-4fc8-a722-52fdda59eb2b
keywords: ["Bug Check 0xA5 ACPI_BIOS_ERROR", "ACPI_BIOS_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ACPI_BIOS_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xA5: ACPI\_BIOS\_ERROR


The ACPI\_BIOS\_ERROR bug check has a value of 0x000000A5. This bug check indicates that the Advanced Configuration and Power Interface (ACPI) BIOS of the computer is not fully compliant with the ACPI specification.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## ACPI\_BIOS\_ERROR Parameters


Parameter 1 indicates the kind of the incompatibility. The meaning of the other parameters depends on the value of Parameter 1.

If the BIOS incompatibility is related to Plug and Play (PnP) or power management, the following parameters are used.

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
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x01</p></td>
<td align="left"><p>ACPI&#39;s <strong>deviceExtension</strong></p></td>
<td align="left"><p>ACPI&#39;s <strong>ResourceList</strong></p></td>
<td align="left"><p><strong>0:</strong> No resource list is found</p>
<p><strong>1:</strong> No IRQ resource is found in list</p></td>
<td align="left"><p>ACPI cannot find the System Control Interrupt (SCI) vector in the resources that are handed to it when ACPI is started.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x02</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>(See the table later on this page)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x03</p></td>
<td align="left"><p>The ACPI object that was being run</p></td>
<td align="left"><p>The return value from the interpreter</p></td>
<td align="left"><p>The name of the control method (in ULONG format)</p></td>
<td align="left"><p>ACPI tried to run a control method while creating device extensions to represent the ACPI namespace, but this control method failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x04</p></td>
<td align="left"><p>The ACPI extension that _PRW belongs to</p></td>
<td align="left"><p>A pointer to the method</p></td>
<td align="left"><p>The <strong>DataType</strong> returned (see Amli.h)</p></td>
<td align="left"><p>ACPI evaluated a _PRW and expected to find an integer as a package element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x05</p></td>
<td align="left"><p>The ACPI extension that _PRW belongs to</p></td>
<td align="left"><p>Aointer to the _PRW</p></td>
<td align="left"><p>The number of elements in the _PRW</p></td>
<td align="left"><p>ACPI evaluated a _PRW, and the package that came back failed to contain at least two elements. The ACPI specification requires that two elements always be present in a _PRW.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x06</p></td>
<td align="left"><p>The ACPI extension that _PRx belongs to</p></td>
<td align="left"><p>A pointer to the _PRx</p></td>
<td align="left"><p>A pointer to the name of the object to look for</p></td>
<td align="left"><p>ACPI tried to find a named object, but it could not find the object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x07</p></td>
<td align="left"><p>The ACPI extension that the method belongs to</p></td>
<td align="left"><p>A pointer to the method</p></td>
<td align="left"><p>The <strong>DataType</strong> returned (see Amli.h)</p></td>
<td align="left"><p>ACPI evaluated a method and expected to receive a buffer in return. However, the method returned some other data type.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x08</p></td>
<td align="left"><p>The ACPI extension that the method belongs to</p></td>
<td align="left"><p>A pointer to the method</p></td>
<td align="left"><p>The <strong>DataType</strong> returned (see Amli.h)</p></td>
<td align="left"><p>ACPI evaluated a method and expected to receive an integer in return. However, the method returned some other data type.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x09</p></td>
<td align="left"><p>The ACPI extension that the method belongs to</p></td>
<td align="left"><p>A pointer to the method</p></td>
<td align="left"><p>The <strong>DataType</strong> returned (see Amli.h)</p></td>
<td align="left"><p>ACPI evaluated a method and expected to receive a package in return. However, the method returned some other data type.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0A</p></td>
<td align="left"><p>The ACPI extension that the method belongs to</p></td>
<td align="left"><p>A pointer to the method</p></td>
<td align="left"><p>The <strong>DataType</strong> returned (see Amli.h)</p></td>
<td align="left"><p>ACPI evaluated a method and expected to receive a string in return. However, the method returned some other data type.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0B</p></td>
<td align="left"><p>The ACPI extension that _EJD belongs to</p></td>
<td align="left"><p>The status that the interpreter returns</p></td>
<td align="left"><p>The name of the object that ACPI is trying to find</p></td>
<td align="left"><p>ACPI cannot find the object that an _EJD string references.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0C</p></td>
<td align="left"><p>The ACPI extension that ACPI found a dock device for</p></td>
<td align="left"><p>A pointer to the _EJD method</p></td>
<td align="left"><p><strong>0:</strong> BIOS does not claim system is dockage</p>
<p><strong>1:</strong> Duplicate device extensions for dock device</p></td>
<td align="left"><p>ACPI provides faulty or insufficient information for dock support.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0D</p></td>
<td align="left"><p>The ACPI extension that ACPI needs the object for</p></td>
<td align="left"><p>The (ULONG) name of the method that ACPI looked for</p></td>
<td align="left"><p><strong>0:</strong> Base case</p>
<p><strong>1:</strong> Conflict</p></td>
<td align="left"><p>ACPI could not find a required method or object in the namespace This bug check code is used if there is no _HID or _ADR present.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0E</p></td>
<td align="left"><p>The NS <strong>PowerResource</strong> that ACPI needs the object for</p></td>
<td align="left"><p>The (ULONG) name of the method that ACPI looked for</p></td>
<td align="left"><p>0: Base case</p></td>
<td align="left"><p>ACPI could not find a required method or object in the namespace for a power resource (or entity other than a &quot;device&quot;). This bug check code is used if there is no _ON, _OFF, or _STA present for a power resource.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0F</p></td>
<td align="left"><p>The current buffer that ACPI was parsing</p></td>
<td align="left"><p>The buffer&#39;s tag</p></td>
<td align="left"><p>The specified length of the buffer</p></td>
<td align="left"><p>ACPI could not parse the resource descriptor.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>(See the table later on this page)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x11</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>(See the table later on this page)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x14</p></td>
<td align="left"><p>The current buffer that ACPI was parsing</p></td>
<td align="left"><p>The buffer&#39;s tag</p></td>
<td align="left"><p>A pointer to a variable that contains the ULONGLONG length of the buffer</p></td>
<td align="left"><p>ACPI could not parse the resource descriptor. The length exceeds MAXULONG.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x15</p></td>
<td align="left"><p>The ACPI Machine Language (AML) context</p></td>
<td align="left"><p><strong>1:</strong> Failed to load table</p>
<p><strong>2:</strong> The Parameter Path String Object was not found</p>
<p><strong>3:</strong> Failed to insert Parameter Data into the ParameterPath String Object</p>
<p><strong>4:</strong> Out of system memory</p></td>
<td align="left"><p>The NT status code</p></td>
<td align="left"><p>ACPI had a fatal error when attempting to load a table.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x16</p></td>
<td align="left"><p>A pointer to the parent NSOBJ</p></td>
<td align="left"><p>A pointer to the illegal child ACPI namespace object</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>ACPI had a fatal error when processing an xSDT. An object was declared as a child of a parent that cannot have children.</p></td>
</tr>
</tbody>
</table>

 

If an interrupt routing failure or incompatibility has occurred, the following parameters are used.

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
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x2001</p></td>
<td align="left"><p><strong>InterruptModel</strong> (integer)</p></td>
<td align="left"><p>The return value from the interpreter</p></td>
<td align="left"><p>A pointer to the PIC control method</p></td>
<td align="left"><p>ACPI tried to evaluate the PIC control method but failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10001</p></td>
<td align="left"><p>A pointer to the device object</p></td>
<td align="left"><p>A pointer to the parent of the device object</p></td>
<td align="left"><p>A pointer to the _PRT object</p>
<p>(See the following Comments section)</p></td>
<td align="left"><p>ACPI tried to do interrupt routing, but failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10002</p></td>
<td align="left"><p>A pointer to the device object</p></td>
<td align="left"><p>A pointer to the string name that ACPI was looking for but could not find</p></td>
<td align="left"><p>A pointer to the _PRT object</p>
<p>(See the following Comments section)</p></td>
<td align="left"><p>ACPI could not find the link node referenced in a _PRT.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10003</p></td>
<td align="left"><p>A pointer to the device object</p></td>
<td align="left"><p>The device ID or function number.</p>
<p>This DWORD is encoded as follows: bits 5:0 are the PCI device number, and bits 8:6 are the PCI function number</p></td>
<td align="left"><p>A pointer to the _PRT object</p>
<p>(See the following Comments section)</p></td>
<td align="left"><p>ACPI could not find a mapping in the _PRT package for a device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10005</p></td>
<td align="left"><p>A pointer to the _PRT object</p>
<p>(See the following Comments section)</p></td>
<td align="left"><p>A pointer to the current _PRT element.</p>
<p>(This pointer is an index into the _PRT.)</p></td>
<td align="left"><p>The device ID or function number.</p>
<p>This DWORD is encoded as follows: bits 15:0 are the PCI function number, and bits 31:16 are the PCI device number</p></td>
<td align="left"><p>ACPI found an entry in the _PRT that the function ID is not all F&#39;s for.</p>
<p>(The generic format for a _PRT entry is that the device number is specified, but the function number is not.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10006</p></td>
<td align="left"><p>A pointer to the link node.</p>
<p>(This device is missing the _DIS method.)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>ACPI found a link node, but it cannot disable the node.</p>
<p>(Link nodes must be disabled to allow for reprogramming.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10007</p></td>
<td align="left"><p>The vector that could not be found</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The _PRT contained a reference to a vector that is not described in the I/O APIC entry&#39;s MAPIC table.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10008</p></td>
<td align="left"><p>The invalid interrupt level.</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The ACPI SCI interrupt level is invalid.</p>
<p></p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10009</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The Fixed ACPI Description Table (FADT) could not be located.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1000A</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The Root System Description Pointer (RSDP) or Extended System Description Table (XSDT) could not be located</p>
<p></p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1000B</p></td>
<td align="left"><p>The ACPI table signature</p></td>
<td align="left"><p>A pointer to the ACPI table</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The length of the ACPI table is not consistent with the table revision.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x20000</p></td>
<td align="left"><p>The I/O port in the Fixed Table</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The PM_TMR_BLK entry in the Fixed ACPI Description Table doesn&#39;t point to a working ACPI timer block.</p></td>
</tr>
</tbody>
</table>

 

If a miscellaneous failure or incompatibility has occurred, the following parameters are used.

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
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x20000</p></td>
<td align="left"><p>The I/O port in the Fixed Table</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The PM_TMR_BLK entry in the Fixed ACPI Description Table does not point to a working ACPI timer block.</p></td>
</tr>
</tbody>
</table>

 

If Parameter 1 equals **0x02**, the ACPI BIOS could not process the resource list for the PCI root buses. In this case, Parameter 3 specifies the exact problem, and the remaining parameters have the following definitions.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>The ACPI extension for the PCI bus</p></td>
<td align="left"><p>0x0</p></td>
<td align="left"><p>A pointer to the QUERY_RESOURCES IRP</p></td>
<td align="left"><p>ACPI cannot convert the BIOS&#39; resource list into the proper format. This probably represents an error in the BIOS&#39; list encoding procedure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>The ACPI extension for the PCI bus</p></td>
<td align="left"><p>0x1</p></td>
<td align="left"><p>A pointer to the QUERY_RESOURCE_REQUIREMENTS IRP</p></td>
<td align="left"><p>ACPI cannot convert the BIOS&#39; resource list into the proper format. This probably represents an error in the BIOS&#39; list encoding procedure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>The ACPI extension for the PCI bus</p></td>
<td align="left"><p>0x2</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>ACPI found an empty resource list.</p></td>
</tr>
<tr class="even">
<td align="left"><p>The ACPI extension for the PCI bus</p></td>
<td align="left"><p>0x3</p></td>
<td align="left"><p>A pointer to the PNP CRS descriptor</p></td>
<td align="left"><p>ACPI could not find the current bus number in the CRS.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>The ACPI extension for the PCI bus</p></td>
<td align="left"><p>A pointer to the resource list for PCI</p></td>
<td align="left"><p>A pointer to the E820 memory table</p></td>
<td align="left"><p>The list of resources that PCI claims to decode overlaps with the list of memory regions that the E820 BIOS interface reports. (This kind of conflict is never permitted.)</p></td>
</tr>
</tbody>
</table>

 

If Parameter 1 equals **0x10**, the ACPI BIOS could not determine the system-to-device-state mapping correctly. In this situation, Parameter 3 specifies the exact problem, and the remaining parameters have the following definitions.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>The ACPI extension whose mapping is needed</p></td>
<td align="left"><p>0x0</p></td>
<td align="left"><p>The DEVICE_POWER_STATE (this is &quot;x+1&quot;)</p></td>
<td align="left"><p>_PRx was mapped back to a non-supported S-state.</p></td>
</tr>
<tr class="even">
<td align="left"><p>The ACPI extension whose mapping is needed</p></td>
<td align="left"><p>0x1</p></td>
<td align="left"><p>The SYSTEM_POWER_STATE that cannot be mapped</p></td>
<td align="left"><p>ACPI cannot find a D-state to associate with the S-state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>The ACPI extension whose mapping is needed</p></td>
<td align="left"><p>0x2</p></td>
<td align="left"><p>The SYSTEM_POWER_STATE that cannot be mapped</p></td>
<td align="left"><p>The device claims to be able to wake the system when the system is in this S-state, but the system does not actually support this S-state.</p></td>
</tr>
</tbody>
</table>

 

If Parameter 1 equals **0x11**, the system could not enter ACPI mode. In this situation, Parameter 2 specifies the exact problem, and the remaining parameters have the following definitions.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The system could not initialize the AML interpreter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The system could not find RSDT.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The system could not allocate critical driver structures.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The system could not load RSDT.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x4</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The system could not load DDBs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x5</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The system cannot connect the Interrupt vector.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x6</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>SCI_EN never becomes set in PM1 Control Register.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x7</p></td>
<td align="left"><p>A pointer to the table that had a bad checksum</p></td>
<td align="left"><p>Creator revision</p></td>
<td align="left"><p>The table checksum is incorrect.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x8</p></td>
<td align="left"><p>A pointer to the table that ACPI failed to load</p></td>
<td align="left"><p>Creator revision</p></td>
<td align="left"><p>ACPI failed to load DDB.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x9</p></td>
<td align="left"><p>FADT version</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Unsupported firmware version.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xA</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The system could not find MADT.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xB</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The system could not find any valid Local SAPIC structures in the MADT.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The value of Parameter 1 indicates the error.

Resolution
----------

If you are debugging this error, use the [**!analyze -v**](-analyze.md) extension. This extension displays all the relevant data (device extensions, nsobjects, or whatever is appropriate to the specific error).

If you are not performing debugging, this error indicates that you have to obtain a new BIOS. Contact your vendor or visit the internet to get a new BIOS.

If you cannot obtain an updated BIOS, or the latest BIOS is still not ACPI compliant, you can turn off ACPI mode during text-mode setup. To turn off ACPI mode, press the F7 key when you are prompted to install storage drivers. The system does not notify you that the F7 key was pressed, but it silently disables ACPI and enables you to continue your installation.

Remarks
-------

A PCI routing table (\_PRT) is the ACPI BIOS object that specifies how all the PCI devices are connected to the interrupt controllers. A computer with multiple PCI buses might have multiple \_PRTs.

You can display a \_PRT in the debugger by using the **!acpikd.nsobj** extension together with the address of the \_PRT object as its argument.

 

 




