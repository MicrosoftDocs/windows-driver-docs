---
title: Application Verifier - Stop Codes - Printing
description: Application Verifier - Stop Codes - Printing
keywords:
- verifying drivers (Application Verifier)
- driver verification (Application Verifier)
- Application Verifier
- AppVerif.exe
- user-mode application testing
ms.date: 01/14/2022
---

# Application Verifier - Stop Codes - Printing

The following stop codes are contained in this set of tests.

<h3>Leaked printer handle detected</h3>
<p></p><i>Probable cause</i><p>An open printer handle was detected when the application terminated. Most likely, the creating thread did not call ClosePrinter() to close the printer handle. To troubleshoot this stop, determine the thread that opened the printer handle by using the second parameter of this verifier stop to provide the stack trace. Dump the stack trace using the dps command in the debugger. Find the first non-winspool and non-vfPrint module name that called vfPrint!VfHookOpenPrinter* or vfPrint!VfHookAddPrinter* - this typically is the 4th or the 6th stack frame in the list.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Printer handle being leaked.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Initialization stack trace. Use dps to dump the stack if this parameter is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Thread id of the thread that opened the handle.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;LEAKED_PRINTER_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000A000</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Leaked printer change notification handle detected</h3>
<p></p><i>Probable cause</i><p>A printer change notification handle that was not closed was detected when the application exited. Most likely the thread that opened the handle did not call FindClosePrinterChangeNotification() to close the handle before the thread exited. To troubleshoot this stop, determine the thread that opened the printer change notification handle: The second parameter of this stop provides the stack address. Use the dps command to dump the stack trace. Find the first non-winspool and non-vfPrint module name that called vfPrint!VfHookFindFirstPrinterChangeNotification. This is typically found in the 4th stack frame.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Printer change notification handle being leaked.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Initialization stack trace. Use dps to dump the stack trace if it is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Thread id of the last thread using it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;LEAKED_PRINTER_CHANGE_NOTIFICATION_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000A001</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Leaked PRINTER_NOTIFY_INFO detected</h3>
<p></p><i>Probable cause</i><p>An allocated PRINTER_NOTIFY_INFO object that had not been freed was detected when the program exited. Most likely, it needs to be freed by calling FreePrinterNotifyInfo() before exiting. To troubleshoot this stop: Determine the routine that called winspool to allocate the PRINTER_NOTIFY_INFO object on its behalf by using the second parameter of this verifier stop. Dump the initialization stack trace using the dps command in the debugger. Find the first non-winspool and non-vfPrint module name that called vfPrint!VfHookFindNextPrinterChangeNotification. This routine is typically found in the 3rd stack frame.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;The pointer to the leaked PRINTER_NOTIFY_INFO object.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Initialization stack trace. Use dps to dump the stack trace if it is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;LEAKED_PPRINTER_NOTIFY_INFO</li>
  <li><b>Stop code:</b>&nbsp;0000A002</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Race condition detected while using a printer handle</h3>
<p></p><i>Probable cause</i><p>A printer handle is being used concurrently in multiple threads. Printer handles are not thread safe which means that simultaneous use of a printer handle in multiple threads is not permitted without application-level synchronization to safely coordinate access to the handle. The application should either open a separate printer handle in each thread or provide custom synchronization access to the printer handle by using the Win32 synchronization API. The Win32 synchronization API is described further at http://msdn.microsoft.com/library/en-us/dllproc/base/synchronization_functions.asp.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Printer handle being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Current thread id.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Thread id of the concurrent thread.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Concurrency count.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;MULTITHREADED_ACCESS_TO_PRINTER_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000A003</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Potential multi-threaded access to a printer handle detected</h3>
<p></p><i>Probable cause</i><p>A printer handle was used in a different thread than the thread that created it. Printer handles are not thread safe which means that simultaneous use of a printer handle in multiple threads is not permitted without application-level synchronization to safely coordinate access to the handle. The application should either open a separate printer handle in each thread or provide custom synchronization access to the printer handle by using the Win32 synchronization API. The Win32 synchronization API is described further at http://msdn.microsoft.com/library/en-us/dllproc/base/synchronization_functions.asp.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Printer handle being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Thread id of the initializing thread.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Stack trace of the initialization.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;PRINTER_HANDLE_ACCESSED_NOT_ON_THE_THREAD_THAT_OPENED_IT</li>
  <li><b>Stop code:</b>&nbsp;0000A004</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;no</li>
  <li><b>Create backtrace:</b>&nbsp;no</li>
</ul>
<p></p>
<h3>Attempt to use a closed printer handle</h3>
<p></p><i>Probable cause</i><p>A printer handle was used after it had been closed. To identify the routine that tried to use the closed printer handle, dump the current stack trace by using the 'k' command in the debugger. To dump the stack trace of the routine that closed the handle, use the dps command with the second parameter of the stop.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Printer handle being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Stack trace of the closing. Use dps to dump the stack trace if it is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;PRINTER_HANDLE_ALREADY_CLOSED</li>
  <li><b>Stop code:</b>&nbsp;0000A005</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use an unknown printer handle</h3>
<p></p><i>Probable cause</i><p>An attempt was made to use a printer handle that was not opened by calling OpenPrinterA, OpenPrinterW, OpenPrinter2W (on Windows Vista), AddPrinterA, or AddPrinterW. To see the stack trace of the routine that attempted this action, use the 'k' command in the debugger.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Printer handle being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_PRINTER_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000A006</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use a closed printer change notification handle</h3>
<p></p><i>Probable cause</i><p>A printer change notification handle was used after it had been closed. To see the routine that tried to use the closed printer change notification handle, dump the current stack trace by using the 'k' command in the debugger. To dump the stack trace of the routine that closed the handle, use the dps command with the second parameter of the stop.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Printer change notification handle being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Stack trace of the closing. Use dps to dump the stack trace if it is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;PRINTER_CHANGE_NOTIFICATION_HANDLE_ALREADY_CLOSED</li>
  <li><b>Stop code:</b>&nbsp;0000A007</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use an invalid printer change notification handle</h3>
<p></p><i>Probable cause</i><p>A handle that was not opened with the FindFirstPrinterChangeNotification Win32 API function was passed as a printer change notification handle. To see the stack trace of the routine that attempted this action, use the 'k' command in the debugger.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Printer change notification handle being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;UNKNOWN_PRINTER_CHANGE_NOTIFICATION_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000A008</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use a freed PRINTER_NOTIFY_INFO object</h3>
<p></p><i>Probable cause</i><p>A PRINTER_NOTIFY_INFO object was used after it has been freed. To see the routine that tried to use the freed PRINTER_NOTIFY_INFO object, dump the current stack trace by using the 'k' command in the debugger. To dump the stack trace of the routine that closed the handle, use the dps command with the second parameter of the stop.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of the PRINTER_NOTIFY_INFO being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Stack trace of the closing. Use dps to dump the stack trace if it is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;PRINTER_NOTIFY_INFO_ALREADY_FREED</li>
  <li><b>Stop code:</b>&nbsp;0000A009</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use an invalid PRINTER_NOTIFY_INFO object</h3>
