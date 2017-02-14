---
title: Child I/O Class
description: Child I/O Class
ms.assetid: e467ef0c-a969-4cc1-a5b5-2416794051f2
keywords: ["child I/O class WDK display"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Child%20I/O%20Class%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




