---
title: Application Verifier - Stop Codes - Hangs
description: Application Verifier - Stop Codes - Hangs
keywords:
- verifying drivers (Application Verifier)
- driver verification (Application Verifier)
- Application Verifier
- AppVerif.exe
- user-mode application testing
ms.date: 01/21/2022
---

# Application Verifier - Stop Codes - Hangs

The Hangs tests for the use of APIs that cause the system to become unresponsive, for example when the DllMain thread is waiting for another thread that was blocked. 

The following stop codes are contained in this set of tests.

<h3>The application called a blocking API from a thread that owns one or more HWNDs, causing an unresponsive user interface.  The API should be called from a background thread.</h3>
<p></p><i>Probable cause</i><p>The application called a blocking API from a thread that owns one or more HWNDs, causing an unresponsive user interface. The API should be called from a background thread.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked GUI Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Window Handle</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;UIBLOCK_BLOCKING_API</li>
  <li><b>Stop code:</b>&nbsp;2000000</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Called an API to play a sound synchronously from a user interface thread.  This caused the user interface to be unresponsive.</h3>
<p></p><i>Probable cause</i><p>Called an API to play a sound synchronously from a user interface thread. This caused the user interface to be unresponsive.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked GUI Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Window Handle</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;UIBLOCK_SYNCHRONOUS_PLAY_SOUND</li>
  <li><b>Stop code:</b>&nbsp;2000001</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Called an API with a slow file path parameter from a UI thread, causing an unresponsive user interface.  This API should be called from a background thread.</h3>
<p></p><i>Probable cause</i><p>Called an API with a slow file path parameter from a UI thread, causing an unresponsive user interface. This API should be called from a background thread.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked GUI Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Window Handle</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;File Path Type</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;UIBLOCK_SLOW_FILE_PATH</li>
  <li><b>Stop code:</b>&nbsp;2000002</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>GUI thread was waiting for another thread that was blocked.  This blocked wait chain caused the user interface to be unresponsive.</h3>
<p></p><i>Probable cause</i><p>GUI thread was waiting for another thread that was blocked. This blocked wait chain caused the user interface to be unresponsive.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked GUI Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Blocked HWND</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Background Thread ID</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;UIBLOCK_BLOCKED_WAIT_CHAIN</li>
  <li><b>Stop code:</b>&nbsp;2000004</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>GUI thread was blocked while waiting for a resource in a different process.  This blocked wait chain caused the user interface to be unresponsive.</h3>
<p></p><i>Probable cause</i><p>GUI thread was blocked while waiting for a resource in a different process. This blocked wait chain caused the user interface to be unresponsive.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked GUI Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Blocked HWND</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Blocking Process ID</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;UIBLOCK_BLOCKED_WAIT_CHAIN_PROCESS</li>
  <li><b>Stop code:</b>&nbsp;2000005</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Deadlock detected between the GUI thread and one or more background threads.  This caused the user interface to be unresponsive.</h3>
<p></p><i>Probable cause</i><p>Deadlock detected between the GUI thread and one or more background threads. This caused the user interface to be unresponsive.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked GUI Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Blocked HWND</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;UIBLOCK_BLOCKED_WAIT_CHAIN_DEADLOCK</li>
  <li><b>Stop code:</b>&nbsp;2000006</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>GUI thread was blocked for an extended duration, causing an unresponsive user interface.</h3>
<p></p><i>Probable cause</i><p>GUI thread was blocked for an extended duration, causing an unresponsive user interface.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked GUI Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Window Handle</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Duration (ms)</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;UIBLOCK_LONG_OPERATION</li>
  <li><b>Stop code:</b>&nbsp;2000007</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Timeout parameter supplied to API has the potential to block a GUI Thread for an extended duration, causing an unresponsive user interface.</h3>
<p></p><i>Probable cause</i><p>Timeout parameter supplied to API has the potential to block a GUI Thread for an extended duration, causing an unresponsive user interface.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked GUI Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Window Handle</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Timeout Parameter Value</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;UIBLOCK_LONG_OPERATION_POSSIBLE</li>
  <li><b>Stop code:</b>&nbsp;2000008</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>An API that accesses a slow printer resource was called on the UI thread.  This caused the user interface to be unresponsive.</h3>
<p></p><i>Probable cause</i><p>An API that accesses a slow printer resource was called on the UI thread. This caused the user interface to be unresponsive.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked GUI Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Window Handle</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;UIBLOCK_PRINTER_RESOURCE</li>
  <li><b>Stop code:</b>&nbsp;2000009</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Called a blocking API from within DllMain.  This caused other threads to be unresponsive.</h3>
