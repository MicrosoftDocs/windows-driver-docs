---
title: Maintenance
description: Maintenance
ms.assetid: 228759ed-f6de-4680-adf2-ca88b83ff4a0
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Maintenance


Schema Path:\\Printer.Maintenance

Node Type:Property

The Maintenance property contains information about the maintenance of the print device.

The Maintenance property contains two child values: **AlignHead** and **CleanHead**.

### <span id="alignhead"></span><span id="ALIGNHEAD"></span> AlignHead

Schema Path:\\Printer.Maintenance.AlignHead

Node Type: Value

Data Type: BIDI\_BOOL

Description: This value represents a command to perform a head alignment procedure on the device. This value is a write-only value. An attempt to read this value should be rejected. If the value is set to 1, the device should perform the command.

### <span id="cleanhead"></span><span id="CLEANHEAD"></span> CleanHead

Schema Path:\\Printer.Maintenance.CleanHead

Node Type: Value

Data Type: BIDI\_BOOL

Description: This value represents a command to perform a head cleaning procedure on the device. This value is a write-only value. An attempt to read this value should be rejected. If the value is set to 1, the device should perform the command.

 

 




