---
title: QueryDeviceNamespace
author: windows-driver-content
description: The IPrintTicketProvider QueryDeviceNamespace routine provides the default namespace that the PrintTicket-to-DEVMODE and DEVMODE-to-PrintTicket conversions will use if they need to put a feature or option from a private namespace in a Print Ticket.
ms.assetid: 5f940cdc-42c3-4521-91c5-cc8e340ce34a
keywords: ["QueryDeviceNamespace"]
---

# QueryDeviceNamespace


The [**IPrintTicketProvider::QueryDeviceNamespace**](https://msdn.microsoft.com/library/windows/hardware/ff554378) routine provides the default namespace that the PrintTicket-to-DEVMODE and DEVMODE-to-PrintTicket conversions will use if they need to put a feature or option from a private namespace in a Print Ticket.

The following sample code illustrates how this method could be implemented.

```
STDMETHODIMP
CPrintTicketProvider::QueryDeviceNamespace(BSTR *pDefaultNamespace)
{
    *pDefaultNamespace = SysAllocString(TEXT("http://schemas.contoso.com/printers/seriesA/v.1.0"));
    
    if (!(*pDefaultNamespace))
    {
        return E_OUTOFMEMORY;
    }
 
    return S_OK;
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20QueryDeviceNamespace%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