<p></p><i>Probable cause</i><p>The PRINTER_NOTIFY_INFO object was not opened by the FindNextPrinterChangeNotification Win32 API function. To see the stack trace of the routine that attempted this action, use the 'k' command in the debugger.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of the PRINTER_NOTIFY_INFO being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_PRINTER_NOTIFY_INFO</li>
  <li><b>Stop code:</b>&nbsp;0000A00A</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Too many open printer handles</h3>
<p></p><i>Probable cause</i><p>Too many printer handles were opened. There might be a resource leak.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Number of currently open printer handles.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;TOO_MANY_OPENED_PRINTER_HANDLES</li>
  <li><b>Stop code:</b>&nbsp;0000A00B</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>OpenPrinter2W seems to be exported from winspool.drv of an earlier version of Windows</h3>
<p></p><i>Probable cause</i><p>Unknown. Report this error to Microsoft.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;WINSPOOL_OPENPRINTER2W_EXPORTED_ON_PRE_VISTA_OS</li>
  <li><b>Stop code:</b>&nbsp;0000A00C</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Too many open PrintTicket provider handles (HPTPROVIDER)</h3>
<p></p><i>Probable cause</i><p>Too many PrintTicket provider handles were opened by calling PTOpenProvider(Ex). This might be the result of not calling PTCloseProvider when the handle is no longer needed, creating a resource leak.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Number of currently opened PrintTicket provider handles.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;TOO_MANY_OPENED_PRINT_TICKET_PROVIDER_HANDLES</li>
  <li><b>Stop code:</b>&nbsp;0000A00D</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use a closed PrintTicket provider handle (HPTPROVIDER)</h3>
<p></p><i>Probable cause</i><p>A PrintTicket provider handle was used after it had been freed. To see the routine that tried to use the closed PrintTicket provider handler, dump the current stack trace by using the 'k' command in the debugger. To dump the stack trace of the routine that closed the handle, use the dps command with the second parameter of the stop.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;HPTPROVIDER handle being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Stack trace of the closing. Use dps to dump the stack trace if it is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;PRINT_TICKET_PROVIDER_HANDLE_ALREADY_CLOSED</li>
  <li><b>Stop code:</b>&nbsp;0000A00E</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use an unknown PrintTicket provider handle (HPTPROVIDER)</h3>
<p></p><i>Probable cause</i><p>A PrintTicket provider handle was used that was not opened by calling PTOpenProvider or PTOpenProviderEx.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;HPTPROVIDER handle being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;UNKNOWN_PRINT_TICKET_PROVIDER_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000A00F</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Race condition detected while using a PrintTicket provider handle</h3>
<p></p><i>Probable cause</i><p>A PrintTicket provider handle was being used concurrently in multiple threads. This requires application-level of synchronization of the access to the handle. PrintTicket provider handles are not thread safe which means that simultaneous use of a PrintTicket provider handle in multiple threads is not permitted. Instead, the application should either open a separate PrintTicket provider handle in each thread or provide custom synchronization access to the PrintTicket provider handle by using the Win32 synchronization API. The Win32 synchronization API is described further at http://msdn.microsoft.com/library/en-us/dllproc/base/synchronization_functions.asp.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;PrintTicket provider handle being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Current thread id.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Thread id of the concurrent thread.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Concurrency count.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;MULTITHREADED_ACCESS_TO_PRINT_TICKET_PROVIDER_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000A010</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Potential multi-threaded access to a PrintTicket provider handle detected</h3>
<p></p><i>Probable cause</i><p>This is a warning that a PrintTicket provider handle was used in a thread different from the thread that created it. This may require application-level synchronization to safely access the handle. PrintTicket provider handles are not thread safe which means that simultaneous use of a PrintTicket provider handle in multiple threads is not permitted. Instead, the application should either open a separate PrintTicket provider handle in each thread or provide custom synchronization access to the PrintTicket provider handle by using the Win32 synchronization API. The Win32 synchronization API is described further at http://msdn.microsoft.com/library/en-us/dllproc/base/synchronization_functions.asp.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;PrintTicket provider  handle being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Thread id of the initializing thread.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Stack trace of the initialization.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;PRINT_TICKET_PROVIDER_HANDLE_ACCESSED_NOT_ON_THE_THREAD_THAT_OPENED_IT</li>
  <li><b>Stop code:</b>&nbsp;0000A011</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Leaked PrintTicket provider handle detected</h3>
<p></p><i>Probable cause</i><p>An open PrintTicket provider handle was detected when the thread exited. The creating routine might not have called PTCloseProvider() to close it prior to exiting. To troubleshoot this stop, determine the thread that opened the PrintTicket provider handle by using the second parameter of this verifier stop to provide the stack trace. Dump the stack trace using the dps command in the debugger. Find the first non-prntvpt and non-vfPrint module name that called vfPrint!VfPTOpenProvider or vfPrint!VfPTOpenProviderEx - this typically is the 4th or the 6th stack frame in the list.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;PrintTicket provider handle being leaked.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Initialization stack trace. Use dps to dump the stack trace if it is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Thread id of the thread that opened the handle.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;LEAKED_PRINT_TICKET_PROVIDER_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000A012</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Too many open printer change notification handles</h3>
<p></p><i>Probable cause</i><p>Too many printer change notification handles were opened. There might be a resource leak. One common form of resource leaks is where a routine will open a printer change notification handle and not close it before exiting.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Number of currently opened printer change notification handles.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;TOO_MANY_OPENED_PRINTER_CHANGE_NOTIFICATION_HANDLES</li>
  <li><b>Stop code:</b>&nbsp;0000A013</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Too many open PRINTER_NOTIFY_INFO objects</h3>
