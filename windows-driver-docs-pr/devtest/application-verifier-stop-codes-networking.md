---
title: Application Verifier - Stop Codes - Networking
description: Application Verifier - Stop Codes - Networking
keywords:
- verifying drivers (Application Verifier)
- driver verification (Application Verifier)
- Application Verifier
- AppVerif.exe
- user-mode application testing
ms.date: 01/13/2022
---

# Application Verifier - Stop Codes - Networking

The following stop codes are contained in this set of tests.

<h3>Illegal networking API called from DllMain</h3>
<p></p><i>Probable cause</i><p>A call was made to a networking API that does not support being called from within DllMain. Many Win32 APIs, not just Win32 networking APIs, cannot be called from DllMain. For more information, read the documentation on DllMain in the MSDN library. To identify the routine that made the call, dump the current stack trace by using the 'k' command in the debugger.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Networking function being called from DllMain</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Name of Dll making invalid call if not NULL</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;UNSUPPORTED_API_CALL_IN_DLLMAIN</li>
  <li><b>Stop code:</b>&nbsp;0000e000</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use a closed SOCKET</h3>
<p></p><i>Probable cause</i><p>A SOCKET was used after it had been closed. To identify the routine that tried to use the closed SOCKET, dump the current stack trace by using the 'k' command in the debugger. To dump the stack trace of the routine that closed the SOCKET, use the dps command with the second parameter of the stop.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SOCKET being accessed</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Stack trace of the function that closed the SOCKET. Use dps to dump the stack trace if not NULL</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;WSA_SOCKET_ALREADY_CLOSED</li>
  <li><b>Stop code:</b>&nbsp;0000e001</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use an unknown SOCKET</h3>
<p></p><i>Probable cause</i><p>An attempt was made to use an unknown value for a SOCKET that was not created by a call to Winsock. To see the stack trace of the routine that attempted this action, use the 'k' command in the debugger.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SOCKET being accessed</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;WSA_INVALID_SOCKET_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000e002</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Leaked SOCKET handle detected</h3>
<p></p><i>Probable cause</i><p>An open SOCKET from a Winsock base service provider was detected to have been leaked from a DLL being unloaded. To troubleshoot this stop, dump the stack trace of the thread that opened the SOCKET handle by using the dps command in the debugger on the second parameter of this verifier stop.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SOCKET handle being leaked</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Initialization stack trace. Use dps to dump the stack if not NULL</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Thread ID of the thread that opened the handle</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;WSA_LEAKED_SOCKET_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000e003</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use a closed SOCKET</h3>
<p></p><i>Probable cause</i><p>A SOCKET from a Winsock base provider was used after it had been closed. This generally indicates a fault in a layered service provider (an LSP - a DLL between the application and Winsock). To identify the routine that tried to use the closed SOCKET, dump the current stack trace by using the 'k' command in the debugger. To dump the stack trace of the routine that closed the SOCKET, use the dps command with the second parameter of the stop.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SOCKET being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Stack trace of the function that closed the SOCKET. Use dps to dump the stack trace if not NULL</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;WSP_SOCKET_ALREADY_CLOSED</li>
  <li><b>Stop code:</b>&nbsp;0000e004</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to use an unknown SOCKET</h3>
