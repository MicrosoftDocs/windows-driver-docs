---
title: Understanding the Sdv-map.h File
description: Understanding the Sdv-map.h File
ms.assetid: 2ad3d94d-3991-414b-ae1c-27a07c10839f
keywords:
- Sdv-map.h WDK Static Driver Verifier , about Sdv-map.h
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Understanding the Sdv-map.h File


Before verifying a driver, SDV scans the driver's source code and creates an Sdv-map.h file in the driver's sources directory. You should examine and approve this header file before verifying your driver.

You can also use a **staticdv /scan** command to direct SDV to scan the driver's code and creates the file. For instructions, see [Scanning the driver](scanning-the-driver.md).

If the Sdv-map.h file is incomplete or incorrect, that is, if any of the entry points are missing, or the entry points are associated with the wrong function role type, the verification is not reliable.

For a list of the functions that SDV uses for the WDM, KMDF, and NDIS drivers, see [Using Function Role Type Declarations](using-function-role-type-declarations.md).

The function role types that appear in the Sdv-map.h file are the ones that SDV uses in its rule verification. SDV uses the function role type declarations that you added to your header files to produce the Sdv-map.h file in the driver's source code directory. In the Sdv-map.h file, SDV maps the declared driver functions to function identifiers that are used by SDV during verification. For example, for a KMDF driver, a callback function called *MyDpc* might be mapped to fun\_WDF\_DPC\_1. 

SDV does not require that the driver declare function role types for all of the callback functions that it uses. It requires only that if the driver has declared the function role type that SDV knows about and interprets it correctly. If a driver does not have a function role type that SDV requires to verify a particular rule, SDV concludes that the rule does not apply to the driver. This is not considered to be an error or a defect. 

It is important that you correct any errors in the Sdv-map.h file before verifying the driver. If the file is wrong, the verification might not be reliable.

 

 