<p></p><i>Probable cause</i><p>Too many PRINTER_NOTIFY_INFO objects were opened. There might be a resource leak. One common form of resource leaks is where a routine will open a PRINTER_NOTIFY_INFO object and not close it before exiting.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Number of currently opened PRINTER_NOTIFY_INFO objects.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;TOO_MANY_OPENED_PRINTER_NOTIFY_INFO_OBJECTS</li>
  <li><b>Stop code:</b>&nbsp;0000A014</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use an invalid PrintTicket</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when the application calls a PrintTicket method with an invalid PrintTicket.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused when the application called the %lS method with an invalid PrintTicket</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Error messages returned by PTConform. Use du to dump the message if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;PrintTicket XML text. Use du to dump the XML if this parameter is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_APPLICATION_PRINTTICKET</li>
  <li><b>Stop code:</b>&nbsp;0000A015</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use an invalid PrintCapabilities document</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when the application calls a PrintTicket method with an invalid PrintCapabilities document.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused when the application called the %lS method with an invalid PrintCapabilities document</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Error messages returned by PTConform. Use du to dump the message if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;PrintCapabilities XML text. Use du to dump the XML if this parameter is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_APPLICATION_PRINTCAPABILITIES</li>
  <li><b>Stop code:</b>&nbsp;0000A016</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>An invalid NULL argument was passed to a PrintTicket method</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when the application calls a PrintTicket method with an invalid NULL argument.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused when the application called the %lS method with a NULL %lS argument</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;PRINTTICKET_API_INVALID_NULL_ARGUMENT</li>
  <li><b>Stop code:</b>&nbsp;0000A017</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>PTConform encountered an unexpected error</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when the PrintVerifier encounters an unexpected error while attempting to verify that the PrintTicket/PrintCapabilities conforms to the PrintSchema. Report this error to Microsoft because it could be a problem in the PrintVerifier.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;PTCONFORM_UNEXPECTED_ERROR</li>
  <li><b>Stop code:</b>&nbsp;0000A018</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Illegal print API called from DllMain</h3>
<p></p><i>Probable cause</i><p>A call was made to a print API that does not support being called from within DllMain. Many Win32 APIs, not just Win32 print APIs, cannot be called from DllMain. For more information, read the documentation on DllMain in the MSDN library.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; Print API called from DllMain: %s</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;UNSUPPORTED_API_CALL_IN_DLLMAIN</li>
  <li><b>Stop code:</b>&nbsp;0000A019</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Leaked spool file handle detected</h3>
<p></p><i>Probable cause</i><p>An open spool file handle was detected when the application terminated. Most likely, CloseSpoolFileHandle() was not called. To troubleshoot this stop: Determine which thread opened the printer handle. Use dps to dump the stack if Parameter 2 is not NULL. Find the first non-winspool and non-vfPrint module name that called vfPrint!VfHookOpenPrinter* or vfPrint!VfHookAddPrinter*. This routine typically is the 4th or the 6th stack frame in the list.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Handle being leaked.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Initialization stack trace. Use dps to dump the stack if this parameter is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Thread id of the thread that opened the handle.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;LEAKED_SPOOL_FILE_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000A01A</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;no</li>
  <li><b>Create backtrace:</b>&nbsp;no</li>
</ul>
<p></p>
<h3>Attempt to use a closed spool file handle</h3>
<p></p><i>Probable cause</i><p>Spool file handle was used after it had been closed. To troubleshoot this stop: Dump the current stack trace by using the 'k' command in the debugger to identify the routine that tried to use the closed handle. Dump the stack trace of the routine that closed the handle by using the dps command with the second parameter of the stop.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Spool file handle being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Stack trace of the closing. Use dps to dump the stack trace if it is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;SPOOL_FILE_HANDLE_ALREADY_CLOSED</li>
  <li><b>Stop code:</b>&nbsp;0000A01B</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use an unknown spool file handle</h3>
<p></p><i>Probable cause</i><p>An attempt was made to use a spool file handle that was not opened by calling GetSpoolFileHandle or CommitSpoolData. Use the 'k' command in the debugger to see the stack trace of the routine that attempted this action.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Handle being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_SPOOL_FILE_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000A01C</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Too many open spool file handles</h3>
<p></p><i>Probable cause</i><p>Too many spool file handles were opened. There might be a resource leak.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Number of currently opened handles.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;TOO_MANY_OPENED_SPOOL_FILE_HANDLES</li>
  <li><b>Stop code:</b>&nbsp;0000A01D</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A DEVMODE buffer parameter spans across non-readable memory page(s).</h3>
<p></p><i>Probable cause</i><p>This stop can be caused by several conditions: the DEVMODE buffer was already freed, the DEVMODE buffer was constructed incorrectly by assigning the dmSize and dmDriverExtra members a value that is larger than it should be, or a NULL devmode buffer was used where a non-NULL buffer was expected.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;
This verifier stop was caused by a software component that called the print subsystem with a bad DEVMODE buffer. Review the current stack trace and check: the allocation, the construction, and the lifetime of the devmode to identify the bug location.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;The bad DEVMODE buffer</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;The total buffer size as calculated from devmode dmSize and dmDriverExtra fields. Zero if the buffer is completely in non-readable memory.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;DEVMODE_BUFFER_SPANS_IN_NON_READABLE_MEMORY_PAGE</li>
  <li><b>Stop code:</b>&nbsp;0000A01E</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Unloading module with active COM callback.</h3>
<p></p><i>Probable cause</i><p>Positive refcount on COM interface was detected while target module is unloaded. Probably caused by incorrect implementation of DllCanUnloadNow export in module or incorrect reference counting.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;
  This verifier stop was caused by %lS module unload while the system still holds a %lS pointer to it.
  </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;COM interface address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Stack trace where callback was provided. Use dps to dump the stack trace if it is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;MODULE_UNLOAD</li>
  <li><b>Stop code:</b>&nbsp;0000A01F</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Async Notify handle returned by RegisterForPrintAsyncNotifications was not released properly</h3>
<p></p><i>Probable cause</i><p>Handle allocated by RegisterForPrintAsyncNotifications API function had not been released until the program exited. Most likely, it needs to be released by calling UnRegisterForPrintAsyncNotifications() before exiting. To troubleshoot this stop: Determine the routine that called winspool to allocate the handle on its behalf by using the second parameter of this verifier stop. Dump the initialization stack trace using the dps command in the debugger. Find the first non-winspool and non-vfPrint module name that called vfPrint!VfHookRegisterForPrintAsyncNotifications. This routine is typically found in the 3rd stack frame.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Handle value.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Initialization stack trace. Use dps to dump the stack trace if it is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;LEAKED_ASYNC_NOTIFY_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000A020</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use an invalid handle in UnRegisterForPrintAsyncNotifications.</h3>
<p></p><i>Probable cause</i><p>The handle was not opened by the RegisterForPrintAsyncNotifications Win32 API function. To see the stack trace of the routine that attempted this action, use the 'k' command in the debugger.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Handle value.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_ASYNC_NOTIFY_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000A021</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use a closed handle in UnRegisterForPrintAsyncNotifications API function</h3>
<p></p><i>Probable cause</i><p>An async notify handle was used after it has been closed. To see the routine that tried to use the closed handle, dump the current stack trace by using the 'k' command in the debugger. To dump the stack trace of the routine that closed the handle, use the dps command with the second parameter of the stop.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Handle value.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Stack trace of the closing. Use dps to dump the stack trace if it is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;ASYNC_NOTIFY_HANDLE_ALREADY_CLOSED</li>
  <li><b>Stop code:</b>&nbsp;0000A022</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Third-party function reports failure but increases reference count for input interface</h3>
