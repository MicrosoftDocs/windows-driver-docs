---
title: C28260
description: Warning C28260 A syntax error in the annotations was found while parsing for a property inside a function.
ms.assetid: fd048e4c-b23c-4ef8-8a0d-e644bfab3ae9
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28260


warning C28260: A syntax error in the annotations was found while parsing for a property inside a function

This warning indicates an error in the annotations, not in the code that is being analyzed. The text mentioned in the text of the message is extracted from the low-level annotations, which usually are encoded as macros. Typically, however, the syntax error is in an expression that is a parameter to one of the macros. The usual location for a syntax error is the header file that contains the annotated function.

 

 





