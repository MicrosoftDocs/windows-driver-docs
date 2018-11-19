---
title: Validating and Certifying Hardware Codecs
description: Validating and Certifying Hardware Codecs
ms.assetid: 8cf96aac-78ba-41f0-b9d0-48948f704262
keywords:
- hardware codecs WDK AVStream , validating
- hardware codecs WDK AVStream , certifying
- hardware codec support WDK AVStream , validating and certifying
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Validating and Certifying Hardware Codecs


If your vendor-supplied AVStream minidriver includes hardware-based codec support, or you have implemented a custom MFT to support your hardware, you must supply an X.509 certificate chain, specify a merit value in the driver INF file, and implement KSPROPSETID\_OPMVideoOutput in the driver.

### **Obtaining an X.509 Certificate**

A Media Foundation Transform (MFT) encoder or decoder that is backed by hardware must provide a valid, Microsoft-signed X.509 certificate that specifies the CodecMeritCertificationPolicy EKU (Extended Key Usage) certificate extension. To license a hardware accelerated codec, you must participate in the PVP-OPM licensing program. To request licensing materials, please contact the [Windows Media License Agreements](mailto://wmla@microsoft.com) alias.

### **Specifying Merit**

In the AddReg section of your INF file, set the DWORD-typed MFTMerit registry value:

```INF
[myVideoDecoder.Reader.AddReg]
HKR,,CLSID,,%Proxy.CLSID%
HKR,,FriendlyName,,%shedVideoDecoder.Reader.FriendlyName%
HKR,,MFTMerit,0x00010001,7
```

### **Implementing KSPROPSETID\_OPMVideoOutput**

The KSPROPSETID\_OPMVideoOutput property set is exposed in the *Ksopmapi.h* and *Opmapi.h* header files, which ship in the Windows SDK for Windows 7 and later.

The property set and methods are defined in the following excerpt from the *Ksopmapi.h* file:

```cpp
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