<p></p><i>Probable cause</i><p>A third-party method receives interface pointer as input. When such method returns fail code, interface ref count should remain the same. But in this case reference count was increased.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; The %lS method returns %x error code but increases ref count of %lS parameter.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Called interface pointer. If NULL, called function is static.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Input interface pointer.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;REFCOUNT_PLUS_AFTER_FAIL</li>
  <li><b>Stop code:</b>&nbsp;0000A023</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Windows API function reports failure but increases reference count for input interface</h3>
<p></p><i>Probable cause</i><p>An API method receives interface pointer as input. When such method returns fail code, interface ref count should remain the same. But in this case reference count was increased. Please report this error to Microsoft because it could be a problem in API code.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; The %lS method returns %x error code but increases ref count of %lS parameter.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Called interface pointer. If NULL, called function is static.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Input interface pointer.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;REFCOUNT_PLUS_AFTER_API_FAIL</li>
  <li><b>Stop code:</b>&nbsp;0000A024</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>IPrintAsyncNotifyChannel contract violation by the operating system.</h3>
<p></p><i>Probable cause</i><p>The platform implementation of IPrintAsyncNotifyChannel violated part of the special contract implied or defined by IPrintAsyncNotifyChannel. IPrintAsyncNotifyChannel has special exceptions to AddRef and Release. This requires that the platform calls OnEventNotify and ChannelClosed with the same pointer value as the channel was created with.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%s was called with the wrong interface pointer.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Actual interface pointer.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Expected interface pointer.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;ASYNCCHANNEL_OS_CONTRACT_VIOLATION</li>
  <li><b>Stop code:</b>&nbsp;0000A025</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>IPrintAsyncNotifyChannel contract violation by channel consumer.</h3>
<p></p><i>Probable cause</i><p>On bidirectional channels, calling SendNotification, CloseChannel, or making the final Release on the interface pointer relinquishes 'ownership'. After creating the channel and sending the first notification, you cannot call Release() until your callback's OnEventNotify is invoked. If either you invoke CloseChannel() or get a ChannelClosed notification, then you must not perform the final Release() call.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%s was called, but channel 'ownership' currently belongs to print spooler</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;IPrintAsyncNotifyChannel interface pointer.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;ASYNCCHANNEL_CLIENT_CONTRACT_VIOLATION</li>
  <li><b>Stop code:</b>&nbsp;0000A026</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Race detected during closing of IPrintAsyncNotifyChannel</h3>
<p></p><i>Probable cause</i><p>*** Please report this stop to Microsoft. *** This stop indicates that a notification arrives _during_ the call to CloseChannel. If this condition occurs, it may be imposible for the consumer to correctly release the channel. This stop should not be frequently encountered. It can be prevented by always ensuring a listener is available before a bidirectional channel is created, AND/OR ensuring that no listener can be started before attempting closing a channel that has already sent a notification but not recieved the callback.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;In function %s, a call is already in progress on a different thread.  See help for more info.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;IPrintAsyncNotifyChannel interface pointer.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Thread id of member function called.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Thread id of callback event function.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;ASYNCCHANNEL_CLOSECHANNEL_RACE_DETECTED</li>
  <li><b>Stop code:</b>&nbsp;0000A027</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Calling a print API that makes network calls on a GUI thread. This can lead to unbound in time UI hangs.</h3>
<p></p><i>Probable cause</i><p>A print API was called that makes network calls on a GUI thread. This can lead to unbound in time UI hangs. Typically such APIs need to be called on a worker thread, with no message pumps.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%s was called on a thread that is a GUI thread. This can lead to unbound in time UI hangs.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;HWND of the top-level visible window.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Current thread ID.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;CALLING_NETBOUND_PRINT_API_ON_GUI_THREAD</li>
  <li><b>Stop code:</b>&nbsp;0000A028</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Calling an API that will pop up user interface is Session0.</h3>
<p></p><i>Probable cause</i><p>A call was made to an API that will pop up user interface is Session0.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; The illegal-to-call in Session0 API: %s</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintAPI</li>
  <li><b>Stop ID:</b>&nbsp;UNSUPPORTED_API_CALLED_IN_SESSION_ZERO</li>
  <li><b>Stop code:</b>&nbsp;0000A029</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>First chance access violation detected</h3>
<p></p><i>Probable cause</i><p>This stop is generated when the printer driver tries to access a virtual memory address that is not accessible because it is non-executable, it has been freed or decommitted, or it is reserved but not committed. To debug this stop: $ u parameter2 - to unassemble the suspect code $ .exr parameter3 - to display the exception information; $ .cxr parameter4 - to display the exception context information $ kb - to display the stack trace when the exception was raised.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Code performing invalid access.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Exception record. Use .exr to display it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Context record. Use .cxr to display it.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;FIRST_CHANCE_ACCESS_VIOLATION</li>
  <li><b>Stop code:</b>&nbsp;0000D000</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The thread tried to divide an integer value by an integer divisor of zero</h3>
<p></p><i>Probable cause</i><p>This stop is generated when the printer driver tries to divide an integer value by an integer divisor of zero. To debug this stop: $ u parameter1 - to unassemble the suspect code $ .exr parameter2 - to display the exception information; $ .cxr parameter3 - to display the exception context information $ kb - to display the stack trace when the exception was raised.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Code performing divide by zero operation.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Exception record. Use .exr to display it.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Context record. Use .cxr to display it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;INT_DIVIDE_BY_ZERO</li>
  <li><b>Stop code:</b>&nbsp;0000D001</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The thread tried to read or write misaligned data on hardware that does not provide alignment</h3>
<p></p><i>Probable cause</i><p>This stop is generated when the driver tries to read or write misaligned data on hardware that does not provide alignment. For example, 16-bit values must be aligned on 2-byte boundaries; 32-bit values on 4-byte boundaries, and so on. To debug this stop: $ u parameter1 - to unassemble the culprit code $ .exr parameter2 - to display the exception information; $ .cxr parameter3 - to display the exception context information $ kb - to display the stack trace when the exception was raised.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Code where the data type misalignment occurred.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Exception record. Use .exr to display it.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Context record. Use .cxr to display it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;DATATYPE_MISALIGNMENT</li>
  <li><b>Stop code:</b>&nbsp;0000D002</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Invalid handle exception for current stack trace</h3>
