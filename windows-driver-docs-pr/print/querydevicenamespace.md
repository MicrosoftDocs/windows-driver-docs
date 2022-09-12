---
title: QueryDeviceNamespace
description: The IPrintTicketProvider QueryDeviceNamespace routine provides the default namespace that the PrintTicket-to-DEVMODE and DEVMODE-to-PrintTicket conversions will use if they need to put a feature or option from a private namespace in a Print Ticket.
keywords:
- QueryDeviceNamespace
ms.date: 09/07/2022
---

# QueryDeviceNamespace

The [**IPrintTicketProvider::QueryDeviceNamespace**](/windows-hardware/drivers/ddi/prdrvcom/nf-prdrvcom-iprintticketprovider-querydevicenamespace) routine provides the default namespace that the PrintTicket-to-DEVMODE and DEVMODE-to-PrintTicket conversions will use if they need to put a feature or option from a private namespace in a Print Ticket.

The following sample code illustrates how this method could be implemented.

```cpp
STDMETHODIMP
CPrintTicketProvider::QueryDeviceNamespace(BSTR *pDefaultNamespace)
{
    *pDefaultNamespace = SysAllocString(TEXT("https://schemas.contoso.com/printers/seriesA/v.1.0"));
    
    if (!(*pDefaultNamespace))
    {
        return E_OUTOFMEMORY;
    }
 
    return S_OK;
}
```
