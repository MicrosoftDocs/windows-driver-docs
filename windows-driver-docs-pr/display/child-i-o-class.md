---
title: Child I/O Class
description: Child I/O Class
ms.assetid: e467ef0c-a969-4cc1-a5b5-2416794051f2
keywords:
- child I/O class WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Child I/O Class


The Windows Display Driver Model (WDDM) does not permit a call into one of the child I/O class functions in a reentrant fashion. That is, at the most, one thread can be running within one of the following functions per child device at a given time:

-   [*DxgkDdiQueryChildStatus*](https://msdn.microsoft.com/library/windows/hardware/ff559754)

-   [*DxgkDdiQueryDeviceDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff559761)

-   [*DxgkDdiI2CReceiveDataFromDisplay*](https://msdn.microsoft.com/library/windows/hardware/ff559675)

-   [*DxgkDdiI2CTransmitDataToDisplay*](https://msdn.microsoft.com/library/windows/hardware/ff559677)

-   [*DxgkDdiOPMConfigureProtectedOutput*](https://msdn.microsoft.com/library/windows/hardware/ff559701)

-   [*DxgkDdiOPMCreateProtectedOutput*](https://msdn.microsoft.com/library/windows/hardware/ff559705)

-   [*DxgkDdiOPMDestroyProtectedOutput*](https://msdn.microsoft.com/library/windows/hardware/ff559708)

-   [*DxgkDdiOPMGetCertificate*](https://msdn.microsoft.com/library/windows/hardware/ff559711)

-   [*DxgkDdiOPMGetCertificateSize*](https://msdn.microsoft.com/library/windows/hardware/ff559715)

-   [*DxgkDdiOPMGetCOPPCompatibleInformation*](https://msdn.microsoft.com/library/windows/hardware/ff559720)

-   [*DxgkDdiOPMGetInformation*](https://msdn.microsoft.com/library/windows/hardware/ff559725)

-   [*DxgkDdiOPMGetRandomNumber*](https://msdn.microsoft.com/library/windows/hardware/ff559730)

-   [*DxgkDdiOPMSetSigningKeyAndSequenceNumbers*](https://msdn.microsoft.com/library/windows/hardware/ff559735)

 

 





