---
title: Functions defined by print processors
description: Provides information about functions defined by print processors.
keywords:
- print processors WDK, functions
- functions WDK print
ms.date: 09/12/2022
---

# Functions defined by print processors

Print processors must export the functions listed in the following table.

| Function name | Description |
|--|--|
| [**ClosePrintProcessor**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-closeprintprocessor) | Closes the print processor. |
| [**ControlPrintProcessor**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-controlprintprocessor) | Provides control over printing a document. |
| [**EnumPrintProcessorDatatypes**](/windows-hardware/drivers/ddi/winspool/nf-winspool-enumprintprocessordatatypesa) | Enumerates the data types supported by a print processor. |
| [**GetPrintProcessorCapabilities**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-getprintprocessorcapabilities) | Returns print processor capabilities for a specified input data type. |
| [**OpenPrintProcessor**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-openprintprocessor) | Opens the print processor for printing. |
| [**PrintDocumentOnPrintProcessor**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-printdocumentonprintprocessor) | Prints a document on the print processor. |
