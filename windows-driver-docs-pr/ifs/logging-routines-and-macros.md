---
title: Logging Routines and Macros
description: Logging Routines and Macros
ms.assetid: 343605bc-7992-4e9c-a9af-f57bb958a38b
keywords: ["RDBSS WDK file systems , logging", "Redirected Drive Buffering Subsystem WDK file systems , logging", "logging WDK RDBSS", "RDBSSLOG macro"]
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
<td align="left"><p>[<strong>RxLogEventDirect</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554515)</p></td>
<td align="left"><p>This routine is called to log an error to the I/O error log.</p>
<p>It is recommended that the <strong>RxLogFailure</strong> or <strong>RxLogEvent</strong> macro be used instead of calling this routine directly.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxLogEventWithAnnotation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554519)</p></td>
<td align="left"><p>This routine allocates an I/O error log record, fills in the log record, and writes this record to the I/O error log.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxLogEventWithBufferDirect</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554524)</p></td>
<td align="left"><p>This routine allocates an I/O error log record, fills in the log record, and writes this record to the I/O error log. This routine encodes the line number and status into the raw data buffer stored in the I/O error log record.</p>
<p>It is recommended that the <strong>RxLogFailureWithBuffer</strong> macro be used instead of calling this routine directly.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>_RxLog</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557368)</p></td>
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
<td align="left"><p>On checked builds, this macro calls the [<strong>_RxLog</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557368) routine.</p>
<p>On retail builds, this macro does nothing.</p>
<p>Note that the arguments to <strong>RxLog</strong> must be enclosed with an additional pair of parenthesis to enable translation into a null call when logging should be turned off.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxLogEvent</strong> (<em>_DeviceObject</em>, <em>_OriginatorId</em>, <em>_EventId</em>, <em>_Status</em>)</p></td>
<td align="left"><p>This macro calls the [<strong>RxLogEventDirect</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554515) routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RxLogFailure</strong> (<em>_DeviceObject</em>, <em>_OriginatorId</em>, <em>_EventId</em>, <em>_Status</em>)</p></td>
<td align="left"><p>This macro calls the [<strong>RxLogEventDirect</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554515) routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxLogFailureWithBuffer</strong> (<em>_DeviceObject</em>, <em>_OriginatorId</em>, <em>_EventId</em>, <em>_Status</em>, <em>_Buffer</em>, <em>_Length</em>)</p></td>
<td align="left"><p>This macro calls the [<strong>RxLogEventWithBufferDirect</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554524) routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RxLogRetail</strong>(<em>Args</em>)</p></td>
<td align="left"><p>On checked builds, this macro calls the [<strong>_RxLog</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557368) routine.</p>
<p>On retail builds, this macro does nothing.</p>
<p>Note that the arguments to <strong>RxLogRetail</strong> must be enclosed with an additional pair of parenthesis to enable translation into a null call when logging should be turned off.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Logging%20Routines%20and%20Macros%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




