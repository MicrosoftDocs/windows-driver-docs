---
title: Sample PrintTicket File for PIN Printing
description: Here is a sample PrintTicket file to show how to specify PIN printing.
ms.date: 01/25/2023
---

# Sample PrintTicket File for PIN Printing

[!include[Print Support Apps](../includes/print-support-apps.md)]

Here is a sample PrintTicket file to show how to specify PIN printing.

```xml
<?xml version="1.0"?>
   <psf:PrintTicket xmlns:psf="https://schemas.microsoft.com/windows/2003/08/printing/printschemaframework" 
      xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance" 
      xmlns:xsd="https://www.w3.org/2001/XMLSchema" version="1" 
           xmlns:psk="https://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords"
           xmlns:pskv11=" https://schemas.microsoft.com/windows/2013/05/printing/printschemakeywordsv11">
      <psf:ParameterInit name="pskv11:JobPasscodeString">
         <psf:Value xsi:type="xsd:string">123456</psf:Value>
      </psf:ParameterInit>
      <psf:Feature name="pskv11:JobPasscode">
         <psf:Option name="psk:On" />
      </psf:Feature>
   </psf:PrintTicket>
```

For more information about protected printing, see [Driver support For Protected Printing](driver-support-for-protected-printing.md).
