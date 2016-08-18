---
title: Scan Job Execution
author: windows-driver-content
description: Scan Job Execution
MS-HAID:
- 'dsm\_des\_theory\_200d7fe2-7539-45ec-b932-02ec91cf4082.xml'
- 'image.scan\_job\_execution'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cefc6aee-725d-4dc4-bbdc-3d152c97b203
---

# Scan Job Execution


The execution phase begins when a user initiates a scan job at a DSM Device. The DSM Device retrieves the scan processes that are available for the user and displays them to the user. The user must select one of the available scan processes. The user may override any individual settings of a scan process that are not marked to disallow user override. The DSM Device uses the scan ticket from the selected scan process or, if the user overrides the scan process settings, creates a new scan ticket from the user-specified settings to use when scanning the document. Insofar as Distributed Scan Device Web Service (WS-DSD) is concerned, the scan job ends when the DSM Device has finished digitizing the final image.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Scan%20Job%20Execution%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