<p></p><i>Probable cause</i><p>This stop is generated when the function on the top of the stack passes an invalid handle to a system routine. Usually the kb command will reveal the value of the handle passed in the call stack. The handle will be one of the parameters of the call. Often it is the first parameter. A null handle value is one example of an invalid handle value. If the handle value appears to be valid, use the !htrace debugger extension to view the history of operations that involved the handle value. Sometimes a handle value that appears to be valid can be invalid if the handle is used after it was closed.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Exception code.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Exception record. Use .exr to display it.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Context record. Use .cxr to display it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000D003</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Core driver is sending a closed printer handle to the plug-in</h3>
<p></p><i>Probable cause</i><p>The core driver is sending the plug-in a printer handle that has already been closed. Report this error to Microsoft because it could be a problem in Microsoft's core printer driver module. To identify the routine that tried to use the closed printer handle, dump the current stack trace by using the 'k' command in the debugger. To dump the stack trace of the routine that closed the handle, use the dps command with the second parameter of the stop.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Printer handle being sent to the plug-in.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Stack trace of the closing routine.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PRINTER_HANDLE_ALREADY_CLOSED</li>
  <li><b>Stop code:</b>&nbsp;0000D004</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Core driver is sending an unknown printer handle to the plug-in</h3>
<p></p><i>Probable cause</i><p>The core driver is sending the plug-in a printer handle that was not opened by calling OpenPrinterA, OpenPrinterW, OpenPrinter2W in Windows Vista, AddPrinterA, or AddPrinterW. Report this error to Microsoft because it could be a problem in Microsoft's core printer driver module.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Printer handle being sent to plug-in.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_PRINTER_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000D005</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The plug-in closed the printer handle</h3>
<p></p><i>Probable cause</i><p>The plug-in closed the printer handle that it received as input from the core driver. This violates the WDK rules for a call from the core driver to the plug-in. Use dps on the second parameter of the stop in order to dump the stack trace of the routine that closed the handle.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the %lS method in the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Printer handle that was closed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Stack trace of the closing. Use dps to dump the stack trace if it is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PLUGIN_CLOSED_PRINTER_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000D006</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Invalid number of supported Print Schema major versions</h3>
<p></p><i>Probable cause</i><p>The PrintTicket provider plug-in returned an invalid number of supported Print Schema major versions. The IPrintOemPrintTicketProvider::GetSupportedVersions method in the plug-in is expected to return at least one supported major version. Because Windows Vista supports only one major version of the Print Schema, the plug-in is expected to return a value of one.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the %lS method in the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Number of supported schema versions that were returned.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PRINTTICKET_PROVIDER_INVALID_NUMBER_OF_SUPPORTED_SCHEMA_VERSIONS</li>
  <li><b>Stop code:</b>&nbsp;0000D007</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Missing supported Print Schema versions</h3>
<p></p><i>Probable cause</i><p>The PrintTicket provider plug-in indicated that it was returning at least one supported Print Schema version but failed to return any. The call to the IPrintOemPrintTicketProvider::GetSupportedVersions method in the plug-in accepts two out pointers as arguments. The ppVersions argument points to an array of integers representing the supported major versions of the Print Schema. The cVersions argument points to the number of elements in the array of integers that is being returned. This verifier stop occurs when the plug-in returns a valid number in cVersions but fails to return anything in the ppVersions array.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the %lS method in the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Number of supported Print Schema versions that were returned.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PRINTTICKET_PROVIDER_MISSING_SUPPORTED_SCHEMA_VERSION</li>
  <li><b>Stop code:</b>&nbsp;0000D008</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Invalid Print Schema major version</h3>
<p></p><i>Probable cause</i><p>The PrintTicket provider plug-in returned an invalid Print Schema major version. The call to the IPrintOemPrintTicketProvider::GetSupportedVersions method in the plug-in is expected to return a value of one (1) because the only major version of the Print Schema supported by Windows Vista is 1.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the %lS method in the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Print Schema version that was returned.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PRINTTICKET_PROVIDER_INVALID_SUPPORTED_SCHEMA_VERSION</li>
  <li><b>Stop code:</b>&nbsp;0000D009</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Invalid OEMPTOPTS value</h3>
<p></p><i>Probable cause</i><p>The PrintTicket provider plug-in returned an invalid OEMPTOPTS value. One of the arguments to the IPrintOemPrintTicketProvider::BindPrinter method in the plug-in is a pointer to an OEMPTOPTS enumeration. The plug-in is expected to set the value of this argument to one of the values supported by Windows Vista. The values supported by Windows Vista are OEMPT_DEFAULT and OEMPT_NOSNAPSHOT. This verifier stop occurs when the plug-in returns a value that is not one of these supported values.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the %lS method in the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;OEMPTOPTS value that was returned.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PRINTTICKET_PROVIDER_INVALID_OEMPTOPTS</li>
  <li><b>Stop code:</b>&nbsp;0000D00A</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Missing Print Schema private namespace</h3>
<p></p><i>Probable cause</i><p>The PrintTicket provider plug-in indicated that it was returning at least one Print Schema private namespace but did not return any. The call to the IPrintOemPrintTicketProvider::BindPrinter method in the plug-in contains two out pointer arguments through which the plug-in can return information about the Print Schema private namespaces that it supports. The ppNamespaces argument points to an array of strings representing the supported Print Schema private namespaces. The cNamespaces argument points to the number of elements in the array of strings that is being returned. This verifier stop occurs when the plug-in returns a valid number in cNamespaces but does not return anything in the ppNamespaces array.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the %lS method in the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Number of expected namespaces.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PRINTTICKET_PROVIDER_MISSING_NAMESPACE</li>
  <li><b>Stop code:</b>&nbsp;0000D00B</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Incorrect reference counting detected in the plug-in</h3>
<p></p><i>Probable cause</i><p>The WDK states that plug-ins must perform accurate reference counting in their implementation of the IUnknown::AddRef and IUnknown::Release methods. The lifetime of the plug-in's interface object depends on accurate reference counting. If the reference counting is inaccurate, it can result in a resource leak or lead to the premature unloading of the plug-in which will cause the driver to fail. This verifier stop occurs when incorrect reference counting is detected in the plug-in.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Expected reference count.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Actual reference count maintained by the plug-in.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PLUGIN_MISMATCHED_REFCOUNT</li>
  <li><b>Stop code:</b>&nbsp;0000D00C</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>pptl is NULL in OEMNextBand</h3>
