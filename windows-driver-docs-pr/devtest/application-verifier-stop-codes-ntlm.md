---
title: Application Verifier - Stop Codes - NTLM
description: Application Verifier - Stop Codes - NTLM
keywords:
- verifying drivers (Application Verifier)
- driver verification (Application Verifier)
- Application Verifier
- AppVerif.exe
- user-mode application testing
ms.date: 01/14/2022
---

# Application Verifier - Stop Codes - NTLM

The following stop codes are contained in this set of tests.

  <h3>AcquireCredentialsHandle acquires NTLM credential explicitly. </h3>
<p></p><i>Probable cause</i><p>AcquireCredentialsHandle is called directly or indirectly by the application with pszPackage = 'NTLM'. 'Negotiate' should be used to fix this issue. An example of bad call: AcquireCredentialsHandle( ... 'NTLM', // pszPackage ... ); An example of good call: AcquireCredentialsHandle( ... 'Negotiate', // pszPackage ... ); Please refer to help for more detailed information of this stop code.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;NTLMCaller</li>
  <li><b>Stop ID:</b>&nbsp;ACH_EXPLICIT_NTLM_PACKAGE</li>
  <li><b>Stop code:</b>&nbsp;5000000</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>AcquireCredentialsHandle prefers NTLM credentials. Please see Param1 for the value of PackageList.</h3>
<p></p><i>Probable cause</i><p>AcquireCredentialsHandle is called directly or indirectly by the application with pszPackage = 'Negotiate'. However, NTLM is preferred in supplied credential (pAuthData). An example of bad call: AcquireCredentialsHandle( ... 'Negotiate', // pszPackage ... pAuthData, // pAuthData, ((SEC_WINNT_AUTH_IDENTITY_EX*)pAuthData)-&gt;PackageList is 'NTLM' or 'NTLM,KERBEROS' etc. ... ); An example of good call: AcquireCredentialsHandle( ... 'Negotiate', // pszPackage ... pAuthData, // pAuthData, ((SEC_WINNT_AUTH_IDENTITY_EX*)pAuthData)-&gt;PackageList = NULL or NTLM is less preferred. ... ); Please refer to help for more detailed information of this stop code.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Packagelist: %.*hs%.*ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;PackageList.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;NTLMCaller</li>
  <li><b>Stop ID:</b>&nbsp;ACH_IMPLICITLY_USE_NTLM</li>
  <li><b>Stop code:</b>&nbsp;5000001</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>AcquireCredentialsHandle mistakenly uses '-NTLM' to exclude NTLM credential. Please see Param1 for the value of PackageList.</h3>
<p></p><i>Probable cause</i><p>AcquireCredentialsHandle is called directly or indirectly by the application with supplied credential (pAuthData), in which '-NTLM' is mistakenly used to exclude NTLM credential. '!NTLM' should be used to fix this issue. An example of bad call: AcquireCredentialsHandle( ... 'Negotiate', // pszPackage ... pAuthData, // pAuthData, ((SEC_WINNT_AUTH_IDENTITY_EX*)pAuthData)-&gt;PackageList uses '-NTLM'. ... ); An example of good call: AcquireCredentialsHandle( ... 'Negotiate', // pszPackage ... pAuthData, // pAuthData, ((SEC_WINNT_AUTH_IDENTITY_EX*)pAuthData)-&gt;PackageList uses '!NTLM'. ... ); Please refer to help for more detailed information of this stop code.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;PackageList: %.*hs%.*ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;PackageList.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;NTLMCaller</li>
  <li><b>Stop ID:</b>&nbsp;ACH_BAD_NTLM_EXCLUSION</li>
  <li><b>Stop code:</b>&nbsp;5000002</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>InitializeSecurityContext uses NULL target or malformed target for Kerberos service. Please see pszTargetName for the value of the target.</h3>
<p></p><i>Probable cause</i><p>InitializeSecurityContext is called directly or indirectly by the application with pszTargetName being NULL or malformed, with which Kerberos cannot be possibly negotiated. The guidance to fix this issue to use Kerberos is provided as below: (1) The service the client application authenticates to should have its SPN uniquely registered in its forest; (2) The service must run under the identity,domain user or computer account, with this SPN registered; (3) InitializedSecuirtyContext should be called with this SPN. An example of bad call: InitializeSecurityContext( ... NULL, // pszTargetName ... ); Another example of bad call: InitializeSecurityContext( ... '\\\\localhost', // pszTargetName ... ); An example of good call: InitializeSecurityContext( ... 'myservice/mymachine.mydomain.com', // pszTargetName, myservice/mymachine.mydomain.com is a uniquely registered SPN under which the service runs. ... ); Please refer to help for more detailed information of this stop code.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;pszTargetName: %hs%ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;NTLMCaller</li>
  <li><b>Stop ID:</b>&nbsp;ISC_MALFORMED_TARGET</li>
  <li><b>Stop code:</b>&nbsp;5000003</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;no</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The client application downgrades to use NTLM authentication as the result of negotiation. Please see pAuthData for more details. pAuthData shows the credential and the target used for this negotiation.</h3>
<p></p><i>Probable cause</i><p>The client application downgrades to use NTLM authentication as the result of negotiation. There can be many reasons for this issue. The guidance of troubleshooting this issue is provided as below: (1) Turn on NTLMCaller appverifier layer if it was not on. This layer will catch commonly known issues that can cause the downgrade; (2) If pszTargetName is an SPN, make sure this SPN is uniquely registered in the forest (the SPN cannot be missing or duplicated); (3) The SPN must be looked up by the client system running client application; (4) The service must run under an identity with its Kerberos credential available; (5) The scenario should be reviewed by Windows security experts. Please refer to help for more detailed information of this stop code.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;pAuthData: %ws \n\tUser: %hs%ws \n\tDomain: %hs%ws \npszTargetName: %hs%ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;NTLMDowngrade</li>
  <li><b>Stop ID:</b>&nbsp;FALLBACK_TO_NTLM</li>
  <li><b>Stop code:</b>&nbsp;5010000</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
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


 





