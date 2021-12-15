---
title: Memory (print)
description: The value entries for the memory installed in the print device
ms.date: 07/07/2020
---

# Memory (print)

Schema Path:\\Printer.Configuration.Memory

Node Type:Property

Description:The value entries for the memory installed in the device

The Memory property contains two child values: **Size** and **PS**.

## Size

Schema Path:\\Printer.Configuration.Memory:Size

Node Type:Value

Data Type:BIDI\_INT

Description:The amount of physical memory, in kilobytes (KB), installed in the device.

## PS

Schema Path:\\Printer.Configuration.Memory:PS

Node Type:Value

Data Type:BIDI\_INT

Description:The amount of memory, in kilobytes (KB), available to the Postscript interpreter in the device. This amount should be less than the amount of physical memory installed.
