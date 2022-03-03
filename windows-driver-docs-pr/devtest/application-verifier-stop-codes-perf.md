---
title: Application Verifier - Stop Codes - Perf
description: Application Verifier - Stop Codes - Perf 
keywords:
- verifying drivers (Application Verifier)
- driver verification (Application Verifier)
- Application Verifier
- AppVerif.exe
- user-mode application testing
ms.date: 01/14/2022
---

# Application Verifier - Stop Codes - Perf

The Perf test check for efficient use of APIs that impact system performance and energy consumption, such as calling a Windows function that uses an incorrect wait period.

The following stop codes are contained in this set of tests.

<h3>Any use of a Windows function that induces a defined wait duration of less than 300 ms is an energy efficiency bug.  Switch to using an event based design or extend the wait duration.</h3>
<p></p><i>Probable cause</i><p>When calling any wait type API with a wait/delay interval duration, should be greater or equal to 300 ms. Calling this API with lower than 300 ms causes Windows to wake the CPUs too often. When Windows is forced to wake the CPUs, more electrical energy is consumed which can greatly decrease battery life and cause unnecessary power draw.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; ERROR: %ws(...%ws=%d...). %ws </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of API Name (use du to dump the string)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address of Parameter Name (use du to dump the string)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Parameter value (wait / delay duration in ms)</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Address of Additional Info (use du to dump the string)</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Power</li>
  <li><b>Stop ID:</b>&nbsp;ERROR_DELAY_INTERVAL_DURATION_TOO_SHORT</li>
  <li><b>Stop code:</b>&nbsp;7000000</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Use of a tolerable delay mechanism less than 300 ms does not allow the system sufficient break intervals and is an energy efficiency bug.  Switch to using an event based design or extend the delay duration.</h3>
<p></p><i>Probable cause</i><p>When calling any wait type API with a tolerable delay, duration should be greater or equal to 300 ms. Calling this API with lower than 300 ms causes Windows to wake the CPUs too often. When Windows is forced to wake the CPUs, more electrical energy is consumed which can greatly decrease battery life and cause unnecessary power draw.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; ERROR: %ws(...%ws=%d...). %ws </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of API Name (use du to dump the string)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address of Parameter Name (use du to dump the string)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Parameter value (tolerable variance in ms)</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Address of Additional Info (use du to dump the string)</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Power</li>
  <li><b>Stop ID:</b>&nbsp;ERROR_TOLERABLE_VARIANCE_DURATION_TOO_SHORT</li>
  <li><b>Stop code:</b>&nbsp;7000001</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Any use of a Windows function that induces a defined wait duration of less than 300 ms is an energy efficiency bug.  Switch to using an event based design or extend the wait duration.</h3>
<p></p><i>Probable cause</i><p>When calling any wait type API with a wait/delay interval, duration should be greater or equal to 300 ms. Calling this API with lower than 300 ms can cause Windows to wake the CPUs too often. When Windows is forced to wake the CPUs, more electrical energy is consumed which can greatly decrease battery life and cause unnecessary power draw.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; WARNING: %ws(...%ws=%d...). %ws </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of API Name (use du to dump the string)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address of Parameter Name (use du to dump the string)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Parameter value (wait / delay duration in ms)</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Address of Additional Info (use du to dump the string)</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Power</li>
  <li><b>Stop ID:</b>&nbsp;WARNING_DELAY_INTERVAL_DURATION_TOO_SHORT</li>
  <li><b>Stop code:</b>&nbsp;7000002</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Use of a tolerable delay mechanism less than 300 ms does not allow the system sufficient break intervals and is an energy efficiency bug.  Switch to using an event based design or extend the delay duration.</h3>
<p></p><i>Probable cause</i><p>When calling any wait type API with a tolerable variance, duration should be greater or equal to 300 ms. Calling this API with lower than 300 ms can cause Windows to wake the CPUs too often. When Windows is forced to wake the CPUs, more electrical energy is consumed which can greatly decrease battery life and cause unnecessary power draw.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; WARNING: %ws(...%ws=%d...). %ws </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of API Name (use du to dump the string)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address of Parameter Name (use du to dump the string)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Parameter value (tolerable variance in ms)</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Address of Additional Info (use du to dump the string)</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Power</li>
  <li><b>Stop ID:</b>&nbsp;WARNING_TOLERABLE_VARIANCE_DURATION_TOO_SHORT</li>
  <li><b>Stop code:</b>&nbsp;7000003</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Adjusting the system wide timer resolution can have large energy efficiency impacts and normally does not lead to better performance.  Do not use this API.</h3>
<p></p><i>Probable cause</i><p>Allowing the system to select this value is best for both performance and energy efficiency. Adjusting the system timer can greatly decrease battery life and cause unnecessary power draw.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; ERROR: %ws(...%ws=%d...). %ws </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of API Name (use du to dump the string)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address of Parameter Name (use du to dump the string)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Parameter value (timer resolution in ms)</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Address of Additional Info (use du to dump the string)</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Power</li>
  <li><b>Stop ID:</b>&nbsp;ERROR_SYSTEM_TIMER_RESOLUTION_ADJUSTMENT</li>
  <li><b>Stop code:</b>&nbsp;7000004</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Adjustments were made to the running system that will likely increase power consumption.  Only applications presenting multimedia (video/audio) that expect no user interaction should call these APIs.</h3>
<p></p><i>Probable cause</i><p>Avoiding use of this API except for multimedia applications (video/audio) that expect no user interaction is recommended to improve energy efficiency. Calling this API causes Windows to forgo power saving operations and will greatly decrease battery life and/or cause unnecessary power draw.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;The API named %ws was called which increases system energy consumption. %ws </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of API Name (use du to dump the string)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address of Additional Info (use du to dump the string)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Power</li>
  <li><b>Stop ID:</b>&nbsp;WARNING_SYSTEM_POWER_USAGE_INCREASE</li>
  <li><b>Stop code:</b>&nbsp;7000005</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
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


 