<p></p><i>Probable cause</i><p>The pptl passed in by the core driver to the OEMNextBand hook in the plug-in was NULL. The core driver should always send a valid pptl to the OEMNextBand hook in the plug-in. Report this error to Microsoft because it could be a problem in Microsoft's core printer driver module.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PPTL_IS_NULL_IN_OEMNEXTBAND</li>
  <li><b>Stop code:</b>&nbsp;0000D00D</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The plug-in returned a NULL PDEV after returning S_OK from the EnablePDEV method</h3>
<p></p><i>Probable cause</i><p>The private PDEV returned by the plug-in was NULL although the return value from the EnablePDEV method was S_OK indicating success. The WDK states that if the EnablePDEV method of a plug-in returns a status of S_OK, it must also allocate an instance of its private PDEV structure, initialize it, and return the address of this structure in the method's pDevOem parameter. This verifier stop occurs when the plug-in does not return a valid private PDEV structure when from its implementation of the EnablePDEV method returns a status of S_OK.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PLUGIN_PRIVATE_PDEV_IS_NULL</li>
  <li><b>Stop code:</b>&nbsp;0000D00E</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The plug-in returned a private DEVMODE that is smaller than the minimum size allowed</h3>
<p></p><i>Probable cause</i><p>The private DEVMODE returned by the plug-in should be at least the size of OEM_DMEXTRAHEADER. The DevMode method of a plug-in must return the size required to store its private DEVMODE members when it is called with the OEMDM_SIZE mode. This value is set the first time the method is called. The DevMode method in the plug-in must set the value of the cbBufSize member in the OEMDMPARAM structure to the number of bytes needed and that value must be greater than or equal to the size of OEM_DMEXTRAHEADER. This verifier stop occurs when the size returned in the cbBufSize member in the OEMDMPARAM structure is less than the size of OEM_DMEXTRAHEADER.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Mode for the current DevMode callback.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Size of the plug-in's private DEVMODE.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Size of OEM_DMEXTRAHEADER.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_PLUGIN_PRIVATE_DEVMODE_SIZE</li>
  <li><b>Stop code:</b>&nbsp;0000D00F</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The plug-in returned a private DEVMODE with a different size than the size returned by the DevMode(OEMDM_SIZE) call</h3>
<p></p><i>Probable cause</i><p>The plug-in should return a private DEVMODE with a size that is the same as that returned by the DevMode call with OEMDM_SIZE mode. The DevMode method of a plug-in must return the size required to store its private DEVMODE members when the DevMode method is called with the OEMDM_SIZE mode. This value is a constant and is set the first time the method is called. It must not change when subsequent calls are made to the plug-in's DevMode method. This verifier stop occurs when the DevMode method in the plug-in returns a value that is different from the value it returned the first time it was called.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Mode for the current Devmode callback.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Size of output plug-in private DEVMODE as specified in pOEMDMOut.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Size of output plug-in private DEVMODE as specified in pOEMDMParam.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Size of plug-in private DEVMODE as specified during the OEMDM_SIZE call.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PLUGIN_PRIVATE_DEVMODE_MISMATCHED_SIZE</li>
  <li><b>Stop code:</b>&nbsp;0000D010</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The plug-in returned an invalid signature from the GetInfo(OEMGI_GETSIGNATURE) call</h3>
<p></p><i>Probable cause</i><p>The plug-in should return a valid, non-zero signature when it is called during the GetInfo call with a mode of OEMGI_GETSIGNATURE. The GetInfo method in the plug-in must return a unique, four-byte identification signature. This verifier stop occurs when the GetInfo(OEMGI_GETSIGNATURE) method in the plug-in returns a zero signature.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_PLUGIN_SIGNATURE</li>
  <li><b>Stop code:</b>&nbsp;0000D011</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The plug-in returned a different signature in the private DEVMODE than it returned from the GetInfo call</h3>
<p></p><i>Probable cause</i><p>The plug-in should return a private DEVMODE that contains the same unique four-byte identification signature that it returned with the OEMGI_GETSIGNATURE call to the GetInfo method in the plug-in. This verifier stop occurs when these two signatures are not identical.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Mode for the current DevMode method call.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Signature as specified in the output plug-in private DEVMODE.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Signature as specified during the GetInfo call.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PLUGIN_PRIVATE_DEVMODE_MISMATCHED_SIGNATURE</li>
  <li><b>Stop code:</b>&nbsp;0000D012</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The EnableDriver method in the plug-in failed.</h3>
<p></p><i>Probable cause</i><p>The EnableDriver method in the plug-in is not expected to fail, although it may fail under exceptional circumstances.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;HRESULT returned by EnableDriver.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Error code set by plug-in.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;ENABLEDRIVER_FAILED</li>
  <li><b>Stop code:</b>&nbsp;0000D013</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The EnableDriver method in the plug-in failed without setting the last error code</h3>
<p></p><i>Probable cause</i><p>The EnableDriver method in the plug-in is not expected to fail although it may fail under exceptional circumstances. If it does fail, it must set the last error code by calling SetLastError. This verifier stop occurs when the EnableDriver method in the plug-in fails without setting the last error.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;HRESULT returned by EnableDriver.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;ENABLEDRIVER_FAILED_WITHOUT_ERROR_CODE</li>
  <li><b>Stop code:</b>&nbsp;0000D014</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The core driver called SetBandSize although the plug-in returned S_OK from DriverDMS</h3>
<p></p><i>Probable cause</i><p>The core driver is not expected to call SetBandSize if the plug-in implements the DriverDMS method and its implementation of the DriverDMS method returns S_OK. Report this error to Microsoft because it could be a problem in Microsoft's core printer driver module.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_SETBANDSIZE_CALL</li>
  <li><b>Stop code:</b>&nbsp;0000D015</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The core driver made the WritePrinter initialization call with invalid parameters</h3>