<p></p><i>Probable cause</i><p>Called a blocking API from within DllMain. This caused other threads to be unresponsive.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;DLLMAINBLOCK_BLOCKING_API</li>
  <li><b>Stop code:</b>&nbsp;200000A</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Called an API to play a sound synchronously from within DllMain.  This caused other threads to be unresponsive.</h3>
<p></p><i>Probable cause</i><p>Called an API to play a sound synchronously from within DllMain. This caused other threads to be unresponsive.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;DLLMAINBLOCK_SYNCHRONOUS_PLAY_SOUND</li>
  <li><b>Stop code:</b>&nbsp;200000B</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Called an API with a slow file path parameter from within DllMain.  This caused other threads to be unresponsive.</h3>
<p></p><i>Probable cause</i><p>Called an API with a slow file path parameter from within DllMain. This caused other threads to be unresponsive.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;File Path Type</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;DLLMAINBLOCK_SLOW_FILE_PATH</li>
  <li><b>Stop code:</b>&nbsp;200000C</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>DllMain thread was waiting for another thread that was blocked.  This blocked wait chain caused other threads to be unresponsive.</h3>
<p></p><i>Probable cause</i><p>DllMain thread was waiting for another thread that was blocked. This blocked wait chain caused other threads to be unresponsive.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Blocking Thread ID</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;DLLMAINBLOCK_BLOCKED_WAIT_CHAIN</li>
  <li><b>Stop code:</b>&nbsp;200000E</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>DllMain thread was blocked while waiting for a resource in a different process.  This blocked wait chain caused other threads to be unresponsive.</h3>
<p></p><i>Probable cause</i><p>DllMain thread was blocked while waiting for a resource in a different process. This blocked wait chain caused other threads to be unresponsive.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Blocking Process ID</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;DLLMAINBLOCK_BLOCKED_WAIT_CHAIN_PROCESS</li>
  <li><b>Stop code:</b>&nbsp;200000F</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Deadlock detected within a DllMain call.  This caused other threads to be unresponsive.</h3>
<p></p><i>Probable cause</i><p>Deadlock detected within a DllMain call. This caused other threads to be unresponsive.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;DLLMAINBLOCK_BLOCKED_WAIT_CHAIN_DEADLOCK</li>
  <li><b>Stop code:</b>&nbsp;2000010</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>DllMain thread was blocked for an extended duration, causing an unresponsive application.</h3>
<p></p><i>Probable cause</i><p>DllMain thread was blocked for an extended duration, causing an unresponsive application.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Duration (ms)</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;DLLMAINBLOCK_LONG_OPERATION</li>
  <li><b>Stop code:</b>&nbsp;2000011</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Timeout parameter supplied to API has the potential to block DllMain for an extended duration, causing an unresponsive application.</h3>
<p></p><i>Probable cause</i><p>Timeout parameter supplied to API has the potential to block DllMain for an extended duration, causing an unresponsive application.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Timeout Parameter Value</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;DLLMAINBLOCK_LONG_OPERATION_POSSIBLE</li>
  <li><b>Stop code:</b>&nbsp;2000012</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>An API that accesses a slow printer resource was called from within DllMain.  This caused other threads to be unresponsive.</h3>
<p></p><i>Probable cause</i><p>An API that accesses a slow printer resource was called from within DllMain. This caused other threads to be unresponsive.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;DLLMAINBLOCK_PRINTER_RESOURCE</li>
  <li><b>Stop code:</b>&nbsp;2000013</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Called a blocking API on a 'special' thread that has been designated as a thread that should not become blocked.</h3>
<p></p><i>Probable cause</i><p>The application called a blocking API on a designated 'special' thread that should not become blocked.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;SPECIALTHREADBLOCK_BLOCKING_API</li>
  <li><b>Stop code:</b>&nbsp;2000014</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Called an API to play a sound synchronously from a 'special' thread that should not be blocked.</h3>
<p></p><i>Probable cause</i><p>The application called an API which is responsible for playing a multimedia sound. The parameter that controls how the sound is played passed to this API could lead to an application hang, as it was called on a 'special' thread that should not be blocked.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;SPECIALTHREADBLOCK_SYNCHRONOUS_PLAY_SOUND</li>
  <li><b>Stop code:</b>&nbsp;2000015</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Called an API from a designated 'special' thread with a slow file path parameter that could cause the application to hang.</h3>
