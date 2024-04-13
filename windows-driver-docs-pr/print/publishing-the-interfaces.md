---
title: Publishing the Interfaces
description: Publishing the Interfaces
keywords:
- IPrintCoreHelperPS
- IPrintCoreHelperUni
- IPrintCoreHelper
- helper interfaces WDK printer interface DLL
- publishing WDK printer interface DLL
ms.date: 01/30/2023
---

# Publishing the Interfaces

[!include[Print Support Apps](../includes/print-support-apps.md)]

Plug-ins typically receive instances of objects that implement behavior in the core drivers by a mechanism called publishing. The [IPrintCoreHelper](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelper), [IPrintCoreHelperPS](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperps), and [IPrintCoreHelperUni](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperuni) helper interfaces are published by means of that same model, with a few minor differences.

The following lists summarize the order in which objects are published in user interface (UI) and render modules, for both Unidrv and Pscript5. For each of the four modules, the number in the list indicates the order in which an object is published, and the COM interfaces that are named indicate which interfaces that the object implements.

In any given module, the driver should keep only one of the objects published by saving a pointer and calling the **AddRef** method on that object. After the plug-in stores the reference to the object, the plug-in should return S\_OK. The core driver will then stop publishing interfaces. This model is not significantly different from the previous publication mechanism.

In the UI context, the objects are published to the **IPrintOemUI** interface on the class whose class identifier is CLSID_OEMUI. In the render context, objects are published to the **IPrintOemPS** or **IPrintOemUni** interfaces.

The objects that are marked with an asterisk (\*) in the following lists are published to the **IPrintOemPrintTicketProvider** interface.

### <a href="" id="unidrv-ui-module-publishing-order"></a> Unidrv UI Module Publishing Order

1. **IUnknown** and \***IPrintCoreHelper** and **IPrintCoreHelperUni**

2. **IUnknown** and **IPrintOemDriverUI**

### <a href="" id="unidrv-render-module-publishing-order"></a> Unidrv Render Module Publishing Order

1. **IUnknown** and **IPrintCoreHelper** and **IPrintCoreHelperUni**

2. **IUnknown** and **IPrintOemDriverUni**

### <a href="" id="pscript5-ui-module-publishing-order"></a> Pscript5 UI Module Publishing Order

1. **IUnknown** and \***IPrintCoreHelper** and **IPrintCoreHelperPS**

2. **IUnknown** and **IPrintCoreUI2**

3. **IUnknown** and **IPrintOemDriverUI**

### <a href="" id="pscript5-render-module-publishing-order"></a> Pscript5 Render Module Publishing Order

1. **IUnknown** and **IPrintCoreHelper** and **IPrintCoreHelperPS**

2. **IUnknown** and **IPrintCorePS2**