<p></p><i>Probable cause</i><p>An unknown SOCKET handle value was used by a Winsock layered service provider (LSP). This is generally pointing to a fault to a specific LSP layered between the application and Winsock. To identify the routine that tried to use the unknown SOCKET, dump the current stack trace by using the 'k' command in the debugger.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SOCKET being accessed</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;WSP_INVALID_SOCKET_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000e005</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Leaked SOCKET handle detected</h3>
<p></p><i>Probable cause</i><p>An open SOCKET from a Winsock base service provider was detected to have been leaked. This is generally pointing to a fault to a specific LSP layered between the application and Winsock. To troubleshoot this stop, dump the stack trace of the thread that opened the SOCKET handle by using the dps command in the debugger on the second parameter of this verifier stop.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SOCKET handle being leaked</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Initialization stack trace. Use dps to dump the stack if not NULL</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Thread ID of the thread that opened the handle</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;WSP_LEAKED_SOCKET_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0000e006</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A Winsock API was called before a successful WSAStartup() or after a balancing successful WSACleanup() call was made</h3>
<p></p><i>Probable cause</i><p>A call was made to a networking API before a successful WSAStarup() or after a balancing successful WSACleanup() call. WSAStartup is required to provide a reference count by any component using Winsock to guarantee initialization for Winsock API usage. An unbalance WSAStartup/WSACleanup call pattern by a component can lead to undefined behavior as this can cause the Winsock layer to unload libraries and release resources while still being used.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Last sucessfull WSAStartup call by this caller. Use dps to dump the stack if not NULL</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Last sucessfull WSACleanup call by this caller. Use dps to dump the stack if not NULL</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Last successful WSAStartup call in this process. Use dps to dump the stack if not NULL</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Last sucessfull WSACleanup call in this process. Use dps to dump the stack if not NULL</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;WSA_NOT_INITIALIZED</li>
  <li><b>Stop code:</b>&nbsp;0000e007</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Networking API called before a successful WSPStartup() or after a balancing successful WSPCleanup() call made</h3>
<p></p><i>Probable cause</i><p>A call was made to a Winsock service provider API before a successful WSPStarup() or after a balancing successful WSPCleanup() call. This is generally pointing to a fault to a specific Winsock layered service provider (LSP) layered between the application and Winsock. WSPStartup is required to provide a reference count by any LSP using Winsock to guarantee initialization for Winsock service provider API usage. An unbalance WSPStartup/WSPCleanup call pattern by an LSP can lead to undefined behavior as this can cause the Winsock layer to unload libraries and release resources while still being used.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Last sucessfull WSPStartup call by this caller. Use dps to dump the stack if not NULL</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Last sucessfull WSPCleanup call by this caller. Use dps to dump the stack if not NULL</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Last successful WSPStartup call in this process. Use dps to dump the stack if not NULL</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Last sucessfull WSPCleanup call in this process. Use dps to dump the stack if not NULL</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;WSP_NOT_INITIALIZED</li>
  <li><b>Stop code:</b>&nbsp;0000e008</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A Winsock name service provider API was called before a successful NSPStartup() or after a balancing successful NSPCleanup() call was made</h3>
<p></p><i>Probable cause</i><p>A call was made to a Winsock name service provider API before a successful NSPStarup() or after a balancing successful NSPCleanup() call. This is generally pointing to a fault to a specific Winsock name service provider (NSP) layered between the application and Winsock. NSPStartup is required to provide a reference count by any NSP using Winsock to guarantee initialization for Winsock name service provider API usage. An unbalance NSPStartup/NSPCleanup call pattern by an NSP can lead to undefined behavior as this can cause the Winsock layer to unload libraries and release resources while still being used.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Last sucessfull NSPStartup call by this caller. Use dps to dump the stack if not NULL</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Last sucessfull NSPCleanup call by this caller. Use dps to dump the stack if not NULL</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Last sucessfull NSPStartup call in this process. Use dps to dump the stack if not NULL</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Last sucessfull NSPCleanup call in this process. Use dps to dump the stack if not NULL</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;NSP_NOT_INITIALIZED</li>
  <li><b>Stop code:</b>&nbsp;0000e009</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Use of an invalid Winsock extension function pointer detected</h3>
<p></p><i>Probable cause</i><p>Microsoft Winsock Extension functions are callable only by querying Winsock for the function pointer value at runtime. The Winsock runtime has been unloaded since this function pointer was returned. The caller likely kept a copy of the function pointer after calling WSACleanup and tried to reuse it.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Last call to get a Winsock function pointer. Use dps to dump the stack if not NULL</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Last call that unloaded mswsock, invalidating the function pointers. Use dps to dump the stack if not NULL</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_FUNCTION_POINTER_DETECTED</li>
  <li><b>Stop code:</b>&nbsp;0000e00A</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>WSACleanup aborted and closed existing SOCKET handles underneath the code that owned those SOCKETs</h3>
