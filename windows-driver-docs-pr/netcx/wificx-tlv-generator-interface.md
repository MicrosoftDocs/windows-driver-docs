---
title: WiFiCx TLV generator interface
description: This section describes an overview of the WiFiCx TLV generator interface
ms.date: 09/10/2021
---

# WiFiCx TLV generator interface

WifiCx re-uses the WDI model's TLV generator and parser library. For more information see [WDI TLV generator/parser topics](../network/wdi-tlv-generator-parser.md).

## Adding the TLV generator/parser to your driver


To add the TLV generator/parser to your driver, follow these steps.

1.  Add this include after dot11wificxintf.h and dot11wificxtypes.hpp.

    `#include "TlvGeneratorParser.hpp"`

2.  Add this library to the linker.

    `TLVGeneratorParser.lib`

3.  Define, create, and write your memory APIs (overloaded operator new/delete).

4.  Start calling the APIs.

 

 





