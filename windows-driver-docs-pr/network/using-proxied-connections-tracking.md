---
title: Using Proxied Connections Tracking
description: Using Proxied Connections Tracking
ms.assetid: 20A737D7-043D-4D05-A15D-85595E48521B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Proxied Connections Tracking


Proxied connections tracking is supported in Windows 8 and later versions of Windows.

This WFP feature facilitates tracking of redirection “records” from the initial redirect of a connection to the final connection to the destination. WFP also allows a callout driver to redirect connections.

### Proxied Connections Tracking

With the presence of multiple proxies (for example, developed by different ISVs) the connection used by one party to communicate with the final destination could in turn be redirected by a 2nd party; and that new connection could again be redirected by the original party. Without connection tracking, the original connection might never reach its final destination as it gets stuck in the infinite proxy loop.

Additions to the Data Field Identifiers to support connection tracking include:

<a href="" id="fwps-field-xxx-ale-original-app-id"></a>FWPS\_FIELD\_Xxx\_ALE\_ORIGINAL\_APP\_ID  
The full path of the original application for proxy connections. If the application has not been proxied, this path is identical to the xxx\_ALE\_APP\_ID.

<a href="" id="fwps-field-xxx-package-id"></a>FWPS\_FIELD\_Xxx\_PACKAGE\_ID  
The package identifier is a security identifier (SID) that identifies the associated AppContainer process. For more information about the SID structure, see the description for the SID structure in the Microsoft Windows SDK documentation.

### Redirecting Connections

A callout driver calls the [**FwpsRedirectHandleCreate0**](https://msdn.microsoft.com/library/windows/hardware/hh439681) function to create a handle that can be used to redirect TCP connections.

This section includes the following topics:

Using a Redirection Handle

Querying the Redirect State

### Using a Redirection Handle

Before an ALE connect redirection callout can redirect connections to a local process, it must obtain a redirect handle with the FwpsRedirectHandleCreate0 function and put the handle in the [**FWPS\_CONNECT\_REQUEST0**](https://msdn.microsoft.com/library/windows/hardware/ff551231) structure. The callout modifies the structure in the classifyFn for the ALE connect redirect layers.

The FWPS\_CONNECT\_REQUEST0 structure contains the following members for redirection:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>localRedirectHandle</strong></p></td>
<td align="left"><p>The redirect handle that the callout driver created by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439681" data-raw-source="[&lt;strong&gt;FwpsRedirectHandleCreate0&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439681)"><strong>FwpsRedirectHandleCreate0</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>localRedirectContext</strong></p></td>
<td align="left"><p>A callout driver context area that the callout driver allocated by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544520" data-raw-source="[&lt;strong&gt;ExAllocatePoolWithTag&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544520)"><strong>ExAllocatePoolWithTag</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>localRedirectContextSize</strong></p></td>
<td align="left"><p>The size, in bytes, of the callout supplied context area.</p></td>
</tr>
</tbody>
</table>

 

After a callout driver has finished using a redirect handle, it must call the [**FwpsRedirectHandleDestroy0**](https://msdn.microsoft.com/library/windows/hardware/hh439684) function to destroy the handle.

### Querying the Redirect State

A callout driver calls the [**FwpsQueryConnectionRedirectState0**](https://msdn.microsoft.com/library/windows/hardware/hh439677) function to get the redirect state of a connection. The [**FWPS\_CONNECTION\_REDIRECT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh439704) enumeration is the return type for a call to the **FwpsQueryConnectionRedirectState0** function.

If the redirect status is FWPS\_CONNECTION\_NOT\_REDIRECTED, the ALE\_CONNECT\_REDIRECT callout can proceed to proxy the connection.

If the redirect status is FWPS\_CONNECTION\_REDIRECTED\_BY\_SELF, the ALE\_CONNECT\_REDIRECT callout should return FWP\_ACTION\_PERMIT/FWP\_ACTION\_CONTINUE.

If the redirect status is FWPS\_CONNECTION\_REDIRECTED\_BY\_OTHER, the ALE\_CONNECT\_REDIRECT callout could proceed to proxy the connection if it does not trust the other inspector’s result.

If the redirect status is FWPS\_CONNECTION\_PREVIOUSLY\_REDIRECTED\_BY\_SELF, the ALE\_CONNECT\_REDIRECT callout must not perform redirection even if other inspectors’ results are not acceptable. In this case, it must either permit or block the connection (at the ALE\_AUTH\_CONNECT layer).

 

 





