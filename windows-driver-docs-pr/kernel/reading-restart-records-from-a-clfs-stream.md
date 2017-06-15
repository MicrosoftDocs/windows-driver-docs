---
title: Reading Restart Records from a CLFS Stream
author: windows-driver-content
description: Reading Restart Records from a CLFS Stream
MS-HAID:
- 'Clfs\_guide\_ef681a39-9ed5-4064-b0d2-421ce3bf2d33.xml'
- 'kernel.reading\_restart\_records\_from\_a\_clfs\_stream'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 310545f6-d10d-481e-829d-287b045b98cd
keywords: ["Common Log File System WDK kernel , restart records", "CLFS WDK kernel , restart records", "restart records WDK CLFS", "reading restart records"]
---

# Reading Restart Records from a CLFS Stream


## <a href="" id="ddk-introduction-to-wmi-kg"></a>


To read all of the restart records in a Common Log File System (CLFS) stream (in reverse order), use the following procedure.

1.  Call [**ClfsReadRestartArea**](https://msdn.microsoft.com/library/windows/hardware/ff541709) to obtain a read context and the restart record that was most recently written to the stream.

2.  Pass the read context you obtained in step 1 to [**ClfsReadPreviousRestartArea**](https://msdn.microsoft.com/library/windows/hardware/ff541699) repeatedly to obtain the remaining restart records in the log.

**Note**  When you call [**ClfsWriteRestartArea**](https://msdn.microsoft.com/library/windows/hardware/ff541770) to write a restart record to a stream, CLFS automatically sets the previous LSN of that record to the LSN of the previous restart record in the stream. Those previous LSNs form the chain that is followed by repeated calls to **ClfsReadPreviousRestartArea**.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Reading%20Restart%20Records%20from%20a%20CLFS%20Stream%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