<p></p><i>Probable cause</i><p>During the initialization call of WritePrinter, the pdevobj and pBuf arguments should be NULL and cbBuf should be zero. One of these conditions wasn't true when the core driver made the initialization call to the WritePrinter method in the plug-in. Report this error to Microsoft because it could be a problem in Microsoft's core printer driver module.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_WRITEPRINTER_INITIALIZATION_CALL</li>
  <li><b>Stop code:</b>&nbsp;0000D016</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The WritePrinter method in the plug-in failed</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when the WritePrinter method in the plug-in failed. This will cause the print job to be aborted.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;HRESULT returned by the WritePrinter method in the plug-in.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;WRITEPRINTER_FAILED</li>
  <li><b>Stop code:</b>&nbsp;0000D017</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Core driver sent an invalid PrintTicket to the plug-in</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when a PrintTicket document that was sent from the core driver to the plug-in did not conform to the PrintSchema. Since the core driver parses the driver's GPD/PPD to construct the PrintTicket that is sent to the plug-in, this stop is usually indicative of a bug in the driver's GPD/PPD.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused when the core driver called the plug-in's %lS method</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Error messages returned by PTConform. Use du to dump the message if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;PrintTicket XML text. Use du to dump the XML if this parameter is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_COREDRIVER_PRINTTICKET</li>
  <li><b>Stop code:</b>&nbsp;0000D018</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The plug-in returned an invalid PrintTicket to the core driver</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when a PrintTicket document that was returned to the core driver from the plug-in did not conform to the PrintSchema.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the %lS method in the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Error messages returned by PTConform. Use du to dump the message if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;PrintTicket XML text. Use du to dump the XML if this parameter is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_PLUGIN_PRINTTICKET</li>
  <li><b>Stop code:</b>&nbsp;0000D019</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Core driver sent an invalid PrintCapabilities document to the plug-in</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when a PrintCapabilities document that was sent from the core driver to the plug-in did not conform to the PrintSchema. Report this error to Microsoft because it could be a problem in Microsoft's core printer driver module.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused when the core driver called the plug-in's %lS method</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Error messages returned by PTConform. Use du to dump the message if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;PrintCapabilities XML text. Use du to dump the XML if this parameter is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_COREDRIVER_PRINTCAPABILITIES</li>
  <li><b>Stop code:</b>&nbsp;0000D01A</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The plug-in returned an invalid PrintCapabilities document to the core driver</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when a PrintCapabilities document that was returned to the core driver from the plug-in did not conform to the PrintSchema.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the %lS method in the plug-in module at %lS</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Error messages returned by PTConform. Use du to dump the message if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;PrintCapabilities XML text. Use du to dump the XML if this parameter is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_PLUGIN_PRINTCAPABILITIES</li>
  <li><b>Stop code:</b>&nbsp;0000D01B</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>PTConform encountered an unexpected error</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when the PrintVerifier encounters an unexpected error while attempting to verify that the PrintTicket/PrintCapabilities conforms to the PrintSchema. Report this error to Microsoft because it could be a problem in the PrintVerifier.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PTCONFORM_UNEXPECTED_ERROR</li>
  <li><b>Stop code:</b>&nbsp;0000D01C</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Print filter calls pipeline manager interface with invalid argument value</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when a print filter calls a pipeline method with an incorrect argument value. Use the stack trace to find the name of the print filter DLL.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; %s method : Invalid value for %s argument.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Print Filter GUID. Use dd to dump it if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Argument value.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;FILTER_INVALID_ARGUMENT</li>
  <li><b>Stop code:</b>&nbsp;0000D01D</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Print filter call to IPrintPipelinePropertyBag overwrites or removes common property</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when a print filter changes or deletes a common property from print pipeline property bag.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; %s method : Overwriting common property %s</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Print Filter GUID. Use dd to dump it if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Property value (variant).</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;FILTER_PROPERTY_BAG_INVALID_CHANGE</li>
  <li><b>Stop code:</b>&nbsp;0000D01E</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Print filter calls pipeline manager interface out of order</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when a print filter calls the pipeline manager interface methods in an unexpected sequence.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; Incorrect call order for %s interface : %s</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Print Filter GUID. Use dd to dump it if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;FILTER_INVALID_CALL_ORDER</li>
  <li><b>Stop code:</b>&nbsp;0000D01F</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Print filter has mismatch of AddRef/Release calls to pipeline manager interface</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when a print filter incorrectly manages the reference count of the pipeline manager interface.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; Interface %s ref count is %d, expected %s.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Print Filter GUID. Use dd to dump it if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;FILTER_REFCOUNT_MISMATCH</li>
  <li><b>Stop code:</b>&nbsp;0000D020</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Print filter call to pipeline manager interface method is not expected</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when a print filter makes an unnecessary or unexpected call to a pipeline interface method. For example, if the print filter makes a second call to IPrintWriteStream::Close.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; Interface method %s : %s</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Print Filter GUID. Use dd to dump it if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;FILTER_UNEXPECTED_CALL</li>
  <li><b>Stop code:</b>&nbsp;0000D021</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Pipeline manager calls print filter interface methods out of order</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when the pipeline manager incorrectly calls the methods of the print filter interface. Report this error to Microsoft because it could be a problem in the print filter pipeline service.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; Invalid call order to Print Filter : %s</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Print Filter GUID. Use dd to dump it if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PIPELINE_INVALID_CALL_ORDER</li>
  <li><b>Stop code:</b>&nbsp;0000D022</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Pipeline manager calls print filter interface method with invalid argument value</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when the pipeline manager calls a print filter interface with an invalid argument value. Report this error to Microsoft because it could be a problem in the print filter pipeline service.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; Method %s: %s</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Print Filter GUID. Use dd to dump it if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Argument value.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PIPELINE_INVALID_INPUT_ARGUMENT</li>
  <li><b>Stop code:</b>&nbsp;0000D023</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Pipeline manager returns invalid value to print filter</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when the pipeline manager returns an invalid value to the print filter. Report this error to Microsoft because it could be a problem in the print filter pipeline service.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; Method %s: %s</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Print Filter GUID. Use dd to dump it if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Value.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;PIPELINE_INVALID_OUTPUT_ARGUMENT</li>
  <li><b>Stop code:</b>&nbsp;0000D024</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A call to a printer driver changed the security context.</h3>
<p></p><i>Probable cause</i><p>This stop usually occurs when a print driver calls either RevertToSelf() or RevertToPrinterSelf() but did not change the security context back to impersonating the user by calling ImpersonatePrinterClient(). This is not allowed and print spooler behavior is undefined after this happens. This can also create a security vulnerability and allow a remote authenticated elevation of privilege type of attack.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by the '%lS' method in the plug-in module at '%lS'</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Account name at driver entry. Type 'du address' to dump it if not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Account name at driver exit. Type 'du address' to dump it if not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Security token at driver entry</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Security token at driver exit</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;SECURITY_CONTEXT_CHANGED_BY_A_PRINT_DRIVER_CALL</li>
  <li><b>Stop code:</b>&nbsp;0000D025</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Print filter sent an invalid PrintTicket to pipeline manager</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when an IPrintTicketPart part was sent to a SetPrintTicket method but its content does not conform to the PrintSchema.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was in %lS method. Use GUID to identify Print filter.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Print Filter GUID. Use dd to dump it if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Error messages returned by PTConform. Use du to dump the message if this parameter is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;PrintTicket XML text. Use du to dump the XML if this parameter is not NULL.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_FILTER_PRINTTICKET</li>
  <li><b>Stop code:</b>&nbsp;0000D026</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Print filter received an invalid PrintTicket from pipeline manager</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when an IPrintTicketPart part was received from Print filter via GetPrintTicket method but its content does not conform to the PrintSchema.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was in %lS method. Use GUID to identify Print filter.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Print Filter GUID. Use dd to dump it if this parameter is not NULL.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Error messages returned by PTConform. Use du to dump the message if this parameter is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;PrintTicket XML text. Use du to dump the XML if this parameter is not NULL.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_PIPELINE_PRINTTICKET</li>
  <li><b>Stop code:</b>&nbsp;0000D027</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Unloading print driver DLL with active COM callback.</h3>
