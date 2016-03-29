---
title: BindPrinter
description: The IPrintTicketProvider BindPrinter method binds a printer or print queue to a specific version of the Print Ticket schema. This enables the core driver to associate a set of private namespace URIs with a device.
ms.assetid: 81f32a9a-417a-4851-972e-373112590e1c
keywords: ["BindPrinter"]
---

# BindPrinter


The [**IPrintTicketProvider::BindPrinter**](https://msdn.microsoft.com/library/windows/hardware/ff554354) method binds a printer or print queue to a specific version of the Print Ticket schema. This enables the core driver to associate a set of private namespace URIs with a device.

Binding to a device enables the provider to cache certain objects and handles that it will use to perform future Print Ticket or device capabilities services for that device.

The [**IPrintTicketProvider::BindPrinter**](https://msdn.microsoft.com/library/windows/hardware/ff554354) method is guaranteed to be called only once for each PrintTicketProvider instance.

The following sample code illustrates the method's arguments.

``` syntax
STDMETHODIMP 
CPrintTicketProvider::
BindPrinter( THIS_ HANDLE    hPrinter,
                   INT       version,
                   PSHIMOPTS pOptions,
                   DWORD    *pDevModeFlags,
                   INT      *pcNamespaces,
                   BSTR    **ppNamespaces)
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20BindPrinter%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




