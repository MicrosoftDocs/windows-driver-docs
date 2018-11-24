---
title: BindPrinter
description: The IPrintTicketProvider BindPrinter method binds a printer or print queue to a specific version of the Print Ticket schema.
ms.assetid: 81f32a9a-417a-4851-972e-373112590e1c
keywords:
- BindPrinter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# BindPrinter


The [**IPrintTicketProvider::BindPrinter**](https://msdn.microsoft.com/library/windows/hardware/ff554354) method binds a printer or print queue to a specific version of the Print Ticket schema. This enables the core driver to associate a set of private namespace URIs with a device.

Binding to a device enables the provider to cache certain objects and handles that it will use to perform future Print Ticket or device capabilities services for that device.

The [**IPrintTicketProvider::BindPrinter**](https://msdn.microsoft.com/library/windows/hardware/ff554354) method is guaranteed to be called only once for each PrintTicketProvider instance.

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
