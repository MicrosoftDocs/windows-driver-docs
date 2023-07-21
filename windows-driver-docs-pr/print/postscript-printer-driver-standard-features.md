---
title: PostScript printer standard features
description: The PostScript printer standard features are the common ones that are provided by most PostScript printers.
ms.date: 07/20/2023
---

# PostScript printer standard features

[!include[Print Support Apps](../includes/print-support-apps.md)]

The PostScript printer standard features are the common ones that are provided by most PostScript printers.

The standard features are identified by predefined names that the PPD language recognizes, and the following table shows the mappings between the feature names and the standard keyword used in the PPD files.

| Feature name | Default print schema feature keyword | Description | Comments |
|--|--|--|--|
| Collate<br><br>- true<br><br>- false | DocumentCollate | Page collation<br><br>- Collated<br><br>- Uncollated | Optional<br><br>If not specified, collation is not supported. |
| JCLResolution | PageResolution | Page resolution | At least one kind of Resolution feature (JCLResolution or Resolution) is required. At least one option must be specified. |
| Duplex<br><br>- DuplexTumble<br><br>- DuplexNoTumble<br><br>- Any other option | JobDuplexAllDocumentsContiguously | Two-sided printing<br><br>- TwoSidedShortEdge<br><br>- TwoSidedLongEdge <br><br>- OneSided | Optional<br><br>If not specified, only single sided printing is supported. |
| InputSlot | JobInputBin | Types of input bins | Required<br><br>Customized input bin names must be 24 characters or less. |
| MediaType | PageMediatype | Types of printing media | Optional<br><br>If not specified, the printer's default medium is always used. |
| OutputBin | JobOutputBin | Types of output bins | Optional<br><br>If not specified, the print system does not attempt to select an output bin. |
| PageSize | PageMediaSize | Paper sizes | Required<br><br>At least one option must be specified. |
| Stapling | JobStapleAllDocuments | Stapling types | Optional |

## Related topics

[Pscript Minidrivers](pscript-minidrivers.md)  

[Standard Options](standard-options.md)  
