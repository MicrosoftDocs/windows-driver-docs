---
title: Validating and Certifying Hardware Codecs
author: windows-driver-content
description: Validating and Certifying Hardware Codecs
ms.assetid: 8cf96aac-78ba-41f0-b9d0-48948f704262
keywords:
- hardware codecs WDK AVStream , validating
- hardware codecs WDK AVStream , certifying
- hardware codec support WDK AVStream , validating and certifying
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Validating and Certifying Hardware Codecs


If your vendor-supplied AVStream minidriver includes hardware-based codec support, or you have implemented a custom MFT to support your hardware, you must supply an X.509 certificate chain, specify a merit value in the driver INF file, and implement KSPROPSETID\_OPMVideoOutput in the driver.

### <a href="" id="obtaining-an-x-509-certificate"></a>**Obtaining an X.509 Certificate**

A Media Foundation Transform (MFT) encoder or decoder that is backed by hardware must provide a valid, Microsoft-signed X.509 certificate that specifies the CodecMeritCertificationPolicy EKU (Extended Key Usage) certificate extension. To license a hardware accelerated codec, you must participate in the PVP-OPM licensing program. To request licensing materials, please contact the [Windows Media License Agreements](mailto://wmla@microsoft.com) alias.

### **Specifying Merit**

In the AddReg section of your INF file, set the DWORD-typed MFTMerit registry value:

```
[myVideoDecoder.Reader.AddReg]
HKR,,CLSID,,%Proxy.CLSID%
HKR,,FriendlyName,,%shedVideoDecoder.Reader.FriendlyName%
HKR,,MFTMerit,0x00010001,7
```

### <a href="" id="implementing-kspropsetid-opmvideooutput"></a>**Implementing KSPROPSETID\_OPMVideoOutput**

The KSPROPSETID\_OPMVideoOutput property set is exposed in the *Ksopmapi.h* and *Opmapi.h* header files, which ship in the Windows SDK for Windows 7 and later.

The property set and methods are defined in the following excerpt from the *Ksopmapi.h* file:

```
#ifdef DEFINE_GUIDSTRUCT
#define STATIC_KSPROPSETID_OPMVideoOutput \
0x6f414bb, 0xf43a, 0x4fe2, 0xa5, 0x66, 0x77, 0x4b, 0x4c, 0x81, 0xf0, 0xdb                         
DEFINE_GUIDSTRUCT("06F414BB-F43A-4fe2-A566-774B4C81F0DB", KSPROPSETID_OPMVideoOutput);          
#define KSPROPSETID_OPMVideoOutput DEFINE_GUIDNAMED(KSPROPSETID_OPMVideoOutput)                   
#endif
 
typedef enum
{                                                                                    
    //  Output is OPM_RANDOM_NUMBER followed by certificate                                        
    KSMETHOD_OPMVIDEOOUTPUT_STARTINITIALIZATION = 0,                                              
 
    //  Input OPM_ENCRYPTED_INITIALIZATION_PARAMETERS                                             
    //  Output OPM_STANDARD_INFORMATION                                                           
    KSMETHOD_OPMVIDEOOUTPUT_FINISHINITIALIZATION = 1,                                             
 
    //  Input is OPM_GET_INFO_PARAMETERS, output is OPM_REQUESTED_INFORMATION                     
    //  Use KsMethod - both input and output in the buffer (not after the KSMETHOD structure)     
    KSMETHOD_OPMVIDEOOUTPUT_GETINFORMATION = 2                                                    
} KSMETHOD_OPMVIDEOOUTPUT;           
```

User-mode components access KSPROPSETID\_OPMVideoOutput through the **IKsControl** interface on the AVStream proxy MFT. For code examples that show an implementation of the OPMVideoOutput method handler routines, see [Codec Merit Validation](codec-merit-validation.md).

For driver-specific information about OPM, see [Supporting Output Protection Manager](https://msdn.microsoft.com/library/windows/hardware/ff569879). For application-specific information about OPM, see [Using Output Protection Manager](http://go.microsoft.com/fwlink/p/?linkid=155059).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Validating%20and%20Certifying%20Hardware%20Codecs%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


