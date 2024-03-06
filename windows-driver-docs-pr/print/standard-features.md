---
title: Standard Features
description: Standard Features
keywords:
- printer features WDK Unidrv , standard
- standard features WDK Unidrv
ms.date: 01/30/2024
---

# Standard features

[!include[Print Support Apps](../includes/print-support-apps.md)]

Standard features are [printer features](printer-features.md) commonly provided by most printers. They are identified by predefined names that the GPD language recognizes. Resource identifiers for strings that represent these names are contained in stdnames.gpd, which is supplied with the Microsoft Windows Driver Kit (WDK). Some standard features are required and must be specified for every printer. Others are optional.

The following table lists all of the standard features, in alphabetical order, and indicates whether each feature accepts standard options or customized options. The features that include a Print Schema keyword are GPD features that are automatically mapped to Print Schema keywords. You can also map GPD features to Print Schema keywords manually by using the PrintSchemaKeywordMap attribute.

| Feature name | Default Print Schema feature keyword | Description | Standard options | Comments |
|--|--|--|--|--|
| Collate | DocumentCollate | Page collation | See [Standard options](standard-options.md). Customized options are not allowed. | Optional. If not specified, Unidrv does not support page collation. |
| ColorMode | PageOutputColor | Color printing modes | None. All options are customized. See [Option attributes for the ColorMode feature](option-attributes-for-the-colormode-feature.md). | Optional. If not specified, Unidrv renders images in single-plane, 1-bit-per-pixel format. |
| Duplex | JobDuplexAllDocumentsContiguously | Two-sided printing | See [Standard options](standard-options.md). Customized options are not allowed. | Optional. If not specified, Unidrv performs only single-sided printing. |
| Halftone | No default keyword. Use the PrintSchemaKeywordMap attribute to assign a Print Schema feature keyword. | Halftoning capabilities | See [Standard options](standard-options.md). Customized options are allowed. See [Option attributes for the Halftone feature](option-attributes-for-the-halftone-feature.md). | Optional. If not specified, Unidrv selects a GDI-supported halftoning method. See [Halftoning with Unidrv](halftoning-with-unidrv.md). |
| InputBin | JobInputBin | Types of input bins | See [Standard options](standard-options.md). Customized options are allowed. See [Option attributes for the InputBin feature](option-attributes-for-the-inputbin-feature.md). | Required. Customized input bin names must be 24 characters or less. |
| MediaType | PageMediaType | Types of printing media | See [Standard options](standard-options.md). Customized options are allowed. | Optional. If not specified, the printer's default medium is always used. |
| Memory | No default keyword. Use the PrintSchemaKeywordMap attribute to assign Print Schema feature keyword. | Printer memory configurations | All options are customized. See [Option attributes for the Memory feature](option-attributes-for-the-memory-feature.md). | Optional. If specified, Unidrv attempts to keep track of memory usage. The default FeatureType value is PRINTER_PROPERTY. |
| Orientation | PageOrientation | Paper orientations | See [Standard options](standard-options.md). Customized options are not allowed. | Optional. If not specified, the default orientation is PORTRAIT. For Windows 7, the **MxdcGetPDEVAdjustment** function has new parameters for landscape rotation. For more information, see [**MxdcXDCGetPDEVAdjustment**](/windows-hardware/drivers/ddi/mxdc/nf-mxdc-mxdcgetpdevadjustment). |
| OutputBin | JobOutputBin | Types of output bins | None. All options are customized. See [Option attributes for the OutputBin feature](option-attributes-for-the-outputbin-feature.md). | Optional. If not specified, Unidrv does not attempt to select an output bin. |
| PageProtect | JobPageProtection | Enables protection of current print page | See [Standard options](standard-options.md). Customized options are not allowed. | Optional. If not specified, the default value is OFF. Unidrv only enables page protection if enough printer memory is available. The default FeatureType value is PRINTER_PROPERTY. See **PageProtectMem**. |
| PaperSize | PageMediaSize | Paper sizes | See [Standard options](standard-options.md). Customized options are allowed. Also see [Option attributes for the PaperSize feature](option-attributes-for-the-papersize-feature.md). | Required. At least one option must be specified. The CUSTOMSIZE option allows printer users to specify a paper size. |
| RESDLL | This feature cannot be mapped to a Print Schema keyword. | Resource DLLs | All options are customized. See [Using resource DLLs in a minidriver](using-resource-dlls-in-a-minidriver.md). | Optional. See ResourceDLL. |
| Resolution | PageResolution | Printing resolutions | All options are customized. See [Option attributes for the Resolution feature](option-attributes-for-the-resolution-feature.md). | Required. At least one option must be specified. |
| Stapling | JobStapleAllDocuments | Stapling capabilities | All options are customized. | Optional. If specified, Directory Services indicates the printer supports stapling. |
| N-Up | NUp | Number of pages to print on each sheet | No standard options. All options are customized. | Optional. |
| Passcode | JobPasscode | Job passcode | See [Driver support for protected printing](driver-support-for-protected-printing.md). Customized options are not allowed. | Optional. If not specified, the default value is OFF. |

For GPD examples, see [Sample GPD files](sample-gpd-files.md).

## Related topics

[Sample GPD files](sample-gpd-files.md)

[V4 printer driver localization](v4-driver-localization.md)
