---
title: Application Verifier - Stop Codes - Services
description: Application Verifier - Stop Codes - Services
keywords:
- verifying drivers (Application Verifier)
- driver verification (Application Verifier)
- Application Verifier
- AppVerif.exe
- user-mode application testing
ms.date: 01/14/2022
---

# Application Verifier - Stop Codes - Services

The services tests, check for the proper use of Windows Services. For example that services are being started and stopped properly. For more information on Windows Services see [Services](/windows/win32/services/services).

The following stop codes are contained in this set of tests.

<h3>Using a non-Unicode API (e.g. RegisterServiceCtrlHandlerA instead of RegisterServiceCtrlHandlerW)</h3>
<p></p><i>Probable cause</i><p>Most probably the application was not compiled with the UNICODE macro defined and therefore non-Unicode interfaces are used.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; API name %ws </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Service</li>
  <li><b>Stop ID:</b>&nbsp;USING_NON_UNICODE_API</li>
  <li><b>Stop code:</b>&nbsp;4000000</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>StartServiceCtrlDispatcher API is being called a second time</h3>
<p></p><i>Probable cause</i><p>This API is meant to be called only once at the start of the service wmain function.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; API name %ws </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SERVICE_TABLE_ENTRY parameter.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Service</li>
  <li><b>Stop ID:</b>&nbsp;CTRL_DISPATCHER_CALLED_TWICE</li>
  <li><b>Stop code:</b>&nbsp;4000001</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Invalid SERVICE_STATUS handle is being passed to SetServiceStatus</h3>
<p></p><i>Probable cause</i><p>Invalid SERVICE_STATUS handle is being passed to SetServiceStatus.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; API name %ws </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SERVICE_STATUS_HANDLE value.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Service</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_SERVICE_STATUS_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;4000002</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>SetServiceStatus is being called from two threads</h3>
<p></p><i>Probable cause</i><p>This API is meant to be called serially.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; API name %ws is being called concurrently from %ws service </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;LPSERVICE_STATUS value passed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Service</li>
  <li><b>Stop ID:</b>&nbsp;SET_SERVICE_STATUS_RACE</li>
  <li><b>Stop code:</b>&nbsp;4000003</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>STOP/SHUTDOWN controls are being accepted while service is in START_PENDING state</h3>
<p></p><i>Probable cause</i><p>Most services cannot accept stop/shutdown controls during initialization</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; Service name: %ws dwControlsAccepted: %08X </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;LPSERVICE_STATUS value passed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Service</li>
  <li><b>Stop ID:</b>&nbsp;STOP_SHUTDOWN_ACCEPTED</li>
  <li><b>Stop code:</b>&nbsp;4000004</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>SERVICE is attempting an invalid state transition</h3>
<p></p><i>Probable cause</i><p>The service attempted to do an invalid state transition or setting identical status parameters</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; Service %ws was found attempting an invalid state transition</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;LPSERVICE_STATUS Current State.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;LPSERVICE_STATUS New State.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Last SetServiceStatus stack trace.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Service</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_STATE_TRANSITION</li>
  <li><b>Stop code:</b>&nbsp;4000005</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>SERVICE is attempting to set identical status parameters</h3>
<p></p><i>Probable cause</i><p>The service attempted to set identical status parameters</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; The service %ws attempted to set identical status parameters </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;LPSERVICE_STATUS Current State.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;LPSERVICE_STATUS New State.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Last SetServiceStatus stack trace.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Service</li>
  <li><b>Stop ID:</b>&nbsp;DUPLICATE_STATE_PARAMS</li>
  <li><b>Stop code:</b>&nbsp;4000006</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>SERVICE is leaving pending threads after entering STOPPED state</h3>
<p></p><i>Probable cause</i><p>The service is leaving pending threads after declaring STOPPED state</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; Service %ws is leaking threads </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Thread Id of the leaked thread.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Service Tag.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Service</li>
  <li><b>Stop ID:</b>&nbsp;LEAKED_THREAD</li>
  <li><b>Stop code:</b>&nbsp;4000007</li>
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


 





