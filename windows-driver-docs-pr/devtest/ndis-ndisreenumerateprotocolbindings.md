---
title: NdisReEnumerateProtocolBindings rule (ndis)
description: Protocol drivers cannot call NdisReEnumerateProtocolBindings from within the context of the ProtocolBindAdapterEx or ProtocolUnbindAdapterEx functions.
ms.date: 05/21/2018
keywords: ["NdisReEnumerateProtocolBindings rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisReEnumerateProtocolBindings
api_type:
- NA
ms.localizationpriority: medium
---

# NdisReEnumerateProtocolBindings rule (ndis)


Protocol drivers cannot call [**NdisReEnumerateProtocolBindings**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreenumerateprotocolbindings) from within the context of the [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) or [*ProtocolUnbindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_unbind_adapter_ex) functions. Also, protocol drivers cannot call **NdisReEnumerateProtocolBindings** from within the context of the [*ProtocolNetPnPEvent*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_net_pnp_event) function if the *ProtocolBindingContext* parameter of *ProtocolNetPnPEvent* is not NULL. However, protocol drivers can call **NdisReEnumerateProtocolBindings** from within the context of *ProtocolNetPnPEvent* if *ProtocolBindingContext* is NULL. A NULL *ProtocolBindingContext* value indicates that the event applies to all bindings.

**Driver model: NDIS**

## How to test

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>NdisReEnumerateProtocolBindings</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

## Applies to

[**NdisReEnumerateProtocolBindings**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreenumerateprotocolbindings)
