---
title: Logging Routines and Macros
description: Logging Routines and Macros
ms.assetid: 343605bc-7992-4e9c-a9af-f57bb958a38b
keywords:
- RDBSS WDK file systems , logging
- Redirected Drive Buffering Subsystem WDK file systems , logging
- logging WDK RDBSS
- RDBSSLOG macro
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Logging Routines and Macros


## <span id="ddk_logging_functions_and_macros_if"></span><span id="DDK_LOGGING_FUNCTIONS_AND_MACROS_IF"></span>


RDBSS provides a number of routines for logging. These logging facilities are always present. When the RDBSSLOG macro is defined, a generation of the logging calls on checked builds is enabled. When NO\_RDBSSLOG is set, the logging calls are disabled.

The logging routines create log records that are stored in a circular buffer. Each record is bounded on either side by a record descriptor. This record descriptor is four bytes long.

The following table includes logging routines.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554515" data-raw-source="[&lt;strong&gt;RxLogEventDirect&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554515)"><strong>RxLogEventDirect</strong></a></p></td>
<td align="left"><p>This routine is called to log an error to the I/O error log.</p>
<p>It is recommended that the <strong>RxLogFailure</strong> or <strong>RxLogEvent</strong> macro be used instead of calling this routine directly.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554519" data-raw-source="[&lt;strong&gt;RxLogEventWithAnnotation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554519)"><strong>RxLogEventWithAnnotation</strong></a></p></td>
<td align="left"><p>This routine allocates an I/O error log record, fills in the log record, and writes this record to the I/O error log.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554524" data-raw-source="[&lt;strong&gt;RxLogEventWithBufferDirect&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554524)"><strong>RxLogEventWithBufferDirect</strong></a></p></td>
<td align="left"><p>This routine allocates an I/O error log record, fills in the log record, and writes this record to the I/O error log. This routine encodes the line number and status into the raw data buffer stored in the I/O error log record.</p>
<p>It is recommended that the <strong>RxLogFailureWithBuffer</strong> macro be used instead of calling this routine directly.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557368" data-raw-source="[&lt;strong&gt;_RxLog&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557368)"><strong>_RxLog</strong></a></p></td>
<td align="left"><p>This routine takes a format string and variable number of parameters and formats an output string for recording as an I/O error log entry if logging is enabled.</p>
<p>It is recommended that the <strong>RxLog</strong> macro be used instead of calling this routine directly.</p>
<p>This routine is only available on checked builds of RDBSS on Windows Server 2003, Windows XP, and Windows 2000.</p></td>
</tr>
</tbody>
</table>

 

The following macros are defined in the rxlog.h and rxprocs.h header files that call the routines listed in the previous table. These macros are normally used instead of calling these routines directly.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Macro</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>RxLog</strong>(<em>Args</em>)</p></td>
<td align="left"><p>On checked builds, this macro calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557368" data-raw-source="[&lt;strong&gt;_RxLog&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557368)"><strong>_RxLog</strong></a> routine.</p>
<p>On retail builds, this macro does nothing.</p>
<p>Note that the arguments to <strong>RxLog</strong> must be enclosed with an additional pair of parenthesis to enable translation into a null call when logging should be turned off.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxLogEvent</strong> (<em>_DeviceObject</em>, <em>_OriginatorId</em>, <em>_EventId</em>, <em>_Status</em>)</p></td>
<td align="left"><p>This macro calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554515" data-raw-source="[&lt;strong&gt;RxLogEventDirect&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554515)"><strong>RxLogEventDirect</strong></a> routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RxLogFailure</strong> (<em>_DeviceObject</em>, <em>_OriginatorId</em>, <em>_EventId</em>, <em>_Status</em>)</p></td>
<td align="left"><p>This macro calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554515" data-raw-source="[&lt;strong&gt;RxLogEventDirect&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554515)"><strong>RxLogEventDirect</strong></a> routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxLogFailureWithBuffer</strong> (<em>_DeviceObject</em>, <em>_OriginatorId</em>, <em>_EventId</em>, <em>_Status</em>, <em>_Buffer</em>, <em>_Length</em>)</p></td>
<td align="left"><p>This macro calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554524" data-raw-source="[&lt;strong&gt;RxLogEventWithBufferDirect&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554524)"><strong>RxLogEventWithBufferDirect</strong></a> routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RxLogRetail</strong>(<em>Args</em>)</p></td>
<td align="left"><p>On checked builds, this macro calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557368" data-raw-source="[&lt;strong&gt;_RxLog&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557368)"><strong>_RxLog</strong></a> routine.</p>
<p>On retail builds, this macro does nothing.</p>
<p>Note that the arguments to <strong>RxLogRetail</strong> must be enclosed with an additional pair of parenthesis to enable translation into a null call when logging should be turned off.</p></td>
</tr>
</tbody>
</table>

 

 

 




