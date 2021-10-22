---
title: Finishing property
description: Contains data about operations performed after printing is complete.
ms.date: 09/07/2021
ms.localizationpriority: medium
---

# Finishing property

Schema Path: \\Printer.Finishing

Node Type: Property

The Finishing property contains data about operations performed after printing is complete. This includes whether the document can be collated, stapled, hole punched, along with information about available output bins.

The Finishing property contains two child values, CollationSupported and JogOffsetSupported; it also is the parent of the [Staple](staple3.md), [HolePunch](holepunch3.md), and [OutputBins](outputbins2.md) properties.

## CollationSupported

Schema Path: \\Printer.Finishing:CollationSupported

Node Type: Value

Data Type: BIDI_BOOL

Description: Indicates whether the printer supports hardware collation of printed documents. If **TRUE**, collation is supported; if **FALSE**, collation is not supported.

## JogOffsetSupported

Schema Path: \\Printer.Finishing:JogOffsetSupported

Node Type: Value

Data Type: BIDI_BOOL

Description: Determines whether the printer supports placing separate copies of a print job or separate print jobs in the output trays in staggered groups. If **TRUE**, the printer supports jog offset; if **FALSE**, the printer does not support this capability.