<p></p><i>Probable cause</i><p>WSACleanup was called decrementing the Winsock reference count to 0 while opened SOCKET handles existed in this process. Winsock closes any opened SOCKET handles when the reference count reaches zero. This is typically a bug in whomever is decrementing the Winsock reference count via WSACleanup too often (unbalanced with WSAStartup), or the SOCKET handles were no longer correctly being tracked by the caller (leaked). Type k in the debugger to show who is currently calling WSACleanup taking the Winsock reference count to 0.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Number of sockets that were outstanding</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;WSA_SOCKETS_ABORTED</li>
  <li><b>Stop code:</b>&nbsp;0000e00B</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>WSPCleanup aborted and closed existing service provider SOCKET handles underneath the code that owned those SOCKETs</h3>
<p></p><i>Probable cause</i><p>WSPCleanup was called by a layered service provider (LSP) decrementing the Winsock reference count to 0 while opened SOCKET handles existed in this process. Winsock closes any opened SOCKET handles when the reference count reaches zero. This is typically a bug in the LSP decrementing the Winsock reference count via WSPCleanup too often (unbalanced with WSPStartup), or the SOCKET handles were no longer correctly being tracked by the caller (leaked). Type k in the debugger to show who is currently calling WSPCleanup taking the Winsock reference count to 0.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Number of service provider sockets that were outstanding</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;WSP_SOCKETS_ABORTED</li>
  <li><b>Stop code:</b>&nbsp;0000e00C</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The immediate return value, or GetLastError, is invalid for the current Winsock call. This generally points to a fault in a Service Provider</h3>
<p></p><i>Probable cause</i><p>The value that is being returned, or the current value in GetLastError, is not following the specified Winsock 2 specification. This generally points to a bug in a layered service provider (LSP) - a DLL layered between the application and Winsock. In these cases, an LSP has broken the Winsock API contract and is returning a bogus value to the caller. Use ln on parameter 3 in the debugger to find the function in the DLL which returned the incorrect return code. View parameters 1 and 2 to see what the incorrect value was with respect to the Winsock call made. View parameter 4 if the call was to any Winsock send or recv function to see the actual number of bytes requested to be sent or received. It is invalid for the returned number of bytes to be greater than the number of bytes requested to be sent or received.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Return Value</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;GetLastError</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Function pointer to the next service provider. Use ln to see who just returned this value</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;For sending/receiving data, the actual number of bytes posted to the API</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;WSA_RETURN_INVALID</li>
  <li><b>Stop code:</b>&nbsp;0000e00D</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The return value, or lpError, is invalid for the current Winsock call. This generally points to a fault in a Base Service Provider or in the networking stack</h3>
<p></p><i>Probable cause</i><p>The value that is being returned, or the current value in lpError, is not following the specified Winsock 2 specification. This generally points to a bug in a loaded Base Service Provider (generally mswsock.dll), or the networking stack. Use ln on parameter 3 in the debugger to find the function in the DLL which returned the incorrect return code. View parameters 1 and 2 to see what the incorrect value was with respect to the Winsock call made. View parameter 4 if the call was to any Winsock send or recv function to see the actual number of bytes requested to be sent or received. It is invalid for the returned number of bytes to be greater than the number of bytes requested to be sent or received.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Return Value</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;GetLastError</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Function pointer to the next service provider. Use ln to see who just returned this value</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;For sending/receiving data, the actual number of bytes posted to the API</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Networking</li>
  <li><b>Stop ID:</b>&nbsp;WSP_RETURN_INVALID</li>
  <li><b>Stop code:</b>&nbsp;0000e00E</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
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


 