<p></p><i>Probable cause</i><p>Called an API from a designated 'special' thread with a slow file path parameter that could cause the application to hang. The special thread should not be blocked.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;File Path Type</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;SPECIALTHREADBLOCK_SLOW_FILE_PATH</li>
  <li><b>Stop code:</b>&nbsp;2000016</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A designated 'special' thread was waiting for another thread that was blocked.  This blocked wait chain can cause the application to hang, as that thread should not be blocked.</h3>
<p></p><i>Probable cause</i><p>A designated 'special' thread was waiting for another thread that was blocked. This blocked wait chain can cause the application to hang, as that thread should not be blocked.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Blocking Thread ID</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;SPECIALTHREADBLOCK_BLOCKED_WAIT_CHAIN</li>
  <li><b>Stop code:</b>&nbsp;2000018</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A designated 'special' thread was blocked while waiting for a resource in a different process.  This blocked wait chain can cause the application to not respond.</h3>
<p></p><i>Probable cause</i><p>A designated 'special' thread was blocked while waiting for a resource in a different process. This blocked wait chain can cause the application to not respond.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Blocking Process ID</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;SPECIALTHREADBLOCK_BLOCKED_WAIT_CHAIN_PROCESS</li>
  <li><b>Stop code:</b>&nbsp;2000019</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Deadlock detected on a designated 'special' thread.  This can cause the application to not respond, as that thread should not become blocked.</h3>
<p></p><i>Probable cause</i><p>Deadlock detected on a designated 'special' thread. This can cause the application to not respond, as that thread should not become blocked.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;SPECIALTHREADBLOCK_BLOCKED_WAIT_CHAIN_DEADLOCK</li>
  <li><b>Stop code:</b>&nbsp;200001A</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A designated 'special' thread was blocked for an extended duration, causing an unresponsive application.</h3>
<p></p><i>Probable cause</i><p>A designated 'special' thread was blocked for an extended duration, causing an unresponsive application. This thread should not be blocked.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Duration (ms)</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;SPECIALTHREADBLOCK_LONG_OPERATION</li>
  <li><b>Stop code:</b>&nbsp;200001B</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Timeout parameter supplied to API has the potential to block a designated 'special' thread for an extended duration, causing an unresponsive user interface.</h3>
<p></p><i>Probable cause</i><p>Timeout parameter supplied to API has the potential to block a designated 'special' thread for an extended duration, causing an unresponsive user interface. This thread should not be blocked.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Timeout Parameter Value</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;SPECIALTHREADBLOCK_LONG_OPERATION_POSSIBLE</li>
  <li><b>Stop code:</b>&nbsp;200001C</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>An API that accesses a slow printer resource was called on designated 'special' thread that should not be blocked.</h3>
<p></p><i>Probable cause</i><p>This function should not be called on a designated 'special' thread since it can wait on a slow printer resource. A thread designated as special should not become blocked.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Window Handle</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;SPECIALTHREADBLOCK_PRINTER_RESOURCE</li>
  <li><b>Stop code:</b>&nbsp;200001D</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Thread attempted to create another thread from within DllMain.  The new thread will immediately become blocked until DllMain exits.  If the calling thread attempts to synchronize with the new thread while still inside DllMain, a deadlock will result.</h3>
<p></p><i>Probable cause</i><p>Thread attempted to create another thread from within DllMain. The new thread will immediately become blocked until DllMain exits. If the calling thread attempts to synchronize with the new thread while still inside DllMain, a deadlock will result.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;DEADLOCK_CREATETHREAD_LOADERLOCKED</li>
  <li><b>Stop code:</b>&nbsp;200001E</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Thread attempted to call SendMessage/SendMessageTimeout (with HWND target on another thread) or DispatchMessage while holding a critical section.  This can cause a deadlock or application unresponsiveness.</h3>
<p></p><i>Probable cause</i><p>Thread attempted to call SendMessage/SendMessageTimeout (with HWND target on another thread) or DispatchMessage while holding a critical section. This can cause a deadlock or application unresponsiveness.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;API Name: %ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Blocked Thread ID</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Locked Critical Section (use !cs [addr])</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;If SendMessage, target HWND.  If DispatchMessage, MSG (use dt MSG [addr])</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Hangs</li>
  <li><b>Stop ID:</b>&nbsp;DEADLOCK_SENDMESSAGE_CRITSECT</li>
  <li><b>Stop code:</b>&nbsp;200001F</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
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


 





