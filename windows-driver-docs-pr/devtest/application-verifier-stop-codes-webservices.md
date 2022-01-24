---
title: Application Verifier - Stop Codes - Webservices
description: Application Verifier - Stop Codes - Webservices
keywords:
- verifying drivers (Application Verifier)
- driver verification (Application Verifier)
- Application Verifier
- AppVerif.exe
- user-mode application testing
ms.date: 01/14/2022
---

# Application Verifier - Stop Codes - Webservices

The following stop codes are contained in this set of tests.

<h3>An invalid address of a Web Services Windows API intrinsic object was passed to the function</h3>
<p></p><i>Probable cause</i><p>A call was made to an Web Services Windows API with an invalid object. The object referenced in parameter 1 may be invalid or have been already freed. To list the objects which have been created and freed, enter !avrf -ws -obj at the debugger prompt.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Invalid address of a Web Services Windows API intrinsic object</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of object.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Webservices</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_OBJECT_ADDRESS</li>
  <li><b>Stop code:</b>&nbsp;00006000</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>An operation in another thread is using a non-thread safe intrinsic Web Services Windows API object</h3>
<p></p><i>Probable cause</i><p>Another thread is using a single threaded Web Services Windows API intrinsic object. To list the operations, and threads which are using the object, enter !avrf -ws -obj [object] at the debugger prompt, where [object] is the address of the single threaded intrinsic object.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Multithreaded use of a Windows Web Services API intrinsic object</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of single threaded intrinsic object.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Webservices</li>
  <li><b>Stop ID:</b>&nbsp;SINGLE_THREADED_OBJECT_VIOLATION</li>
  <li><b>Stop code:</b>&nbsp;00006001</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>An intrinsic Web Services Windows API was freed when an asynchronous operation is still pending</h3>
<p></p><i>Probable cause</i><p>An object is being freed while an asynchronous operation is still pending. To show the stack containing the operation still pending, enter !avrf -ws -obj [object] at the debugger prompt, where [object] is the address of the object still in use.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Freeing of an object whilst still in use</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of  intrinsic object.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Webservices</li>
  <li><b>Stop ID:</b>&nbsp;OBJECT_IN_USE</li>
  <li><b>Stop code:</b>&nbsp;00006002</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A Web Services Windows API is taking too long to execute</h3>
<p></p><i>Probable cause</i><p>An operation is taking too long to execute. To find out the operation, output the stack (using 'k') in the debugger.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Web Services Windows API</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Webservices</li>
  <li><b>Stop ID:</b>&nbsp;API_TIMEOUT</li>
  <li><b>Stop code:</b>&nbsp;00006003</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A corrupt WS_ASYNC_CONTEXT was passed into the callback function</h3>
<p></p><i>Probable cause</i><p>A corrupt call context was passed into the callback function. This the result of memory corruption. To isolate this problem, re-run your application with heap checking enabled.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;A corrupt WS_ASYNC_CONTEXT was passed into the callback function</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Webservices</li>
  <li><b>Stop ID:</b>&nbsp;CORRUPT_CALL_CONTEXT</li>
  <li><b>Stop code:</b>&nbsp;00006004</li>
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


 