<p></p><i>Probable cause</i><p>Positive reference count on COM interface was detected while target module is unloaded. Probably caused by incorrect implementation of DllCanUnloadNow export in module or incorrect reference counting.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;
  This verifier stop was caused by %lS module unload while the system still holds a %lS pointer to it.
  </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;COM interface address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Stack trace where callback was provided. Use dps to dump the stack trace if it is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;DLL_PREMATURE_UNLOAD</li>
  <li><b>Stop code:</b>&nbsp;0000D028</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use a released COM interface</h3>
<p></p><i>Probable cause</i><p>COM interface was used after being released. To troubleshoot this stop: - Dump the current stack trace by using the 'k' command in the debugger to identify the routine that tried to use the released interface. - Dump the stack trace of the routine that released it by using the dps command with the second parameter of the stop if available.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;This verifier stop was caused by %lS interface being used after release.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;COM interface address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Stack trace of the Release call when reference count went to zero. Use dps to dump the stack trace if it is not NULL.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;COM_INTERFACE_ALREADY_RELEASED</li>
  <li><b>Stop code:</b>&nbsp;0000D029</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A print driver called ExitThread</h3>
<p></p><i>Probable cause</i><p>A print driver module called ExitThread. When a print driver module calls ExitThread, the thread is exited before any destructors can be called or any other automatic cleanup can be performed. This can lead to undefined behavior. Therefore, print drivers should always return from their thread function. To troubleshoot this stop: Dump the current stack trace by using the 'k' command in the debugger to identify the routine that invoked ExitThread.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;DRIVER_CALLED_EXITTHREAD</li>
  <li><b>Stop code:</b>&nbsp;0000D02A</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A print driver called TerminateThread</h3>
<p></p><i>Probable cause</i><p>A print driver module called TerminateThread. TerminateThread is used to cause a thread to exit. When this occurs, the target thread has no chance to execute any user-mode code. DLLs attached to the thread are not notified that the thread is terminating. The system frees the thread's initial stack. TerminateThread is a dangerous function that should only be used in the most extreme cases. For example, TerminateThread can result in the following problems: - If the target thread owns a critical section, the critical section will not be released. - If the target thread is allocating memory from the heap, the heap lock will not be released. - If the target thread is executing certain kernel32 calls when it is terminated, the kernel32 state for the thread's process could be inconsistent. - If the target thread is manipulating the global state of a shared DLL, the state of the DLL could be destroyed, affecting other users of the DLL. To troubleshoot this stop: Dump the current stack trace by using the 'k' command in the debugger to identify the module and routine that invoked TerminateThread.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;DRIVER_CALLED_TERMINATETHREAD</li>
  <li><b>Stop code:</b>&nbsp;0000D02B</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Print filter changed the COM apartment type for the current thread.</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when a print filter changes the COM apartment type in one of it's methods (InitializeFilter, StartOperation, or ShutdownOperation). Use the 'ln poi(&lt;Param1&gt;)' command in the debugger to identify the name of the print filter DLL.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;
  This verifier stop was caused by a print filter's %lS method changing the COM apartment type from %lS(%d) to %lS(%d).
  </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Filter interface pointer.  Use 'ln poi(&lt;Param1&gt;)' to find the filter.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Expected apartment type</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Actual apartment type</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;COM_APARTMENT_TYPE_CHANGED</li>
  <li><b>Stop code:</b>&nbsp;0000D02C</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>COM is not initialized for the current thread after call to print filter method.</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when a print filter has unbalanced CoInitialize[Ex] and CoUninitialize calls. This could be due to CoInitialize[Ex] unexpectedly returning failure, such as when the request apartment type does not match the thread's current type. Use the 'ln poi(&lt;Param1&gt;)' command in the debugger to identify the name of the print filter DLL.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;
  This verifier stop was likely caused by a print filter's %lS method calling COM's CoUninitialize without a corresponding successful CoInitialize[Ex].
  </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Filter interface pointer.  Use 'ln poi(&lt;value&gt;)' to find the filter.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;COM_NOT_INITIALIZED</li>
  <li><b>Stop code:</b>&nbsp;0000D02D</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Print driver has mismatch of AddRef/Release calls of PT/PC XML Document.</h3>
<p></p><i>Probable cause</i><p>This verifier stop occurs when a print driver incorrectly manages the reference count of an XML Document (eg, PrintTicket or PrintCapabilities). The reference count was not expected to be changed by the method call and will likely lead to a leak and/or an orphaned critical section in the XML DOC.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; After %lS method call, %lS XML Document ref count is %d, expected %d.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Name of offending method call.  If not NULL, Use 'du' to display this.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Type of XML Document.  If not NULL, Use 'du' to display this.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Current reference count.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Expected reference count.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;XML_DOM_REFCOUNT_CHANGED</li>
  <li><b>Stop code:</b>&nbsp;0000D02E</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>FatalExit was called</h3>
<p></p><i>Probable cause</i><p>FatalExit was called. This is a form of abnormal termination which may cause other verifier stops to be reported (eg. leaks), but for which no corrective action is possible (ie, the stops are unreliable and noisy). To troubleshoot this stop: Dump the current stack trace by using the 'k' command in the debugger to identify the module and routine that invoked FatalExit.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Exit code.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;PrintDriver</li>
  <li><b>Stop ID:</b>&nbsp;FATALEXIT</li>
  <li><b>Stop code:</b>&nbsp;0000D02F</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>



 ## See Also

[Application Verifier - Stop Codes and Definitions](application-verifier-stop-codes-and-definitions.md)

[Application Verifier - Overview](application-verifier.md)

[Application Verifier - Features](application-verifier-features.md)

[Application Verifier - Testing Applications](application-verifier-testing-applications.md)
 
[Application Verifier - Tests within Application Verifier](application-verifier-tests-within-application-verifier.md)

[Application Verifier - Debugging Application Verifier Stops](application-verifier-debugging-application-verifier-stops.md)
  
[Application Verifier - Frequently Asked Questions](application-verifier-faqs.md)


 





