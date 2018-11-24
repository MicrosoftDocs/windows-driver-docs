---
title: Adding the WDI TLV generator/parser to your driver
description: To add the WDI TLV generator/parser to your driver, follow these steps.
ms.assetid: 625FDE43-7A42-4840-9AFD-B8F5850F845E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding the WDI TLV generator/parser to your driver


To add the WDI TLV generator/parser to your driver, follow these steps.

1.  Add this include after dot11wdi.h and wditypes.hpp.

    `#include "TlvGeneratorParser.hpp"`

2.  Add this library to the linker.

    `TLVGeneratorParser.lib`

3.  Define, create, and write your memory APIs (overloaded operator new/delete).

4.  Start calling the APIs.

 

 





