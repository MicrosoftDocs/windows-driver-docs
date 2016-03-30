---
title: Logging
ms.assetid: CB7FE988-6E5A-4669-9FFB-A2B3F8DAF30F
description: 
---

# Logging


For function/method and other verbose logging, *Windows software trace preprocessor* (WPP) logging is used. For NCI packet/protocol logging, Event Tracing for Windows (ETW) is used. To enable WPP logging for debugging, use the following commands:

```
tracelog -start MySession1 -f C:\Data\MySession.etl
tracelog -enableex MySession1 -guid #351734b9-8706-4cee-9247-04accd448c76 -matchanykw 0xFF -level 7
tracelog -enableex MySession1 -guid #696D4914-12A4-422C-A09E-E7E0EB25806A -matchanykw 0xFF -level 7
tracelog -stop MySession1
```

This will generate an ETL file named MySession.etl in the C:\\Data folder. You can then decode them using [Tracepdb](https://msdn.microsoft.com/library/windows/hardware/ff553034) (Tracepdb.exe) and [Tracefmt](https://msdn.microsoft.com/library/windows/hardware/ff552974) (Tracefmt.exe), which are included in the Windows Driver Kit.

The NFC CX does not include any debugging extensions.

## Related topics


[Event Tracing for Windows (Windows Drivers)](https://msdn.microsoft.com/library/windows/hardware/ff552961)

[Tools for Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Logging%20%20RELEASE:%20%283/30/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





