---
title: Functions Defined by Print Providers
description: Functions Defined by Print Providers
ms.assetid: 4fae4b69-ed4b-47b6-b6e8-41733aed51a5
keywords:
- print providers WDK , functions
- functions WDK print providers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Functions Defined by Print Providers





**Warning**  
Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

 

This topic lists all of the functions a print provider can supply. Most of these functions are described in the Microsoft Windows SDK documentation. If the function is described in the Windows Driver Kit (WDK), the function name provides a link to the associated reference page.

All print providers must supply pointers for all listed functions. However, most vendor-supplied print providers are "partial providers" which do not need to support many of the operations defined by the functions. Therefore, many of the function pointers can be **NULL**. For more information about partial print providers, see [Writing a Network Print Provider](writing-a-network-print-provider.md).

In the following function lists, functions that must be supported are labeled "Required".

All print providers must export the initialization function, [**InitializePrintProvidor**](https://msdn.microsoft.com/library/windows/hardware/ff551614). Pointers to all the other functions must be supplied in a [**PRINTPROVIDOR**](https://msdn.microsoft.com/library/windows/hardware/ff560993) structure. (Note that these two names are misspelled, but are consistent with the names that appear in the header file, Winsplp.h.)

Functions are divided into groups, and presented in the following sections:

Initialization Function

Print Queue Management Functions

Printer Driver Management Functions

Print Job Creation Functions

Print Job Scheduling Functions

Forms Management Functions

Print Processor Management Functions

Print Monitor Management Functions

Port Management Functions

Registry Management Functions

Other Functions

### <a href="" id="ddk-initialization-function-gg"></a>Initialization Function

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551614" data-raw-source="[&lt;strong&gt;InitializePrintProvidor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551614)"><strong>InitializePrintProvidor</strong></a> (Required)</p></td>
<td><p>Initializes the print provider and returns pointers to supplied functions.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-print-queue-management-functions-gg"></a>Print Queue Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>AddPrinter</strong></p></td>
<td><p>Adds a print queue to the list of those managed by the print provider, and associates a print processor with the print queue.</p></td>
</tr>
<tr class="even">
<td><p><strong>AddPrinterConnection</strong></p></td>
<td><p>Creates a connection to the specified print queue.</p></td>
</tr>
<tr class="odd">
<td><p><strong>ClosePrinter</strong> (Required)</p></td>
<td><p>Disables caller access to a specified print queue.</p></td>
</tr>
<tr class="even">
<td><p><strong>DeletePrinter</strong></p></td>
<td><p>Deletes a print queue from the list of those managed by the print provider.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DeletePrinterConnection</strong></p></td>
<td><p>Removes a connection to the specified print queue.</p></td>
</tr>
<tr class="even">
<td><p><strong>EnumPrinters</strong> (Required)</p></td>
<td><p>Enumerates the list of print queues currently managed by the print provider.</p></td>
</tr>
<tr class="odd">
<td><p><strong>FindClosePrinterChangeNotification</strong></p></td>
<td><p>Disables printer change notifications that were enabled by <strong>FindFirstPrinterChangeNotification</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>FindFirstPrinterChangeNotification</strong></p></td>
<td><p>Returns a handle to a wait object that the caller can use to wait for specified printer events.</p></td>
</tr>
<tr class="odd">
<td><p><strong>GetPrinter</strong> (Required)</p></td>
<td><p>Returns current parameter values for a specified print queue.</p></td>
</tr>
<tr class="even">
<td><p><strong>OpenPrinter</strong> (Required)</p></td>
<td><p>Enables caller access to a specified print queue.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561930" data-raw-source="[&lt;strong&gt;RefreshPrinterChangeNotification&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561930)"><strong>RefreshPrinterChangeNotification</strong></a></p></td>
<td><p>Called by router if client calls <strong>FindNextPrinterChangeNotification</strong> (see the Microsoft Windows SDK documentation) with the PRINTER_NOTIFY_OPTIONS_REFRESH flag set.</p></td>
</tr>
<tr class="even">
<td><p><strong>ResetPrinter</strong></p></td>
<td><p>Modifies a print queue&#39;s data type or <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837" data-raw-source="[&lt;strong&gt;DEVMODEW&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552837)"><strong>DEVMODEW</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td><p><strong>SetPrinter</strong> (Required)</p></td>
<td><p>Sets parameters for a specified print queue.</p></td>
</tr>
<tr class="even">
<td><p><strong>WaitForPrinterChange</strong></p></td>
<td><p>Obsolete.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-printer-driver-management-functions-gg"></a>Printer Driver Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>AddPrinterDriver</strong></p></td>
<td><p>Adds a specified printer&#39;s driver files to a specified server.</p></td>
</tr>
<tr class="even">
<td><p><strong>AddPrinterDriverEx</strong></p></td>
<td><p>Same as <strong>AddPrinterDriver</strong>, with additional parameters.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DeletePrinterDriver</strong></p></td>
<td><p>Deletes access to a specified printer&#39;s driver files, on a specified server.</p></td>
</tr>
<tr class="even">
<td><p><strong>DeletePrinterDriverEx</strong></p></td>
<td><p>Same as <strong>DeletePrinterDriver</strong>, with additional parameters.</p></td>
</tr>
<tr class="odd">
<td><p><strong>EnumPrinterDrivers</strong></p></td>
<td><p>Returns a list of printer drivers that have been added to a specified server by calling <strong>AddPrinterDriver</strong> or <strong>AddPrinterDriverEx</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>GetPrinterDriver</strong></p></td>
<td><p>Returns information about a printer driver, which the caller can then pass to <strong>AddPrinterDriver</strong>. (The returned information is typically obtained from an INF file.)</p></td>
</tr>
<tr class="odd">
<td><p><strong>GetPrinterDriverEx</strong></p></td>
<td><p>Same as <strong>GetPrinterDriver</strong>, with additional parameters.</p></td>
</tr>
<tr class="even">
<td><p><strong>GetPrinterDriverDirectory</strong></p></td>
<td><p>Returns the name of the server&#39;s printer driver directory.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-print-job-creation-functions-gg"></a>Print Job Creation Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p></p>
<strong>AbortPrinter</strong>
(Required)</td>
<td><p>Attempts to delete the current job from the specified print queue.</p></td>
</tr>
<tr class="even">
<td><p></p>
<strong>AddJob</strong>
(Required)</td>
<td><p>Returns a job identifier and spool file path. The caller uses <a href="https://msdn.microsoft.com/library/windows/desktop/aa363858" data-raw-source="[&lt;strong&gt;CreateFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa363858)"><strong>CreateFile</strong></a> and <strong>WriteFile</strong> to send data to the spool file.</p></td>
</tr>
<tr class="odd">
<td><p></p>
<strong>EndDocPrinter</strong>
(Required)</td>
<td><p>Performs job completion operations.</p></td>
</tr>
<tr class="even">
<td><p><strong>EndPagePrinter</strong></p></td>
<td><p>Performs page completion operations.</p></td>
</tr>
<tr class="odd">
<td><p><strong>ReadPrinter</strong></p></td>
<td><p>Obtains status information from a bidirectional printer.</p></td>
</tr>
<tr class="even">
<td><p></p>
<strong>ScheduleJob</strong>
(Required)</td>
<td><p>Informs the provider that a specified job can be scheduled. The job is specified by a job identifier previously returned by <strong>AddJob</strong>.</p></td>
</tr>
<tr class="odd">
<td><p></p>
<strong>StartDocPrinter</strong>
(Required)</td>
<td><p>Prepares the print provider to begin spooling a print job.</p></td>
</tr>
<tr class="even">
<td><p><strong>StartPagePrinter</strong></p></td>
<td><p>Prepares the print provider to receive a print job page.</p></td>
</tr>
<tr class="odd">
<td><p></p>
<strong>WritePrinter</strong>
(Required)</td>
<td><p>Receives a portion of the print job&#39;s data stream.</p></td>
</tr>
</tbody>
</table>

 

**Note**   The **AddJob**...**ScheduleJob** sequence is an alternative to the **StartDocPrinter**...**EndDocPrinter** sequence.

 

### <a href="" id="ddk-print-job-scheduling-functions-gg"></a>Print Job Scheduling Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p></p>
<strong>EnumJobs</strong>
(Required)</td>
<td><p>Returns a list of scheduled print jobs.</p></td>
</tr>
<tr class="even">
<td><p></p>
<strong>GetJob</strong>
(Required)</td>
<td><p>Returns job parameters.</p></td>
</tr>
<tr class="odd">
<td><p></p>
<strong>SetJob</strong>
(Required)</td>
<td><p>Cancels, pauses, resumes, or restarts a print job, or sets job parameters.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-forms-management-functions-gg"></a>Forms Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>AddForm</strong></p></td>
<td><p>Adds a specified form to the list of those available for a specified printer.</p></td>
</tr>
<tr class="even">
<td><p><strong>DeleteForm</strong></p></td>
<td><p>Removes a specified form from the list of those available for a specified printer.</p></td>
</tr>
<tr class="odd">
<td><p><strong>EnumForms</strong></p></td>
<td><p>Returns a list of forms available for a specified printer.</p></td>
</tr>
<tr class="even">
<td><p><strong>GetForm</strong></p></td>
<td><p>Returns characteristics of a specified form.</p></td>
</tr>
<tr class="odd">
<td><p><strong>SetForm</strong></p></td>
<td><p>Modifies characteristics of a specified form.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-print-processor-management-functions-gg"></a>Print Processor Management Functions

Function
Description
**AddPrintProcessor**

Installs a print processor on the specified server and adds it to the list of those that the print provider can call.

**DeletePrintProcessor**

Deletes a print processor from the list of those that the print provider can call.

**EnumPrintProcessorDataTypes**

Returns a list of the data types supported by the print processors that are callable by the print provider.

**EnumPrintProcessors**

Returns the list of print processors that the print provider can call.

**GetPrintProcessorDirectory**

Returns the directory path in which print processor files must be stored.

 

### <a href="" id="ddk-print-monitor-management-functions-gg"></a>Print Monitor Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>AddMonitor</strong></p></td>
<td><p>Adds a print monitor to the list of those that the print provider can call.</p></td>
</tr>
<tr class="even">
<td><p><strong>DeleteMonitor</strong></p></td>
<td><p>Deletes a print monitor from the list of those that the print provider can call.</p></td>
</tr>
<tr class="odd">
<td><p><strong>EnumMonitors</strong></p></td>
<td><p>Returns the list of print monitors that the print provider can call.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-port-management-functions-gg"></a>Port Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>AddPort</strong></p></td>
<td><p>Adds a printer port to the list of those available, typically by calling the specified port monitor&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff545026" data-raw-source="[&lt;strong&gt;AddPortUI&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545026)"><strong>AddPortUI</strong></a> function.</p></td>
</tr>
<tr class="even">
<td><p><strong>AddPortEx</strong></p></td>
<td><p>Same as <strong>AddPort</strong>, with additional parameters.</p></td>
</tr>
<tr class="odd">
<td><p></p>
<strong>ConfigurePort</strong>
(Required)</td>
<td><p>Configures a printer port, typically by calling the specified port monitor&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff546290" data-raw-source="[&lt;strong&gt;ConfigurePortUI&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546290)"><strong>ConfigurePortUI</strong></a> function.</p></td>
</tr>
<tr class="even">
<td><p></p>
<strong>DeletePort</strong>
(Required)</td>
<td><p>Deletes a printer port from the list of those available, typically by calling the specified port monitor&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff547432" data-raw-source="[&lt;strong&gt;DeletePortUI&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547432)"><strong>DeletePortUI</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td><p></p>
<strong>EnumPorts</strong>
(Required)</td>
<td><p>Returns a list of available printer ports.</p></td>
</tr>
<tr class="even">
<td><p><strong>SetPort</strong></p></td>
<td><p>Sets parameters for a specified printer port.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-registry-management-functions-gg"></a>Registry Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DeletePrinterData</strong></p></td>
<td><p>Deletes the value currently assigned to a specified value name, under the specified printer&#39;s <strong>PrinterDriverData</strong> key.</p></td>
</tr>
<tr class="even">
<td><p><strong>DeletePrinterDataEx</strong></p></td>
<td><p>Same as <strong>DeletePrinterData</strong>, with additional parameters.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DeletePrinterKey</strong></p></td>
<td><p>Deletes a specified key and its subkeys, if they are currently stored in the registry under the specified printer&#39;s <strong>PrinterDriverData</strong> key.</p></td>
</tr>
<tr class="even">
<td><p><strong>EnumPrinterData</strong></p></td>
<td><p>Returns each of the value names and currently assigned values that are stored in the registry under the specified printer&#39;s <strong>PrinterDriverData</strong> key.</p></td>
</tr>
<tr class="odd">
<td><p><strong>EnumPrinterDataEx</strong></p></td>
<td><p>Same as <strong>EnumPrinterData</strong>, with additional parameters.</p></td>
</tr>
<tr class="even">
<td><p><strong>EnumPrinterKey</strong></p></td>
<td><p>Returns a list of subkeys currently contained in the registry under a specified key name.</p></td>
</tr>
<tr class="odd">
<td><p><strong>GetPrinterData</strong></p></td>
<td><p>Returns the value currently assigned to a specified value name, which is stored in the registry under the specified printer&#39;s <strong>PrinterDriverData</strong> key.</p></td>
</tr>
<tr class="even">
<td><p><strong>GetPrinterDataEx</strong></p></td>
<td><p>Same as <strong>GetPrinterData</strong>, with additional parameters.</p></td>
</tr>
<tr class="odd">
<td><p><strong>SetPrinterData</strong></p></td>
<td><p>Stores a specified value name and value in the registry, under the specified printer&#39;s <strong>PrinterDriverData</strong> key.</p></td>
</tr>
<tr class="even">
<td><p><strong>SetPrinterDataEx</strong></p></td>
<td><p>Same as <strong>SetPrinterData</strong>, with additional parameters.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-other-functions-gg"></a>Other Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564255" data-raw-source="[&lt;strong&gt;XcvData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564255)"><strong>XcvData</strong></a></p></td>
<td><p>Provides a communication path between a port monitor UI DLL and a port monitor server DLL.</p></td>
</tr>
</tbody>
</table>

 

 

 




