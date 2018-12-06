---
title: Logging
ms.assetid: CB7FE988-6E5A-4669-9FFB-A2B3F8DAF30F
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
description: NFC logging for functions/methods, NCI packets/protocols, and other verbose logging.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Logging


For function/method and other verbose logging, *Windows software trace preprocessor* (WPP) logging is used. For NCI packet/protocol logging, Event Tracing for Windows (ETW) is used. To enable WPP logging for debugging, use the following commands:

```cpp
tracelog -start MyNfcSession -f C:\Data\test\bin\MyNfcSession.etl
tracelog -enableex MyNfcSession -guid #351734b9-8706-4cee-9247-04accd448c76 -matchanykw 0xFFFFFFFFFFFFFFFF -level 7
tracelog -enableex MyNfcSession -guid #696D4914-12A4-422C-A09E-E7E0EB25806A -matchanykw 0xFFFFFFFFFFFFFFFF -level 7
tracelog -enableex MyNfcSession -guid #9d97cb90-8dee-42b8-b553-d1816be6fb9e -matchanykw 0xFFFFFFFFFFFFFFFF -level 7
tracelog -enableex MyNfcSession -guid #4EB7CC58-145C-4a79-9418-68CD290DD9D4 -matchanykw 0xFFFFFFFFFFFFFFFF -level 7
tracelog -enableex MyNfcSession -guid #D976D933-B88B-4227-95F8-00513C0986DE -matchanykw 0xFFFFFFFFFFFFFFFF -level 7
tracelog -stop MyNfcSession
```

This will generate an ETL file named MySession.etl in the C:\\Data folder. You can then decode them using [Tracepdb](https://msdn.microsoft.com/library/windows/hardware/ff553034) (Tracepdb.exe) and [Tracefmt](https://msdn.microsoft.com/library/windows/hardware/ff552974) (Tracefmt.exe), which are included in the Windows Driver Kit.

The NFC CX does not include any debugging extensions.

## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[NFC class extension (CX) reference](https://msdn.microsoft.com/library/windows/hardware/dn905536)  
[Event Tracing for Windows (Windows Drivers)](https://msdn.microsoft.com/library/windows/hardware/ff552961)  
[Tools for Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204)  
