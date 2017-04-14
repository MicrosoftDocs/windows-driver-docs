---
title: Sample PrintTicket File for PIN Printing
author: windows-driver-content
description: Here is a sample PrintTicket file to show how to specify PIN printing.
ms.assetid: FC1BE797-7097-4BEF-A530-3846CED3E400
---

# Sample PrintTicket File for PIN Printing


Here is a sample PrintTicket file to show how to specify PIN printing.

```XML
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Sample%20PrintTicket%20File%20for%20PIN%20Printing%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


