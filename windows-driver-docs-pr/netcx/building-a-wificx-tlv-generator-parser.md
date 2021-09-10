---
title: Adding the WiFiCx TLV generator/parser to your driver
description: To add the WiFiCx TLV generator/parser to your driver, follow these steps.
ms.date: 09/10/2021
ms.localizationpriority: medium
---

# Adding the WiFiCx TLV generator/parser to your driver


To add the WiFiCx TLV generator/parser to your driver, follow these steps.

1.  Add this include after dot11wificxintf.h and dot11wificxtypes.hpp.

    `#include "TlvGeneratorParser.hpp"`

2.  Add this library to the linker.

    `TLVGeneratorParser.lib`

3.  Define, create, and write your memory APIs (overloaded operator new/delete).

4.  Start calling the APIs.

 

 





