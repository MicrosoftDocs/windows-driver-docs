---
title: Print Pipeline Property Bag
description: The print pipeline property bag is used to pass information between filters in the filter pipeline.
keywords: ["Print Pipeline Property Bag Print Devices"]
ms.date: 01/26/2024
---

# Print pipeline property bag

The print pipeline property bag is used to pass information between filters in the filter pipeline.

| Property name | Symbolic name | Property type | Description |
|--|--|--|--|
| PrinterName | XPS_FP_PRINTER_NAME | VT_BSTR | The printer name. |
| ProgressReport | XPS_FP_PROGRESS_REPORT |VT_UNKNOWN| A pointer to an **IUnknown** interface. Call **QueryInterface** to obtain a pointer to the [**IPrintPipelineProgressReport**](/windows-hardware/drivers/ddi/filterpipeline/nn-filterpipeline-iprintpipelineprogressreport) interface. |
| PrinterHandle | XPS_FP_PRINTER_HANDLE | VT_BYREF | The printer handle. The filter should not close this handle. |
| PerUserPrintTicket | XPS_FP_USER_PRINT_TICKET | VT_UNKNOWN | A pointer to an **IUnknown** interface. Call **QueryInterface** to obtain a pointer to the [**IPrintReadStreamFactory**](/windows-hardware/drivers/ddi/filterpipeline/nn-filterpipeline-iprintreadstreamfactory) interface. |
| UserSecurityToken | XPS_FP_USER_TOKEN | VT_BYREF | A handle that the filter can use to impersonate the user account that submitted the print job. |
| PrintJobId | XPS_FP_JOB_ID | VT_UI4 | The print job identification number. |
| PrintClassFactory | XPS_FP_PRINT_CLASS_FACTORY | VT_UNKNOWN | A pointer to an **IUnknown** interface. Call **QueryInterface** to obtain a pointer to the [**IPrintClassObjectFactory**](/windows-hardware/drivers/ddi/filterpipeline/nn-filterpipeline-iprintclassobjectfactory) interface. |
| IPrintCoreHelper | (There is no symbolic name for this property name.) | VT_UNKNOWN | A pointer to an **IUnknown** interface. Call **QueryInterface** to obtain a pointer to the [**IPrintCoreHelper**](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelper) interface. This property is only available in XPSDrv printer drivers that use the unidrvui.dll as the configuration UI DLL. |
| PrintDeviceCapabilities | XPS_FP_PRINTDEVICECAPABILITIES | VT_UNKNOWN | A pointer to an **IUnknown** interface. Call **QueryInterface** to obtain a pointer to the [**IPrintReadStreamFactory**](/windows-hardware/drivers/ddi/filterpipeline/nn-filterpipeline-iprintreadstreamfactory) interface. Allows XPS rendering filters to retrieve PrintDeviceCapabilities XML files from the Print filter pipeline property bag. |

## See also

[V4 Printer Driver Property Bags](v4-driver-property-bags.md)
