---
title: V4 Printer Driver Localization
description: Windows provides standard localized display strings to support development of printer extensions and UWP device apps.
ms.date: 08/27/2021
---

# V4 Printer Driver Localization

Windows provides standard localized display strings to support development of printer extensions and UWP device apps provided through [**IPrintSchemaCapabilities**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemacapabilities) objects.

The following table shows the features that Windows can localize with its standard display strings:

| Feature | Standard options |
|--|--|
| Input bins | Job/Document/PageInputBin |
| Media types | PageMediaType |
| Duplexing | JobDuplexAllDocumentsContiguously |
| Collation | DocumentCollate |
| Output color | PageOutputColor |
| Orientation | PageOrientation |
| N-Up | JobNUpAllDocumentsContiguously |
| Hole punching | JobHolePunch<br><br>DocumentHolePunch |
| Stapling | JobStapleAllDocuments<br><br>DocumentStaple |
| Binding | JobBindAllDocuments<br><br>DocumentBinding |
| Output quality | PageOutputQuality |
| Media size | PageMediaSize |

In addition, these strings are available in the XML forms of PrintCapabilities, provided that the driver does not specify a display name using a resource DLL for the feature or option. If a driver does specify a display name using a resource DLL, it will be provided in the XML, as well as to the legacy COMPSTUI-based print preferences UI used on previous versions of Windows.

Across the different user interfaces and APIs, the display names vary. Use the following three flowcharts to see an overview of the expected localization behavior for a given scenario.

The following flowchart shows the expected localization behavior in UWP apps, as well as in the [**IPrintSchemaFeature**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemafeature) and [**IPrintSchemaOption**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemaoption) families of objects.

![localization behavior flowchart for Windows apps, iprintschemafeature or iprintschemaoption.](images/locstringmodern.png)

The following flowchart shows the expected localization behavior in **PrintCapabilities** XML documents.

![localization behavior flowchart for printcapabilities xml documents.](images/locstringpcap.png)

The following flowchart shows the expected localization behavior in the standard, Compstui-based print preferences dialog.

![localization behavior flowchart for compstui-based dialog .](images/locstringcomp.png)

To use the Microsoft-localized display names, follow the instructions in this table to properly edit your GPD or PPD configuration files.

| File type | Instructions |
|--|--|
| GPD | Specify the ***Name*** entry for the GPD feature or option.<br><br>Do not specify the **rcNameID** entry.<br><br>For the following features or options, you must also specify ***PrintSchemaKeywordMap*** to map GPD features or options to the corresponding Print Schema-defined features or options, unless they are specified as [Standard Features](standard-features.md). To see examples showing how to use ***PrintSchemaKeywordMap*** to map features, see [GPD/PPD-Based Feature Description Changes](gpd-ppd-based-feature-description-changes.md)<br><br>JobHolePunch, DocumentHolePunch<br><br>JobStapleAllDocuments, DocumentStaple<br><br>JobBindAllDocuments, DocumentBinding<br><br>PageOutputQuality<br><br>PageMediaType<br><br>For N-Up, do not use **PrintSchemaKeywordMap** on the option values. |
| PPD | Use **PrintSchemaKeywordMap** to map PPD features or options to the corresponding Print Schema-defined features or options. To see examples showing how to use **PrintSchemaKeywordMap** to map features, see [GPD/PPD-Based Feature Description Changes](gpd-ppd-based-feature-description-changes.md)<br><br>For N-Up, do not use **PrintSchemaKeywordMap** on the option values. |

## Localizing PPD Based Drivers

PPD based drivers do not support resource DLLs. As a result, it may be necessary to provide multiple PPD files. Microsoft recommends that v4 print drivers that use PPD configuration files should use the techniques outlined in this topic to include one PPD file per locale.

## Related topics

[**IPrintSchemaCapabilities**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemacapabilities)  

[**IPrintSchemaFeature**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemafeature)  

[**IPrintSchemaOption**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemaoption)  

[GPD/PPD-Based Feature Description Changes](gpd-ppd-based-feature-description-changes.md)  

[Standard Features](standard-features.md)
