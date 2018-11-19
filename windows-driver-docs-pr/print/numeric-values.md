---
title: Numeric Values
description: Numeric Values
ms.assetid: 4f1f4145-aeda-4770-9a49-d8fe701763c8
keywords:
- GPD file entries WDK Unidrv , numeric values
- numeric values WDK GPD files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Numeric Values





All numeric values that you specify as entry values or parameter values in a GPD file must be integers. Decimal points are not allowed, except within text strings.

Numeric values are assumed to be positive unless preceded by a minus sign.

Numeric values are assumed to be decimal unless preceded by 0x, in which case they are unsigned hexadecimal values.

The asterisk character (\*) can be used to indicate either an infinite value or a "don't care" value, if applicable within the context of a particular GPD file entry.

 

 




