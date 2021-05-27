---
title: BindPrinter
description: The IPrintTicketProvider BindPrinter method binds a printer or print queue to a specific version of the Print Ticket schema.
keywords:
- BindPrinter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# BindPrinter


The [**IPrintTicketProvider::BindPrinter**](/previous-versions/windows/hardware/drivers/ff554354(v=vs.85)) method binds a printer or print queue to a specific version of the Print Ticket schema. This enables the core driver to associate a set of private namespace URIs with a device.

Binding to a device enables the provider to cache certain objects and handles that it will use to perform future Print Ticket or device capabilities services for that device.

The [**IPrintTicketProvider::BindPrinter**](/previous-versions/windows/hardware/drivers/ff554354(v=vs.85)) method is guaranteed to be called only once for each PrintTicketProvider instance.

The following sample code illustrates the method's arguments.

```cpp
STDMETHODIMP 
CPrintTicketProvider::
BindPrinter( THIS_ HANDLE    hPrinter,
                   INT       version,
                   PSHIMOPTS pOptions,
                   DWORD    *pDevModeFlags,
                   INT      *pcNamespaces,
                   BSTR    **ppNamespaces)
```
