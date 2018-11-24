---
title: Sample PrintTicket File for PIN Printing
description: Here is a sample PrintTicket file to show how to specify PIN printing.
ms.assetid: FC1BE797-7097-4BEF-A530-3846CED3E400
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample PrintTicket File for PIN Printing


Here is a sample PrintTicket file to show how to specify PIN printing.

```xml
<?xml version="1.0"?>
   <psf:PrintTicket xmlns:psf="http://schemas.microsoft.com/windows/2003/08/printing/printschemaframework" 
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
      xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1" 
           xmlns:psk="http://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords"
           xmlns:pskv11=" http://schemas.microsoft.com/windows/2013/05/printing/printschemakeywordsv11">
      <psf:ParameterInit name="pskv11:JobPasscodeString">
         <psf:Value xsi:type="xsd:string">123456</psf:Value>
      </psf:ParameterInit>
      <psf:Feature name="pskv11:JobPasscode">
         <psf:Option name="psk:On" />
      </psf:Feature>
   </psf:PrintTicket>
```

For more information about protected printing, see [Driver support For Protected Printing](driver-support-for-protected-printing.md).

 

 




